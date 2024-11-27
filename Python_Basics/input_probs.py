
# Area of Rectangle 
w = int(input("Rectangle width: "))
b = int(input("Rectangle bredth: "))
rec_area = w*b
print(f"Area of the rectangle is {rec_area}")

# Area of circle (pir^2)
r = int(input("Radius of the circle: "))
circle_area = 3.14*r**2
print(f"Area of the circle is {circle_area}")

# Grocery Bill
item_name1 = input("Enter 1st item name: ")
item_price1 = float(input("Enter 1st item price: "))
item_name2 = input("Enter 2nd item name: ")
item_price2 = float(input("Enter 2nd item price: "))
item_name3 = input("Enter 3rd item name: ")
item_price3 =float(input("Enter 3rd item price: "))
total = item_price1+item_price2+item_price3
print(f"{item_name1} = {item_price1}rs")
print(f"{item_name2} = {item_price2}rs")
print(f"{item_name3} = {item_price3}rs")
print(f"Total = {total}rs")


