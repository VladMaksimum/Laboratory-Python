inp = open("lab_5/input2.txt")
nums = []
for n in range(10):
    nums.append(inp.readline())


for i in range(9):
    for j in range(i+1, 10):
        if nums[i] > nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

outp = open("lab_5/output2.txt", 'w')
for k in range(10):
    outp.write(nums[k])


inp.close()
outp.close()