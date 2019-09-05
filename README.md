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

    \>\>\> price = 13.6250
    \>\>\> price
    13.6250
    \>\>\> round(_, 2)
    13.63

