#!/usr/bin/env python
#coding=utf-8
'''
Created on 2014-1-24

@author: haha
'''

import json
import urllib2

request = urllib2.Request("http://web.juhe.cn:8080/finance/gold/bankgold?key=5ce57568e8f5ac1162fa360e04248ea2")
request.add_header('User-Agent', 'fake-client')
response = urllib2.urlopen(request)

page = response.read()
#jsonVal = json.loads(page)
s = json.loads(page)
#s = json.dumps(page)
#s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
#print s
#print s.keys()
print s["result"][0].keys()
print s["result"][0]["1"]
print s["result"][0]["1"]["variety"]
print s["result"][0]["1"]["maxpri"]
print s["result"][0]["1"]["time"]
#print s["type"]["name"]
#print s["type"]["parameter"][1]
#for val in s.keys():
#	if
#print s["result"]
#s1 = json.dumps(s["result"])
#print s1[0]
#s2 = json.loads(s1)
#print s1
#print s2.keys()
#	for val1 in s["result"].keys():
#		print s["result"][val1]
#print s[val]
#	print val["text"]
'''
class MyDecoder(json.JSONDecoder):

def __init__(self):
json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

def dict_to_object(self, d):
if '__class__' in d:
	class_name = d.pop('__class__')
	module_name = d.pop('__module__')
	module = __import__(module_name)
	print 'MODULE:', module
	class_ = getattr(module, class_name)
	print 'CLASS:', class_
	args = dict( (key.encode('ascii'), value) for key, value in d.items())
	print 'INSTANCE ARGS:', args
	inst = class_(**args)
else:
	inst = d
	

return inst
'''

