'''for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

for i in range (1, 21):
    print(i)

for i in range (20,0,-1):
    print(i)

#Print all even numbers between 1 and 50
for i in range (1, 51):
    if i%2 == 0:
        print(i)

#Print all odd numbers between 1 and 50
for i in range (1, 51):
    if i%2 !=0:
        print(i)

#Print the square of numbers from 1 to 10
for i in range (11):
    square = i*i
    print(square)

#Find the sum of numbers from 1 to N
n = int(input("Enter number: "))
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(sum)

#Print multiplication table of a number
# 5 x 1 = 5
n = int(input("Enter number: "))

for i in range (1, 11):
    print(f"{n} x {i} = {n*i}")

#Count how many numbers between 1 and 100 are divisible by 3
count = 0
for i in range (1, 101):
    if i% 3 == 0:
        count = count + 1
print(count)

#Find the Factorial number 
n = int(input("Enter the number: "))
fact = 1 
for i in range (1, n+1):
    fact = fact * i
print(fact)

for i in range(1,4):
    for j in range(1,4):
        print(i*j)

for i in range(3):
    print(i)
else:
    print("Loop finished")

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished")
'''