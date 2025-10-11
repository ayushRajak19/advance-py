nums = [23,4354,112 ,-23,8482]

# lar = nums[0]
lar = float("-inf")

for i in nums:
    lar = max(lar,i)
    # if i > lar:
    #     lar = i
print(lar)