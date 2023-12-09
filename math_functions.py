def add_numbers(a, b):
	return a + b
	
def subtract_numbers(a, b):
	return a - b

def multiply_numbers(a, b):
	return a * b
	
def divide_numbers(a, b):
	return a / b

def power_numbers(a, b):
    return a ** b

def mod_numbers(a, b):
    return a % b


if __name__ == "__main__":
    print("adding", add_numbers(2, 4))
    print("Subtracting", subtract_numbers(9, 2))
    print("multiplying", multiply_numbers(5, 2))
    print("dividint", divide_numbers(10,2))
    print("squaring", power_numbers(3,2))
    print("modulo", mod_numbers(25,7))
