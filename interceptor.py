#!/usr/bin/env python

import os
import re
import cgi
import cgitb
import Cookie
cgitb.enable()

class HTTPRequest(object):
    
    def __init__(self, uri):
        self.__DATA = {}
        env = os.environ
        cookie_string = env.get("HTTP_COOKIE")
        if cookie_string:
            cookie = Cookie.SimpleCookie()
            cookie.load(cookie_string)
            for key in cookie.keys():
                val = cookie[key].value
                if val:
                    self.__DATA[key] = val
        form = cgi.FieldStorage()
        for key in form.keys():
            val = form[key].value
            if val:
                self.__DATA[key] = val
    
    def get(self, key):
        return self.__DATA[key]


def intercept():
    __APIRE = re.compile(r'/avatar/(?P<md5>[\w]+)')
    env = os.environ
    uri = env["REQUEST_URI"]
    req = HTTPRequest(uri)
    path = uri.split("?", 1)[0]
    if path == '/register':
        import user
        username = req.get('username')
        password = req.get('password')
        user.register(username, password)
    elif path == '/login':
        import user
        user.login(username, password)
    elif path == '/logout':
        import user
        user.logout(username, sid)
    elif path == '/info':
        import user
        user.showinfo(username, sid)
    elif path == '/uploadavatar':
        import avatar
        avatar.uploadavatar(req)
    elif __APIRE.match(path):
        import avatar
        avatar.backavatar(req)
    else:
        import error
        error.errorprocess(req)

if __name__ == '__main__':
    intercept()
