fruits = ("apple","cherry","melon","orange")
print(fruits)

# fruits[1] = "mango" --> we can not reassign the tupple variable
print(fruits[1:3]) #slicing operations can be done on tupple 

number_tupple = (1,2,3,4,5,6,7,8)
print(number_tupple)

single_tupple = ("hey")  
print(type(single_tupple))  #output <class 'str'>

single_tupple1 = ("hey",) #in the end we need to add ,
print(type(single_tupple1)) #output <class 'tuple'>

#tupple operation 
add_tupple = fruits + number_tupple
print(add_tupple) #add both the tupples

#tupple repetation
tuple_repeat = fruits * 3
print(tuple_repeat)

number_repeat = (1,2,3,4) * 2
print(number_repeat)

#checking membership (is the element present in tupple)
print("cherry" in fruits) #O/P true

#Tupple methods 
print(fruits.count("apple")) #O/P 1
print(fruits.index("cherry")) #O/P 1