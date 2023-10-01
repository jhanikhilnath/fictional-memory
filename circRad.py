# Program to input radius of a circle and output circumference and area


rad = float(input("Enter Radius of the circle(in cm): "))

PI = 3.1415

# Calculation

circum = 2 * rad * PI
area = PI * (rad ** 2)

# Output
print()
print("The Circumference of the circle is: ", circum, "cm")
print("The Area of the circle is: ", area, "cm²")
