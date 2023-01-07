---
layout: post
title:  "A one-plug commute from home to work: my cheap KVM alternative"
date:   2023-01-07 16:03:00 -0400
categories: hardware
---

Currently, I work from home most days.
My living space isn't very large so I do my work at the same space where I use my personal computer outside of work hours.

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

For my wired keyboard and mouse on both computers, I needed to bring in [a USB switch](https://www.amazon.ca/-/en/gp/product/B07TS5JNT3/) ($24 CAD).
This is a USB hub that is simultaneously connected to two computers.
Similar to my monitor, it automatically switches to the right computer if both are off and one turns on.

This technically works as-is, but the laptop needs a power cable, the USB switch's cable (plus a USB-A to USB-C adapter), and the HDMI cable from the monitor.

Luckily there are dongles that can map all of those into a single Thunderbolt cable.
I've used a few [all-in-one dongles](https://www.amazon.ca/-/en/gp/product/B09QKFGNS8/) ($27 CAD), though they can get hot if used for laptop charging as well.
I find this to be slightly less of an issue with the M1 Macbook since it uses so much less power than the Intel series.

## The end result

When I'm ready to start my work day, I ensure my home computer is off and then plug the one dongle into my work laptop.

At the end of the work day, I unplug the dongle from my laptop and my home computer is ready to use (should I need it right away).

**Total cost:** $51 CAD / $38 USD

---

# Addenda

## My work bag

It's icing on the cake, but I have a few extra items that I leave in my work bag for those days when I do go into the office.

I have:

- a backup charger
- [a portable laptop stand](https://www.therooststand.com/)
- a compact bluetooth [keyboard](https://www.logitech.com/en-ca/products/keyboards/k380-multi-device.920-011135.html) and [mouse](https://www.logitech.com/en-ca/products/mice/mx-anywhere-3.910-005833.html)

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
