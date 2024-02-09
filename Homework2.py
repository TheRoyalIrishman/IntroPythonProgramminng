import doctest
from math import sin, cos

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke", "Dr. Annexstein"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

# =============================================================================
# HELPER FUNCTION
# =============================================================================

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================

def fixed_point_iteration(f, startingPoint, tolerance = 1e-15):
    
    """
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)

    >>> fixed_point_iteration(lambda x: cos(x), 3.0)
    (0.7390851332151611, 86)
    """
    
    x = f(startingPoint)
    iterationCounter = 1
    
    while abs(x - f(x)) > tolerance:
        x = f(x)
        iterationCounter += 1
    
    return x, iterationCounter

def newton_find_zero(f, df, startingPoint, tolerance = 1e-15):
    """
    >>> newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0)
    (0.0, 4)   

    >>> newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0)
    (0.7390851332151607, 6)
    """
    
    x = f(startingPoint)
    
    iterationCounter = 1
    
    while abs(f(x)) > tolerance:
        n = newton_update(f, df)
        x = n(x)
        iterationCounter += 1
    
    return x, iterationCounter

if __name__ == "__main__":
  doctest.testmod(verbose=True)