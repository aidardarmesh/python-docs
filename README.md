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

## 4.4 break and continue Statements and else Clauses on Loops

`break` (like in C) breaks (`for`, `while`) innermost enclosing. 
`else` loop statement is executed when loop terminates through exhaustion of list (with `for`) or when condition becomes false (with `while`), but not when loop is terminated by `break` statement. 

## 4.5 pass Statements

`pass` does nothing. It can be used when statement is required syntactically:

    def initlog(*args):
        pass # remember to implement this!

## 4.6 Defining Functions

Arg-s are passed using *call by value* (where *value* is object *reference*, not the value of object). 

Function name *user-defined* type. This value can be assigned to another name and used as function:

    >>> fib
    <function fib at 10042ed0>
    >>> f = fib
    >>> f(100)
    0 1 1 2 3 5 8 13 21 34 55 89

Function without `return` statement (procedures) do return value `None`.

## 4.7.1 Default Argument Values

`in` tests whether sequence contains certain value. 

Default values are evaluated at the point of function definition in *defining* scope:

    i = 5

    def f(arg=i):
        print(arg)

    i = 6
    f()

**BUT**. When default value is mutable (list, dictionary or class instance), it accumulates arg-s on subsequent calls:

    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))

    [1]
    [1, 2]
    [1, 2, 3]

If you don't want default be shared with subsequent calls:

    def f(a, L=None)
        if L is None:
            L = []
        L.append(d)
        return L

    print(f(1))
    print(f(2))
    print(f(3))

    [1]
    [2]
    [3]

## 4.7.2 Keyword Arguments

Func-s can also be called using `keyword_argument=value`:

    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")

Only `voltage` is required and other three arg-s are optional. Function can be called in next ways:

    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000, action='VOOOM')
    parrot(action='VOOOM', voltage=1000)
    parrot('a million', 'a bereft of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')

**BUT** following calls are *invalid*:

    parrot()                    # required arg is missing
    parrot(voltage=0.5, 'dead') # non-keyword arg after keyword arg
    parrot(110, voltage=220)    # duplicate value for same argument
    parrot(actor='John Cleese') # unknown keyword arg

Keyword arg-s MUST follow positional arg-s. 

`*name` (tuple) contains positional arg-s, `**name` (dict) receives keyword arg-s:

    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

    -- Do you have any Limburger ?
    -- I'm sorry, we're all out of Limburger
    It's very runny, sir.
    It's really very, VERY runny, sir.
    ----------------------------------------
    shopkeeper : Michael Palin
    client : John Cleese
    sketch : Cheese Shop Sketch

`*name` should always be before `**name`

## 4.7.4 Unpacking Argument Lists

`*` operator unpacks arg-s out of list of tuple:

    >>> list(range(3, 6))
    [3, 4, 5]
    >>> args = [3, 6]
    >>> list(range(*args))
    [3, 4, 5]

`**` unpacks arg-s out of dict:

    >>> def parrot(voltage, state='a stiff', action='voom'):
    ...     print("-- This parrot wouldn't", action, end=' ')
    ...     print("if you put", voltage, "volts through it.", end=' ')
    ...     print("E's", state, "!")

    >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    >>> parrot(**d)
    -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

## 4.7.5 Lambda Expressions

Small anonymous func-s can be created with *lambda* keyword (it returns function objects):

    >>> def make_incrementor(n):
    ...     return lambda x: x + n

    >>> f = make_incrementor(42)
    >>> f(0)
    42
    >>> f(1)
    43

## 4.8 Intermezzo: Coding style

* Use 4-space indentation and no tabs
* Don't exceed 79 char-s
* Use blank lines to separate func-s and classes, and larger block of code inside func-s
* Put comments on line of their own
* Use docstrings
* Use spaces round operators and after commas
* `UpperCamelCase` for classes and `lowercase_with_underscores` for func-s and methods. Always use `self`

## 5.1 More on Lists

`list.append(x)` adds item at the end of list

`list.extend(iterable)` extends list by appending all items from iterable

`list.insert(i, x)` inserts item at given position, so `a.insert(0, x)` inserts at the front of the list

`list.remove(x)` removes first item from list whose value == x. Raises `ValueError` if there is no such item

`list.pop([i])` removes item at given position and returns it. If no index is specified, `a.pop()` removes nd returns last item in list

`list.clear()` removes all elem-s from list

`list.index(x[, start[, end]])` returns zero-based index in list of first item whose value == x. Raises `ValueError` if there is no such item. *start* and *end* are used to limit search to particular subsequence. Returned index is relative to full list beginning, not to *start*

`list.count(x)` returns number of items x appears in list

`list.sort(key=None, reverse=False)` sorts items of list in place

`list.reverse()` reverses elem-s of list in place

`list.copy()` returns shallow copy of list. Equivalent to `a[:]`

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.count('apple')
    2
    fruits.count('tangerine')
    0
    fruits.index('banana')
    3
    fruits.index('banana', 4)
    6

## 5.1.2 Using Lists as Queues

It is possible to use list as queue (FIFO), however list is not efficient for this purpose. While `append` and `pop` from the end are fast, `insert` or `pop` from beginnig are slow (because all other elem-s are shifted by one)

Use `collections.deque` instead:

    from collections import deque
    queue = deque(['Eric', 'John', 'Michael'])
    queue.append('Terry')
    queue.append('Graham')
    queue.popleft()
    'Eric'
    queue.popleft()
    'John'
    queue
    ['Michael', 'Terry', 'Graham']

## 5.1.3 List Comprehension

List comprehension consists of brackets containing expression followed by `for` clause, then zero or more `for` or `if` clauses. The result will be new list resulting from evaluating expression:

    squares = [x**2 for x in range(10)]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

## 5.1.4 Nested List Comprehensions

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    [[row[i] for row in matrix] for i in range(4)]
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

## 5.2 del Statement

Removes item at given index or slice:

    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    a
    [1, 66.25, 333, 333, 1234.5]
    del a[2:4]
    [1, 66.25, 1234.5]
    del a[:]
    a
    []

## 5.3 Tuple and Sequences

Tuple consists of number of values separated by commas:

    t = 12345, 54321, 'hello' # example of tuple packing
    t[0]
    12345
    t
    (12345, 54321, 'hello')
    u = t, (1, 2, 3, 4, 5)
    ((12345, 54321, 'hello'), (1, 2, 3, 4, 5))
    empty = ()
    singleton = 'hello',
    len(empty)
    0
    len(singleton)
    1
    singleton
    ('hello',)

Tuples are immutable and usually contain different type sequence of elem-s. Unpacking requires as many equal elem-s number on both sides of equal sign.

    x, y, z = t

## 5.5 Dictionaries

Keys are immutable. Tuples can be keys if they contain only strings, number or tuples: if tuple contains any mutable object either directly or indirectly , it cannot be used as keys. 

`list(d)` on dictionary returns list of all keys. `dist()` builds dictionaries from sequences of key-value pairs:

    dict([('sape', 4139), (guido, 4127)])
    {'sape': 4139, 'guido': 4127}

Dict comprehensions also can be used:

    {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}

Using keyword arg-s:
    
    dict(sape=4139, guido=4127, jack=4098)
    {'sape': 4139, 'guido': 4127, 'jack': 4098}

## 5.6 Looping Techniques

Use `items()` to get key and value when looping dictionary:

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}

    for k, v in knights.items():
        print(k, v)

To loop through sequence, index and value can be retrieved by `enumerate()`:

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

`reversed` to loop in reverse order. `sorted` to loop sorted sequence. 

## 6. Modules

Module is file containing defitions and statements. Module name is file name without suffix `.py` attended. Within a module, module's name (as string) is available as value of global variable `__name__`. 

    import fibo # importing definitions and statements from fibo.py

    fibo.fib(1000)
    fib = fibo.fib # if fibo.fib is often used, assigning to shorter name variable
    fib(1000)

## 6.1 More on Modules

    from fibo import fib, fib2
    fib(500)

Imported names directly, `fibo` is not defined.

`as` makes pseudonames when importing:

    import fibo as fib
    fib.fib(500)

    from fibo import fib as fibonacci
    fibonacci(500)

## 6.1.1 Executing modules as scripts

When running Python module with:

    python fibo.py <arguments>

code in module will be executed, just as if you imported it, but with `__name__` set to `__main__`. If you add next code to end of module:

    if __name__ = '__main__":
        import sys
        fib(int(sys.argv[1]))

you can run module as a script

## 6.2 Standard Modules

`sys` is built-in in every Python interpreter. `sys.ps1` and `sys.ps2` are primary and secondary prompts. `sys.path` is list of str-s that determines interpreter's search path for modules. It is initialized to default path taken from env var `PYTHONPATH` or from built-in default when `PYTHONPATH` is not set. 

## 6.3 dir() Function

Is used to find out which names module defines:

    a = [1, 2, 3, 4, 5]
    import fibo
    fib = fibo.fib
    dir()
    ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Listed all names: var-s, modules, func-s, etc. BUT, it doesn't list names of built-in func-s and var-s. They are defined in module `builtins`

# 6.4 Packages

Packages are a way of structuring Python's module namespace y using "dotted module names":

    from sound.effects.echo import echofilter
    echofilter(input, output, delay=0.7, atten=4)

direct access to `echofilter` from module `echo`. When using `from package import item`, item can be either submodule (or subpackage) or some other name defined in package, like function or class or variable. `import` first tests whether item is defined in package; if not, it assumes it is module and attempts to load it. If it fails to find it, `ImportError` is raised.

Contrarily, when using `import item.subitem.subsubitem`, each item except last must be package; last item can be module or package, but not class, function or variable defined in previous item.

## 7.1 Fancier Output Formatting

Several ways:

* begin string with `f` or `F` before opening quotation mark or triple quotation mark. Inside this string you can write Python expression between `{` and `}`:

    year = 2006
    event = 'Referendum'
    f'Results of the {year} {event}'
    'Results of the 2006 Referendum'

* `str.format()` requires also information be formatted:

    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes  49.67%'

* handling by yourself by slicing and concatenation

## 7.2 Reading and Writing Files

`open()` returns file object:

    f = open('workfile', 'w')

When finished don't forget to `f.close()`. Instead use `with` because:

* file is properly closed after its suite finishes, even if exception is raised
* shorter than `try/finally`

    with open('workfile') as f:
        read_data = f.read()
    f.closed
    True

`f.read(size)` reads some quantity of data and returns it as string (in text mode) or bytes object (in binary mode). When size is ommitted or negative, entire content of file will be read and returned. If end of file is reached, '' is returned:

    f.read()
    'This is the entire file.\n'
    f.read()
    ''

`f.readline()` reads single line from file. If returns '', end of file reached, while blank line is represented by '\n' is a string containing only single newline.

For reading lines from file:

    for line in f:
        print(line, end='')
    This is the first line of the file.
    Second line of the file

To read all lines of file: `list(f)` or `f.readlines()`.

`f.write(string)` writes contents of *string* to file, returning number of char-s written:

    f.write('This is a test\n')
    15

`f.tell()` returns integer giving file object's current position in file represented as number of bytes from beginning of file in binary mode and opaque number when in text mode. 

`f.seek(offset, from_what)` changes file object's position. Position is computed from adding *offset* to ref-ce point; ref-ce point is selected by *from_what* arg. *from_what* 0 is beginning of file (default), 1 is current position and 2 is end of file. 

## 8 Errors and Exceptions

There are 2 kinds of errors: *syntax errors* and *exceptions*. 

## 8.2 Exceptions

Errors detected during execution are called *exceptions* and are not always fatal (if handled).

`try` works as follows:

* code between `try` and `except` is executed
* if no exception occurs, `except` is skipped
* if exception occurs, rest of `try` is skipped. If exception type matches one that is in `except`, this clause is executed
* if exception type does not match, it is passed to outer `try` statement. If no handler found, it is *unhandled exception* and execution stops

`try ... except` statement as optional `else` , which when present, must follow all except clauses. Code in `else` is executed, when exception was not raised:

    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

`raise` forces specified exception to occur:

    raise NameError('HiThere)

To create specific Exception class:

    class Error(Exception):
        """Base class for exceptions in this module."""
        pass
    
    class InputError(Error):
        """Exception raised for errors in the input."""
        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

`finally` always executes before leaving `try` statement whether exception has raised or not. When exception as occured in `try` clause and has not been handled by `except` clause, it is re-raised after `finally` clause has been executed. `finally` is executed "on the way out" when `try` statement is left via `break`, `continue` or `return`. 

## 9 Classes

*namespace* is mapping from names to objects. Most namespaces are currently implemented as Python dictionaries. Examples:

* set of built-in names (abs(), built-in exception names)
* global names in module
* local names in function invocation

Set of attributes of object also form namespace. **NOTE** there is absolutely no relation between names n different namespaces: 2 modules may have `maximize` func - users of module must prefix it with module name.

Namespaces are created at different moments and have different lifetimes. Namespace containing `built-in names` is created when Python *interpreter starts up and is never deleted*.

*Global namespace* for module is created when module definition is read in and last until interpreter quits. 

*Local namespace* for func is created when func is called and is deleted when func returns or raises an exception that is not handled within func. Recursive invocations each have their own local namespace.

*Scope* is textual region where namespace is directly accessible. 

