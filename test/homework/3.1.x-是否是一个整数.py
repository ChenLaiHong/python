"""
【问题描述】
输入一个字符串，判别它是否符合整数的写法。正整数的写法是：用数字开头，其后可以跟数字。负整数的写法是：用负号开头，其后
跟数字。输入的字符串的头尾可能包含空格。
【输入形式】
一行。一个字符串。
【输出形式】
yes或者no。如果符合整数写法，输出yes，否者输出no。
【样例输入】
-897
【样例输出】
yes
【样例输入2】
9.67
【样例输出2】
no
【提示】
1. 字符串头尾可能有空格。
2. 用字符串的strip方法删除头尾空格。
3. 用isdigit方法判别字符串是否由数字字符组成。
"""
strInput = input().strip()
num = strInput.count("-")
temp = strInput.lstrip("-")
if strInput.isdigit() or num == 1 and temp.isdigit():
    print("yes")
else:
    print("no")


