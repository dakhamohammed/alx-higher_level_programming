# 0x08. Python - More Classes and Objects

## General
   - Why Python programming is awesome
   - What is OOP
   - “first-class everything”
   - What is a class
   - What is an object and an instance
   - What is the difference between a class and an object or instance
   - What is an attribute
   - What are and how to use public, protected and private attributes
   - What is self
   - What is a method
   - What is the special __init__ method and how to use it
   - What is Data Abstraction, Data Encapsulation, and Information Hiding
   - What is a property
   - What is the difference between an attribute and a property in Python
   - What is the Pythonic way to write getters and setters in Python
   - What are the special __str__ and __repr__ methods and how to use them
   - What is the difference between __str__ and __repr__
   - What is a class attribute
   - What is the difference between a object attribute and a class attribute
   - What is a class method
   - What is a static method
   - How to dynamically create arbitrary new attributes for existing instances of a class
   - How to bind attributes to object and classes
   - What is and what does contain __dict__ of a class and of an instance of a class
   - How does Python find the attributes of an object or class
   - How to use the getattr function

### Files
1. **0-rectangle.py** & **0-main.py**
   - An empty class ***Rectangle*** that defines a rectangle.

2. **1-rectangle.py** & **1-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***0-rectangle.py***)
     - Private instance attribute: ***width***:
       - property ***def width(self):*** to retrieve it
       - property setter ***def width(self, value):*** to set it:
     - Private instance attribute: ***height***:
       - property ***def height(self):*** to retrieve it
       - property setter ***def height(self, value):*** to set it:
      

3. **2-rectangle.py** & **2-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***1-rectangle.py***)
     - Public instance method: ***def area(self):*** that returns the rectangle area.
     - Public instance method: ***def perimeter(self):*** that returns the rectangle perimeter.

4. **3-rectangle.py** & **3-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***2-rectangle.py***)
     - Print the rectangle with the character ***#***

5. **4-rectangle.py** & **4-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***3-rectangle.py***)
     - Return a string representation of the rectangle to be able to recreate a new instance by using ***eval()***

6. **5-rectangle.py** & **5-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***4-rectangle.py***)
     - Print the message ***Bye rectangle...*** (***...*** being 3 dots not ellipsis) when an instance of ***Rectangle*** is deleted

7. **6-rectangle.py** & **6-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***5-rectangle.py***)
     - Public class attribute ***number_of_instances***:
       - Initialized to ***0***
       - Incremented during each new instance instantiation
       - Decremented during each instance deletion

8. **7-rectangle.py** & **7-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***6-rectangle.py***)
     - Public class attribute ***print_symbol***:
       - Initialized to ***#***
       - Used as symbol for string representation
       - Can be any type

9. **8-rectangle.py** & **8-main.py**
   - Class ***Rectangle*** that defines a rectangle by: (based on ***7-rectangle.py***)
     - Static method ***def bigger_or_equal(rect_1, rect_2):*** that returns the biggest rectangle based on the area
       - ***rect_1*** must be an instance of ***Rectangle***, otherwise raise a ***TypeError*** exception with the message ***rect_1 must be an instance of Rectangle***
       - ***rect_2*** must be an instance of ***Rectangle***, otherwise raise a ***TypeError*** exception with the message ***rect_2 must be an instance of Rectangle***
       - Returns ***rect_1*** if both have the same area value

10. **9-rectangle.py** & **9-main.py**
    - Class ***Rectangle*** that defines a rectangle by: (based on ***8-rectangle.py***)
      - Class method ***def square(cls, size=0):*** that returns a new ***Rectangle*** instance with ***width == height == size***

