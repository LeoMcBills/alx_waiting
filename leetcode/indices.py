nums = [3, 2, 4]
target = 6
indices = []

for index, elem in enumerate(nums):
    for num in nums:
        oslo = nums[index]
        if oslo == num:
            continue
        num = oslo + num
        if num == target:
            indices.append(index)

print(nums)
print(indices)
