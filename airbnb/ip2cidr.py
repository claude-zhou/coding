def ipToCIDR(ip, n):
    """
    :type ip: str
    :type n: int
    :rtype: List[str]
    """
    ret = []

    def ip_add(ip, m):
        nums = [int(num) for num in ip.split('.')]
        for i in range(3, -1, -1):
            if m >= 8:
                m -= 8
            else:
                break
        carry, nums[i] = divmod(nums[i] + 2 ** m, 256)
        for j in range(i - 1, -1, -1):
            if carry == 0:
                break
            carry, nums[j] = divmod(nums[j] + carry, 256)
        return '.'.join([str(num) for num in nums])

    while n > 0:
        trailn = len(bin(n)) - 3
        trail0 = 0
        nums = [int(num) for num in ip.split('.')]
        for num in nums[::-1]:
            if num != 0:
                while num % 2 == 0:
                    trail0 += 1
                    num >>= 1
                break
            else:
                trail0 += 8
        move = min(trailn, trail0)
        ret.append(ip + "/%d" % (32 - move))
        ip = ip_add(ip, move)
        n -= 2 ** move
    return ret


print(ipToCIDR("255.0.0.7", 10))

# leetcode 751
