def houserobber(nums):
    n = len(nums)
    if n == 1:
        return nums[0], [0]
    dp = [0] * n
    dp[0] = nums[0]
    choice2 = [0]
    if nums[1] > nums[0]:
        dp[1] = nums[1]
        choice1 = [1]
    else:
        dp[1] = nums[0]
        choice1 = [0]

    for i in range(2, n):
        if nums[i] + dp[i-2] > dp[i-1]:
            dp[i] = nums[i] + dp[i-2]
            now_choice = choice2 + [i]
        else:
            dp[i] = dp[i-1]
            now_choice = choice1.copy()
        choice2, choice1 = choice1, now_choice

    return dp[-1], choice1

print(houserobber([4, 4, 3, 1, 5, 6, 4]))
