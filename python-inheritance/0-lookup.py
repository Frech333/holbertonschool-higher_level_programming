#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attribute and method names.
    """
    return [name for name in dir(obj)]

# Example usage:
class Example:
    def __init__(self):
        self.name = "Example"
    
    def say_hello(self):
        print("Hello!")

obj = Example()
attributes_and_methods = lookup(obj)
print(attributes_and_methods)
