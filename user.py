#!/usr/bin/env python

import os
import hashlib
import random
import Cookie

import db
import util
import session

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
        util.msg_redirect('/register', 'username format msg')
        return
    if not check_username_occupied(username):
        util.msg_redirect('/register', 'username occupied')
        return
    if not util.check_password_format(password):
        util.msg_redirect('/register', 'password format msg')
        return
    salt = os.urandom(64)
    password = hashlib.sha256(salt + password).hexdigest()
    success = db.add_user(username, password, salt)
    if success:
        sid = hashlib.md5(str(random.random())).hexdigest()
        cookie = Cookie.SimpleCookie()
        cookie['sid'] = sid
        cookie['username'] = username
        session.add_session(sid, username)
        util.set_cookie(cookie)
        util.msg_redirect('/info','register success')
        return
    else:
        util.msg_redirect('/register', 'register failure')


def login(username, password):
    username = username.strip()
    password = password.strip()
    if not util.check_username_format(username):
        util.msg_redirect('/login', 'username format msg')
        return
    if not util.check_password_format(password):
        util.msg_redirect('/login', 'password format msg')
        return
    user = db.get_user(username)
    if user == None:
        util.msg_redirect('/login', 'username or password incorrect')
        return
    salt = user.get('salt')
    encrypted_password = user.get('password')
    if hashlib.sha256(salt + password).hexdigest() == encrypted_password:
        util.msg_redirect('/login', 'login success')
        return
    else:
        util.msg_redirect('/login', 'username or password incorrect')
        return


def logout(req):
    print 'content-Type: text/html\n'
    print 'logout() invoked()'

def showinfo(username, sid):
    username = username.strip()
    sid = sid.strip()
    if not session.auth_login(username, sid):
        util.msg_redirect('/login', 'You need to login')
        return
    md5 = hashlib.md5(username).hexdigest()
    ext = db.get_avatar_ext(md5)
    if ext:
        filename = 'avatar/' + md5 + ext
    else:
        filename = 'static/default.jpg'
    util.back_info_page(username, filename)

