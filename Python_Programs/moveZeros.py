def moveZero(num):
    j = 0
    for i in range(len(num)):
        if num[i] !=0:
            num[j], num[i] = num[i], num[j]
            j+=1
    return num
nums = list(map(int, input("Enter the number with spaces: ").split()))
result = moveZero(nums)
print(result)
