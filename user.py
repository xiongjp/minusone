#!/usr/bin/env python

import os
import hashlib
import db
import util


def check_username_occupied(username):
    username = username.strip()
    if not db.get_user(username):
        return True
    else:
        return False


def register(username, password):
    username = username.strip()
    password = password.strip()
    if not util.check_username_format(username):
        util.error_redirect('/register', 'username format error')
        return
    if not check_username_occupied(username):
        util.error_redirect('/register', 'username occupied')
        return
    if not util.check_password_format(password):
        util.error_redirect('/register', 'password format error')
        return
    salt = os.urandom(64)
    password = hashlib.sha256(salt + password).hexdigest()
    success = db.add_user(username, password, salt)
    if success:
        util.error_redirect('/login', 'register success')
        return
    else:
        util.error_redirect('/register', 'register failure')


def login(username, password):
    username = username.strip()
    password = password.strip()
    if not util.check_username_format(username):
        util.error_redirect('/login', 'username format error')
        return
    if not util.check_password_format(password):
        util.error_redirect('/login', 'password format error')
        return
    result = db.get_user(username)
    if result == None:
        util.error_redirect('/login', 'username or password incorrect')
        return
    salt = result.get('salt')
    encrypted_password = result.get('password')
    if hashlib.sha256(salt + password).hexdigest() == encrypted_password:
        util.error_redirect('/login', 'login success')
        return
    else:
        util.error_redirect('/login', 'username or password incorrect')
        return


def logout(req):
    print 'content-Type: text/html\n'
    print 'logout() invoked()'

def showinfo(username, md5):
    util.back_info_page(username, md5)

