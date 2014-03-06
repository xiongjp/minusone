#!/usr/bin/env python
'''
This module defines some functions used to process requests
relevant to avatar operations.
'''

import os
import db
import hashlib

import util
import session


def upload_avatar(req):
    '''
    Process avatar upload request.
    First check whether the user has logined.
    If uploading for the first time, insert a record to avatar table,
    else, if ext of the uploaded file is different from the old one, 
    remove the old avatar and update avatar table.
    Then save the uploaded image and update last_visit_time.
    '''
    if not req.has_key('cur_user') or not req.has_key('sid'):
        util.msg_redirect('/static/login.html', 'You havenot login')
        return
    filename = req.get('avatar').filename
    if not filename:
        util.msg_redirect('/info', "You haven't choose a image")
        return
    username = req.get('cur_user').value
    sid = req.get('sid').value
    username = username.strip()
    sid = sid.strip()
    if not session.auth_login(username, sid):
        util.msg_redirect('/static/login.html', 'You need to login')
        return
    filename = os.path.basename(filename)
    file_content = req.get('avatar').value
    md5 = hashlib.md5(username).hexdigest()
    ext = os.path.splitext(filename)[-1]
    old_ext = db.get_avatar_ext(md5)
    if old_ext:
        if old_ext != ext:
            # if update fails ?
            os.remove('avatar/'+ md5 + old_ext)
            db.update_avatar_ext(md5, ext)
    else:
        #if add fails ?
        db.add_avatar(md5, ext)
    # if save fails ?
    with open('avatar/'+ md5 + ext, 'wb') as f:
        f.write(file_content)
    session.update_visit_time(username)
    util.redirect('/info')


def back_avatar(md5):
    '''
    This function is the handler of avatar access API.
    We assure that the md5 hash of each email is unique.
    If corresponding user have uploaded an avatar, send it back;
    else send the default one back.
    '''
    ext = db.get_avatar_ext(md5)
    if ext != None:
        abspath = os.path.abspath('avatar/' + md5 + ext)
    else:
        abspath = os.path.abspath('static/default.jpg')
    print 'Content-Type: image'
    print 'Content-Disposition: inline; filename="%s"\n' % (md5 + ext)
    with open(abspath, 'rb') as f:
        content = f.read()
        print content
