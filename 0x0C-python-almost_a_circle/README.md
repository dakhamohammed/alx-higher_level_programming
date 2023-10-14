# 0x0C. Python - Almost a circle

## General
   - What is Unit testing and how to implement it in a large project
   - How to serialize and deserialize a Class
   - How to write and read a JSON file
   - What is *args and how to use it
   - What is **kwargs and how to use it
   - How to handle named arguments in a function


### Files:

1. **models/base.py** & **models/__init__.py**
   - Class ***Base***:
     - private class attribute ***__nb_objects = 0***
       - if ***id*** is not ***None***, assign the public instance attribute ***id*** with this argument value - you can assume ***id*** is an integer and you don’t need to test the type of it
       - otherwise, increment ***__nb_objects*** and assign the new value to the public instance attribute ***id***
     - This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs).

