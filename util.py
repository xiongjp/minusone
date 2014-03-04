#!/usr/bin/env python

import re
import os
import Cookie

COOKIE_VALIDITY = 10 * 24 * 60 * 60

def set_cookie(data):
    if not data:
        return
    cookie = Cookie.SimpleCookie()
    for key in data.keys():
        cookie[key] = data[key]
        cookie[key]['expires'] = COOKIE_VALIDITY
    print cookie


def save_avatar(filename, file_content):
    open('avatar/'+filename, 'wb').write(file_content)


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


def msg_redirect(location, msg, time=2):
    print 'content-Type: text/html\n'
    msg_redirect_page = open('template/msg_redirect', 
                             'r').read() % (time, location, msg)
    print msg_redirect_page

def redirect(location):
    location = location[1:]
    print 'Location: %s\n' % location


def back_info_page(username, filename):
    print 'content-Type: text/html\n'
    info_page = open('template/info', 'r').read() % (username, filename)
    print info_page
