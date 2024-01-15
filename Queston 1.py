def remove_duplicates(nums):
    if not nums:
        return 0

    unique_count = 1  # Initialize with the first element as it is always unique
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_count] = nums[i]
            unique_count += 1

    return unique_count, nums

# Example usage:
nums = [1, 1, 2]
k, modified_nums = remove_duplicates(nums)
print(f"Output: {k}, nums = {modified_nums}")