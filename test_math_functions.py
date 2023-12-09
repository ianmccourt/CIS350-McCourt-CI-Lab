from math_functions import *

def test_calc_addition():
	output = add_numbers(2, 4)
	assert output == 6
	
def test_calc_subtraction():
	output = subtract_numbers(2, 4)
	assert output == -2
	
def test_calc_multiplication():
	output = multiply_numbers(2, 4)
	assert output == 8
	
def test_calc_division():
	output = divide_numbers(10, 2)
	assert output == 5

def test_calc_power():
    output = power_numbers(3,2)
    assert output == 9

def test_calc_mod():
    output = mod_numbers(25, 7)
    assert output == 4


