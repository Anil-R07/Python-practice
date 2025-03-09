#print 1 to 10
n = 1
while n<=10:
    print(n)
    n = n+1

#print 2 to 20 only even numbers 
even = 1
while even<=20:
    if(even%2 == 0):
        print(even)
    even = even+1

even1 = 2
while even1 <= 20:
    print(even1)
    even1 += 2

#sum of natural numbers 
num = int(input("Enter the number: "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
    print(sum)
print("Sum of the natural number is: ",sum)

#ATM password with 3 attempts 
pin = 1234
attempt = 1
while attempt <= 3:
    password = int(input("Please enter the pin: "))
    if (password == pin):
        print("Correct password please collect your cash!")
        break
    else:
        print("You have entered a wrong password please try again")
    attempt += 1
  
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
i = 0
while i < len(days):
    if days[i] == "sunday":
        print(f"{days[i]}: Office closed")
    else:
        print(f"{days[i]}: 9 to 5")
    i += 1

#Bus ticket booking 
available_seats = 5
while available_seats > 0:
    print(f"{available_seats}: seats available")
    booking = input("Do you want to book a seat yes/no: ").lower()
    if booking == "yes":
        available_seats -= 1
        print(f"Seat booked!")
    else:
        print("No bookings made")
print("All the available seats are booked!")
