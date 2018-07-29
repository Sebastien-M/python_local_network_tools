import os
from Tools import *
from socket import *
from termcolor import colored
import argparse
import sys
import ipdb


clear = lambda: os.system('cls')
clear()
print(colored("NETWORK Tools 0.0.1","green",attrs=['bold']))
print(colored("Made by Seb.M","green"))
print("------------------\n")

tools = Tools()
port = 22
start = 1
while start == 1 :


	network = '192.168.1.' 

	def is_up(addr, port):
	    s = socket(AF_INET, SOCK_STREAM)
		# print(socket.getfqdn())
	    s.settimeout(0.05)
	    if not s.connect_ex((addr,port)):    
	        s.close()                       
	        return 1
	    else:
	        s.close()

	def run(port):
	    print ('')
	    for ip in range(1,256):    ## 'ping' addresses 192.168.1.1 to .1.255
	        addr = network + str(ip)
	        if is_up(addr, port):
	            print ('%s \t- %s' %(addr, getfqdn(addr)) )   
	    print ()
		
	def scan(port):  
		print (colored("[*] Scanning local network on port " + str(port),"green"))
		run(22)
		print('Done')



	try:
		inp = colored(">>>","red",attrs=['bold'])
		command = input(inp)
		if command[:9] == "port_scan":
			tools.port_scan()
		elif command[:4] == "scan":
			if '--' in command:
				port = command[command.find('p') + 2:]
			scan(port)
		elif command == "exit":
			print(colored("\n[*] Shutting down","red",attrs=['bold']))
			break
		elif command == "deauth_attack":														#todo
			"""
			monitor mode
			scan mac ad
			select(and host)
			buil pack
			send(num choose)
	
			"""
			#print(colored("\n[*] ERROR NO MAC ADRESS AND NUM","red",attrs=['bold']))
			break
		else:
			print(' \'{}\'is not an internal command'.format(command))
	except KeyboardInterrupt:
		print(colored("\n[*] Shutting down","red",attrs=['bold']))
		print(colored("Type \"exit\" to exit the program properly",'green',attrs=['bold']))
		break
	except EOFError :
		print(colored("\n[*] Shutting down(ERROR)","red",attrs=['bold']))
		break
	




