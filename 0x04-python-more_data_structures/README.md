# 0x04. Python - More Data Structures: Set, Dictionary

Python project covering concepts of sets, dictionaries, and related functions.

## Table of Contents
* [Description](#description)
* [Learning Objectives](#learning-objectives)
* [Resources](#resources)
* [Requirements](#requirements)

## Description
This project focuses on expanding your knowledge of Python data structures, specifically sets and dictionaries. It includes tasks that cover the usage of sets, common set methods, iterating over sets, dictionaries and their methods, iterating over dictionaries, lambda functions, and map, reduce, and filter functions.

## Learning Objectives
Upon completing this project, you should be able to explain the following concepts without the help of external resources:
* The awesomeness of Python programming
* Sets and their usage
* Common set methods and their application
* Determining when to use sets instead of lists
* Iterating over a set
* Dictionaries and their usage
* Choosing between dictionaries, lists, and sets
* Understanding dictionary keys
* Iterating over a dictionary
* Lambda functions and their purpose
* Map, reduce, and filter functions

## Resources
To enhance your understanding of the concepts covered in this project, you may refer to the following resources:
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Lambda, filter, reduce, and map](https://www.youtube.com/watch?v=1GAC6KQUPeg)
* [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
* All files should end with a new line
* The first line of all files should be `#!/usr/bin/python3`
* A `README.md` file at the root of the project folder is mandatory
* Your code should adhere to the pycodestyle (version 2.8.\*) guidelines
* All files must be executable
* The length of your files will be tested using `wc`

Please make sure to adhere to the requirements and guidelines specified above to successfully complete this project. Avoid plagiarism and copying someone else's work, as it is strictly prohibited and may lead to removal from the program.
# ALX Higher Level Programming - Python More Data Structures

This repository contains Python scripts that demonstrate various tasks related to more data structures in Python.

## Tasks

1. **Squared Simple**
   - Prototype: `def square_matrix_simple(matrix=[])`
   - Description: Computes the square value of all integers in a matrix and returns a new matrix with the squared values. The original matrix should not be modified. Regular loops, map, etc. are allowed, but importing modules is not.
   - Example:
     ```python
     matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
     ]
     new_matrix = square_matrix_simple(matrix)
     print(new_matrix)
     print(matrix)
     ```
     Output:
     ```
     [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
     ```

2. **Search and Replace**
   - Prototype: `def search_replace(my_list, search, replace)`
   - Description: Replaces all occurrences of an element with another element in a new list. Importing modules is not allowed.
   - Example:
     ```python
     my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
     new_list = search_replace(my_list, 2, 89)
     print(new_list)
     print(my_list)
     ```
     Output:
     ```
     [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
     [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
     ```

3. **Unique Addition**
   - Prototype: `def uniq_add(my_list=[])`
   - Description: Adds all unique integers in a list only once and returns the sum. Importing modules is not allowed.
   - Example:
     ```python
     my_list = [1, 2, 3, 1, 4, 2, 5]
     result = uniq_add(my_list)
     print("Result: {:d}".format(result))
     ```
     Output:
     ```
     Result: 15
     ```

4. **Present in Both**
   - Prototype: `def common_elements(set_1, set_2)`
   - Description: Returns a set of common elements between two sets. Importing modules is not allowed.
   - Example:
     ```python
     set_1 = {"Python", "C", "Javascript"}
     set_2 = {"Bash", "C", "Ruby", "Perl"}
     c_set = common_elements(set_1, set_2)
     print(sorted(list(c_set)))
     ```
     Output:
     ```
     ['C']
     ```
# 0x04. Python - More Data Structures: Set, Dictionary

This repository contains solutions to the tasks assigned in the "0x04. Python - More Data Structures: Set, Dictionary" project as part of the ALX Higher Level Programming curriculum. The project focuses on enhancing Python programming skills by working with sets, dictionaries, and various related operations.

### 5. Number of keys

Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module

### 6. Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted in alphabetical order
- Only sort keys at the first level (do not sort keys of dictionaries inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module

### 7. Update dictionary

Write a function that replaces or adds a key/value in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- The `key` argument will always be a string
- The `value` argument can be of any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn't exist in the dictionary, it will be created
- You are not allowed to import any module

### 8. Simple delete by key

Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- The `key` argument will be a string
- If the key doesn't exist, the dictionary won't change
- You are not allowed to import any module

### 9. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are integers
- The function should return a new dictionary
- You are not allowed to import any module

### 10. Best score

Write a function that returns the key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are integers
- If no score is found, return `None`
- You can assume all students have a different score
- You are not allowed to import any module

### 11. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def

 multiply_list_map(my_list=[], number=0):`
- The function should return a new list
- The new list should have the same length as the original list
- Each value in the new list should be multiplied by `number`
- The original list should not be modified
- You are not allowed to import any module
- You have to use `map`
- Your code should not be more than 3 lines

### 12. Roman to Integer

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- You can assume the number will be between 1 and 3999.
- `roman_to_int` must return an integer.
- If the `roman_string` is not a string or `None`, return 0.

## Repository

The code is stored in the following GitHub repository: [alx-higher_level_programming](https://github.com/username/alx-higher_level_programming)

### Directory: 0x04-python-more_data_structures

The relevant files for the tasks are located in the directory `0x04-python-more_data_structures` of the repository.

#### File: 5-number_keys.py

Contains the implementation of the `number_keys` function that returns the number of keys in a dictionary.

#### File: 6-print_sorted_dictionary.py

Contains the implementation of the `print_sorted_dictionary` function that prints a dictionary by ordered keys.

#### File: 7-update_dictionary.py

Contains the implementation of the `update_dictionary` function that replaces or adds a key/value in a dictionary.

#### File: 8-simple_delete.py

Contains the implementation of the `simple_delete` function that deletes a key in a dictionary.

#### File: 9-multiply_by_2.py

Contains the implementation of the `multiply_by_2` function that returns a new dictionary with all values multiplied by 2.

#### File: 10-best_score.py

Contains the implementation of the `best_score` function that returns the key with the biggest integer value.

#### File: 11-multiply_list_map.py

Contains the implementation of the `multiply_list_map` function that returns a list with all values multiplied by a number without using any loops.

#### File: 12-roman_to_int.py

Contains the implementation of the `roman_to_int` function that converts a Roman numeral to an integer.

## Usage

To use the code, follow these steps:

1. Clone the repository using the following command:

   ```
   git clone https://github.com/username/alx-higher_level_programming.git
   ```

2. Navigate to the `0x04-python-more_data_structures` directory:

   ```
   cd alx-higher_level_programming/0x04-python-more_data_structures
   ```

3. Open the desired Python file in your preferred text editor.

4. Run the Python file using the `python3` command followed by the name of the file. For example:

   ```
   python3 5-number_keys.py
   ```

   The output of the program will be displayed in the terminal.
