---
layout: post
title:  "The rules of Set"
date:   2024-04-22 23:31:00 -0400
categories: misc
---

Set is a card game for 1-8 (best with 3-4).
Here are some things I like about it:

- it is conceptually very simple
- it is weirdly difficult
- it is played in real time, so _it is always everyone's turn_
- it plays well online, e.g. via [Set with Friends](https://setwithfriends.com/)

The rules of Set are simple, but hard to explain in words.
In fact, most of the game is about one rule, which I'll refer to as **the rule**.
Set is about finding sets of 3 cards which satisfy **the rule**.
Instead of telling you what **the rule** is, I will let you experiment and discover it.

Let's with a simplified version of the game.

From the following 4 cards, only 1 valid set can be formed.
Select the 3 cards that obey **the rule**.
This page is _slightly_ interactive and you can click on cards to select them.

<form>
{% include setcard.html id="1-1" card="1_purple_filled_diamond" class="correct" %}
{% include setcard.html id="1-2" card="1_purple_filled_diamond" class="correct" %}
<br>
{% include setcard.html id="1-3" card="1_purple_filled_oval" %}
{% include setcard.html id="1-4" card="1_purple_filled_diamond" class="correct" %}
</form>

<details>
<summary>Solution</summary>
<p>The 3 matching cards make a set.</p>
</details>

{% include sectionbreak.html %}

In the following 4 cards, 1 valid set can be made.
What is it?

<form>
{% include setcard.html id="2-1" card="1_purple_filled_diamond" class="neutral" %}
{% include setcard.html id="2-2" card="1_purple_filled_diamond" class="neutral" %}
<br>
{% include setcard.html id="2-3" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="2-4" card="1_purple_filled_squiggle" class="correct" %}
</form>

<details>
<summary>Solution</summary>
<p>The 3 distinct cards make a set.</p>
</details>

That summarizes the two types of sets that can be formed.

{% include sectionbreak.html %}

**The rule** has a nice property: if I pick out any two cards, then there exists only one card that can round out a valid set of 3.

Let's practice:

If we start with these 2 cards, what third card would make a set?

<form>
{% include setcard.html id="3-1" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="3-2" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="3-3" card="blank" class="neutral" %}
</form>

As a reminder, here are all types of cards we've seen so far:

<form>
{% include setcard.html id="3-4" card="1_purple_filled_diamond" %}
{% include setcard.html id="3-5" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="3-6" card="1_purple_filled_squiggle" %}
</form>

<details>
<summary>Solution</summary>
<p>A third oval would make a set.</p>
</details>

{% include sectionbreak.html %}

If we start with these 2 cards, what third card would make a set?

<form>
{% include setcard.html id="4-1" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="4-2" card="1_purple_filled_squiggle" class="correct" %}
{% include setcard.html id="4-3" card="blank" class="neutral" %}
</form>

The possible choices:

<form>
{% include setcard.html id="4-4" card="1_purple_filled_diamond" class="correct" %}
{% include setcard.html id="4-5" card="1_purple_filled_oval" %}
{% include setcard.html id="4-6" card="1_purple_filled_squiggle" %}
</form>

<details>
<summary>Solution</summary>
<p>A diamond would make a set.</p>
</details>

{% include sectionbreak.html %}

Now let's make the game more complex.
Previously, cards had only one property: suit (shape).
From now on, cards will have two properties: suit and cardinality (number).

<br>

Given the two starting cards, find the third card that satisfies **the rule**:

<form>
{% include setcard.html id="5-1" card="3_purple_filled_squiggle" class="correct" %}
{% include setcard.html id="5-2" card="1_purple_filled_oval" class="correct" %}
{% include setcard.html id="5-3" card="blank" class="neutral" %}
</form>

As a reference, here is every combination of suit and cardinality.

The third card of the set is in here somewhere:

<form>
{% include setcard.html id="5-4" card="1_purple_filled_oval" %}
{% include setcard.html id="5-5" card="2_purple_filled_oval" %}
{% include setcard.html id="5-6" card="3_purple_filled_oval" %}

{% include setcard.html id="5-7" card="1_purple_filled_diamond" %}
{% include setcard.html id="5-8" card="2_purple_filled_diamond" class="correct" %}
{% include setcard.html id="5-9" card="3_purple_filled_diamond" %}

{% include setcard.html id="5-10" card="1_purple_filled_squiggle" %}
{% include setcard.html id="5-11" card="2_purple_filled_squiggle" %}
{% include setcard.html id="5-12" card="3_purple_filled_squiggle" %}
</form>

<details>
<summary>Solution</summary>
<p>The 2 of diamonds would make a set.</p>
</details>

{% include sectionbreak.html %}

As above, find the third card that satisfies **the rule**:

<form>
{% include setcard.html id="6-1" card="1_purple_filled_squiggle" class="correct" %}
{% include setcard.html id="6-2" card="2_purple_filled_squiggle" class="correct" %}
{% include setcard.html id="6-3" card="blank" class="neutral" %}
</form>

Choices:

<form>
{% include setcard.html id="6-4" card="1_purple_filled_oval" %}
{% include setcard.html id="6-5" card="2_purple_filled_oval" %}
{% include setcard.html id="6-6" card="3_purple_filled_oval" %}

{% include setcard.html id="6-7" card="1_purple_filled_diamond" %}
{% include setcard.html id="6-8" card="2_purple_filled_diamond" %}
{% include setcard.html id="6-9" card="3_purple_filled_diamond" %}

{% include setcard.html id="6-10" card="1_purple_filled_squiggle" %}
{% include setcard.html id="6-11" card="2_purple_filled_squiggle" %}
{% include setcard.html id="6-12" card="3_purple_filled_squiggle" class="correct" %}
</form>

<details>
<summary>Solution</summary>
<p>The 3 of squiggle would make a set.</p>

<p>Notice how everything matches for suit, but everything is distinct in number.
Going that other way (all the same number but all different suits) would have worked as well.</p>
</details>

{% include sectionbreak.html %}

You are almost ready to play.
Cards in Set actually have 4 properties: suit, cardinality, colour and texture.
<!-- TODO: are these the correct set names (and value names)? -->

<form>
{% include setcard.html id="7-1" card="1_red_filled_squiggle" class="correct" %}
{% include setcard.html id="7-2" card="2_purple_outlined_diamond" class="correct" %}
{% include setcard.html id="7-3" card="3_green_striped_oval" class="correct" %}
</form>

There are 4 suits, but the same principles apply as before.

<br>

Let's work out one last example.

Given the following two cards, what third would form a set?

<form>
{% include setcard.html id="8-1" card="2_purple_outlined_oval" class="correct" %}
{% include setcard.html id="8-2" card="3_green_striped_oval" class="correct" %}
{% include setcard.html id="8-3" card="blank" class="neutral" %}
</form>

With 4 different properties, there are slightly too many cards to show you every possibility.
I'll draw a few from the deck, and hopefully the matching card is in there somewhere.

<form>
{% include setcard.html id="8-4" card="1_green_filled_diamond" %}
{% include setcard.html id="8-5" card="2_purple_striped_oval" %}
{% include setcard.html id="8-6" card="1_purple_filled_oval" %}

{% include setcard.html id="8-7" card="3_red_outlined_diamond" %}
{% include setcard.html id="8-8" card="1_green_striped_oval" %}
{% include setcard.html id="8-9" card="1_red_outlined_oval" %}

{% include setcard.html id="8-10" card="1_green_striped_diamond" %}
{% include setcard.html id="8-11" card="1_red_filled_squiggle" %}
{% include setcard.html id="8-12" card="3_purple_filled_oval" %}

{% include setcard.html id="8-13" card="2_purple_outlined_squiggle" %}
{% include setcard.html id="8-14" card="2_green_outlined_oval" %}
{% include setcard.html id="8-15" card="1_red_striped_diamond" %}
</form>

<details>
<summary>Solution</summary>

{% include setcard.html id="8-16" card="1_red_filled_oval" class="correct" %}

<p>Oops!
Looks like the matching card was still in the deck.
It was the red, solid-filled ace of ovals.
</p>

<p>
If this seems uncertain, we can verify the answer.
Looking at the starting two cards, we can work through the properties one-by-one.
</p>

<ul>
<li><b>Suit:</b> the two starting cards are both ovals.</li>
<li><b>Cardinality:</b> the two starting cards have different cardinalities (2 and 3).
The third card must have a cardinality of 1.</li>
<li><b>Colour:</b> the two starting cards have different colours (purple and green).
The third card must be red.</li>
<li><b>Texture:</b> the two starting cards have different textures (empty outline and striped).
The third card must have a solid fill texture.</li>
</ul>

<p>Therefore, we know that the the matching card will be the <b>red, solid-filled, ace of ovals.</b></p>
</details>

{% include sectionbreak.html %}

That is the core of how to play Set!
The challenge of the game is figuring out how to do that _quickly_, while competing with others.

The rest of the rules are straightforward.
There is a deck with one copy of each possible card (that makes 3<sup>4</sup> = 81 cards).
12 cards are turned face up.
Players compete in real time to point out sets.
If you pick a valid set, you keep the cards as points, remove them from the table, and turn over new cards from the deck to replenish the cards on the table back up to a total of 12.
In the rare case that no sets can be made, an additional 3 cards can be turned face up (bringing the total up to 15).
The game ends when the deck is empty and no more sets can be made.

{% include sectionbreak.html %}

For online multiplayer I recommend the free and excellent [Set with Friends](https://setwithfriends.com).
Their [code](https://github.com/ekzhang/setwithfriends) is also on Github and I adapted it to render the cards.

Go forth and enjoy!
