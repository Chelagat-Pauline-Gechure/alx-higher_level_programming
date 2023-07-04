#!/usr/bin/python3
#!/usr/bin/python3
def add_integer(a, b=98):
"""
    Check if a and b are integers or floats
    Convert a and b to integers if they are floats
    Perform the addition
    Return the result as an integer
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    result = a + b
    return int(result)
