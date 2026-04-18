def missingNumber(num):
    n = len(num)+1
    actual = sum(num)
    expected = n * (n+1) // 2
    return expected - actual
num = list(map(int, input("enter the number with space: ").split()))
result = missingNumber(num)
print(result)

'''input("Enter numbers separated by space: ")
expected input - "1 2 3 5"

"1 2 3 5".split()  ---> ['1', '2', '3', '5']

map(int, ['1', '2', '3', '5']) --> 1, 2, 3, 5

list(map(...)) --> [1, 2, 3, 5]

"1 2 3 5"        # input
↓
['1','2','3','5'] # split
↓
[1,2,3,5]        # map + list

'''