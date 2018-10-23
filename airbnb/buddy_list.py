# python sort array of iterable objects in dictionary order (if elements that must be compared can be compared)

def find(nums, nums2):
    return sorted([
        (sum([num in set(nums) for num in nums2[i]]) / float(len(nums2[i])),
        i)
        for i in range(len(nums2))])


blists = [["aa", "bb", "ee", "ff"],
          ["aa", "bb", "cc", "gg"],
          ["aa", "bb", "cc", "dd"],
          ["xx", "yy", "zz", "aa"]]

mlist = ["aa", "bb", "cc", "dd"]

print(find(mlist, blists))

