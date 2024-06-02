import math

def foo(radius):
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return (4/3) * math.pi * radius**3