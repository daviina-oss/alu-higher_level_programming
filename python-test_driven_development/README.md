# python-test_driven_development

Test driven development in Python: writing the tests that describe a function,
with `doctest` (interactive tests in `.txt` files) and `unittest`.

Run the interactive tests from this directory:

```
python3 -m doctest -v ./tests/0-add_integer.txt
python3 -m doctest -v ./tests/2-matrix_divided.txt
python3 -m doctest -v ./tests/3-say_my_name.txt
python3 -m doctest -v ./tests/4-print_square.txt
python3 -m doctest -v ./tests/5-text_indentation.txt
```

Run the unittest file:

```
python3 -m unittest tests.6-max_integer_test
```

| File | Description |
|------|-------------|
| 0-add_integer.py | `add_integer(a, b=98)`: adds two integers or floats (floats are cast to int) |
| 2-matrix_divided.py | `matrix_divided(matrix, div)`: divides all the elements of a matrix |
| 3-say_my_name.py | `say_my_name(first_name, last_name="")`: prints a name |
| 4-print_square.py | `print_square(size)`: prints a square with `#` |
| 5-text_indentation.py | `text_indentation(text)`: prints a text with 2 new lines after `.`, `?` and `:` |
| 6-max_integer.py | `max_integer(list=[])`: finds the biggest integer of a list (given with the task) |
| tests/0-add_integer.txt ... tests/5-text_indentation.txt | Interactive tests (doctest) for tasks 0 to 4 |
| tests/6-max_integer_test.py | Unit tests (unittest) for `max_integer` |
