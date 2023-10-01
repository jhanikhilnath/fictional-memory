# Program to input marks of three subject along with the name of student and print the name along with the percentage

name = input("Enter your name: ")

print()
sub1 = float(input("Enter the marks obtained in subject 1(out of 40): "))
sub2 = float(input("Enter the marks obtained in subject 2(out of 40): "))
sub3 = float(input("Enter the marks obtained in subject 3(out of 40): "))

# Calculation
percentage = ((sub1 + sub2 + sub3) / (40 * 3)) * 100

print()
print("Hello", name, ", you have obtained a percentage aggregate of", percentage, "%")
