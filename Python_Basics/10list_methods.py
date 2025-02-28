l = [100,300,600,300,200,500,400]

length = len(l)  #find the lenght of the list
print(length)  

sort = sorted(l)  #sort the data using sorted function
print(sort)  

l.sort()  #sort the data using sort function
print(l)

l.reverse()  #Reverse the list
print(l)

count = l.count(300)  #count the occurance of the element
print(count)

l.pop(3)  #removes the 3rd index
print(l)
 
index = l.index(400)  #returns the index of the element 400
print(index)

sum = sum(l)  #adding the all the elements in a list
print(sum)

l.clear()  #remove all the data from list
print(l)


#Advanced topic 
numbers = [1, 2,"Anil", "Teju", 3, 4]
# sum(numbers) ---> This will give type error since it containd string 
new_numbers = [x for x in numbers if isinstance(x, (int, float))] #o/p --> [1, 2, 3, 4]
print(new_numbers)
total = sum(new_numbers)
print(total)
