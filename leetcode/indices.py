nums = [3, 3]
target = 6
indices = []

for index, elem in enumerate(nums):
    for pos, num in enumerate(nums):
        oslo = nums[index]
        print(pos)
        if oslo == num and index == pos:
            continue
        num = oslo + num
        if num == target:
            indices.append(index)

print(nums)
print(indices)
