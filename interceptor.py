#!/usr/bin/env python
'''
Apache redirect all dynamic requests to this script.
On each dynamic request, this script invokes corresponding function 
according to request path.
'''
import re
import cgitb
import os

import user
import avatar
import util
import request


cgitb.enable()


def intercept():
    '''
    This function will be invoked when a dynamic request comes.
    It firstly gets request path from evironment variables,
    then invokes corresponding functions according to request path.
    '''
    env = os.environ
    # Get request uri from environment variables 
    uri = env['REQUEST_URI']
    # Get request path, leaving out query string
    path = uri.split('?', 1)[0]
    # Construct HTTPResquest object
    req = request.HTTPRequest()
    
    # Invoke corresponding functions according to request path
    if path == '/register':
        user.register(req)
    elif path == '/login':
        user.login(req)
    elif path == '/logout':
        user.logout(req)
    elif path == '/info':
        user.showinfo(req)
    elif path == '/upload':
        avatar.upload_avatar(req)
    elif re.compile(r'/avatar/(?P<md5>[\w]+)').match(path):
        # Get 32-char long md5, leaving out image ext or other chars.
        # If the length of md5 part is less than 32, get all the part. 
        md5 = path[8:40]
        avatar.back_avatar(md5)
    else:
        util.msg_redirect('/static/homepage.html','unsupported url')


if __name__ == '__main__':
    intercept()
