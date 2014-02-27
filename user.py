#!/usr/bin/env python

import db
import util

def check_username(username):
    return True
    
def check_password(password):
    return True

def register(username, password):
    if not check_username(username):
        util.error_redirect('/register', 'username format error')
        return
    if not check_password(password):
        util.error_redirect('/register', 'password format error')
        return
    mydb = db.database()
    salt = 'salt'
    n = mydb.add_user(username, password, salt)
    if n == 1:
        util.error_redirect('/login', 'register success')
        return
    else:
        util.error_redirect('/register', 'register failure')

def login(req):
    print 'content-Type: text/html\n'
    print 'login() invoked'

def logout(req):
    print 'content-Type: text/html\n'
    print 'logout() invoked()'

def showinfo(req):
    print 'content-Type: text/html\n'
    print 'info() invoked'

