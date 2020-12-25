#!/usr/bin/python
# FTP Digger - FTP Banner Grabbing
# Written by m0zi

import socket
import sys

script_name = sys.argv[0]
host = sys.argv[1]

success_login = '230'

if len(sys.argv) != 2:
	print "\n[+] FTP Digger - File Tranfer Protocol Banner Grabbing"
	print "[+] Written by m0zi"
	print "[+] Usage: %s <IP Address>\n" % script_name
	sys.exit()

try:
	print "\n# FTP Digger - File Tranfer Protocol Banner Grabbing"
	print "# Written by Brian HM (Gr3x)"
	print "# Make sure destination port is open and not blocked by firewall!!!\n"
	print "[+] Target: %s\n" % host

	# Creating TCP Connection...
	s = socket.socket()
	
	# Connecting to host on port 21...
	s.connect((host, 21))
	# Get response from remote host...
	service_name = s.recv(1042)

	# Try Anonymous Login...
	s.send("USER anonymous\r\n")
	s.recv(1042)

	s.send("PASS whatever\r\n")
	response = s.recv(1042)
	response_string = response.decode('utf-8')
	s.close()

	# Print out scanning results
	print "[+] %s" % service_name
	
	if success_login in response_string:
		print "[+] Anonymous login is allowed\n"
	
	else:
		sys.exit()

except socket.gaierror, err:
	print "[-] Whoops!!! We have some issue!!!\n\n" ,sys.argv[1] ,err
	print
	sys.exit()
