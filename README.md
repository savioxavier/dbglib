# dbglib

> A macro for `print(some_variable)`-style debugging fans.
> 
> Debuggers are great. But sometimes you just don't have the time or patience to set up everything correctly and just want a quick way to inspect some values.

dbglib is a library that provides quick and easy debugging for your Python scripts

No more of typing stuff like `print("here")` or `print("value =", value)` or `print(f"The output of data is {data} and it has a length of {len(data)}")`, dbglib is here to save the day!

dbglib currently exports one function named `dbg`. It's inspired by Rust's `dbg!(...)` macro and provides a wide variety of information useful for debugging literally anything in your code

**Installation**

```text
pip install dbglib
```

**Usage**

```py
from dbglib import dbg

a = 10
dbg(a)
```

- Information provided:
  - file in which dbg was called
  - line number at which dbg was called 
  - function in which dbg was called
  - variable name
  - variable value
  - variable type
  - length, if variable type is an iterable
 
Variable values are syntax highlighted and color coded so that they are easy to read

dbglib can also be used as conditionals in if statements while dynamically evaluating them (see examples below)

**Screenshot**

![image](https://github.com/savioxavier/dbglib/assets/38729705/1bf3d752-608c-4fc7-b42f-ec7a48072c4f)

> [!WARNING]
> Once imported, dbglib prints out a warning message at the very top (see above). This is to remind you that the module has to be removed as you're done with debugging. Trust me, you _definitely_ do not want to see random debug logs in production
>
> The best way to remove dbglib before deploying to production is by removing the main `from dbglib import dbg` import and see if your IDE can automatically detect undefined names and auto remove all `dbg()` calls

## Examples

`dbg` can be used for...

- regular variables

```py
a = 10
dbg(a)
```

- literals

```py
hello = "Hello, World!"
dbg(hello) # will print the length of string too
```

- expressions

```py
b = 15
dbg(b * 2) # 30
```

- functions

```py
def add(x, y):
    return x + y

dbg(add(10, 20)) # dbg result will output actual function call, with arguments used and result
```

- conditionals

```py
num = 5

if dbg(num < 10):
    print("It's less than ten!")

# here, dbg will print the boolean result of the conditional `num < 10` (which in this case is True) and actually evaluate the if block as normal and print the statement above
# If the dbg conditional evaluates to False, it will print the dbg output but it will not execute anything inside the if block
```

- iterables

```py
# lists
powers_of_two = [1, 2, 4, 8, 16, 32, 64]
dbg(powers_of_two) # will print the length of list too

# dicts
number_names = {1: "One", 2: "Two", 3: "Three"}
dbg(number_names) # will print the length of dict too

# works with other iterables like tuples, sets, etc...
# also works with deeply nested iterables too
```

## Attributions and special thanks

- [Rust's `dbg!(...)` macro](https://doc.rust-lang.org/nightly/std/macro.dbg.html) for inspiring me to make this in the first place
- [tylerwince/pydbg](https://github.com/tylerwince/pydbg) for helping me write an improved version of their debugger package
- [sharkdp/dbg-macro](https://github.com/sharkdp/dbg-macro) for helping me figure out the best interface for dbglib
