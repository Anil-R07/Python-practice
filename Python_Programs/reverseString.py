s = input("Please type the word: ")

# Method 1 --> using split function 
print(s[::-1])

# Method 2 --> using for loop 
rev = ""
for ch in s:
    rev= ch + rev
print (rev)
    