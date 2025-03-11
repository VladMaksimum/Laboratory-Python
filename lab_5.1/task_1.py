nums = open("lab_5/input1.txt").read().split()

res = 1
for n in nums:
    res*= int(n)

out = open("lab_5/output1.txt", 'w')
out.write(str(res))

nums.close()
out.close()