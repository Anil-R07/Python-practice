#find two numbers in an array whose sum equals a target. Give first atched pair
def findNum(nums, target):
    hashmap = {}
    for i in range (len(nums)):
        num = nums[i]
        diff = target - num 

        if diff in hashmap:
            return[hashmap[diff], i]

        hashmap [num] = i

output = findNum([1, 6, 3, 4], 7)
print(output)

#find two numbers in an array whose sum equals a target. Gives all the pair
def findNum(nums, target):
    hashmap = {}
    result = []
    for i in range (len(nums)):
        num = nums[i]
        diff = target - num 

        if diff in hashmap:
            result.append([hashmap [diff], i])
        hashmap[num] = i
    return result

output = findNum([1, 6, 3, 4], 7)
print(output)