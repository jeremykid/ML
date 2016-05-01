# -*- coding: utf-8 -*-  
# https://gitcafe.com/callmewhy/whyspider

import urllib
import urllib2
import cookielib  


class Spider:
	def __init__(self):
        self.cookie_jar = cookielib.CookieJar()  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))  
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}  
