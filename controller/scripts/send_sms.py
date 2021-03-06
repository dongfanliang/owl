#!/usr/bin/env python

import random
import sys
import httplib
import json
import urllib

address = ""

def send(subject, content, phone):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(address, timeout=30)
    url = "/sendalart?severity=1&subject={0}&msg={1}&phones={2}".format(subject, content, phone)
    conn.request("GET", urllib.quote(url, ":/=&()?,>."))
    response = conn.getresponse()
    return response.status, response.reason, response.read()

if __name__ == "__main__":
    script_name, subject, content, receiver = sys.argv[:]
    status, reason, response = send(subject, content, receiver)
    if status != 200:
        sys.exit("{0} {1} {2}".format(status, reason, response))
    print status, reason, response
