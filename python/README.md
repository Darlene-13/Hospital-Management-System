### SHORT NOTES IN PYTHON

1. isintance() function in python.
- The isinstance() function is used to check if an object is an instance or a subclass of a class or a tuple of classes.
- Syntax: isinstance(object, classinfo)
- It returns True if the object is an instance or subclass of classinfo, otherwise it return False.
- Example:
```aiignore
class Animal:
    pass
    class Dog(Animal):
        pass
        print(isinstance(Dog(), Animal))  
       
# The output should be True because Dog is a subclass of Animal



x = 10
print(ininstance(x, int))

# The output should be True because x is an instance of int.
```

2. Difference between a class method, static method and instance method in python.
- Instance Method:
  - An instance method is a method that is defined within a class and is called on an instance of that class.
  - It takes self as the first parameter, which refers to the instance of the class.
- Static Method:
  - A static method is a method that is defined within a class but does not take self as the first parameter. 
  - It is called on the class itself rather than on an instance of the class.
- Class Method:
  - A class method is a method that is defined within a class and takes cls as the first parameter, which refers to the class itself.
  - It is called on the class itself rather than on an instance of the class.