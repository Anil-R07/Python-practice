url = "https://api.company.com/v1/users"

endpoint = url.split("/")[-1]
print(endpoint)

    

#1 --- Positive, Negative, and Zero
n = float(input("Provide the number: "))
if n > 0:
    print(f"{n} is Positive number")
elif n < 0:
    print(f"{n} is Negative number")
else:
    print(f"{n} is Zero")

#2 --- Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


#3 --- Find Greatest of Two Numbers
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} equals to {num2}")


#4 Find Greatest of Three Numbers
a = int(input("Number one: "))
b = int(input("number two: "))
c = int(input("number three: "))

if a > b and a > c:
    print(f"{a} is largest")
elif b > a and b > c:
    print(f"{b} is largest")
elif c > a and c > b:
    print(f"{c} is largest")
elif a == b == c:
    print(f"{a} = {b} = {c}")
else:
    print("Two numbers are equal and largest")

# single line code
print(max(a, b, c))

# find Leap year 
year = int(input("Enter the Year: "))
if (year%4 == 0 and year%100 != 0) or (year%400) == 0:
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a leap year")

# Student Grade Program
marks = int(input("Enter the marks: "))
if marks <0 or marks > 100:
    print("Invalid number provide a number between 0 to 100")
elif marks>= 90:
    print(f"Congratulations you have scored A grade")
elif marks>=75:
    print(f"Congratulations you have scored B grade")
elif marks>=60:
    print(f"Do better next time, you have scored C grade")
elif marks>=50:
    print(f"Do better next time, you have scored D grade")
else:
    print("Better luck next time you have failed")


# Check Largest Among Three Numbers (Using Nested If)
number = input("Provide 3 numbers: ").split()
if len(number) != 3:
    print("Please provide 3 numbers")
else:
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    if a>b and a>c:
        print(f"{a} is largest")
    elif b>a and b>c:
        print(f"{b} is largest")
    elif c>a and c>b:
        print(f"{c} is largest")

        #Or
    
if len(number) != 3:
    print("Please provide 3 numbers")
else:
    print(f"{max(number)} is largest")

#Check Triangle Validity
triangle = input("provide base, height, width: ").split()
if len(triangle)!=3:
    print("Please provide 3 values")
else:
    a = int(triangle[0])
    b = int(triangle[1])
    c = int(triangle[2])
    if a + b > c and a + c > b and b + c > a:
        print("Its a valid triangle")
    else:
        print("its a invalid triangle")

# ATM Withdrawal Program

Conditions:
    Balance = 10000
    If withdrawal amount > balance → "Insufficient balance"
    If withdrawal amount > 5000 → "Limit exceeded"
    Otherwise allow withdrawal 

balance = 10000
ammount = int(input("Enter the ammount you want to withdrawn: "))
if ammount > balance:
    print(f"Insufficient fund")
elif ammount > 5000:
    print(f"Limit exceeded")
else:
    balance = balance - ammount
    print(f"{ammount} withdrwn from your account, your balance is {balance}")

# Number Type Checker
Check if number is:
    Positive Even
    Positive Odd
    Negative Even
    Negative Odd
    Zero 

num = int(input("Enter the number: "))
if num == 0:
    print(f"{num} is Zero")
elif num % 2 == 0:
        if num > 0:
            print(f"{num} is Positive Even")
        elif num < 0:
            print(f"{num} is Negative Even")
else:
        if num > 0:
            print(f"{num} is Positive Odd")
        elif num < 0:
            print(f"{num} is Negative Odd")

