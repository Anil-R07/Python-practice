fruits = ["apple", "banana", "cherry", "orange"]  #declaring th list 
print(fruits)  #print the list 

length = len(fruits)
print(length)

print (fruits[0]) #getting the specific element from a list 

fruits.append("water melon") #adding a new fruit to the list
print(fruits)

fruits.pop() #removing the last element in the list 
print(fruits)

fruits.pop(1) #removing the specific element from a list using index
print(fruits)

fruits.insert(1,"mango") #adding the element to the specific index
print(fruits)

fruits[2] = "pineapple"
print(fruits)

fruits.reverse()  #reverse a list
print(fruits)

index = fruits.index("mango")  #getting the index of watermelon
print(index)