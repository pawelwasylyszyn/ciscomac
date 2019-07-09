#!/usr/bin/python

import urllib2
import json
import sys
import re

#MY_KEY="at_Hg0uN4kWZkDUpS1PNRzodcfnBofu4"
MY_KEY="at_Hg0uN4kWZkDUpS1PNRzodcfnBofu4"
URL="https://api.macaddress.io/v1?output=json&apiKey=" + MY_KEY + "&search="

allowed_chars = "abcdefABCDEF0123456789-:"

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "Usage: %s <MAC address>" % sys.argv[0]
        sys.exit(1)

    if len(sys.argv[1]) < 12:
        print "MAC address too short: %s" % sys.argv[1]
        sys.exit(2)

    for i in range(len(sys.argv[1])):
        if sys.argv[1][i] not in allowed_chars:
           print "Incorrect characters in MAC address: %s" % sys.argv[1]
           sys.exit(1)

    URL = URL + sys.argv[1]
    
    req = urllib2.Request(URL)

    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as e:
        print e
        sys.exit(3)

    the_page = response.read()
    json_data = json.loads(the_page)
    vendor = json_data['vendorDetails']['companyName']
    if vendor:
        print "Vendor: %s" % vendor
    else:
        print "Vendor not found for MAC address %s" % sys.argv[1]
