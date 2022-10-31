---
layout: post
title:  "David Beazley's Rafting course: a retrospective"
date:   2022-10-29 15:29:00 -0400
categories: personal
---

Recently, I took David Beazley's [Rafting trip](https://www.dabeaz.com/raft.html), an intensive course on distributed systems.
It was a surprisingly wonderful time, and I want to organize my thoughts about it on paper since it might change how I approach learning going forward.

# Why did I take the course

There are a few reasons that drove me to take this course.

Primarily, I have a sense that I would enjoy learning about applied topics in computer science. For various reasons I never got to study much CS during university, and I feel like I missed out.

Distributed systems is one such topic I wish I had studied. I could take a self-paced course or read a textbook, but I've had problems finishing traditional online courses like you find on Coursera. Seeing this non-traditional format got my interest.

Finally, I simply expected it to be a great experience. I had previously watched and thoroughly enjoyed some of the instructor's conference presentations, particularly [Lambda Calculus from the Ground Up](https://www.youtube.com/watch?v=pkCLMl0e_0k). And I knew people (who knew people) who had taken some of his other courses like Compilers and said very nice things about them.

# What was in the course

It was an online course with a small classroom size - the instructor and 10 students.

Every day had the same format: a few short lecture segments over Zoom, with large blocks of time for independent coding on a suggested topic.

There was a course repo where everyone pushed their code to their own branch and an associated Gitter chat room.

The purpose of the course was essentially to build an implementation of the [Raft algorithm](https://raft.github.io/), more or less in 5 days.

The lectures served to reinforce key aspects of Raft, provide some ideas on programming paradigms that might be helpful in our attempt, and a suggested order of which part to build next.

# What was magical about the course

The course was a very positive experience, perhaps near the pinnacle of educational experiences I've had thus far. When I start describing it to people, I get visibly worked up and excited about it. Why is that?

## It was short, intense and focused

I was able to devote a week to it where it was essentially my only focus.

It was a difficult topic - perhaps too difficult to really fit in a week if we're being honest, but nonetheless extremely interesting.

And it was over before I could get bored of it.

## The instructor took it with us

The instructor also worked on his own Raft implementation during the coding blocks. At this point he's taught the course over 10 times. Each time he's tried some new things with his own implementation, iterating on the course content.

I feel like the course benefitted from such extensive testing, and it also lent itself to a more collegial atmosphere since the instructor was struggling alongside the students.

## I and the other students were motivated to be there

This course had some disincentives to taking it. It was on a difficult topic. It's not a purely academic topic, but it's also not directly applicable - if I want a Raft implementation, I'll use someone else's. It also had a substantial cost and conferred no credentials.

I believe this selected for students who were primarily motivated to learn, myself included. Being in this environment of like-minded people who were enjoying the topic was incredibly motivating.

## It was purely project-based

Most of my prior education has been lecture driven.
There are usually assignments with a big list of small questions, which tend to be not fun at all.

In contrast, this was basically one big project and a small amount of lecturing. Big projects can be fun, but pretty disappointing if they don't come together in the end.

In this case, it really did start coming together (even if I didn't completely finish it).

## I built something amazing

I don't want to overstate my achievement since I didn't exactly invent Raft, but when I had finally implemented enough of the pieces to spin up a virtual cluster and see it working on my computer, it was an incredible feeling.

Let me try to explain.

At the beginning of the project, you more or less have a handful of functions.
You can plug things in and see that they behave as expected, but it feels about as exciting as talking to a sock puppet.

Eventually you have more pieces and they start to mesh together more intricately.
Calling one function sets off a cascade of other functions.

But the real magic happens once you start making function calls across the network.
Now you can spin up multiple instances, even on multiple computers, and see them communicating with one another.
Each message generates some internal activity and replies back and forth.

You append data on one instance and see it bubble outward to the others, getting tentatively replicated, then committed on the leader, then committed across the cluster.
You terminate the leader process and watch as the other nodes realize something is wrong, kick off an election and choose a replacement leader.

This dynamic living system, which I essentially made from scratch, was extremely satisfying to see in action.

## It let me practice the craft

In my day job, I have to be pragmatic in order to get things done.

This often means using out-of-the-box libraries for stuff like this since implementing it yourself is time-consuming and it's easy to build something buggy.

Also, it often means coming up with simple solutions with the tools closest at hand, particularly using design patterns and technology that is already widely used at the company, even if it's not the theoretically ideal fit.

This tends to result in solutions that are quick to implement and easily understood across the team.
These are wonderful properties in a business context.
But it also trades off craftsmanship in favour of more practicality.

I love the feeling of making something well-crafted, and **this course helped me feel the joy of programming**.

# How should I approach my studies in CS going forward?

Thinking again about taking a Master's degree in CS, I feel like I should be extremely hesitant, since that traditional format lacks so much of the magic that this class had.

I could revisit self-paced courses and textbooks, but perhaps there's a way to apply some of the principles that made this course enjoyable. I could drop everything and devote a ton of focus to one course, trying to get through it quickly. I could also find a way to do it in a motivated group of people, like getting a group of friends together for a study hall.

Lastly, I could try to find a killer project for each area I want to study. It might not be trivial to find the perfect project idea for a given topic, but it could pay dividends in terms of motivation and enjoyment.

Or I could just take the other Beazley courses. I'm half joking, but it's not a bad option. If I can be satisfied with the list of topics, that is.
