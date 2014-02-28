#!/usr/bin/env python

import os
import db

def uploadavatar(req):
    print 'content-Type: text/html\n'
    print 'uploadavatar() invoked'

def back_avatar(md5):
    md5 = md5.strip()
    ext = db.get_avatar_ext(md5)
    if ext:
        abspath = os.path.abspath('avatar/' + md5 + ext)
    else:
        abspath = os.path.abspath('static/default.jpg')
    content = open(abspath, 'rb').read()
    print 'content-Type: image\n'
    # print 'content-Type: %s\n' % mimetypes.types_map.get(ext)
    print content
