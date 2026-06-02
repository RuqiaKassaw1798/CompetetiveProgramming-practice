t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    nums = [a, b, c]
    nums.sort()
    print(nums[1])
