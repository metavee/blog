---
layout: post
title:  "A one-plug commute from home to work: my cheap KVM alternative"
date:   2023-01-07 16:03:00 -0400
categories: hardware
---

Currently, I work from home most days.
My living space isn't that large so I do my work at the same space where I use my personal computer outside of work hours.

**Problem statement**: I want to be able to easily switch over my monitor and peripherals between my work and home computers.

Additionally, on days where I do go into the office, it would be nice to be able to pack up my work stuff quickly (and of course to be able to put everything back together quickly when I come home).

## My hardware

My work computer is a Macbook Pro with 3 Thunderbolt / USB-C ports and an HDMI port as well as Bluetooth.
My home computer is a desktop.
It has lots of ports of different kinds and a Bluetooth adapter and is not really a constraint.

I have a wired keyboard and mouse (both USB-A) and a single Dell Ultrasharp monitor.
The monitor has multiple ports and if you have multiple computers plugged into it at once, it will automatically switch to whichever one is on; this is very convenient for my purposes.

## My solution: a USB switch and a dongle

The monitor essentially solves itself, so that part is easy.

For my wired keyboard and mouse on both computers, I needed to bring in a USB switch.
This is a USB hub that is simultaneously connected to two computers.
Similar to my monitor, it automatically switches to the right computer if both are off and one turns on.

This technically works as-is, but the laptop needs a power cable, the USB switch's cable (plus a USB-A to USB-C adapter), and the HDMI cable from the monitor.

Luckily there are dongles that can map all of those into a single Thunderbolt cable.
I've used a few cheapo dongles in the past, but they tended to get quite hot if I was using them for power as well, which I didn't like.
Currently I'm using this dongle from Apple which gets the job done.

I also have a laptop stand for my desk so that I can use the work laptop as a second monitor and have the screen at a similar height to my main monitor.
Currently I'm using this stand which can get the laptop up quite high and also leaves the space underneath relatively open, which makes it easier to clean when my desk gets dusty.

## The end result

When I'm ready to start my work day, I ensure my home computer is off and then plug the one dongle into my work laptop.

At the end of the work day, I unplug the dongle from my laptop and my home computer is ready to use (should I need it right away).

## My work bag

It's somewhat icing on the cake, but I have a few extra items that I leave in my work bag for those days when I do go into the office.

I have:

- a backup charger
- a slightly more portable laptop stand
- a compact bluetooth keyboard and mouse

None of it is essential but it makes it easy to get out of the house if that's what I need.

## A blurred line between work and home

One unfortunate side effect of my setup is that my keyboard muscle memory can get pretty confused between work and home contexts.

A trivial example: my home computer is running Windows and my work computer is running Mac OS, which have different keyboard shortcuts.
I usually mess these up at least once or twice a day in either direction.
When I was using a separate keyboard just for my work laptop, this basically never happened.

One example that I find a bit more baffling is passwords.
Sometimes I'll sit down at my home computer and draw a blank about my password (that I type at least once every day); the only passwords that pop into my head are my work passwords, or vice versa.
This doesn't happen too often but it's the strangest feeling when it does.
It seems to happen more often if I use both computers in quick succession; e.g., turning on my home computer before work in the morning and then immediately opening my work computer to double check my calendar for the day.

It just goes to show how sensitive the brain is to the various elements of context.

## Alternatives: Docks and KVMs

My experience with "docks" which accomplish this task is that they're quite expensive, and the ones I used had wonky display drivers that frequently caused my Macbook to lock up and require a reboot.

I've never tried a proper KVM; I had a preconception that they were all insanely expensive, but it seems like there are some cheap models out there these days.
That being said I'm not sure if you can get a KVM that's cheap _and_ has support for Thunderbolt.

In any case, there are lots of options out there and I'm sure my own setup will continue to evolve as I make various upgrades.
