import socket


if __name__ == '__main__':
    # 声明服务端地址和端口
    address = ('127.0.0.1', 3333)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        trigger = input('Input: ')
        s.sendto(trigger.encode(), address)
        # 返回数据和接入连接的（服务端）地址
        data, addr = s.recvfrom(1024)
        data = data.decode()

        print(f'Received {data}')

        if trigger == 'quit':
            break
    s.close()
