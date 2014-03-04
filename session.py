#!/usr/bin/env python

import db
import time

SESSION_VALIDITY = 15 * 60


def auth_login(username, sid):
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
    return db.add_session(username, sid)


def set_session(username, sid):
    now_time = time.time()
    return db.set_session(username, sid, now_time)


def clear_sid(username):
    return db.set_session_sid(username, '')


def update_visit_time(username):
    now_time = time.time()
    return db.set_session_time(username, now_time)
