# Day 1 – Python Essentials Recap

## Lists
- Ordered, mutable
- Methods: append(), insert(), pop(), remove(), slicing

## Tuples
- Ordered, immutable
- Used for fixed data

## Sets
- Unordered, unique elements
- Operations: union, intersection, difference

## Dictionaries
- Key-value pairs
- Methods: get(), keys(), values(), items()

## Functions
- def func_name(args):
- Default args, *args, **kwargs
- Recursion = function calling itself (base case + recursive case)

## Classes
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"{self.name}: {self.marks}")
