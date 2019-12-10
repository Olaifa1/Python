# calculate the area and circumference of a circle from its radius
# step 1
import math

radius_str = input("Enter the radius of the circle: ")
radius_int = int(radius_str)


area = math.pi * math.pow(radius_int, 2)

circumference = 2 * math.pi * radius_int

print("The area is ", area, "The area is ", circumference)

