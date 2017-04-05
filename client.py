import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.128.245"
port=12345
s.connect((host,port))
msg="happy new year\n"
s.send(msg)
s.close()
#we need to open a server using 'nc -l 12345' to test this client
#be careful to change ip address to avoid errors
