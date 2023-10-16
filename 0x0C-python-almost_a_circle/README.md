# 0x0C. Python - Almost a circle

## General
   - What is Unit testing and how to implement it in a large project
   - How to serialize and deserialize a Class
   - How to write and read a JSON file
   - What is *args and how to use it
   - What is **kwargs and how to use it
   - How to handle named arguments in a function


### Files:

[] Task-0 **Unit tested and be PEP 8 validation""

[x] Task-1  **models/base.py** & **models/__init__.py**
   - Class ***Base***:
     - private class attribute ***__nb_objects = 0***
       - if ***id*** is not ***None***, assign the public instance attribute ***id*** with this argument value - you can assume ***id*** is an integer and you don’t need to test the type of it
       - otherwise, increment ***__nb_objects*** and assign the new value to the public instance attribute ***id***
     - This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs).

[x] Task-2 **models/rectangle.py** & **1-main.py**
   - Class ***Rectangle*** that inherits from ***Base***:
     - Private instance attributes, each with its own public getter and setter:
       - ***__width*** -> ***width***
       - ***__height*** -> ***height***
       - ***__x*** -> ***x***
       - ***__y*** -> ***y***
     - Class constructor: ***def __init__(self, width, height, x=0, y=0, id=None):***
       - Call the super class with ***id*** - this super call with use the logic of the ***__init__*** of the Base class
       - Assign each argument ***width***, ***height***, ***x*** and ***y*** to the right attribute

[x] Task-3 **models/rectangle.py** & **2-main.py**
   - Update the class ***Rectangle*** by adding validation of all setter methods and instantiation (***id*** excluded):
     - If the input is not an integer, raise the ***TypeError*** exception with the message: ***<name of the attribute> must be an integer***. Example: ***width must be an integer***
     - If ***width*** or ***height*** is under or equals ***0***, raise the ***ValueError*** exception with the message: ***<name of the attribute> must be > 0***. Example: ***width must be > 0***
     - If ***x*** or ***y*** is under ***0***, raise the ***ValueError*** exception with the message: ***<name of the attribute> must be >= 0***. Example: ***x must be >= 0***

[x] Task-4 **models/rectangle.py** & **3-main.py**
   - Update the class ***Rectangle*** by adding the public method ***def area(self):*** that returns the area value of the ***Rectangle*** instance.

[x] Task-5 **models/rectangle.py** & **4-main.py**
   - Update the class ***Rectangle*** by adding the public method ***def display(self):*** that prints in stdout the ***Rectangle*** instance with the character ***#***

[x] Task-6 **models/rectangle.py** & **5-main.py**
   - Update the class ***Rectangle*** by overriding the ***__str__*** method so that it returns ***[Rectangle] (***<id>***) ***<x>***/***<y>*** - ***<width>***/***<height>******

[x] Task-7 **models/rectangle.py** & **6-main.py**
   - Update the class ***Rectangle*** by improving the public method ***def display(self):*** to print in stdout the ***Rectangle*** instance with the character ***#*** by taking care of ***x*** and ***y***

[x] Task-8 **models/rectangle.py** & **7-main.py**
   - Update the class ***Rectangle*** by adding the public method ***def update(self, *args):*** that assigns an argument to each attribute:
     - 1st argument should be the ***id*** attribute
     - 2nd argument should be the ***width*** attribute
     - 3rd argument should be the ***height*** attribute
     - 4th argument should be the ***x*** attribute
     - 5th argument should be the ***y*** attribute

[x] Task-9 **models/rectangle.py** & **8-main.py**
   - Update the class ***Rectangle*** by updating the public method ***def update(self, *args):*** by changing the prototype to ***update(self, *args, **kwargs)*** that assigns a key/value argument to attributes:
     - *****kwargs*** can be thought of as a double pointer to a dictionary: key/value
     - *****kwargs*** must be skipped if ****args*** exists and is not empty
     - Each key in this dictionary represents an attribute to the instance

[x] Task-10 **models/square.py** & **9-main.py**
    - Class ***Square*** that inherits from Rectangle.

[x] Task-11 **models/square.py** & **10-main.py**
    - Update the class ***Square*** by adding the public getter and setter ***size***

[x] Task-12 **models/square.py** & **11-main.py**
    - Update the class ***Square*** by adding the public method ***def update(self, *args, **kwargs)*** that assigns attributes:
      - ****args*** is the list of arguments - no-keyworded arguments
        - 1st argument should be the ***id*** attribute
        - 2nd argument should be the ***size*** attribute
        - 3rd argument should be the ***x*** attribute
        - 4th argument should be the ***y*** attribute
      - *****kwargs*** can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
      - *****kwargs*** must be skipped if *args exists and is not empty

[ ] Task-13
[ ] Task-14
[ ] Task-15
[ ] Task-16
[ ] Task-17
[ ] Task-18
[ ] Task-19

