# finding smallest positive missing number  

def first_missing_positve(nums):
    n=len(nums)
    for i in range(n):
        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
    for i in  range(n):
        if nums[i]!=i+1:
            return i+1
    return n+1
nums=[3,4,-1,1]
number=[5,7,2,4]
num=[1,-1,3,-5]
print(first_missing_positve(nums))
print(first_missing_positve(number))
print(first_missing_positve(num))
            