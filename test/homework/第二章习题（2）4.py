"""
编写一个程序，输出以下三角形
    *
  ***
*****
说明：每一行都左对齐输出，行末无多余空格。
【输入形式】
无输入。
【输出形式】
第一行4个空格加1个星号；第二行2个空格加3个星号；
第三行没有空格。
"""
i = 2
while i >= 0:
    for j in range(0, 5):
        if j < i*2:
            print(" ", end="")
        else:
            print("*", end="")
    print()
    i -= 1
