#!/usr/bin/env python

import re

def check_username_format(username):
    username = username.strip()
    username_re = re.compile(r'([a-zA-Z]([\w]*[-_]?[\w]+)*@([\w]*[-_]?[\w]+)+)'
                             r'([\.][a-zA-Z]{2,3}([\.][a-zA-Z]{2})?)')
    if username_re.match(username):
        return True
    else:
        return False
    
def check_password_format(password):
    password = password.strip()
    if re.compile(r'([\w]{6,15})').match(password):
        return True
    else:
        return False

def error_redirect(location, msg, time=3):
    print 'content-Type: text/html\n'
    print """<html>
        <head>
        <meta http-equiv="refresh" content="%s;url=%s">
        <title></title>
        </head>
        <h2>%s</h2>
        <body>
        </body>
        </html>
    """ % (time, location, msg)
    
def redirect(location):
    print 'Location: %s' % location
    
def back_info_page(username, md5):
    print 'content-Type: text/html\n'
    print '''
            <html>
            <body>
            <h2>Hello, %s!</h2>
            <img src="http://www.gravatar.com/avatar/%s" /></div>
            <h2>This is your avatar, Change it?</h2><div>
            <form enctype="multipart/form-data" action="/upload" method="post">
            <p><input type="file" name="file"></p>
            <p><input type="submit" value="Upload"></p>
            </form>
            </body>
            </html>
           ''' % (username, md5)
