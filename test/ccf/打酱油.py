"""
问题描述
　　小明带着N元钱去买酱油。酱油10块钱一瓶，商家进行促销，每买3瓶送1瓶，或者每买5瓶送2瓶。请问小明最多可以得到多少瓶酱油。
输入格式
　　输入的第一行包含一个整数N，表示小明可用于买酱油的钱数。N是10的整数倍，N不超过300。
输出格式
　　输出一个整数，表示小明最多可以得到多少瓶酱油。
样例输入
40
样例输出
5
样例说明
　　把40元分成30元和10元，分别买3瓶和1瓶，其中3瓶送1瓶，共得到5瓶。
样例输入
80
样例输出
11
样例说明
　　把80元分成30元和50元，分别买3瓶和5瓶，其中3瓶送1瓶，5瓶送2瓶，共得到11瓶。
"""
# 输入用于买酱油的钱，input接收到的都是str型的，所以要用int进行转型
money = int(input())
# 用result变量记录买到酱油的数目
result = 0
# 三种情况特殊点，要买7瓶酱油只需要花50块，因为买5瓶会送两瓶，10块钱一瓶
# 下面两个列表是酱油瓶数与相应价格一一对应的
moneyList = [50, 30, 10]
numList = [7, 4, 1]
# 用变量n来控制循环
n = 0
while n < 3 and money >= 10:
    # 如果手上的钱大于等于价格列表的某个值时
    if money >= moneyList[n]:
        # 进来计算能买到多少瓶
        result += (money // moneyList[n])*numList[n]
        # 买完某一次之后把钱减少
        money -= (money // moneyList[n])*moneyList[n]
    # n进行加1，继续循环，看看还可以买多少瓶
    n += 1
print(result)
"""
思路：根据题目可以看出三种买酱油比较特别的地方，就是如果买1瓶酱油就10块，如果买3瓶就30块但是你最终得到的酱油是4瓶，因为
商家还会送1瓶，同理买5瓶花50块但是得到的一共是7瓶酱油。那么我们就可以利用这里来设置两个列表，他们的最终得到的酱油瓶数对应
各自需要花费的钱，那么我们就可以知道这两个列表都是等长的并且长度还是3，我们就可以通过循环去计算我们可以买多少个7瓶多少个4瓶
多少个1瓶。
例如：第二个样例输入80.
讲解循环部分：
     n初始值为0，并且钱是80，那么这时候就进入if判断进行判断，我当前的钱是否大于或等于50块呢（这里就是决定我们可以买到多少个7瓶）
     这时明显是大于的，那么我就要计算能买多少瓶了，(money // moneyList[n])*numList[n]就相当于（80//50）*7答案是7，买到7瓶就花费了
     50元，那么就要更新当前的钱的值，再去计算可以买多少个4瓶和1瓶
"""