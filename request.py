#!/usr/bin/env python

'''This module defines a class used to wrap request data.'''

import os
import Cookie
import cgi

class HTTPRequest(object):
    '''
    Wrap all data relevant to a request into a dict,
    including the data in form and the data in cookie.
    Values in the dict are objects, not strings.
    You can access request parameter like this:
    
        username = req.get('username').value
        In this case, 'username' is the name of an input field.
    
        filename = req.get('avatar').filename
        In this case, 'avatar' is the name of a uploaded file.
    '''
    def __init__(self):
        self.__DATA = {}
        env = os.environ
        cookie_string = env.get('HTTP_COOKIE')
        if cookie_string:
            cookie = Cookie.SimpleCookie()
            cookie.load(cookie_string)
            for key in cookie.keys():
                val = cookie[key]
                if val != None:
                    self.__DATA[key] = val
        form = cgi.FieldStorage()
        for key in form.keys():
            val = form[key]
            # It's likely that __nonzero__() in class FieldStorage always 
            # return False when upload a file
            # so I use 'if val != None:' instead of 'if val:'
            if val != None:
                self.__DATA[key] = val
    
    def get(self, key):
        return self.__DATA[key]
        
    def has_key(self, key):
        return self.__DATA.has_key(key)
        
    def keys(self):
        return self.__DATA.keys()

