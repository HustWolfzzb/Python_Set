from socket import *
from time import ctime
HOST = '119.29.74.46'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
  print 'waiting for connection...'
  tcpCliSock, addr = tcpSerSock.accept()
  print '...connected from:', addr
  while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
      break
    tcpCliSock.send('[%s] %s' %(ctime(), data))
  tcpCliSock.close()
tcpSerSock.close()






class stuudent(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not ininstance(value,int):
			raise ValueError('score musy be integer')
		if value<0 or value>100:
			raise ValueError('score must between 0 ~ 100!')
		self._score=value

