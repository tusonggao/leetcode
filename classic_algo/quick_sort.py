#快速排序的实现

def quick_sort_r(nums, m, n):
    if m >= n:
        return

    val = nums[m]  #pivot value
    low_idx = m + 1
    high_idx = n

    while low_idx < high_idx:
        if nums[high_idx] < val:
            nums[high_idx], val = val, nums[high_idx]
        if nums[low_idx] > val:
            nums[low_idx], val = val, nums[low_idx]
        low_idx += 1
        high_idx -= 1

    quick_sort_r(nums, m, low_idx-1)
    quick_sort_r(nums, high_idx+1, n)

    return

def quick_sort(nums):
    quick_sort_r(nums, 0, len(nums)-1)
    return