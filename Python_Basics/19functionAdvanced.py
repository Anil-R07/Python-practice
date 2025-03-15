#args
def add (*numbers):
    return sum(numbers) # using sum inbuilt function
sum = add(1,2,3)
print(sum)

def addition(*num):
    sum = 0
    for numbers in num: # using for loop
        sum += numbers
    print(sum)
addition(1,3,4,5)

#kwargs
def team_info(**info):
    for key, value in info.items():
        print(f"{key}:{value}")
team_info(name="RCB", place="Bengaluru", captain="Kohli", viceCaptain="Deviliers")

#lambda functions
triple = lambda x : x * 3
print(triple(7))

double = lambda x,y : x+y
print(double(4,5))

#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#nested functions
def outer(name):
    print(f"Hello {name} this is outer function")
    def inner():
        print(f"Hello {name} this is inner function")
    inner()
outer("Anil")
    