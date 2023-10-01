# Program to Input two numbers and print their sum, difference, product, remainder and quotient

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Actual Calculations
sum = num1+num2
prod = num1*num2
diff = num1-num2
quot = num1/num2
rema = num1 % num2

# Output
print()
print("The Sum of", num1, "and", num2, "is", sum)
print("The Difference of", num1, "and", num2, "is", diff)
print("The Product of", num1, "and", num2, "is", prod)
print("The Quotient on dividing", num1, "by", num2, "is", quot)
print("The Remainder on dividing", num1, "and", num2, "is", rema)
