def ipl():
    print("Tala Ipl 2025")

ipl()

def team(name):
    if name == "RCB":
        print("King Kohli")
    elif name == "CSK":
        print("MS Dhoni")
    else:
        print("No player found")
team(input("Please Enter the team name: "))

#add 2 numbers 
def add(a, b):
    print(f"sum of the provided number is: {a+b}")
num1 = int(input("please provide the first number: "))
num2 = int(input("please provide the second number: "))
add(num1, num2)

#default parameter 
def car(favcar = "Defender110"):
    print(f"{favcar} is my favorite car")
car("ferari")

#local and global variable 
def variable():
    name = "Anil"
    print(name)
    print(name1)
name1 = "Akash"
variable()