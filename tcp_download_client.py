import socket




def main():
    # 创建socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取用户输入的服务器ip，port，文件名
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器端口:"))
    file_name = input("请输入要下载的文件名:")
    # 连接服务器
    tcp_client_socket.connect((server_ip, server_port))
    # 发送请求的文件名
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 接收返回的内容写入文件
    file_content = tcp_client_socket.recv(1024*1024)
    # 内容不为空就写入文件
    if file_content:
        with open("download_"+file_name, "wb") as f:
            f.write(file_content)
    # 关闭客户端socket
    tcp_client_socket.close()




if __name__ == '__main__':
    main()
