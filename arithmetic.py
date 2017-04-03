# Assigned to variables to have numbers calculated before return


def add(num1, num2):
    """Return the sum of two numbers"""
    add = num1 + num2
    return add


def subtract(num1, num2):
    """Return the difference of two numbers"""
    subtract = num1 - num2
    return subtract


def multiply(num1, num2):
    """Return the product of two numbers"""
    multiply = num1 * num2
    return multiply


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    divide = float(num1) / float(num2)
    return divide


def square(num):
    """Return the square of a number"""
    square = num * num
    return square


def cube(num):
    """Return the cube of a number"""
    cube = num * num * num
    return cube


def power(num, exponent):
    """Return num raised to the power of exponent"""
    power = num ** exponent
    return power


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    mod = num1 % num2
    return mod
