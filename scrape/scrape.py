import urllib2

def gethtml():
	response = urllib2.urlopen('http://www.google.com/')
	html = response.read()
	print html

def fileopen():
	req = urllib2.Request('http://www.baidu.com')  
	response = urllib2.urlopen(req)  
	the_page = response.read()  
	print the_page

def main():
	gethtml()
	fileopen()
main()