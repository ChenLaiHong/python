"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
示例 :
输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

    结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
    你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    tempDict = {}
    for i in range(len(nums)):
        if nums[i] in tempDict:
            tempDict[nums[i]] = tempDict[nums[i]] + 1
        else:
            tempDict[nums[i]] = 1
    temp = list(sorted(tempDict.items(), key=lambda n: n[1]))
    result_final = [temp[i][0] for i in range(2)]
    return result_final
print(singleNumber([1,2,1,3,2,5]))