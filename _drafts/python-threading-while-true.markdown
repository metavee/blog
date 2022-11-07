---
layout: post
title:  "while True: do_work(); the graceful operation of multithreaded Python programs"
# date:   2022-11-06 09:51:00 -0500
categories: technical
---

If you're used to writing single-threaded synchronous code, threads in Python can be tricky to work with.
Aside from the famous Python-specific performance quirks which I won't get into, they have a bunch of awkward properties that might break your typical workflows and tools as a developer such as your testing library, your REPL and your debugger.

I'd like to introduce the issues around thread termination and interacting with running threads, and show some workarounds that I've figured out.

# The Architecture

There are different ways of architecting a multithreaded program, but I want to talk about programs that use _message queues_ or _work queues_, such as the producer-consumer pattern.

The basic idea is that threads use queues to communicate with one another.
One thread (the producer) inserts some tasks in the queue, and the other thread pulls them off and executes them (the consumer).

In code, the consumer looks sort of like this:

```python
while True:
    message = inbox_queue.get()
    process_message(message)
```

The first thing that might jump out at you is that this snippet loops infinitely.
Of course we want to keep looping while there is work to be done, but once it's time to finish we can exit the loop.
One straightforward fix is to watch for a special message that indicates that we should exit.

```python
while True:
    message = inbox_queue.get()
    if message is None:
        break

    process_message(message)
```

# Exception handling and graceful shutdown

The next problem is somewhat off-screen from the consumer.
When a thread in Python hits an unhandled exception, it dies.
But the Python program itself doesn't terminate until there are no more running threads.

So if the producer thread hits an exception, it will silently stop inserting items into the queue.
And the consumer will patiently continue waiting, forever.

In this situation, the sane thing to do is probably to wind down all the threads at once.
In general, it's bad practice to terminate a thread from the outside, so instead each thread must keep checking to see whether it _should_ shut down.
One option is to simply check if [all the other threads are still alive](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive).

One caveat: we need to call `.get()` with a timeout, since otherwise the call blocks forever.

```python
while True:
    # check if the other thread died
    if not producer_thread.is_alive():
        break

    # grab from the queue with a timeout
    try:
        message = inbox_queue.get(timeout=0.100)
    except queue.Empty:
        time.sleep(0.100)
        continue

    # program finished normally
    if message is None:
        break

    process_message(message)
```

For other types of communication, a [threading.Event](https://docs.python.org/3/library/threading.html#threading.Event) flag can also be handy.
You can use one to represent some state change (like a requested shutdown) and have all threads periodically check it and take appropriate action.

# Running unit tests

<!-- setDaemon(True) -->

# Using the REPL

The REPL is a surprisingly powerful way to write Python code, allowing you to experiment and manually test at the same time that you develop.
Popular tools like Jupyter build on it, but the core functionality is the same.

For multithreaded programs, most of the action is happening in background threads, so you might naturally assume that 

<!-- python -i -->
<!-- setDaemon(True) -->
<!-- how to check if we are in the REPL -->

# Using the debugger

I am a huge fan of the debugger.
When my tests fail, I drop into the debugger with `--pdb`.
When I hit a weird exception in a Jupyter notebook, I use `%debug` to poke around.
And when writing code and manually trying stuff out, I use `breakpoint()`.

Unfortunately, the built-in debugger `pdb` isn't always easy to use with threads.
The main problem is that when it hits a breakpoint, it pauses that thread but the others continue running.
The main reason I use the debugger is that it can **pause the world** and let me carefully inspect all the variables and walk `up` and `down` the call stack.
But if the other threads are still running, they might be actively changing the state while I'm trying to look at it.

Also, if the main thread is the REPL and the background thread hits a breakpoint, you enter this weird dance where your inputs alternate between executing in the REPL and executing in the debugger in the background thread.

Unfortunately, this is a shortcoming of pdb.
But, there are alternatives.
If you're using an IDE or powerful editor such as Pycharm or VS Code, its built-in debugger functionality should pause _all_ threads when any of them hit a breakpoint.
You can then jump between all the threads and check out their local state and call stacks one by one.

<!-- TODO: alternative debuggers that do this but work in terminal -->
