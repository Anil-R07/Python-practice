#check if the given number is even 
number = int(input("Enter the number"))
if number %2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")


age = int(input("Enter your age: "))
if age >= 18:
    print("You are elegible to vote")
else:
    print("You are not eligible to vote")


#if elif 
time = 9 
if time == 9:
    print("its a time to login")
elif time >= 10 and time<= 12:
    print("you are late to office")
elif time >= 1:
    print("You came at lunch time")
else:
    print("You are absent")

#nested if 
day = "Sunday"
is_raining = False
is_sunny = True
if day == "Sunday":
    if not is_raining:
        if not is_sunny:
            print("lets go to Temple")
        else:
            print("too sunny lets go another day")
    else:
        print("its raining lets plan another day")

#problem 1
# Program to declare eligibility for bus pass
def buspass(age):
    if age <= 5:
        print("Bus pass is free below 5 years")
    elif age >= 60:
        print("You are applicable for senior sitizen discount")  
    elif age > 5 and age < 60:
        print("You have to pay full amount") 
buspass(int(input("Please enter your age: ")))