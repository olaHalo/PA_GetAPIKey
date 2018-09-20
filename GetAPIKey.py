#Script used to get an API key from a Palo Alto Firewall. Tested on version 7.1.x and higher

import urllib2 #used for http requests
import xml.etree.ElementTree as ET #used for parsing XML
import sys
import os
import datetime

ip_address = raw_input('Enter the IP address:   ') or "x.x.x.x"
username = raw_input('Enter a username:   ') or "username"
password = raw_input('Enter the password:   ') or "password"
filePath = os.path.join('C:', 'log.txt')

str =  "*****Script started*****"

def getTime(): #Gets the current time and formats it
	time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
	return time

filePath = os.path.join('C:/', 'log.txt')

def setLog(str): #Logs to a file and appends newlines
	with open(filePath, 'a') as logFile:
		logFile.write(getTime() + " : " + str + '\n')


def getAPIkey():
	try:
		url = 'https://'+ip_address+'/api/?type=keygen&user='+username+'&password='+password
		response = urllib2.urlopen(url) #Basically a curl
		html = response.read() #Read the curl and assign it to string variable
		str = "HTML successfully accessed"
		setLog(str)
	except:
		str = "Invalid credentials or IP address. Check username and password"
		setLog(str)
		sys.exit(1) #Stop the script

	
	contents = ET.fromstring(html) #import the xml through a string

	if contents.attrib == {'status': 'success'}:
		for item in contents.iter('key'): #loop through the contents and search for key
			print item.text 
			str = "API Key = " + item.text
			setLog(str)
	else:
		print "API call failed. Check credentials"
		str = "API call failed. Check credentials"
		setLog(str)
		sys.exit(1) #Stop the script

setLog(str)
getAPIkey()
str = "*****Script complete*****"
setLog(str)
sys.exit(1)
