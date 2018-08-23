#!/usr/bin/env python

import MySQLdb
import sys

# Create connection to database
try:
    # Create connection to database
    db = MySQLdb.connect(host='rtdb',port=3306, passwd='toor',db='racktables',user='root')
except MySQLdb.Error:
    e = sys.exc_info()[1]
    print("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)

