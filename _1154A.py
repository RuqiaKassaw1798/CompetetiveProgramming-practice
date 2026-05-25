nums = list(map(int, input().split()))

nums.sort()

total = nums[3]

a = total - nums[0]
b = total - nums[1]
c = total - nums[2]

print(a, b, c)
