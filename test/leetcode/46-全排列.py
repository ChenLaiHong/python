"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import itertools
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    for i in itertools.permutations(nums, len(nums)):
        result.append(list(i))
    return result
print(permute([1, 2, 3]))