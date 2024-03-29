# rtapi

[![pipeline status](https://gitlab.com/rvojcik/rtapi/badges/master/pipeline.svg)](https://gitlab.com/rvojcik/rtapi/commits/master) [![coverage report](https://gitlab.com/rvojcik/rtapi/badges/master/coverage.svg)](https://gitlab.com/rvojcik/rtapi/commits/master)

Racktables API

Python module for accessing and manipulating RackTables objects.

# Installation

```bash
pip install mysqlclient
pip install racktables-api
```

# PyPi project

https://pypi.org/project/racktables-api/

# Documentation

https://rtapi.readthedocs.io

# Example

```python
import MySQLdb
import rtapi
import sys

# Create connection to database
try:
    # Create connection to database
    db = MySQLdb.connect(host='hostname',port=3306, passwd='mypass',db='racktables',user='racktables')
except MySQLdb.Error:
    e = sys.exc_info()[1]
    print("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)

# Initialize rtapi with database connection
rt = rtapi.RTObject(db)

# List all objects from database
print (rt.ListObjects(data='list'))

# List all IPv4 Networks from database
print (rt.GetIpv4Networks())
```
