import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Example usage:
radius = 5  # Replace this with the desired radius
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")
