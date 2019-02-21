#!/usr/bin/env python

import rtapi_con as rt
import object_for_test
test_dict_value = None
test_chapter = 'kernels'
test_object_id = 1


def test_GetAttributeIdByName():
    assert isinstance(rt.rtapi.GetAttributeIdByName('HW type'), int) == True

def test_GetAttributeId():
    assert isinstance(rt.rtapi.GetAttributeId('HW type'), int) == True

def test_GetDictionaryChapterId():
    chapter_id = rt.rtapi.GetDictionaryChapterId('Yes/No')
    assert isinstance(chapter_id, int) == True

def test_IntertDictionaryValue():
    chapter_id = rt.rtapi.GetDictionaryChapterId('server models')
    assert rt.rtapi.InsertDictionaryValue(chapter_id, 'testmodel') == None

def test_GetDictionaryIdByValue():
    global test_dict_value
    test_dict_value = rt.rtapi.GetDictionaryIdByValue('testmodel')
    assert isinstance(test_dict_value, int) == True 

def test_GetDictionaryValueById():
    assert rt.rtapi.GetDictionaryValueById(test_dict_value) == 'testmodel'

def test_InsertDictionaryChapter():
    assert rt.rtapi.InsertDictionaryChapter(test_chapter) == None

def test_InsertAttribute():
    att_id = rt.rtapi.GetAttributeId("HW type")
    hw_id = rt.rtapi.GetDictionaryId('testmodel')
    assert rt.rtapi.InsertAttribute(test_object_id,4,att_id,"NULL",hw_id, 'TESTNAME') == None
