'''
Program the takes two numbers as input from the user and check if:
   a. Both numbers are greater than 10
   b. At least one of the numbers is less than 5
   c. The first number is not greater than the second
'''
a = int(input("Please Enter First number: "))
b = int(input("Please Enter Second number: "))

c = str(a > 10 and b > 10)
print(f"The provided values are greater than 10: {c}")

d = str(a < 10 or b < 10)
print(f"The provided value/values are lesser than 10: {d}")

e = str(not(a > b))
print(f"The first provided value is not greater than the second value: {e}")
