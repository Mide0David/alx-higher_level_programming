# 0x02. Python - import & modules

Resources
Read or watch:

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

**man or help**:

- `python3`

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.\*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Import a simple function from a simple file

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- You have to use `print` function with string format to display integers.
- You have to assign:
  - the value `1` to a variable called `a`
  - the value `2` to a variable called `b`
- and use those two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported - by using `__import__`, like the example below:

```bash
$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

$ ./0-add.py
1 + 2 = 3
$ cat 0-import_add.py
__import__("0-add")
$ python3 0-import_add.py
$
```
## Task 1: My first toolbox!

**File**: 1-calculation.py

This program imports functions from the file `calculator_1.py` and performs various mathematical operations.

Example usage and output:
```
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

## Task 2: How to make a script dynamic!

**File**: 2-args.py

This program prints the number of and the list of its arguments.

Example usage and output:
```
$ ./2-args.py
0 arguments.

$ ./2-args.py Hello
1 argument:
1: Hello

$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```

## Task 3: Infinite addition

**File**: 3-infinite_add.py

This program prints the result of the addition of all arguments.

Example usage and output:
```
$ ./3-infinite_add.py
0

$ ./3-infinite_add.py 79 10
89

$ ./3-infinite_add.py 79 10 -40 -300 89
-162
```

## Task 4: Who are you?

**File**: 4-hidden_discovery.py

This program prints all the names defined by the compiled module `hidden_4.pyc`.

Example usage and output:
```
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
```

## Task 5: Everything can be imported

**File**: 5-variable_load.py

This program imports the variable `a` from the file `variable_load_5.py` and prints its value.

Example usage and output:
```
$ ./5-variable_load.py
98
```

## Task 6: Build my own calculator!

**File**: 100-my_calculator.py

This program imports all functions from the file `calculator_1.py` and handles basic operations.

Example usage and output:
```
$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1

$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0

$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
```

## Task 7: Easy print

**File**: 101-easy_print.py

This program prints `#pythoniscool` in the standard output.

Example usage and output:
```
$ ./101-easy_print.py
#pythoniscool
```

## Task 8: ByteCode -> Python #3

**File**: 102-magic_calculation.py

This program defines the Python function `magic_calculation(a, b)` that performs the same operations as the given Python bytecode.

---

Feel free to explore the code files in this repository to understand the implementation of each task.

**

 from my-program.md.
