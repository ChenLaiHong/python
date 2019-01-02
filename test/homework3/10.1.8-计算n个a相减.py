"""
例如：若输入的a为5，n为6，则要计算下面公式的值：
555555-55555-5555-555-55-5。
【输入形式】
从标准输入读入整数a和n，两者之间以一个空格分隔。
【输出形式】
在标准输出上输出公式的计算结果。
【样例1输入】
5 6
【样例1输出】
493830
【样例1说明】
输入的a为5，n为6，按照上述公式计算的结果为493830。
【样例2输入】
5 20
【样例2输出】
49382716049382716060
【样例2说明】
输入的a为5，n为20，按照上述公式计算的结果为49382716049382716060。
"""
a, n = input().split()
n = int(n)
result = int(n * a)
i = n - 1
while i > 0:
    result -= int(i * a)
    i -= 1
print(result)