import socket

print(1)
udp_sock_server = socket.socket()
udp_sock_server.connect(('', 9090))


msg = ''

while msg != 'exit':
    msg = input('введите сообщение: ')

    udp_sock_client = socket.socket()
    udp_sock_client.bind(('', 9091))
    udp_sock_client.listen(1)

    udp_sock_server.send(msg.encode())

    conn_client, addr_client = udp_sock_client.accept()
    data = conn_client.recv(1024)
    conn_client.close()
    print(data.decode())



