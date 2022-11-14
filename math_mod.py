from math import pi

def sq_foot():
    """
    Multiplies both values to return the area.
    Expects both values as integers
    """
    length = float(input('Length? '))
    width = float(input('Width? '))
    return length * width

def circumference():
    """
    Follows the formula to find the circumference given the radius of a circle.
    Expects the value as an integer.
    """
    radius = float(input('Radius? '))
    return 2 * pi * radius