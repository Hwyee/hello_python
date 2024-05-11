# socket 编程
import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建套接字

    try:
        # 绑定端口
        tcp_server_socket.bind(("0.0.0.0", 7788))
        # 设置监听 客户端个数
        tcp_server_socket.listen(128)
        # 等待客户端的链接
        # 客户端地址
        new_client_socket, client_address = tcp_server_socket.accept()
        while True:
            recv_data = new_client_socket.recv(1024)

            if recv_data:
                data = recv_data.decode("utf-8")
                print("客户端发送过来的数据是%s" % data)
                # new_client_socket.send("收到".encode("utf-8"))
                new_client_socket.send(recv_data)
                if data == "exit":
                    tcp_server_socket.close()
                    break
            else:
                break
    finally:
        new_client_socket.close()


main()
