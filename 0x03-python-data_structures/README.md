# Python Data Structures

This repository contains Python programs that demonstrate various data structure operations.

## Task List

1. [Print a list of integers](./0x03-python-data_structures/0-print_list_integer.py)
   - Write a function that prints all integers of a list.
   - Prototype: `def print_list_integer(my_list=[])`
   - Format: one integer per line.
   - You are not allowed to import any module.

2. [Secure access to an element in a list](./0x03-python-data_structures/1-element_at.py)
   - Write a function that retrieves an element from a list like in C.
   - Prototype: `def element_at(my_list, idx)`
   - If `idx` is negative, the function should return None.
   - If `idx` is out of range, the function should return None.
   - You are not allowed to import any module.

3. [Replace element](./0x03-python-data_structures/2-replace_in_list.py)
   - Write a function that replaces an element of a list at a specific position (like in C).
   - Prototype: `def replace_in_list(my_list, idx, element)`
   - If `idx` is negative, the function should not modify anything, and return the original list.
   - If `idx` is out of range, the function should not modify anything, and return the original list.
   - You are not allowed to import any module.

4. [Print a list of integers... in reverse!](./0x03-python-data_structures/3-print_reversed_list_integer.py)
   - Write a function that prints all integers of a list, in reverse order.
   - Prototype: `def print_reversed_list_integer(my_list=[])`
   - Format: one integer per line.
   - You are not allowed to import any module.

5. [Replace in a copy](./0x03-python-data_structures/4-new_in_list.py)
   - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
   - Prototype: `def new_in_list(my_list, idx, element)`
   - If `idx` is negative, the function should return a copy of the original list.
   - If `idx` is out of range, the function should return a copy of the original list.
   - You are not allowed to import any module.

6. [Can you C me now?](./0x03-python-data_structures/5-no_c.py)
   - Write a function that removes all characters 'c' and 'C' from a string.
   - Prototype: `def no_c(my_string)`
   - The function should return the new string.
   - You are not allowed to import any module.

7. [Lists of lists = Matrix](./0x03-python-data_structures/6-print_matrix_integer.py)
   - Write a function that prints a matrix of integers.
   - Prototype: `def print_matrix_integer(matrix=[[]])`
   - You are not allowed to import any module.

8. [Tuples addition](./0x03-python-data_structures/7-add_tuple.py)
   - Write a function that adds 2 tuples.
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=())`
   - The function should return a tuple with 2 integers.
   - You are not allowed to import any module.

## Task 9: Find the max

Write a function `max_integer(my_list=[])` that finds the biggest integer in a list. The function returns the maximum value, or `None` if the list is empty. The following restrictions apply:
- You can assume that the list only contains integers.
- You are not allowed to import any modules.
- You are not allowed to use the built-in `max()` function.

**Example:**
```python
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
```
Output:
```
Max: 90
```

## Task 10: Only by 2

Write a function `divisible_by_2(my_list=[])` that finds all the multiples of 2 in a list. The function returns a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2. The new list should have the same size as the original list. The following restrictions apply:
- You are not allowed to import any modules.

**Example:**
```python
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
```
Output:
```
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```

## Task 11: Delete at

Write a function `delete_at(my_list=[], idx=0)` that deletes the item at a specific position in a list. If the index is negative or out of range, nothing changes (the function returns the same list). The following restrictions apply:
- You are not allowed to use the `pop()` method.
- You are not allowed to import any modules.

**Example:**
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
```
Output:
```
[1, 2, 3, 5]
[1, 2, 3, 5]
```

## Task 12: Switch

Complete the source code in `12-switch.py` to switch the values of variables `a` and `b`. Your code should be inserted where the comment is (line 4). The program should be exactly 5 lines long.

**Example:**
```bash
$ ./12-switch.py
a=10 - b=89
```

## Task 13: Linked list palindrome

Write a function `is_palindrome(listint_t **head)` in C that checks if a singly linked list is a palindrome. The function returns `1` if the list is a palindrome, and `0` if it is not. An empty list is considered a palindrome.

**Example:**
```c
listint_t *head;

head = NULL;
add_nodeint_end(&head, 1

);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 1);
print_listint(head);

if (is_palindrome(&head) == 1)
    printf("Linked list is a palindrome\n");
else
    printf("Linked list is not a palindrome\n");

free_listint(head);
```
Output:
```
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
```

---

Please note that the C code provided for Task 13 assumes the existence of additional files (`linked_lists.c` and `lists.h`) in order to compile and run the program. Make sure you have those files available in the appropriate directory.

I hope this helps! Let me know if you have any other questions.
