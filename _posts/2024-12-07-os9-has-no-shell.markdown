---
layout: post
title:  "OS 9 has no shell"
date:   2024-12-07 23:38:00 -0500
categories: technical
---

Mac OS X is only partially related to its predecessors - large parts of OS X were imported from Apple's acquisition of [NeXTSTEP](https://en.wikipedia.org/wiki/NeXTSTEP), which had a different kernel and design from Mac OS 9.
This is significant enough that applications made for one don't run [natively\*](https://en.wikipedia.org/wiki/List_of_built-in_macOS_apps#Classic) in the other.

Recently, I got a 2001 iMac which was dual booting OS 9 and OS X.

![iMac G3]({{site.baseurl}}/images/os9_shell/imac.png)

There was a little problem - I didn't know the admin password on the OS X install.

I thought that maybe I could reset it from inside OS 9 - in an OS with less concept of user permissions, maybe I would be able to pop open some kind of terminal with admin rights and run a password reset command.

![iMac G3]({{site.baseurl}}/images/os9_shell/os9_control_panels.png)

But not only is there no password reset command, there is actually no shell at all.

What???

I had this feeling that I should have known better, but this honestly surprised me a lot - it didn't occur to me that anyone would build an OS without a shell.
Even Windows has a shell!

Here's one weird related fact - there is no standard output stream on OS 9 either.
This is even stranger to me - do you need to write GUI code just to make a standalone hello world program?

Funnily enough, this would have seemed totally reasonable to me when I was a kid - I thought CLIs were a thing of the past and not essential any more.
Now that I've been programming for a long time, I've come to expect stdout (or something analogous) to exist in every environment.

In spite of (or perhaps because of) taking stdout for granted, I only have a hazy understanding of what stdout is/where it "lives".
Nevertheless, it is disorienting for it to simply *not be there*.

⚫
