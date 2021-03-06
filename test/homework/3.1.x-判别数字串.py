"""
【问题描述】
输入一个字符串，判别该字符串内的字符是否都是数字（即0~9）。
【输入形式】
一行。一个字符串。
【输出形式】
输出yes或者no。yes表示全部都是，no表示有部分不是。
【样例输入】
98e-7
【样例输出】
no
【样例说明】
e字母不是数字字符。
【提示】
用字符串的isdigit方法。
"""
strInput = input()
if strInput.isdigit():
    print("yes")
else:
    print("no")