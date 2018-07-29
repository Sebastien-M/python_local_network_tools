import socket, threading


class Tools():

	def __init__(self):
		pass

	
		

	def TCP_connect(self, ip, port_number, delay, output):
	    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    TCPsock.settimeout(delay)
	    try:
	        TCPsock.connect((ip, port_number))
	        output[port_number] = 'Listening'
	    except:
	        output[port_number] = ''



	def scan_ports(self, host_ip, delay):

	    threads = []        # To run TCP_connect concurrently
	    output = {}         # For printing purposes

	    # Spawning threads to scan ports
	    for i in range(10000):
	        t = threading.Thread(target=self.TCP_connect, args=(host_ip, i, delay, output))
	        threads.append(t)

	    # Starting threads
	    for i in range(10000):
	        threads[i].start()

	    # Locking the script until all threads complete
	    for i in range(10000):
	        threads[i].join()

	    # Printing listening ports from small to large
	    for i in range(10000):
	        if output[i] == 'Listening':
	            print(str(i) + ': ' + output[i])

	def port_scan(self):
		host_ip = input("Enter host IP: ")
		delay = int(input("How many seconds the socket is going to wait until timeout: "))   
		self.scan_ports(host_ip, delay)