def twoSum(nums, target):
    num_map = {}  # Dictionary to store number -> index mapping
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  # Found the two numbers
        num_map[num] = i  # Store index of current number
    return []  # This line will never be reached as per problem constraints
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
nums = [3,2,4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]
