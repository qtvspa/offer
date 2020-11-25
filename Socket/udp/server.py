import socket

if __name__ == '__main__':

    # 声明服务端地址和端口
    address = ('127.0.0.1', 3333)
    # 绑定服务端地址和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)

    while True:
        # 返回数据和接入连接的（客户端）地址
        data, addr = s.recvfrom(1024)
        data = data.decode()
        if not data:
            break

        print(f'Received {data}')
        send = input('Input: ')

        # UDP 是无状态连接，所以每次连接都需要给出目的地址
        s.sendto(send.encode(), addr)

    s.close()
