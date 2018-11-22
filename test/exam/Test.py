"""
时间限制：1秒
空间限制：32768K
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？
输入描述:
输入包含多组测试数据。
对于每组测试数据：
N - 本组测试数据有n个数
a1,a2...an - 需要计算的数据
保证:
1<=N<=100000,0<=ai<=INT_MAX.
  
输出描述:
对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。
输入例子1:
6
45 12 45 32 5 6
输出例子1:
1 2
"""

from itertools import combinations

num = input()
nums = [int(n) for n in input().split()]
result = []
for i in combinations(nums, 2):
    result.append(abs(i[0]-i[1]))
temp = sorted(result)
print(temp.count(temp[0]),temp.count(temp[len(temp)-1]))