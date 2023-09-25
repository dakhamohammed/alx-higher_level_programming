# 0x05. Python - Exceptions

## General
   - Why Python programming is awesome
   - What’s the difference between errors and exceptions
   - What are exceptions and how to use them
   - When do we need to use exceptions
   - How to correctly handle an exception
   - What’s the purpose of catching exceptions
   - How to raise a builtin exception
   - When do we need to implement a clean-up action after an exception

### File
1. **0-safe_print_list.py** & **0-main.py**
   - Python function that prints x elements of a list.
     - x represents the number of elements to print
     - x can be bigger than the length of my_list
     - Returns the real number of elements printed

2. **1-safe_print_integer.py** & **1-main.py**
   - Python function that prints an integer with "{:d}".format().
     - The integer should be printed followed by a new line
     - Returns True if value has been correctly printed (it means the value is an integer)
     - Otherwise, returns False

3. **2-safe_print_list_integers.py** & **2-main.py**
   - Python function that prints the first x elements of a list and only integers.
     - x represents the number of elements to access in my_list
     - x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
     - Returns the real number of integers printed

4. **3-safe_print_division.py** & **3-main.py**
   - Python function that divides 2 integers and prints the result.
     - The result of the division should print on the finally: section preceded by Inside result:
     - Returns the value of the division, otherwise: None

5. **4-list_division.py** & **4-main.py**
   - Python function that divides element by element 2 lists.
     - Returns a new list (length = list_length) with all divisions
     - If 2 elements can’t be divided, the division result should be equal to 0
     - If an element is not an integer or float:
       - print: wrong type
     - If the division can’t be done (/0):
       - print: division by 0
     - If my_list_1 or my_list_2 is too short
       - print: out of range

6. **5-raise_exception.py** & **5-main.py**
   - Python function that raises a type exception.

7. **6-raise_exception_msg.py** & **6-main.py**
   - Python function that raises a name exception with a message.

8. **100-safe_print_integer_err.py** & **100-main.py**
   - Python function that prints an integer.
     - Return True if value has been correctly printed
     - Return False if value not been printed and prints in stderr the error precede by Exception.

