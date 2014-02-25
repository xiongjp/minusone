#!/usr/bin/env python

import os
import re
import cgi
import cgitb
cgitb.enable()

class HTTPRequest(object):
    
    def __init__(self, uri):
        pass


def intercept():
    __APIRE = re.compile(r'/avatar/(?P<md5>[\w]+)')
    env = os.environ
    uri = env["REQUEST_URI"]
    req = HTTPRequest(uri)
    path = uri.split("?", 1)[0]
    if path == '/register':
        from user import register
        register(req)
    elif path == '/login':
        from user import login
        login(req)
    elif path == '/logout':
        from user import logout
        logout(req)
    elif path == '/info':
        from user import showinfo
        showinfo(req)
    elif path == '/uploadavatar':
        from avatar import uploadavatar
        uploadavatar(req)
    elif __APIRE.match(path):
        from avatar import backavatar
        backavatar(req)
    else:
        from error import errorprocess
        errorprocess(req)

if __name__ == '__main__':
    intercept()
