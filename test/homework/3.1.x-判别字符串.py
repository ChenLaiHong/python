"""
【问题描述】
输入一个字符串，去掉头尾空格，判别其内的字符是否都是字母。如果是，则视为一个单词。
【输入形式】
一行。一个字符串，其内可能包含空格。
【输出形式】
如果是一个单词，则输出yes，否则输出no。
【样例输入】
 hello
【样例输出】
yes
【样例输入2】
 great wall
【样例输出2】
no
【样例说明】
样例输出2中，有两个单词，也视为不符合要求，故输出no。
【提示】
用字符串的strip方法删除空格。
用isalpha方法判别是否有字母组成。
"""
strInput = input().strip()
num = 0
if " " in strInput or not strInput.isalpha():
    print("no")
elif strInput.isalpha():
    print("yes")