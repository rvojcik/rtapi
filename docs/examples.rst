Working Examples
================

.. highlight:: python

Some of working example to help starting with rtapi.

.. code-block:: python
    
    import MySQLdb
    import rtapi

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
    print rt.ListObjects()

