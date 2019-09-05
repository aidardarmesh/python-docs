# Python 3.7 [Tutorial](https://docs.python.org/3/tutorial/)

## Intro
Python is easy to use interpreted language. Works on Windows, Linux or Mac OS

Python is extensible: if you know C language, it is easy to add new built-in function or 
module to the interpreter, either to perform operations at maximum speed or link to libraries 
that may only be available in binary form.

## 2.1 Invoking the Interpreter

Python interpreter is usually installed into `/usr/local/bin/python3.7`. *Putting binary to `/usr/local/bin` makes possible to run it from terminal*:

    python3.7

`/usr/local/python` is also popular location

Second way to start Python interpreter is `python -c "command [arg]"` (analogous to shell). You can use single or double quotes.

Modules (scripts) are called by `python -m module [arg]`. To run script and open interactive mode pass `-i` flag before script name.

## 2.1.1 Argument Passing

When known to interpreter, script name and additional arg-s thereafter are turned into list of strings and assigned to `argv` variable in `sys` module. 

    python3.7 test.py # import sys, print(sys.argv)
    
    Output: ['test.py']

## 2.1.2 Interactive Mode

When commands are read from tty, interpreter is said to be in *interactive mode*, where `>>>` is primary prompt and `...` is secondary prompt. 

## 2.2.1 Source Code Encoding

By default, Python source files are treated as UTF-8 encoded. To declare encoding other than default one:

    # -*- coding: encoding -*-

    Example: # -*- coding: cp1252 -*-

## 3.1.1 Numbers

* division (/) always returns float
* floor division (//) returns integer and discards fractional part
* modulo (%) calculates remainder
* power (**) calculates powers

In interactive mode, last printed expression is assigned to `_` variable:

    >>> price = 13.6250
    >>> price
    13.6250
    >>> round(_, 2)
    13.63

## 3.1.2 Strings

    >>> '"Isn\'t," they said.'
    '"Isn\'t," they said.'
    >>> print('"Isn\'t," they said.')
    "Isn't", they said.
    >>> s = 'First line.\nSecond line.'  # \n means newline
    >>> s # without print(), \n is included in the output
    'First line.\nSecond line.'
    >>> print(s)  # with print(), \n produces a new line
    First line.
    Second line.

If you don't want char-s prefaced by **\\** to be interpreted as special char-s, you can make it `raw` by adding `r` before first quote:

    >>> print('C:\some\name') # here \n means newline!
    C:\some
    ame
    >>> print(r'C:\some\name') # note r before quote
    C:\some\name

Strings can be concatenated with `+` and repeated with `*`. Two or more *string literals* next to each other are automatically concatenated:

    >>> 'Py' 'thon'
    'Python'

This feature is useful to break long strings.

There is no separate `char` type. Character is string with size one.

When `slicing` start is always included and end always excluded.

`IndexError` exception does not raise when slicing:

    >>> word[4:42]
    'on'
    >>> word[42:]
    ''
Python strings are immutable (cannot be changed). `len()` returns length of string. 

## 3.1.3 Lists

List (mutable) might contain items of different types, can be extended (concatenation) and sliced. 
All **slice** operations return new list containing requested elem-s (example below):

    >>> squares = [1, 4, 9, 16, 25]
    >>> squares[:]
    [1, 4, 9, 16, 25]

`append()` adds new item at the end of list. Assignment to slices is also possible:

    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    >>> letters[2:5] = ['C', 'D', 'E']
    >>> letters
    ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    >>> letters[2:5] = []
    >>> letters
    ['a', 'b', 'f', 'g']

`len()` also works for lists. Possible to nest lists:

    >>> a = ['a', 'b', 'c']
    >>> n = [1, 2, 3]
    >>> x = [a, n]
    >>> x
    [['a', 'b', 'c'], [1, 2, 3]]
    >>> x[0][1]
    'b'

## 3.2 First Steps Towards Programming

*Multiple assignment*:

    >>> a, b = 0, 1
    >>> while (a < 10):
    ...     print(a)
    ...     a, b = b, a+b

In Python (like in C) non-zero `int` == True, 0 is False,
non-zero length string (list) == True, empty == False,

## 4.1 if Statements

if ... elif ... elif ... sequence is substitute for `switch` or `case`.

## 4.2 for Statements

Iterates over items of any sequence (list, string) in order they appear in sequence. 

If you need to modify sequence you are iterating over while, it is recommended to make a sequence copy firstly. With `for w in words:` would attempt to create infinite list, inserting `defenestrate` over and over again. The reason is that `words[:]` returned limited requested list of items that didn't increase (copy of `words`).

    >>> words = ['cat', 'window', 'defenestrate']
    >>> for w in words[:]:
    ...     if len(w) > 6:
    ...     words.insert(0, w)
    >>> words
    ['defenestrate', 'cat', 'window', 'defenestrate']

## 4.3 range() Function

    range(5)
    1, 2, 3, 4
    range(5, 10)
    5, 6, 7, 8, 9
    range(0, 10, 3)
    0, 3, 6, 9
    range(-10, -100, -30)
    -10, -40, -70

Object returned by range() behaves as if it is a list, but in fact it isn't. It is an object which returns successive items of desired sequence when you iterate over it, but it doesn't really make list, thus saving space.

