rtapi
=====

Racktables API

Python module for accessing and manipulating racktables objects.

Installation
----------------
    pip install racktables-api

Example
-------

    import MySQLdb
    import rtapi

    # Create connection to database
    try:
        # Create connection to database
        db = MySQLdb.connect(host='hostname',port=3306, passwd='mypass',db='racktables',user='racktables')
    except MySQLdb.Error ,e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    # Initialize rtapi with database connection
    rt = rtapi.RTObject(db)

    # List all objects from database
    print rt.ListObjects()




