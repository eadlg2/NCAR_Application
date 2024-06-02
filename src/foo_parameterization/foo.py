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

if __name__ == "__main__":
    while True:
        radius = input("Enter the radius of the sphere ('q' to quit): ")

        if (radius == "q"):
            break
        
        try:
            radius = float(radius)
        except ValueError:
            print("Please enter a valid number")
            continue

        try:
            volume = foo(radius)
            print(f"\nThe volume of the sphere is {volume}\n")
        except ValueError as e:
            print(e)