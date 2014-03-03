#!/usr/bin/env python

import os
import db
import hashlib

import util
import session

def upload_avatar(username, sid, filename, file_content):
    username = username.strip()
    sid = sid.strip()
    if not session.auth_login(username, sid):
        util.msg_redirect('/static/login.html', 'You need to login')
        return
    md5 = hashlib.md5(username).hexdigest()
    ext = os.path.splitext(filename)[-1]
    old_ext = db.get_avatar_ext(md5)
    if old_ext:
        if old_ext != ext:
            # if update fails ?
            db.update_avatar_ext(md5, ext)
    else:
        #if add fails ?
        db.add_avatar(md5, ext)
    # if save fails ?
    util.save_avatar(md5 + ext, file_content)
    session.update_visit_time(username)
    util.redirect('/info')

def back_avatar(md5):
    ext = db.get_avatar_ext(md5)
    if ext:
        abspath = os.path.abspath('avatar/' + md5 + ext)
    else:
        abspath = os.path.abspath('static/default.jpg')
    content = open(abspath, 'rb').read()
    print 'content-Type: image\n'
    print content
