import select,socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('127.0.0.1',50000))
serversocket.listen(10)
serversocket.setblocking(0)

poll=select.poll()
poll.register(serversocket.fileno(),select.POLLIN)

connections={}
filenames={}

def sendfile(sc,filename):
	with open(filename,'rb') as file:
		file_data=file.read()
	sc.sendall(file_data)

def main():
	while True:
		for fd,event in  poll.poll():
			if event==select.POLLIN:
				if fd==serversocket.fileno():
					sc,addr=serversocket.accept()
					poll.register(sc.fileno(),select.POLLIN)
					connections[sc.fileno()]=sc
				else:
					sc=connections[fd]
					filename=sc.recv(1024).decode('ascii')
					if filename:
						filenames[fd]=filename
						poll.modify(fd,select.POLLOUT)
			elif event==select.POLLOUT:
				sc =connections[fd]
				sendfile(sc,fielnames[fd])
				poll.unregister(fd)
				sc.close()

if __name__ == '__main__':
	main()