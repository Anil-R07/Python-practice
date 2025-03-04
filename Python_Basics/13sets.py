set1 = {1,2,3,4,5,6,7,8}
set2 = {"Ind", "Aus", "Afg", "Nzl"}
set3 = {10,9,8,7,12,13}

print(set1)
print(set2)

#set operations 
union_set =  set1 | set3
print(union_set) #combine both

intersection_set = set1 & set3
print(intersection_set) #get the common element present in both set 

difference_set = set1 - set3
print(difference_set) #elements from 1st not in second

symmetric_set = set1 ^ set3
print(symmetric_set) #gets the elements not common in both or ignoring the common 

#set methods 
set2.add("Pak")
print(set2)

set2.remove("Pak")
print(set2)

set2.discard("Ban")
print(set2)
 
set2.pop()
print(set2)