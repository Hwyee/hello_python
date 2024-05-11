# socket_client.py
"""
socket_client.py

This module contains the SocketClient class, which is used to communicate with
a socket server.
"""

import socket


# 链接服务器,发送数据,接收数据
class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data):
        self.sock.send(data.encode("utf-8"))

    def recv(self):
        try:
            data = self.sock.recv(1024).decode("utf-8")
            return data
        except socket.timeout:
            return None

    def close(self):
        self.sock.close()
        print("socket closed")


client = SocketClient("localhost", 7788)
try:
    while True:
        data = input(">>> ")
        client.send(data)
        data = client.recv()
        print(data)

        if data == "exit":
            client.close()
            break
finally:
    client.close()
