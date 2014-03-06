#!/usr/bin/env python
'''
This module defines some functions used to process requests
relevant to user operations.
'''

import os
import hashlib
import random
import Cookie

import db
import util
import session
import request


def check_username_occupied(username):
    '''
    If the username has been occupied, return True;
    else return False.
    '''
    if not db.get_user(username):
        return True
    else:
        return False


def register(req):
    '''
    Process register request.
    A successful register includes inserting a record to user table, 
    initializing a session record and setting a cookie.
    '''
    if not req.has_key('username'):
        util.msg_redirect('/static/register.html', 'username must not empty')
        return
    if not req.has_key('password'):
        util.msg_redirect('/static/register.html', 'password must not empty')
        return
    username = req.get('username').value
    password = req.get('password').value
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
        data['cur_user'] = username
        util.set_cookie(data)
        util.redirect('/info')
        return
    else:
        util.msg_redirect('/static/register.html', 'register failure')


def login(req):
    '''
    Process login request.
    After login, a cookie will be set.
    '''
    if not req.has_key('username'):
        util.msg_redirect('/static/login.html', 'username must not empty')
        return
    if not req.has_key('password'):
        util.msg_redirect('/static/login.html', 'password must not empty')
        return
    username = req.get('username').value
    password = req.get('password').value
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
        data['cur_user'] = username
        util.set_cookie(data)
        util.redirect('/info')
        return
    else:
        util.msg_redirect('/static/login.html', 
                          'username or password incorrect')
        return


def logout(req):
    '''
    Process logout request.
    First check whether the user has logined,
    then clear the corresponding session.
    '''
    if not req.has_key('cur_user') or not req.has_key('sid'):
        util.msg_redirect('http://' +os.environ['HTTP_HOST'],
                          'You havenot login')
        return
    username = req.get('cur_user').value
    sid = req.get('sid').value
    if not session.auth_login(username, sid):
        util.msg_redirect('http://' +os.environ['HTTP_HOST'],
                          'You havenot login')
        return
    username = username.strip()
    if session.clear_sid(username):
        util.redirect('/http://'+os.environ['HTTP_HOST'])
    else:
        util.msg_redirect('http://' +os.environ['HTTP_HOST'],
                          'logout fails')


def showinfo(req):
    '''
    Process info display request.
    First check whether the user has logined, then display his avatar.
    If the user hasn't upload an avatar, display the default one.
    '''
    if not req.has_key('cur_user') or not req.has_key('sid'):
        util.msg_redirect('/static/login.html', 'You havenot login')
        return
    username = req.get('cur_user').value
    sid = req.get('sid').value
    username = username.strip()
    sid = sid.strip()
    if not session.auth_login(username, sid):
        util.msg_redirect('/static/login.html', 'You havenot login')
        return
    md5 = hashlib.md5(username).hexdigest()
    ext = db.get_avatar_ext(md5)
    if ext != None:
        filename = 'avatar/' + md5 + ext
    else:
        filename = 'static/default.jpg'
    print 'content-Type: text/html\n'
    with open('template/info', 'r') as f:
        info_page = f.read() % (username, filename)
        print info_page

