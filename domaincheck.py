#!/usr/local/bin/python

import urllib2,cookielib
import re

def checkDomain(domain):
	site='http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=' + domain
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Encoding': 'none',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	response = urllib2.urlopen(req)
	data = response.read()
	pat = re.compile("has already been registered by the organization below")
	availableList=list()
	unavailableList=list()
	if pat.search(data) is None:
		availableList.append(domain)
	else:
		unavailableList.append(domain)
	return availableList, unavailableList

fo = open("domains.txt",'r')
lines = fo.readlines()
fo.close()

fo = open("extensions.txt",'r')
extensions = fo.readlines()
fo.close()

for line in lines:
	line = line.strip()
  for extension in extensions:
		extension = extension.strip()
		url = line+extension
		print "Checking if %s is available..." %(url)
		availableList, unavailableList = checkDomain(url)

print "DISPLAYING RESULTS"

for domain in availableList:
	print "Domain %s : might be available." %(domain)