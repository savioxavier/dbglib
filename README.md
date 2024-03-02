# dbglib

> A macro for `print(some_variable)`-style debugging fans.
> 
> Debuggers are great. But sometimes you just don't have the time or patience to set up everything correctly and just want a quick way to inspect some values.

dbglib is a library that provides quick and easy debugging for your Python scripts

dbglib currently exports one function named `dbg`. It's inspired by Rust's `dbg!(...)` macro and provides a wide variety of information useful for debugging anything in your code

Usage:

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

**Screenshot**

![image](https://github.com/savioxavier/dbglib/assets/38729705/1bf3d752-608c-4fc7-b42f-ec7a48072c4f)

