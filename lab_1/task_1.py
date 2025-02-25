nums = [int(i) for i in input().split()]
ma=0
mi=10**10

for i in range(len(nums)):
    if ma<nums[i]:
        ma=nums[i]
    if mi>nums[i]:
        mi=nums[i]

print(ma,mi)