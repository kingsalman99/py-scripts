#!/usr/bin/python3
#coding: utf-8
import urllib.request, urllib.error
import sys, csv, time
from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock

if len(sys.argv) < 2:
    print("Usage: %s /path/to/users.csv" % (str(sys.argv[0])))
    sys.exit(1)

filecsv=sys.argv[1] 

PERISCOPE_URL = 'https://www.periscope.tv/'
usernames = []

def attempt(unames):
    try:
        conn = urllib.request.urlopen(PERISCOPE_URL+unames[:-2])
    except urllib.error.HTTPError as e:
    	print("[-] " + unames[:-2] + " " + str(e.code))
    else:
        print("[+] " + unames[:-2] + " " + str(conn.getcode()))

with open(filecsv, "r") as f:
    reader = csv.reader(f, delimiter=',')
    usernames2 = list(reader)
    unames = usernames2[0]
lock = Lock()
pool = ThreadPool(5)

pool.map(attempt, unames)
pool.close()
pool.join()