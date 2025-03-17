# socket_client.py
"""
socket_client.py

This module contains the SocketClient class, which is used to communicate with
a socket server.
"""

import socket


# 链接服务器,发送数据,接收数据
class SocketClient:
    """_summary_
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        self.sock.send(data.encode("utf-8"))

    def recv(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            data = self.sock.recv(1024).decode("utf-8")
            return data
        except socket.timeout:
            return None

    def close(self):
        """_summary_
        """
        self.sock.close()
        print("socket closed")


client = SocketClient("localhost", 7788)
try:
    while True:
        datat = input(">>> ")
        client.send(datat)
        datat = client.recv()
        print(datat)

        if datat == "exit":
            client.close()
            break
finally:
    client.close()
