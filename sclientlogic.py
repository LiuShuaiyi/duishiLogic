# -*- coding: UTF-8 -*-
import socket,cPickle,sio,time,t

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	conn.connect((sio.HOST,sio.LOGIC_PORT))
except:
	print 'failed to connect, the program will exit...'
	time.sleep(2)
	exit(1)

mapInfo=sio._recvs(conn)
aiInfo=sio._recvs(conn)

#get roundInfo here
roundInfo={'process':sio.GAME_CONTINUE,'roundNumber':1}

sio._sends(conn,(0,roundInfo)) #第0回合的信息
while True:
	roundCommand=sio._recvs(conn)
	#do some calculation: roundEffect,roundInfo=Calculate(Command)
	roundEffect={}
	roundInfo=roundInfo
	sio._sends(conn,(roundEffect,roundInfo))
	
conn.send('|')

conn.close()

raw_input()