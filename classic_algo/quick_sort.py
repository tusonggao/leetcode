#快速排序的实现

def quick_sort_r(nums, m, n):
    if m > n:
        return

    val = nums[m]
    low_idx = m
    high_idx = n + 1

    while low_idx < high_idx:
        if nums[high_idx] < val:
            nums[high_idx], nums[low_idx] = nums[low_idx], nums[high_idx]
            high_idx -= 1

        if nums[high_idx] < val:
            return

    return nums


def quick_sort(nums):
    quick_sort_r(nums, 0, len(nums)-1)
    return