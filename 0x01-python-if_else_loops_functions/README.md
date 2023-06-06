# Project Name: Python - if/else, loops, functions

This project focuses on learning and practicing various concepts in Python programming, including if/else statements, loops, and functions. It consists of several tasks that cover different aspects of these topics.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome
- Understand the importance of indentation in Python
- Use if and if...else statements effectively
- Add comments to your code
- Assign values to variables
- Utilize while and for loops
- Differentiate Python's for loop from C's for loop
- Use break and continue statements
- Apply else clauses to loops
- Understand the purpose of the pass statement and when to use it
- Use the range function effectively
- Define and use functions in Python
- Understand the behavior of functions that do not use a return statement
- Understand variable scope
- Identify and interpret tracebacks
- Utilize arithmetic operators in Python

## Resources

Before starting the project, it is recommended to read or watch the following resources:

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until "4.6. Defining Functions" included)
- [IndentationError](https://docs.python.org/3/tutorial/errors.html#indentation-error)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd)
- [Learn to Program 2: Looping](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)
- `man` or `help` for:
  - python3

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should follow the Pycodestyle style guide (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### C Scripts

- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should follow the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

### Quiz Questions

During this project, you will encounter quiz questions that you need to answer successfully. Make sure to complete them to assess your understanding.

## Tasks

# Project Name: Python If-Else, Loops, and Functions

This project is a collection of Python programs that demonstrate the use of if-else statements, loops, and functions. Each program focuses on a specific concept and provides examples of its implementation. The programs are written in Python and can be executed directly from the command line.

## Table of Contents

1. [Positive Anything is Better Than Negative Nothing](#positive-anything-is-better-than-negative-nothing)
2. [The Last Digit](#the-last-digit)
3. [The Alphabet Game](#the-alphabet-game)
4. [Alphabet Soup](#alphabet-soup)
5. [Hexadecimal Printing](#hexadecimal-printing)
6. [00...99](#00...99)
7. [Combinations of Two Digits](#combinations-of-two-digits)
8. [Is Lowercase](#is-lowercase)
9. [To Uppercase](#to-uppercase)
10. [Print Last Digit](#print-last-digit)
11. [Addition of Two Integers](#addition-of-two-integers)

## Positive Anything is Better Than Negative Nothing

### Description
This program assigns a random signed number to the variable `number` each time it is executed. The program checks whether the number stored in `number` is positive or negative and prints the result.

### Usage
The program can be executed by running the following command:
```
$ ./0-positive_or_negative.py
```

### The Last Digit

### Description
This program assigns a random signed number to the variable `number` each time it is executed. The program prints the last digit of the number stored in `number` along with additional information.

### Usage
The program can be executed by running the following command:
```
$ ./1-last_digit.py
```

### The Alphabet Game

### Description
This program prints the ASCII alphabet in lowercase, without a new line.

### Usage
The program can be executed by running the following command:
```
$ ./2-print_alphabet.py
```

### Alphabet Soup

### Description
This program prints the ASCII alphabet in lowercase, excluding the letters 'q' and 'e', without a new line.

### Usage
The program can be executed by running the following command:
```
$ ./3-print_alphabt.py
```

### Hexadecimal Printing

### Description
This program prints numbers from 0 to 98 in decimal and hexadecimal format.

### Usage
The program can be executed by running the following command:
```
$ ./4-print_hexa.py
```

### 00...99

### Description
This program prints numbers from 0 to 99, separated by commas and a space.

### Usage
The program can be executed by running the following command:
```
$ ./5-print_comb2.py
```

### Combinations of Two Digits

### Description
This program prints all possible different combinations of two digits, separated by commas and a space.

### Usage
The program can be executed by running the following command:
```
$ ./6-print_comb3.py
```

### Is Lowercase

### Description
This program defines a function `islower(c)` that checks whether a character `c` is lowercase or not.

### Usage
The `islower(c)` function can be used in your own Python code by importing the module and calling the function. Here's an example:
```python
from 7-islower import islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
```
