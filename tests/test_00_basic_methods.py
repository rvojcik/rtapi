#!/usr/bin/env python

import rtapi_con as rt
import object_for_test
import sys
test_object = object_for_test.test_object_basic
test_object_id = 0

if sys.version_info[0] == 2:
    test_instance = long
else:
    test_instance = int

def test_noObjectExistST():
    assert rt.rtapi.ObjectExistST('asdf000') == False

def test_noObjectExistName():
    assert rt.rtapi.ObjectExistName('asdf000') == False

def test_AddObject():
    global test_object_id
    test_object_id = rt.rtapi.AddObject(test_object["name"],test_object["typeid"],test_object["asset"], test_object["label"])
    assert isinstance(test_object_id, test_instance) == True

def test_ObjectExistST():
    assert rt.rtapi.ObjectExistST(test_object["asset"]) == True

def test_ObjectExistName():
    assert rt.rtapi.ObjectExistName(test_object["name"]) == True

def test_GetObjectName():
    assert rt.rtapi.GetObjectName(test_object_id) == test_object["name"]

def test_GetObjectNameByAsset():
    assert rt.rtapi.GetObjectNameByAsset(test_object["asset"]) == test_object["name"]

def test_GetObjectIdByAsset():
    assert rt.rtapi.GetObjectIdByAsset(test_object["asset"]) == test_object_id

def test_GetObjectLabel():
    assert rt.rtapi.GetObjectLabel(test_object_id) == test_object["label"]

def test_UpdateObjectComment():
    assert rt.rtapi.UpdateObjectComment(test_object_id, 'commentXY') == None

def test_GetObjectComment():
    assert rt.rtapi.GetObjectComment(test_object_id) == 'commentXY'

def test_UpdateObjectLabel():
    assert rt.rtapi.UpdateObjectLabel(test_object_id, 'labelXY') == None

def test_UpdateObjectName():
    assert rt.rtapi.UpdateObjectName(test_object_id, 'TESTNAME') == None

def test_GetObjectId():
    assert rt.rtapi.GetObjectId('TESTNAME') == test_object_id


