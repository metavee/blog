---
layout: post
title:  "TIL: I'm older than most booleans"
# date:   2022-11-20 00:15:00 -0500
categories: technical
---

Recently I was writing a shell script and letting my mind wander a bit.

I needed to force an expression to always return true even if it fails, and so I wrote:

```shell
($EXPRESSION) || true
```

Now, POSIX shell doesn't have much in the way of data types: there aren't any booleans.
Anything to do with conditionals is thus somewhat hacked together.
`true` and `false` are not literal boolean values, but executables that run when you invoke them.

```shell
which true
/usr/bin/true

which false
/usr/bin/false
```

They simply exit immediately, returning an integer that represents the corresponding boolean.

If you had to map booleans to integers, how might you do it?
Personally, I would do something like this:

| Boolean | Integer |
| ------- | ------- |
| false   | 0       |
| true    | 1       |

Sure enough, if you cast booleans to integers in most languages these days, that's what you get.
For example, in Python:

```python
>>> int(False)
0
>>> int(True)
1
```

The shell stores the previous exit code in the special variable `$?` so we can print it out to check:

```shell
false
echo $?
1

true
echo $?
0
```

That's the opposite!
Since these are POSIX exit codes, 0 doesn't represent `true` so much as it represents success.
Non-zero doesn't represent `false`, it represents failure.

So wait, then what do `||` and `&&` actually do?
Since they deal in numbers I had always assumed they were bitwise operators, but that gets weird when `false` is 1 and `true` is 0.

Actually, the
[POSIX standard defines these expressions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_03)
as "OR lists" and "AND lists", respectively, that have a well-defined syntax and behaviour.

> The exit status ... shall be the exit status of the last command that is executed in the list.

Okay, so they are more like logical operators.
Even in Python it works similarly, though I've never had the occasion to do this:

```python
>>> 'abc' and 2
2

>>> 'abc' or 2
'abc'
```

We could go on about what they do in the Bash-specific conditional environment `[[ ]]`, but that's a story for another day.

Instead, let's talk a bit about the history of this data type.

# How does C do it?

When I think of the era of Unix and Bash, I also think of C.

The boolean as a formal datatype seems to have been absent in C prior to C99, which is somewhat shocking to me.

All non-zero values are considered _truthy_, and 0 itself is _falsy_ inside `if` statements or other condition checks.

Traditionally you could define a macro yourself that maps true and false to integers 1 and 0, respectively. [comp.lang.c FAQ](https://c-faq.com/bool/booltype.html) delightfully alludes to alternatives:

> Using an int may be faster, while using char may save data space. [[footnote](https://c-faq.com/bool/bitfield.html)]
> Smaller types may make the generated code bigger or slower, though, if they require lots of conversions to and from int.

Of course, since C doesn't really have namespacing, you might find yourself importing a third-party library that _also_ creates a global definition of `true` and `false`.
[Hopefully it doesn't conflict with your code!](https://c-faq.com/bool/thirdparty.html)

From C99 thereafter, there is a `bool` datatype and `true` and `false` literals which can be imported from stdbool.h.
I poked around the Clang source code and found [their implementation of stdbool.h](https://github.com/llvm/llvm-project/blob/llvmorg-15.0.5/clang/lib/Headers/stdbool.h) which seems to be using macros and ints.

# Python and SQL

Of the languages I've used the most, [Python only added a boolean type in 2002 as part of Python 2.3](https://peps.python.org/pep-0285/).
In very concrete ways, they behave as the integers 0 and 1 despite being their own type.

```python
>>> 1 == True
True

>>> sum([True, False, True])
2

>>> d = {0: 'a', 1: 'b'}
>>> d[True]
'b'
```



# History

[According to Wikipedia](https://en.wikipedia.org/wiki/Boolean_data_type), ALGOL was among the first languages to have a boolean type.
In ALGOL 58 it seems to have been just an integer 0/1, but as of ALGOL 60 they are more distinctly their own type.

http://www.math.bas.bg/bantchev/place/algol60.html

https://www.masswerk.at/algol60/report.htm



## Fortran

## Lisp

## SQL

## Python
