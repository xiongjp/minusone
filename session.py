#!/usr/bin/env python

'''
This module defines some functions relevant to session operation,
mainly used to do access control.
'''

import db
import time

# Session valid time, 15 mins.
SESSION_VALIDITY = 15 * 60


def auth_login(username, sid):
    '''
    Check whether the user have logined.
    If so, check whether the login have expired.
    '''
    session = db.get_session(username)
    if session == None:
        return False
    if session['sid'] != sid:
        return False
    now_time = time.time()
    if now_time - session['last_visit_time'] > SESSION_VALIDITY:
        return False
    update_visit_time(username)
    return True


def add_session(username, sid):
    '''Initialize a session.'''
    return db.add_session(username, sid)


def set_session(username, sid):
    '''
    Set sid of the user's session.
    The sid should be a 32-char md5 hash of a random number.
    '''
    if len(sid) != 32:
        return False;
    now_time = time.time()
    return db.set_session(username, sid, now_time)


def clear_sid(username):
    '''Invalid a session by setting sid to ''.'''
    return db.set_session_sid(username, '')


def update_visit_time(username):
    '''Update last_viast_time in a session to now time.'''
    now_time = time.time()
    return db.set_session_time(username, now_time)
