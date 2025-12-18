import sys, os  # F401: 'os' imported but unused
import math

def bad_function(x,y):  # E231, E203: Missing spaces around comma
    """Poorly formatted function."""
    unused_var = 42  # F841: Local variable is assigned but never used
    result = x**2 + math.sqrt(y)
    return result

print(bad_function(1,4))  # E231: Missing space after comma
data = [1,2,3,4]