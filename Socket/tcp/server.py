# -*- coding:utf-8 -*-

import socket

""" 使用socket实现TCP协议 

- socket有三大属性
  - 域：AF_UNIX（Unix文件系统/地址为文件名/对应文件IO）和AF_INET（Internet网络）两类
  - 类型：SOCK_STREAM（流，对应 TCP） 和 SOCK_DGRAM（数据报，对应 UDP）
  - 协议：只要底层的传输机制允许不止一个协议来提供套接字类型，就可以为套接字选择一个特定的协议；通常只需要使用默认值0。


"""

if __name__ == '__main__':

    # 声明服务地址和端口
    address = ('127.0.0.1', 2222)
    print(address)
    # 绑定服务器地址和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    # 开始监听 设置两次backlog的间隔时间为5秒
    s.listen(5)
    # 被动接收客户端连接 阻塞式
    conn, addr = s.accept()
    # 这里打印的是客户端连接的地址
    print(f"Connected with {addr}")

    while True:
        # buffer size 设置为1024
        data = conn.recv(1024).decode()

        if not data:
            break

        print(f"Received {data}")

        # 发送数据
        msg = input('Please input sth:')
        conn.sendall(msg.encode())

    conn.close()
    s.close()
