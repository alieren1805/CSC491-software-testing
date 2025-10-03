import math
from numbers import Real
import numpy as np

def add(a: int, b: int) -> int:
    """Return a + b."""
    if type(a) == int and type(b) == int:
        return a + b
    raise TypeError

def div(a: float, b: float) -> float:
    """Return a / b. Raise ValueError if b == 0."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
    # TODO: to uncomment the below line and comment the above line and observe the effects
    # return float(np.float32(a) / np.float32(b))

def clamp(x: float, low: float, high: float) -> float:
    """Confine x to [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    if math.isnan(x) or math.isnan(low) or math.isnan(high):
        raise ValueError
    if math.isinf(x) or math.isinf(low) or math.isinf(high):
        raise ValueError
    return max(low, min(x, high))
