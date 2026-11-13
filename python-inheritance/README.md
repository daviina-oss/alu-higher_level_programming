# python-inheritance

Inheritance in Python: introspection, type checks, and a geometry class hierarchy.

| File | Description |
|------|-------------|
| 0-lookup.py | `lookup(obj)`: returns the attributes and methods of an object |
| 1-my_list.py | `MyList`: a list with a `print_sorted()` method (tests in `tests/1-my_list.txt`) |
| 2-is_same_class.py | `is_same_class(obj, a_class)`: exact instance of a class |
| 3-is_kind_of_class.py | `is_kind_of_class(obj, a_class)`: instance of a class or of a subclass |
| 4-inherits_from.py | `inherits_from(obj, a_class)`: instance of a strict subclass only |
| 5-base_geometry.py | Empty class `BaseGeometry` |
| 6-base_geometry.py | Adds `area()`, which is not implemented |
| 7-base_geometry.py | Adds `integer_validator()` (tests in `tests/7-base_geometry.txt`) |
| 8-rectangle.py | `Rectangle` with private, validated `width` and `height` |
| 9-rectangle.py | `Rectangle` with `area()` and a `[Rectangle] w/h` description |
| 10-square.py | `Square` inheriting from `Rectangle` |
| 11-square.py | `Square` with a `[Square] w/h` description |

Run the tests from this directory:

```
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```
