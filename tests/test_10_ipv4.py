#!/usr/bin/env python

import rtapi_con as rt
import object_for_test as tobj

rt.rtapi.AddObject(tobj.test_object_ip['name'], tobj.test_object_ip['typeid'], tobj.test_object_ip['asset'], tobj.test_object_ip['label'])
obj_id = rt.rtapi.GetObjectId(tobj.test_object_ip['name'])

def test_UpdateNetworkInterface():
    # Add test interfaces
    for i in tobj.test_ip_interfaces:
        rt.rtapi.UpdateNetworkInterface(obj_id, i)

    # Check number of interfaces
    assert len(rt.rtapi.GetInterfaceList(obj_id)) == len(tobj.test_ip_interfaces)

def test_GetInterfaceName():
    assert rt.rtapi.GetInterfaceName(obj_id, rt.rtapi.GetInterfaceId(obj_id, tobj.test_ip_interfaces[0])) == tobj.test_ip_interfaces[0]

def test_InterfaceAddIpv4IP():
    assert rt.rtapi.InterfaceAddIpv4IP(obj_id, tobj.test_ip_interfaces[0], tobj.test_ip_addresses["ipv4"]) == None

def test_InterfaceGetIpv4IP():
    assert rt.rtapi.InterfaceGetIpv4IP(obj_id, tobj.test_ip_interfaces[0])[0][0] == tobj.test_ip_addresses["ipv4"]

def test_InterfaceAddIpv6IP():
    assert rt.rtapi.InterfaceAddIpv6IP(obj_id, tobj.test_ip_interfaces[0], tobj.test_ip_addresses["ipv6"]) == None

