#args kwargs 
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