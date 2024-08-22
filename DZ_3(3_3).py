nums = [1,2,3,4,5,6,7,8,9]
size = len(nums)
n = (size+1) // 2
print(n)
if size % 2 == 1:
    part1 = nums[:n]
    part2 = nums[n:]
    print(part1,part2)
else:
    part1 = nums[:len(nums)//2]
    part2 = nums[len(nums)//2:]
    print(part1,part2)
