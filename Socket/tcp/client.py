import socket
import sys


if __name__ == '__main__':

    # 声明服务端地址和端口
    address = ('127.0.0.1', 2222)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 尝试连接服务端
    try:
        s.connect(address)
    except ConnectionRefusedError:
        print('Server not found')
        sys.exit()

    while True:
        trigger = input('Please input sth: ')
        s.sendall(trigger.encode())
        data = s.recv(1024).decode()

        print(f'Received {data}')

        # 自定义结束字符串
        if trigger == 'quit':
            break

    s.close()
