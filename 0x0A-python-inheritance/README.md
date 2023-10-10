# 0x0A. Python - Inheritance

## General
   - Why Python programming is awesome
   - What is a superclass, baseclass or parentclass
   - What is a subclass
   - How to list all attributes and methods of a class or instance
   - When can an instance have new attributes
   - How to inherit class from another
   - How to define a class with multiple base classes
   - What is the default class every class inherit from
   - How to override a method or attribute inherited from the base class
   - Which attributes or methods are available by heritage to subclasses
   - What is the purpose of inheritance
   - What are, when and how to use isinstance, issubclass, type and super built-in functions

### Files

1. **0-lookup.py** & **0-main.py**
   - Function that returns the list of available attributes and methods of an object.

2. **1-my_list.py** & **1-main.py** & **tests/1-my_list.txt**
   - Class MyList that inherits from list.

3. **2-is_same_class.py** & **2-main.py**
   - Function that returns True if the object is exactly an instance of the specified class ; otherwise False.

4. **3-is_kind_of_class.py** & **3-main.py**
   - Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

5. **4-inherits_from.py** & **4-main.py**
   - Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

6. **5-base_geometry.py**
   - Empty class BaseGeometry.

7. **6-base_geometry.py** & **6-main.py**
   - Class BaseGeometry (based on 5-base_geometry.py).

8. **7-base_geometry.py** & **7-main.py**
   - Class BaseGeometry (based on 6-base_geometry.py).

9. **8-rectangle.py** & **8-main.py**
   - Class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

10. **9-rectangle.py** & **9-main.py**
    - Class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

11. **10-square.py** & **10-main.py**
    - Class Square that inherits from Rectangle (9-rectangle.py).

12. **11-square.py** & **11-main.py**
    - Class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

13. **100-my_int.py** & **100-main.py**
    - Class MyInt that inherits from int.

14. **101-add_attribute.py** & **101-main.py**
    - Function that adds a new attribute to an object if it’s possible.

