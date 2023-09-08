# 0x02. Python - import & modules


### General
1. Why Python programming is awesome
2. How to import functions from another file
3. How to use imported functions
4. How to create a module
5. How to use the built-in function dir()
6. How to prevent code in your script from being executed when imported
7. How to use command line arguments with your Python programs

#### Files
1. 0-add.py
   - Python program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.

2. 1-calculation.py
   - Python program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

3. 2-args.py
   - Python program that prints the number of and the list of its arguments.

4. 3-infinite_add.py
   - Python program that prints the result of the addition of all arguments.

5. 4-hidden_discovery.py
   - Python program that prints all the names defined by the compiled module hidden_4.pyc.
     - Download hidden_4.pyc locally:
       - ```curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"```

6. 5-variable_load.py
   - Python program that imports the variable a from the file variable_load_5.py and prints its value.

7. 100-my_calculator.py
   - Python program that imports all functions from the file calculator_1.py and handles basic operations.
     - Usage: ./100-my_calculator.py a operator b
       - If the number of arguments is not 3, your program has to:
         - print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
         - exit with the value 1
       - operator can be:
         - + for addition
         - - for subtraction
         - * for multiplication
         - / for division
      - If the operator is not one of the above:
        - print Unknown operator. Available operators: +, -, * and / followed with a new line
        - exit with the value 1
      - You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
      - The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line

