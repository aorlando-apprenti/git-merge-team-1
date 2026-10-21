# test_app.py
from app import add_numbers
from app import subtract_numbers
from app import multiply_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(3, 5) == -2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(1500, 294) == 1206

def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(-2, 5) == -10
    assert multiply_numbers(0, 7) == 0

   # Extra test cases for multiplication:
    assert multiply_numbers(-5, -5) == 25         # Testing two negative numbers
    assert multiply_numbers(1000, 2000) == 2000000 # Testing large numbers 
