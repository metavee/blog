---
layout: post
title:  "The rules of Set"
date:   2024-04-05 13:35:00 -0400
categories: misc
---

<!-- TODO: give the cards mouseover highlight -->
<!-- TODO: make the cards look nicer -->
<!-- TODO: can we reveal the answer when clicking on the cards, instead of having a separate Solution block? Ideally without javascript -->
<!-- TODO: Proper section spacing -->
<!-- TODO: Nicer layout for showing groups of cards -->

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
Which 3 cards obey **the rule**?

![]({{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg)

<details>
<summary>Solution</summary>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<p>The 3 matching cards make a set.</p>

</details>

<br>

---

<br>

In the following 4 cards, 1 valid set can be made.
What is it?

![]({{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg)

<details>
<summary>Solution</summary>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg'>

<p>The 3 distinct cards make a set.</p>

</details>

That summarizes the two types of sets that can be formed.

<br>

---

<br>

**The rule** has a nice property: if I pick out any two cards, then there exists only one card that can round out a valid set of 3.

Let's practice:

If we start with these 2 cards, what third card would make a set?

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

As a reminder, here are all types of cards we've seen so far:

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg'>
</p>

<details>
<summary>Solution</summary>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>

<p>A third oval would make a set.</p>
</details>

<br>

---

<br>

If we start with these 2 cards, what third card would make a set?

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg)

<details>
<summary>Solution</summary>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<p>A diamond would make a set.</p>
</details>

<br>

---

<br>

Now let's make the game more complex.
Previously, cards had only one property: suit (shape).
From now on, cards will have two properties: suit and cardinality (number).

<br>

Given the two starting cards, find the third card that satisfies **the rule**:

![]({{site.baseurl}}/images/set_cards/3_purple_filled_squiggle.svg)

![]({{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg)

As a reference, here is every combination of suit and cardinality.
The third card of the set is in here somewhere:

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_oval.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_diamond.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_squiggle.svg'>
</p>

<details>
<summary>Solution</summary>
<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_diamond.svg'>

<p>The 2 of diamonds would make a set.</p>
</details>

<br>

---

<br>

As above, find the third card that satisfies **the rule**:

![]({{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg)

![]({{site.baseurl}}/images/set_cards/2_purple_filled_squiggle.svg)

<details>
<summary>Solution</summary>
<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_squiggle.svg'>

<p>The 3 of squiggle would make a set.</p>

</details>

<br>

---

<br>

Considering all 9 distinct cards so far, how many different sets exist?

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_oval.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_diamond.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_squiggle.svg'>
</p>

<details>
<summary>Solution</summary>
<p>12 sets are possible.</p>

<p>With the cards laid out in this way, the rows and columns are valid sets.
Additionally, any diagonal line of 3 (including wrapping around the borders) is a set.</p>
</details>

<br>

---

<br>

You are almost ready to play.
Cards in Set actually have 4 properties: suit, cardinality, colour and texture.
<!-- TODO: are these the correct set names (and value names)? -->

<p>
<img src='{{site.baseurl}}/images/set_cards/1_red_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_outlined_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_green_striped_oval.svg'>
</p>

There are 4 suits, but the same principles apply as before.

<br>

Let's work out one last example.

Given the following two cards, what third would form a set?

![]({{site.baseurl}}/images/set_cards/2_purple_outlined_oval.svg)

![]({{site.baseurl}}/images/set_cards/3_green_striped_oval.svg)

With 4 different properties, there are slightly too many cards to show you every possibility.
I'll draw a few from the deck, and hopefully the matching card is in there somewhere.

<p>
<img src='{{site.baseurl}}/images/set_cards/1_green_filled_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_purple_striped_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_purple_filled_oval.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/3_red_outlined_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_green_striped_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_red_outlined_oval.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/1_green_striped_diamond.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_red_filled_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/3_purple_filled_oval.svg'>
</p>

<p>
<img src='{{site.baseurl}}/images/set_cards/2_purple_outlined_squiggle.svg'>

<img src='{{site.baseurl}}/images/set_cards/2_green_outlined_oval.svg'>

<img src='{{site.baseurl}}/images/set_cards/1_red_striped_diamond.svg'>
</p>

<details>
<summary>Solution</summary>

<img src='{{site.baseurl}}/images/set_cards/1_red_filled_oval.svg'>

<p>Oops!
Looks like the matching card was still in the deck.
It was the red, solid-filled ace of ovals.
</p>

<p>
If this seems uncertain, we can verify the answer.
Looking at the starting two cards, we can work through the properties one-by-one.
</p>

<p>Suit: the two starting cards are both ovals.
The third card must also be an oval.
</p>

<p>Cardinality: the two starting cards have different cardinalities (2 and 3).
The third card must have a cardinality of 1.
</p>

<p>Colour: the two starting cards have different colours (purple and green).
The third card must be red.
</p>

<p>Texture: the two starting cards have different textures (empty outline and striped).
The third card must have a solid fill texture.
</p>

<p>Therefore, we know that the the matching card will be the red, solid-filled, ace of ovals.</p>
</details>

<br>

---

<br>

That is the core of how to play Set!
The challenge of the game is figuring out how to do that _quickly_, while competing with others.

The rest of the rules are straightforward.
There is a deck with one copy of each possible card (that makes 3<sup>4</sup> = 81 cards).
12 cards are turned face up.
Players compete in real time to point out sets.
If you pick a valid set, you keep the cards as points, remove them from the table, and turn over new cards from the deck to replenish the cards on the table back up to a total of 12.
In the rare case that no sets can be made, an additional 3 cards can be turned face up (bringing the total up to 15).
The game ends when the deck is empty and no more sets can be made.

---

For online multiplayer I recommend the free and excellent [Set with Friends](https://setwithfriends.com).
Their [code](https://github.com/ekzhang/setwithfriends) is also on Github and I adapted it to render the cards.

Go forth and enjoy!
