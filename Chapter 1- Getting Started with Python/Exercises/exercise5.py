import math

# Accept the radius from the user as input
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula: π * r^2
area = math.pi * (radius ** 2)

# Print the computed area
print(f"The area of the circle with radius {radius} is: {area:.2f}")

