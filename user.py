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
        util.msg_redirect('/static/register.html', 'username format error')
        return
    if not check_username_occupied(username):
        util.msg_redirect('/static/register.html', 'username occupied')
        return
    if not util.check_password_format(password):
        util.msg_redirect('/static/register.html', 'password format error')
        return
    salt = os.urandom(64)
    password = hashlib.sha256(salt + password).hexdigest()
    success = db.add_user(username, password, salt)
    if success:
        sid = hashlib.md5(str(random.random())).hexdigest()
        session.add_session(username, sid)
        data = {}
        data['sid'] = sid
        data['username'] = username
        util.set_cookie(data)
        util.redirect('/info')
        return
    else:
        util.msg_redirect('/static/register.html', 'register failure')


def login(username, password):
    username = username.strip()
    password = password.strip()
    if not util.check_username_format(username):
        util.msg_redirect('/static/login.html', 'username format error')
        return
    if not util.check_password_format(password):
        util.msg_redirect('/static/login.html', 'password format error')
        return
    user = db.get_user(username)
    if user == None:
        util.msg_redirect('/static/login.html', 
                          'username or password incorrect')
        return
    salt = user.get('salt')
    encrypted_password = user.get('password')
    if hashlib.sha256(salt + password).hexdigest() == encrypted_password:
        sid = hashlib.md5(str(random.random())).hexdigest()
        session.set_session(username, sid)
        data = {}
        data['sid'] = sid
        data['username'] = username
        util.set_cookie(data)
        util.redirect('/info')
        return
    else:
        util.msg_redirect('/static/login.html', 
                          'username or password incorrect')
        return


def logout(username):
    username = username.strip()
    session.clear_sid(username)
    util.redirect('/http://'+os.environ['HTTP_HOST'])


def showinfo(username, sid):
    username = username.strip()
    sid = sid.strip()
    if not session.auth_login(username, sid):
        util.msg_redirect('/static/login.html', 'You need to login')
        return
    md5 = hashlib.md5(username).hexdigest()
    ext = db.get_avatar_ext(md5)
    if ext != None:
        filename = 'avatar/' + md5 + ext
    else:
        filename = 'static/default.jpg'
    util.back_info_page(username, filename)

