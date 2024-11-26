
boy_name = input("Enter Boy Name: ")
boy_age = int(input("Enter Boy Age: "))
girl_name = input("Enter Girl name: ")
girl_age = int(input("Enter Girl Age:"))
diff = abs(boy_age - girl_age)   # abs = absolute it will ignore symbols and fractions 


print(boy_name+" loves "+girl_name+" age difference is "+ str(diff))

# formatted string
print(f"{boy_name} loves {girl_name} and their age difference is {diff}")