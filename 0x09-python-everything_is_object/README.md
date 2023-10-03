# 0x09. Python - Everything is object

## Why Python programming is awesome
   - What is an object
   - What is the difference between a class and an object or instance
   - What is the difference between immutable object and mutable object
   - What is a reference
   - What is an assignment
   - What is an alias
   - How to know if two variables are identical
   - How to know if two variables are linked to the same object
   - How to display the variable identifier (which is the memory address in the CPython implementation)
   - What is mutable and immutable
   - What are the built-in mutable types
   - What are the built-in immutable types
   - How does Python pass variables to functions

### File

1. **0-answer.txt**
   - Function name would you use to get the type of an object.
     - use type() function.

2. **1-answer.txt**
   - To get the variable identifier (which is the memory address in the CPython implementation).
     - id() function.

3. **2-answer.txt**
   - The following code, do **a** and **b** point to the same object
     ```bash
     >>> a = 89
     >>> b = 100
     ```
     - The answer is **no**

4. **3-answer.txt**
     - The following code, do **a** and **b** point to the same object
       ```bash
       >>> a = 89
       >>> b = 89
       ```
       - The answer is **yes**

5. **4-answer.txt**
   - The following code, do **a** and **b** point to the same object
       ```bash
       >>> a = 89
       >>> b = a
       ```
       - The answer is **yes**

6. **5-answer.txt**
   - The following code, do **a** and **b** point to the same object
       ```bash
       >>> a = 89
       >>> b = a + 1
       ```
       - The answer is **no**

7. **6-answer.txt**
   - These 3 lines print:
     ```nash
     >>> s1 = "Best School"
     >>> s2 = s1
     >>> print(s1 == s2)
     >>> True
     ```

