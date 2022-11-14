---
layout: post
title:  "while True: do_work(); the graceful operation of multithreaded Python programs"
# date:   2022-11-14 18:50:00 -0500
categories: technical
---

If you're used to writing single-threaded synchronous code, threads in Python can be tricky to work with.
Aside from the infamous performance quirks with Python threads (which I won't get into), they have a bunch of awkward properties that might break your typical workflows and tools.

This post is about how to make threads play nicely with your:

- exceptions
- unit tests
- REPL
- debugger

# The Architecture

Let's talk about programs that use _message queues_ or _work queues_, such as the producer-consumer pattern.
In code, the consumer looks sort of like this:

```python
while True:
    message = inbox_queue.get()
    process_message(message)
```

The producer code is off in another thread, adding items to the queue to get processed.

The first thing that might jump out at you is that this snippet loops infinitely.
One straightforward fix is to watch for a special message that indicates that we should exit.

```python
while True:
    message = inbox_queue.get()
    if message is None:
        break

    process_message(message)
```

# Exception handling and graceful shutdown

When a thread in Python hits an unhandled exception, it dies.
But the Python program itself doesn't terminate until there are no more running threads.

So if the producer thread hits an exception, it will die while the consumer will patiently continue waiting, forever.
Vice versa if the consumer thread dies.

The sane thing to do is to wind down all the threads at once.
Each thread must keep checking to see whether it _should_ shut down.
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

# Running unit tests

Your unit tests will probably create many new threads.
Unfortunately, some of them will still be alive and kicking after the tests finish, resulting in tools like `pytest` hanging indefinitely at the prompt without exiting:

```
...
tests\test_replication.py .........                                       [ 77%]
tests\test_merge.py .......                                               [ 95%]
tests\test_timeouts.py ..                                                 [100%] 

======================== 40 passed, 1 warning in 13.24s ========================



```

One trick is to use a [threading.Event](https://docs.python.org/3/library/threading.html#threading.Event) flag to signal a request for graceful shutdown.
The unit test logic itself could set this flag as part of test cleanup.

```python
def test_something():
    producerconsumer = ...
    # test logic goes here

    # trigger thread shutdown
    producerconsumer.exit_flag.set()
...

# inside consumer
while True:
    if exit_flag.is_set():
        break

    ...
```

The other important thing is to [mark all worker threads as daemon threads](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) - i.e., background workers that will terminate when the main thread exits. 

```python
producer_thread = threading.Thread(target=producer_fxn, daemon=True)
producer_thread.start()

consumer_thread = threading.Thread(target=consumer_fxn, daemon=True)
consumer_thread.start()
```

This is often a good idea anyway.
Inside pytest, this means that whatever threads get created during the tests, any survivors will get wound down after the tests are over.

# Using the REPL (and not)

The REPL is a surprisingly powerful way to write Python code, allowing you to experiment and manually test at the same time that you develop.

For multithreaded programs, it can be nice to let the background threads run freely while you make stuff happen manually from the REPL.

It's easy: just execute your script with `python -i myscript.py`.
This drops you into a REPL after starting the script, but the background threads should still be running.

Now you can do stuff like this and see the result:

```python
>>> inbox_queue.put("manually inserted item")

```

One wrinkle: if you set `daemon=True` as in the previous section, when you _don't_ run it in the REPL the script will probably exit immediately.
When running non-interactively, the main method should probably wait indefinitely, until killed by the user hitting CTRL+C or one of the threads dying.

Luckily we can do this, and even test if we are inside a REPL to have the same script work both interactively and non-interactively.

```python
import sys
import time

...

# main method

if not sys.flags.interactive:
    print("Running non-interactively")
    while True:
        time.sleep(1)
        if (not producer_thread.is_alive()) or (not consumer_thread.is_alive()):
            print("Worker thread died")
            break
else:
    print("Running in REPL / interactive mode")

```

# Using the debugger

I am a huge fan of the debugger.
I use `--pdb` in pytest, `%debug` in Jupyter, and `breakpoint()` everywhere.

Unfortunately, the built-in debugger `pdb` isn't always easy to use with threads.
When it hits a breakpoint, it pauses that thread **but the others continue running**.
That means the program state keeps changing while I'm trying to look at it.

Luckily, there are alternatives to `pdb`.
If you're using an IDE or powerful editor such as Pycharm or VS Code, its built-in debugger functionality should pause _all_ threads when any of them hit a breakpoint.
You can then jump between all the threads and check out their local state and call stacks one by one.

![Screenshot of VS Code debugger showing threads being paused after a breakpoint is hit]({{site.baseurl}}/images/threads/vscode_multithreaded_debugger.png)

There might be some terminal debuggers out there that offer this feature, but I haven't encountered any yet.

# Demo: Seeing it all together

In summary:

- use timeouts instead of letting queue gets, network requests etc. hang forever
- check if other threads are still running with [`.is_alive()`]((https://docs.python.org/3/library/threading.html#threading.Thread.is_alive))
- use a [threading.Event](https://docs.python.org/3/library/threading.html#threading.Event) to communicate a graceful request for shutdown
- [set `daemon=True`]((https://docs.python.org/3/library/threading.html#threading.Thread.daemon)) on background worker threads


<!-- TODO -->
