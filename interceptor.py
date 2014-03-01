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
                val = cookie[key]
                if val != None:
                    self.__DATA[key] = val
        form = cgi.FieldStorage()
        for key in form.keys():
            val = form[key]
            if val != None:
                self.__DATA[key] = val
    
    def get(self, key):
        return self.__DATA[key]
        
    def has_key(self, key):
        return self.__DATA.has_key(key)
        
    def keys(self):
        return self.__DATA.keys()


def intercept():
    env = os.environ
    uri = env["REQUEST_URI"]
    req = HTTPRequest(uri)
    path = uri.split("?", 1)[0]
    if path == '/register':
        import user
        username = req.get('username').value
        password = req.get('password').value
        user.register(username, password)
    elif path == '/login':
        import user
        username = req.get('username').value
        password = req.get('password').value
        user.login(username, password)
    elif path == '/logout':
        import user
        user.logout(username, sid)
    elif path == '/info':
        import user
        username = req.get('username').value
        sid = req.get('sid').value
        user.showinfo(username, sid)
    elif path == '/upload':
        import avatar
        import util
        username = req.get('username').value
        sid = req.get('sid').value
        filename = os.path.basename(req.get('avatar').filename)
        file_content = req.get('avatar').value
        avatar.upload_avatar(username, sid, filename, file_content)
    elif re.compile(r'/avatar/(?P<md5>[\w]+)').match(path):
        import avatar
        md5 = path[8:40]
        avatar.back_avatar(md5)
    else:
        import util
        util.msg_redirect('/login','unsupported url')

if __name__ == '__main__':
    intercept()
