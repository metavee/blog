---
layout: post
title:  "Analog video is surprisingly squishy"
date:   2024-08-15 21:17:00 -0400
categories: technical
---

I spent a bit of my time at the [Recurse Center](https://www.recurse.com/) trying to restore one of the old computers in the collection: the [Olivetti M24](https://en.wikipedia.org/wiki/Olivetti_M24).
The first problem was figuring out how to connect it to a monitor - the port on the back was a 25-pin DSUB connector, which is not traditionally used for video.

Supposedly the original release had a proprietary monochrome monitor, and later versions had a colour display.
This made me feel pessimistic about getting it to work with something off-the-shelf.

<a title="Blake Patterson from Alexandria, VA, USA, CC BY 2.0 &lt;https://creativecommons.org/licenses/by/2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Vintage_ATT_6300.jpg"><img width="100%" alt="Vintage ATT 6300" src="https://upload.wikimedia.org/wikipedia/commons/4/48/Vintage_ATT_6300.jpg?20090127233832"></a>

However, there are pinouts for the Olivetti graphics card online, and some people have taken the trouble of [matching these up with standard VGA pins](http://hadesnet.org/olivettim24/docs/video_converter.pdf) - it seemed doable, even if it meant jamming wires into the ports.

Luckily, I found a few "breakout" adapters on Amazon, with one side being a normal VGA adapter, and the other having individual jumpers corresponding to each pin.
This still ended up being pretty messy, but not nearly as bad as it might have been.

![Photo of messy wiring]({{site.baseurl}}/images/olivetti_vga/vga_adapter_wiring.jpg)

After wiring it up I got some help from [Jessie Grosen](https://jessie.grosen.systems/) to double check my work, and to test for any unintentional shorts between pins.
This was semantically confusing because there was a red _wire_ and also a wire carrying a red _video signal_ and these were not the same wire.

After plugging everything in and turning it on... the first monitor we tried did not like the signal.
But the second monitor did!
The BIOS POST screen showed the specs of the computer, including the Intel 8086 CPU and 640 kB of RAM.

![Photo of BIOS POST]({{site.baseurl}}/images/olivetti_vga/bios.jpg)

From there, it booted into gorgeous Italian DOS ("Olivetti Personal Computer DOS Version 3.30").
I was hoping to test out some 3.5" floppy disks, but unfortunately the drive was perpetually _non pronto_, so I had to call it quits there.

![Photo of failed disk formatting]({{site.baseurl}}/images/olivetti_vga/non_pronto.jpg)

Between the serial/parallel ports on the back and the meagre included software, there must be _some_ way to connect this to a modern computer and move data on and off.
That could be a fun "escape room" challenge, albeit for another day.

## The thing that surprised me

You don't need all the pins!

The wiring that I used doesn't cover [EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data)-related pins, so it relies on the monitor to autodetect the video signal correctly (resolution, refresh rate, etc.).
Surprisingly, this worked on most (but not all) monitors that I tried!

There were other, non-EDID pins on the VGA side that were left unconnected, and this was also more or less fine.

In spite of using an unusually large 25-pin connector, most of the pins on the Olivetti side were also either different kinds of ground or else not connected at all (as can be seen from my wiring photo).
