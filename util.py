#!/usr/bin/env python

def error_redirect(location, msg, time=3):
    print 'content-Type: text/html\n'
    print """<html>
        <head>
        <meta http-equiv="refresh" content="%s;url=%s">
        <title></title>
        </head>
        <h2>%s</h2>
        <body>
        </body>
        </html>
    """ % (time, location, msg)
    
def redirect(location):
    print 'Location: %s' % location
