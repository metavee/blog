---
layout: post
title: "Editing music in a spreadsheet"
date: 2024-09-12 20:20:00 -0400
categories: technical
---

I was talking to my piano teacher about how I'm finding it hard to record a good take, and he gave me this interesting thought - why not record in MIDI? It's such a compact file format that you could literally record every session you ever have on the keyboard.
Then, if you ever happen to have a good practice session or improvise something nice, it's already recorded.
I think that's a pretty interesting concept!
But isn't it a pain to set up a recording?

Actually, it isn't!
There are lots of little apps out there.
In fact, MIDI is so universal that you can even [record it from your browser](https://midi-recorder.web.app) (as long as your browser is Google Chrome).
For me, that means I can plug my keyboard into my phone over USB and start recording in seconds.

Once I have some recordings, I need to think about editing.
Editing creates interesting possibilities beyond just touching up my own mistakes.
If I were a serious musician, I would use Ableton or some tool made for the job.
But I am in fact a programmer with a whimsical aesthetic sense.
I went looking for other options, and found [midicsv](https://www.fourmilab.ch/webtools/midicsv/) - a little C program that can convert MIDI into CSV and back.

As a little example, I recorded myself playing a C major scale.

<audio controls>
  <source src="{{site.baseurl}}/images/midi2csv/cmajor.mp3" type="audio/mpeg">
  Your browser does not support the audio tag.
</audio>

Here's what the complete file looks like in CSV form.
You can see some metadata in the header, then a list of `NOTE_ON` and `NOTE_OFF` commands, with notes specified by a semitone number (60 is middle C).

| Track | Time | Type           | Channel | Note | Velocity | ... |
| ----- | ---- | -------------- | ------- | ---- | -------- | --- |
| 0     | 0    | Header         | 1       | 2    | 192      |     |
| 1     | 0    | Start_track    |         |      |          |     |
| 1     | 0    | Time_signature | 4       | 2    | 24       | 8   |
| 1     | 0    | Tempo          | 500000  |      |          |     |
| 1     | 3263 | End_track      |         |      |          |     |
| 2     | 0    | Start_track    |         |      |          |     |
| 2     | 0    | Note_on_c      | 0       | 60   | 61       |     |
| 2     | 272  | Note_on_c      | 0       | 62   | 67       |     |
| 2     | 301  | Note_off_c     | 0       | 60   | 5        |     |
| 2     | 545  | Note_on_c      | 0       | 64   | 62       |     |
| 2     | 584  | Note_off_c     | 0       | 62   | 5        |     |
| 2     | 829  | Note_on_c      | 0       | 65   | 58       |     |
| 2     | 844  | Note_off_c     | 0       | 64   | 5        |     |
| 2     | 1104 | Note_on_c      | 0       | 67   | 68       |     |
| 2     | 1129 | Note_off_c     | 0       | 65   | 5        |     |
| 2     | 1380 | Note_on_c      | 0       | 69   | 68       |     |
| 2     | 1414 | Note_off_c     | 0       | 67   | 5        |     |
| 2     | 1646 | Note_on_c      | 0       | 71   | 59       |     |
| 2     | 1677 | Note_off_c     | 0       | 69   | 5        |     |
| 2     | 1926 | Note_on_c      | 0       | 72   | 64       |     |
| 2     | 1947 | Note_off_c     | 0       | 71   | 5        |     |
| 2     | 2872 | Note_off_c     | 0       | 72   | 5        |     |
| 2     | 2872 | End_track      |         |      |          |     |
| 0     | 0    | End_of_file    |         |      |          |     |

Editing the notes played is as simple as editing some numbers into a spreadsheet!
It's easy to see how to do basic changes, like merging multiple recordings, transposing the key or adjusting the timings.

I love how this representation reveals the design of MIDI.
It's obvious why the files are so compact (at least for piano!), and how even underpowered electronics from the 1980s could work with it.
The varying number (and function) of the columns makes CSV a bit of a funny format, but the fact that it's text-based makes it easy to plug in to any other tool for programming or calculation (a la Unix philosophy), just like how MIDI is a lingua franca for musical tools.

It gets me thinking about the possibilities of more complex opertions - what about adding wavery pitch bends that depend on the notes being played, or screaming choruses that pop in if I hold a key down for a certain duration?
Some of these transformations could work in real time during a performance, but others might require peeking at the future, and would only work as a delayed step.
If I think about this for too long, my mind turns to [Apache Flink](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/time/), which is probably a sign that it's time to stop.

![Music does not need this level of complexity]({{site.baseurl}}/images/midi2csv/flink_event_processing_time.svg)

Regardless of the practicality of CSV as an intermediary format, I feel like I have a stronger mental model of MIDI now.
If you're curious about midicsv, I have ported it to run from the browser (including browsers that are and aren't Google Chrome!).
Check it out [here!](https://metavee.github.io/midi2csv/)
