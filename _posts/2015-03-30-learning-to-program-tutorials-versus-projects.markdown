---
layout: post
title:  "Learning to Program: Tutorials versus Projects"
date:   2015-03-30 18:49:28 -0400
categories: personal
---

In science and engineering, many people want to learn to program. Programming is a useful skill to have, in science and elsewhere, but people often struggle with it. One common way to learn programming is to try and finish a course or tutorial for some programming language. From people I've talked to, the problem does not lie in taking this first step, but rather what comes after. Programming is a broad skill with many components; not all topics can be easily learned from a tutorial, and some are all but impossible to learn that way.

Tutorials and courses, by their nature, have an acutely linear format: topics typically build on each other in order of appearance. If you're a student, this serves to hold your hand and shield you from excessive uncertainty or challenge. Consider Codecademy, for example, which is designed to introduce programming to people who have never coded before. A screenshot from an early lesson in Codecademy's Python track can be seen below. Every barrier that could possibly deter a beginner has been removed. The code editor and programming environment is entirely contained in the browser, so there is no need to install and configure an IDE or compiler. On the left hand side there's a friendly explanation of what's happening, and very clear instructions on the next step, which involves writing just one line of code. If you're stuck, there's a hint containing instructions that are even less ambiguous. And when you successfully write that single line of code, there's immediate and clear positive feedback.


![Hand-holding in action]({{site.baseurl}}/images/learning_to_program/codecademy-hand-holding.png)
  
I don't mean to be critical of sites like Codecademy. The complete beginner is easily discouraged, and such measures prevent students from giving up on programming. Past a certain point, though, these crutches lose their usefulness. Whether for personal or professional use, real programming does not have step-by-step instructions. Sometimes all you have is a vague goal and a blank file, and you must produce something from nothing. Therefore, tutorials cannot (by themselves) form a complete education. Even if you don't feel ready (*especially* if you don't feel ready), you must push yourself past your comfort zone in order to grow.

Thankfully, the way forward is simple, at least in concept. You must program something that you don't know how to. On the way you will encounter obstacles, and in grappling with them, develop some very general and widely-applicable problem solving strategies. The purpose of the exercise is not to develop high-quality software or to observe the best practices of software engineering, but rather to **empower yourself to approach any problem**.

The importance of this ability is self-evident. It also extends beyond programming. In life in general, we are faced with challenges we are not prepared for, and there are times when we are not sure of the next step. With this problem solving mindset, you are well-equipped for this scenario, and can succeed in your life goals.

## Tips

Although there is no formal way to develop this skill other than struggle itself, there are some pitfalls which may slow down your progress. Here are some practical guidelines so as to struggle safely and efficiently:

- Don't cheat. If you need help, restrict it to documentation and sites like Stack Overflow. If you find yourself copying more than a few lines of someone else's code, something is wrong.
- Challenge yourself on your own time, when the stakes are low. Doing experimental work during your day job is risky and puts undue pressure on yourself.
- Forget about perfectionism. And best practices. Get ready to do things the wrong way and reinvent the wheel. 
- If you get stuck, maybe your project is too hard. See if you can make some assumptions or approximations to simplify things.
- Have fun. Working on a project you're personally interested in will help you push through the challenge.
- Move on when you get bored. Sometimes projects fail, or you lose interest, and that's perfectly okay. Save your files and work on it another time.

## Project Ideas

I've compiled a few ideas below. I've intentionally kept the list short, since my experience is that reading lists of ideas (ironically) kills creativity.

### Rainy Day Strategy

If you get caught in the rain on the way home, you might be tempted to run, or at least walk faster. But will that actually keep you drier? The faster you go, the more raindrops you'll run into. Write a program to answer this question, perhaps simulating a person walking from point A to point B, and counting the number of raindrops that hit them. Try to identify if there's a simple trend between movement speed and the number of raindrops hit, or if there's some optimal speed for moving in the rain.

### Web Scraper

Pick a website with regularly updated text-based content, perhaps a news site or online discussion board, and write a program that can extract the content. For instance, for a news site, the program could find out what the most recently published article is and download its text, ignoring any advertisements, comments, and other unrelated material. The modern way to do things like this is to find the official API, and download the material in a relatively clean format such as JSON or an RSS feed, but if you're up for the challenge, you should just download the raw HTML and look for patterns that signify the start and end of the content.

### Programming Challenges

Sites such as [Project Euler](https://projecteuler.net/) and the [Daily Programmer subreddit](https://www.reddit.com/r/dailyprogrammer/) have a large collection of relatively small, well-specified, and self-contained problems. They're a handy way to sharpen your algorithm design skills. Their convenience is somewhat of a weak point, however, since the relatively focused nature of the problems limits the scope of the challenges you face.

## Conclusion

When learning to program, tutorials can be tremendously helpful, but they are also have their limitations. As a student of programming, you can fill in those gaps by by working on projects. Even if they fail at their original goal, you will learn many things along the way, and gain the confidence needed to approach bigger problems. So roll up your sleeves, and take on a project of your own.