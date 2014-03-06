#!/usr/bin/env python

import re
import os
import Cookie

# cookie valid time, 10 days
COOKIE_VALIDITY = 10 * 24 * 60 * 60


def set_cookie(data):
    '''
    Construct a cookie using data in a dict,
    then write the cookie to http header.
    '''
    if not data:
        return
    cookie = Cookie.SimpleCookie()
    for key in data.keys():
        cookie[key] = data[key]
        cookie[key]['expires'] = COOKIE_VALIDITY
    print cookie


def check_username_format(username):
    '''Check whether username match the format of email'''
    username = username.strip()
    username_re = re.compile(r'([a-zA-Z]([\w]*[-_]?[\w]+)*@([\w]*[-_]?[\w]+)+)'
                             r'([\.][a-zA-Z]{2,3}([\.][a-zA-Z]{2})?)')
    if username_re.match(username):
        return True
    else:
        return False


def check_password_format(password):
    '''Check whether password is 6-15-char(only letters and digits) long'''
    password = password.strip()
    if re.compile(r'([\w]{6,15})').match(password):
        return True
    else:
        return False


def msg_redirect(location, msg, time=2):
    '''
    Redirect browser to the specified location 
    after displaying the hint msg for specified time.
    Default displaying time is 2s.
    '''
    print 'content-Type: text/html\n'
    with open('template/msg_redirect', 'r') as f:
        msg_redirect_page = f.read() % (time, location, msg)
        print msg_redirect_page


def redirect(location):
    '''Redirect browser to the specified location instantly.'''
    location = location[1:]
    print 'Location: %s\n' % location
