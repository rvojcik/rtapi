rtapi
=====

Racktables API

Python module for accessing and manipulating racktables objects.

Dependency
------------------

* ipaddr module - https://code.google.com/p/ipaddr-py/

This module must be installed along with rtapi.

Installation
----------------
Simply copy rtapi and ipaddr into your projects folder or in place from where your project importing python modules.


Class manual
--------------------
    CLASSES
        RTObject
        
        class RTObject
         |  Ractables object. Require database object as argument.
         |  
         |  Methods defined here:
         |  
         |  AddDockerContainer(self, container_ip, container_name, docker_host)
         |      Add new Docker container to racktables
         |  
         |  AddObject(self, name, server_type_id, asset_no, label)
         |      Add new object to racktables
         |  
         |  AssignChassisSlot(self, chassis_name, slot_number, server_name)
         |      Assign server objects to server chassis
         |  
         |  CheckIfIp4IPExists(self, ip)
         |      Check if ipv4 record exist in database
         |  
         |  CleanIPAddresses(self, object_id, ip_addresses, device)
         |      Clean unused ip from object. ip addresses is list of IP addresses configured on device (device) on host (object_id)
         |  
         |  CleanIPv6Addresses(self, object_id, ip_addresses, device)
         |      Clean unused ipv6 from object. ip_addresses mus be list of active IP addresses on device (device) on host (object_id)
         |  
         |  CleanUnusedInterfaces(self, object_id, interface_list)
         |      Remove unused old interfaces
         |  
         |  CleanVirtuals(self, object_id, virtual_servers)
         |      Clean dead virtuals from hypervisor. virtual_servers is list of active virtual servers on hypervisor (object_id)
         |  
         |  FindIPFromComment(self, comment, network_name)
         |      Find IP address based on comment
         |  
         |  FindIPv6FromComment(self, comment, network_name)
         |      Find IP address based on comment
         |  
         |  GetAllServerChassisId(self)
         |      Get list of all server chassis IDs
         |  
         |  GetAttributeId(self, searchstring)
         |      Search racktables database and get attribud id based on search string as argument
         |  
         |  GetAttributeIdByName(self, attr_name)
         |      Get the ID of an attribute by its EXACT name
         |  
         |  GetAttributeValue(self, object_id, attr_id)
         |      Search racktables database and get attribute values
         |  
         |  GetDictionaryId(self, searchstring)
         |      Search racktables dictionary using searchstring and return id of dictionary element
         |  
         |  GetDictionaryIdByValue(self, dict_value)
         |      Get the ID of a dictionary entry by its EXACT value
         |  
         |  GetDictionaryValueById(self, dict_key)
         |      Get value from Dictionary by ID reference
         |  
         |  GetDockerContainerHost(self, ip)
         |      Get Docker container host
         |  
         |  GetDockerContainerName(self, ip)
         |      Get Docker container name
         |  
         |  GetInterfaceId(self, object_id, interface)
         |      Find id of specified interface
         |  
         |  GetInterfaceName(self, object_id, interface_id)
         |      Find name of specified interface. Required object_id and interface_id argument
         |  
         |  GetObjectComment(self, object_id)
         |      Get object comment
         |  
         |  GetObjectId(self, name)
         |      Translate Object name to object id
         |  
         |  GetObjectIdByAsset(self, service_tag)
         |      Get Object ID by Asset Tag
         |  
         |  GetObjectLabel(self, object_id)
         |      Get object label
         |  
         |  GetObjectName(self, object_id)
         |      Translate Object ID to Object Name
         |  
         |  GetObjectNameByAsset(self, service_tag)
         |      Translate Object AssetTag to Object Name
         |  
         |  GetObjectTags(self, object_id)
         |      Get object tags
         |  
         |  GetPortDeviceNameById(self, port_id)
         |      Get Device name and Port Name by port ID, return dictionary device_name, port_name
         |  
         |  InsertAttribute(self, object_id, object_tid, attr_id, string_value, uint_value, name)
         |      Add or Update object attribute. 
         |      Require 6 arguments: object_id, object_tid, attr_id, string_value, uint_value, name
         |  
         |  InsertDictionaryValue(self, dict_id, value)
         |      Insert value into dictionary identified by dict_id
         |  
         |  InsertIPv4Log(self, ip, message)
         |      Attach log message to IPv4
         |  
         |  InsertLog(self, object_id, message)
         |      Attach log message to specific object
         |  
         |  InsertOrUpdateAttribute(self, object_id, attr_id, new_value)
         |  
         |  InsertOrUpdateAttribute_FunctionDispatcher(self, attr_type)
         |  
         |  InsertOrUpdateFloatAttribute(self, object_id, objtype_id, attr_id, new_value)
         |  
         |  InsertOrUpdateStringAttribute(self, object_id, objtype_id, attr_id, new_value)
         |  
         |  InsertOrUpdateUintAttribute(self, object_id, objtype_id, attr_id, new_value)
         |  
         |  InterfaceAddIpv4IP(self, object_id, device, ip)
         |      Add/Update IPv4 IP on interface
         |  
         |  InterfaceAddIpv6IP(self, object_id, device, ip)
         |      Add/Update IPv6 IP on interface
         |  
         |  LinkNetworkInterface(self, object_id, interface, switch_name, interface_switch)
         |      Link two devices togetger
         |  
         |  LinkVirtualHypervisor(self, object_id, virtual_id)
         |      Assign virtual server to correct hypervisor
         |  
         |  ListDockerContainersOfHost(self, docker_host)
         |      List all Docker containers of specified host
         |  
         |  ListObjects(self)
         |      List all objects
         |  
         |  ObjectExistName(self, name)
         |      Check if object exist in database based on name
         |  
         |  ObjectExistST(self, service_tag)
         |      Check if object exist in database based on asset_no
         |  
         |  ObjectExistSTName(self, name, asset_no)
         |      Check if object exist in database based on name
         |  
         |  QueryTypedAttributeValue(self, object_id, attr_id, attr_type)
         |      # Attribute methods
         |  
         |  RemoveDockerContainerFromHost(self, container_name, docker_host)
         |      Remove Docker container from racktables
         |  
         |  UpdateDockerContainerHost(self, ip, host)
         |      Update Docker container host
         |  
         |  UpdateDockerContainerName(self, ip, name)
         |      Update Docker container name
         |  
         |  UpdateNetworkInterface(self, object_id, interface)
         |      Add network interfece to object if not exist
         |  
         |  UpdateObjectComment(self, object_id, comment)
         |      Update comment on object
         |  
         |  UpdateObjectLabel(self, object_id, label)
         |      Update label on object
         |  
         |  UpdateObjectName(self, object_id, name)
         |      Update name on object
         |  
         |  __init__(self, dbobject)
         |      Initialize Object
         |  
         |  db_fetch_lastid(self)
         |      SQL function which return ID of last inserted row.
         |  
         |  db_insert(self, sql)
         |      SQL insert/update function. Require sql query as parameter
         |  
         |  db_query_all(self, sql)
         |      SQL query function, return all rows. Require sql query as parameter
         |  
         |  db_query_one(self, sql)
         |      SQL query function, return one row. Require sql query as parameter

Example
-------


    import ipaddr
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




