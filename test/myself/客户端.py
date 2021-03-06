from socket import *
import sys, os
import signal


# 发送消息
def do_child(s, name, addr):
    while True:
        text = input('发言(quit退出):')
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            # 从子进程中杀死父进程
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit('退出聊天室')
        # 聊天
        else:
            msg = 'C %s %s' % (name, text)
            s.sendto(msg.encode(), addr)


# 接收消息
def do_parent(s):
    while True:
        msg, addr = s.recvfrom(1024)
        print(msg.decode() + '\n发言(quit退出):', end='')


# 创建套接字,创建父子进程
def main():
    if len(sys.argv) < 3:
        print('error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    s = socket(AF_INET, SOCK_DGRAM)

    # 登录
    while True:
        name = input('请输入姓名:')
        # L里面要加空格,按空格切割
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('@进入聊天室@')
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        print('创建子进程失败')
    elif pid == 0:
        # 连接函数do_child实现一次运行
        do_child(s, name, ADDR)
    else:
        # 连接函数do_parent实现一次运行
        do_parent(s)


if __name__ == '__main__':
    main()
