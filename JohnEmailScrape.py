# read a webpage
import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()
import re		#Regex

#Author: John Nicholson
#Scrapes Webpage and pulls all lines with an email to a .txt
def WebToTxt():
	print ("Would you like to use a different url other than https://pastebin.com/n9phcmx4?")
	answer = raw_input("(y/n?) ")

	if answer == 'n':
		url = 'https://pastebin.com/n9phcmx4' #Name of file being scraped
	else:
		print ("Please enter the URL you want to scrape")
		url = raw_input(">> ")

	r = urllib2.urlopen(url, timeout=100)

	f = open('output.xls', 'w')

	for line in r.readlines():
	
		if re.search("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}", line):
		
			#found = re.findall("\>(.*?)\<", line) #finds everything between html tags
			f.write(line.replace(':', '\t'))
		
	f.close()


#Main Method
def Main():
	WebToTxt()

Main()	