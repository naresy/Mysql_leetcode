def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is larger than the length of the list
    return nums[-k:] + nums[:-k]

# Example usage
nums1 = [1, 2, 3, 4, 5, 6, 7]
result1 = rotate(nums1, 3)
print(result1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
result2 = rotate(nums2, 2)
print(result2) 