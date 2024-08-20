# def product_except_self(self, nums):
#         n = len(nums)
#         answer = [1] * n
    
#         # Fill left products
#         left_product = 1
#         for i in range(n):
#             answer[i] = left_product
#             left_product *= nums[i]
    
#         # Fill right products and calculate the result
#         right_product = 1
#         for i in range(n-1, -1, -1):
#             answer[i] *= right_product
#             right_product *= nums[i]
    
#         return answer

# here is the solution

class Solution(object):
   def product_except_self(self, nums):
        n = len(nums)
        answer = [1] * n
    
        # Fill left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
    
        # Fill right products and calculate the result
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
    
        return answer


   