from statistics import median

def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    def rewire(idx):
        if n % 2 == 0 and idx == n - 1:
            return idx
        return (2 * idx) % ((n - 1) // 2 * 2 + 1)

    for i in range(len(nums)):
        print(rewire(i))
    med = median(nums)
    # print(med)

    i, j, k = 0, 0, n - 1
    while j <= k:
        if nums[rewire(j)] < med:
            nums[rewire(j)], nums[rewire(i)] = nums[rewire(i)], nums[rewire(j)]
            i += 1
            j += 1
        elif nums[rewire(j)] > med:
            nums[rewire(j)], nums[rewire(k)] = nums[rewire(k)], nums[rewire(j)]
            k -= 1
        else:
            j += 1

# lc324
