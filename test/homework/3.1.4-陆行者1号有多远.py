"""
【问题描述】
旅行者1号飞船，与1977年9月5日发射，目前到达了太阳系的外缘，是离地球最远的人造飞行器。据2009年9月25日美国航天局的网站报道，
它离太阳约166.37亿英里，以约每小时38241英里的速度驶离太阳。
    编写一个程序，提示用户输入一个整数y。接下来，计算自2009年9月25日起y年后，旅行者1号离太阳的距离（假定一年为365天，且飞
    船飞离太阳的速度是恒定的。）输出以下结果：
1. 以英里为单位的距离。
2. 以千米为单位的距离（1.609344千米/英里）。
3. 以天文单位计量的距离。天文单位（英文：Astronomical Unit，简写AU）是长度的单位，历史上约等于地球跟太阳的平均距离。
（92955887.6英里/AU）
4. 对于以上距离，无线电往返一次要多少小时？无线电波以光速传播，速度为每秒299 792 458米。
【输入形式】
输入年数y。计算自2009年9月25日起y年的距离。
【输出形式】
输出上文描述的四项内容。输出的数值保留两位小数。
【样例输入】
1
【样例输出】
distance:
16971991160.00 miles
27313772141.40 km
182.58 AU
time: 50.62 hours
输出的每一行中，单位之前有一个空格。最后一行的冒号是西文字符，之后有一个空格。
【输出说明】
如何做到保留两位小数？下面举例说明。
假如'以英里为单位的距离'用dist变量存储，那么下面的写法将做到保留两位小数，并且尾部附加了miles这个串。
print("%.2f %s"%(dist, 'miles'))
这里，"%.2f %s"是格式控制串，这与C语言的格式化输出是类似的。%.2f是指要在这个位置输出一个浮点数，
'.2'是指要保留(dist, 'miles')是指要保留两位小数。%s是指要在这个位置输出一个字符串。
整体效果是，拿dist的值填充到%.2f所占位置，拿'miles'填充到%s所占位置，而后输出。
假如'无线电往返小时数'用time变量存储，那么下面的写法将达成【样例输出】中的最后一行输出的效果。
print("%s %.2f %s"%("time:", time, 'hours'))
这里，"%s %.2f %s"是格式控制串，这与C语言的格式化输出是类似的。
整体效果是，拿"time:"填充到第一个%s所占的位置，拿time的值填充到%.2f所占的位置，
拿'hours'填充到第二个%s所占的位置，而后输出。
如何让time:之后有一个空格，在格式控制串中的第一个%s所占的位置之后留一个空格即可。
"""
y = int(input())
miles = y*365*24*38241+16637*10**6
km = (y*365*24*38241+16637*10**6)*1.609344
AU = miles/92955887.6
hours = (km*10**3/299792458/3600)*2
print("distance:")
print('%0.2f' % miles, "miles")
print('%0.2f' % km, "km")
print('%0.2f' % AU, "AU")
print("time:", '%0.2f' % hours, "hours")
