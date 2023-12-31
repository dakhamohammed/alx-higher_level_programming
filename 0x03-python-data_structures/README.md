# 0x03. Python - Data Structures: Lists, Tuples

## General
1. Why Python programming is awesome
2. What are lists and how to use them
3. What are the differences and similarities between strings and lists
4. What are the most common methods of lists and how to use them
5. How to use lists as stacks and queues
6. What are list comprehensions and how to use them
7. What are tuples and how to use them
8. When to use tuples versus lists
9. What is a sequence
10. What is tuple packing
11. What is sequence unpacking
12. What is the del statement and how to use it

### Files
1. **0-print_list_integer.py** & **0-main.py**
   - Python function that prints all integers of a list.

2. **1-element_at.py** & **1-main.py**
   - Python function that retrieves an element from a list like in C.
     - If idx is negative, the function should return None
     - If idx is out of range (> of number of element in my_list), the function should return None

3. **2-replace_in_list.py** & **2-main.py**
   - Python function that replaces an element of a list at a specific position (like in C).
     - If idx is negative, the function should not modify anything, and returns the original list
     - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list

4. **3-print_reversed_list_integer.py** & **3-main.py**
   - Python function that prints all integers of a list, in reverse order.

5. **4-new_in_list.py** & **4-main.py**
   - Python function that replaces an element in a list at a specific position without modifying the original list (like in C).
     - If idx is negative, the function should return a copy of the original list
     - If idx is out of range (> of number of element in my_list), the function should return a copy of the original list

6. **5-no_c.py** & **5-main.py**
   - Python function that removes all characters c and C from a string.

7. **6-print_matrix_integer.py** & 6-main.py
   - Python function that prints a matrix of integers.

8. **7-add_tuple.py** & **7-main.py**
   - Python function that adds 2 tuples.
     - Returns a tuple with 2 integers:
       - The first element should be the addition of the first element of each argument
       - The second element should be the addition of the second element of each argument
     - If a tuple is smaller than 2, use the value 0 for each missing integer
     - If a tuple is bigger than 2, use only the first 2 integers

9. **8-multiple_returns.py** & **8-main.py**
   - Python function that returns a tuple with the length of a string and its first character.
     - If the sentence is empty, the first character should be equal to None

10. **9-max_integer.py** & **9-main.py**
    - Python function that finds the biggest integer of a list.
      - If the list is empty, return None

11. **10-divisible_by_2.py** & **10-main.py**
    - Python function that finds all multiples of 2 in a list.
      - Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2

12. **11-delete_at.py** & **11-main.py**
    - Python function that deletes the item at a specific position in a list.
      - If idx is negative or out of range, nothing change (returns the same list)

13. **12-switch.py**
    - Switch value of a and b.

14. **13-is_palindrome.c**
    - Function in C that checks if a singly linked list is a palindrome.
      - Return: 0 if it is not a palindrome, 1 if it is a palindrome
      - An empty list is considered a palindrome

15. **100-print_python_list_info.c** & **100-test_lists.py**
    - C function that prints some basic info about Python lists.
      - Python version: 3.4
      - Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
      - OS: Ubuntu 14.04 LTS

