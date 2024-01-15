def rob(nums):
    def simple_rob(nums):
        prev_max = 0
        curr_max = 0

        for num in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + num)
            prev_max = temp

        return curr_max

    # Two cases: rob the first house to the second-to-last house or rob the second house to the last house
    return max(simple_rob(nums[:-1]), simple_rob(nums[1:])) if len(nums) != 1 else nums[0]

# Example usage:
nums1 = [2, 3, 2]
print(rob(nums1))  # Output: 3

nums2 = [1, 2, 3, 1]
print(rob(nums2))  # Output: 4

nums3 = [1, 2, 3]
print(rob(nums3))  # Output: 3