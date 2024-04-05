---
layout: post
title:  "The rules of Set"
date:   2024-04-05 13:35:00 -0400
categories: misc
---

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

**The rule** has a nice property: if I pick out any two cards, then there exists only 1 card that can round out a valid set of 3.

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

Now let's make the game slightly more complex.
Previously, cards had only one property: suit (shape).
From now on, cards will have two properties: suit and cardinality (number).

Find all sets in the example below.
Now there are 7 possible sets.

(X) (XX) (XXX)
(O) (OO) (OOO)
(S) (SS) (SSS)

Find the third card that satisfies **the rule**:

(X) (XX) (?)

<br>

---

<br>

(X) (OO) (?)

<br>

---

<br>

You are almost ready to play.
Cards in Set normally have 4 properties: suit, cardinality, colour and texture.
The same principles apply.

(Todo: one more example)

The rest of the rules are straightforward.
There is a deck with one copy of each possible card (that makes 3^4 = 81 cards).
12 cards are turned face up.
Players compete in real time to identify sets.
If you pick a valid set, you keep the cards as points, remove them from the table, and turn over new cards from the deck to replenish the cards on the table back up to a total of 12.
In the rare case that no sets can be made, an additional 3 cards can be turned face up (bringing the total up to 15).
The game ends when the deck is empty and no more sets can be made.

That is how to play Set!
For online multiplayer I recommend the free and excellent [Set with Friends](https://setwithfriends.com).
Their [code](https://github.com/ekzhang/setwithfriends) is also on Github and I adapted it to render the cards.

The end