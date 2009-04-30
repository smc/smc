# -*- coding: utf-8 -*-
import socket
import sys
import datetime
import time

#get stuff from command line
network = sys.argv[1]
port = 6667
nick = sys.argv[2]
channel = sys.argv[3]

#setup socket and connect to network
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((network,port))

#send nick, user info to network
sock.send('NICK ' + nick + '\r\n')
sock.send('USER ' + nick + ' ' + nick + ' '+ nick + ' :' + 'localhost\r\n')

#join channel
sock.send('JOIN ' + channel + '\r\n')

currentdate = str(datetime.date.today())
filename = currentdate + '-' + channel + '.log'
#Loop to keep listening
while True:
    data = sock.recv(5120)
    #check current date and if changed open new file
    if currentdate != str(datetime.date.today()):
	#close existing log
	logfile.close() 
  
	#update filename 
	currentdate = str(datetime.date.today());
	filename = currentdate + '-' + channel + '.log'
	#open new log
	logfile = open(filename ,'a')
	
    #check for PING from server and reply with PONG if found
    if data.find('PING')!=-1 :
	sock.send('PONG ' + data.split()[1] + '\r\n')
    if data.find('PRIVMSG ' + channel) != -1:
	logfile = open(filename,'a')
	speaker = data.split('!')[0].replace(':','')
	message = ''.join(data.split(':')[2:])
	logfile.write('<' + str(time.strftime("%H:%M:%S", time.localtime())) + '> ' + speaker + ' : ' + message)
	logfile.close()