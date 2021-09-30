import socket

udp_sock_server = socket.socket()
udp_sock_server.bind(('', 9090))

udp_sock_server.listen(0)

conn_server, addr_server = udp_sock_server.accept()

msg = ''

while True:
	data = conn_server.recv(1024)
	if not data:
		break
	msg += data.decode()
	udp_sock_client = socket.socket()
	udp_sock_client.connect(('', 9091))

	udp_sock_client.send(data)
	udp_sock_client.close()

print(msg)

conn_server.close()
