#!/usr/bin/env python

'''This module defines some functions used to manage database.'''

import time

import MySQLdb

from config import *


conn = MySQLdb.connect(HOST, USER, PWD, DB)
conn.autocommit(1)
cursor = conn.cursor()


def add_user(username, password, salt):
    '''
    Insert a record to user table.
    Return whether the operation is successful.
    '''
    username = MySQLdb.escape_string(username)
    password = MySQLdb.escape_string(password)
    salt = MySQLdb.escape_string(salt)
    sql = "INSERT INTO yagra_user(username, password, salt) \
           VALUES('%s', '%s', '%s')" % (username, password, salt)
    n = cursor.execute(sql)
    return n == 1


def get_user(username):
    '''
    Retrieve the user record corresponding to the username.
    If the record don't exist, return None;
    else return the tuple in a dict form.
    '''
    username = MySQLdb.escape_string(username)
    sql = "SELECT id,password,salt \
           FROM yagra_user WHERE username='%s'" % username
    n = cursor.execute(sql)
    if n == 0:
        return None
    row = cursor.fetchone()
    result = {}
    result['id'] = row[0]
    result['password'] = row[1]
    result['salt'] = row[2]
    return result


def add_avatar(md5, ext):
    '''
    Insert a record to avater table.
    Return whether the operation is successful.
    '''
    md5 = MySQLdb.escape_string(md5)
    ext = MySQLdb.escape_string(ext)
    sql = "INSERT INTO yagra_avatar(md5, ext) VALUES('%s', '%s')"  % (md5, ext)
    n = cursor.execute(sql)
    return n == 1


def get_avatar_ext(md5):
    '''
    Retrieve ext of the avatar record corresponding to the md5 hash.
    If the record don't exist, return None; else return the found ext.
    '''
    md5 = MySQLdb.escape_string(md5)
    sql = "SELECT ext FROM yagra_avatar WHERE md5='%s'" % md5
    n = cursor.execute(sql)
    if n==0:
        return None
    row = cursor.fetchone()
    return row[0]


def update_avatar_ext(md5, ext):
    '''
    Update ext of the avatar record corresponding to the md5 hash.
    Return whether the operation is successful.
    '''
    md5 = MySQLdb.escape_string(md5)
    ext = MySQLdb.escape_string(ext)
    sql = "UPDATE yagra_avatar SET ext='%s' WHERE md5='%s'" % (ext, md5)
    n = cursor.execute(sql)
    return n == 1


def add_session(username, sid):
    '''
    Insert a record to session table.
    Return whether the operation is successful.
    '''
    username = MySQLdb.escape_string(username)
    sid = MySQLdb.escape_string(sid)
    now_time = time.time()
    sql = "INSERT INTO yagra_session(username, sid, last_visit_time) \
           VALUES('%s', '%s', '%s')" % (username, sid, now_time)
    n = cursor.execute(sql)
    return n == 1


def get_session(username):
    '''
    Retrieve session corresponding to the username.
    If the record don't exist, return None;
    else return the session in a dict form.
    '''
    username = MySQLdb.escape_string(username)
    sql = "SELECT sid,last_visit_time \
           FROM yagra_session WHERE username='%s'" % username
    n = cursor.execute(sql)
    if n == 0:
        return None
    row = cursor.fetchone()
    session = {}
    session['sid'] = row[0]
    session['last_visit_time'] = row[1]
    return session


def set_session(username, sid, now_time):
    '''
    Update sid and last_visit_time of the session corresponding to the 
    username. Return whether the operation is successful.
    '''
    username = MySQLdb.escape_string(username)
    sid = MySQLdb.escape_string(sid)
    sql = "UPDATE yagra_session SET sid='%s',last_visit_time='%s' \
           WHERE username='%s'" % (sid, now_time, username)
    n = cursor.execute(sql)
    return n == 1


def set_session_time(username, now_time):
    '''
    Update last_visit_time of the session corresponding to the username.
    Return whether the operation is successful.
    '''
    username = MySQLdb.escape_string(username)
    sql = "UPDATE yagra_session SET last_visit_time='%s' \
           WHERE username='%s'" % (now_time, username)
    n = cursor.execute(sql)
    return n == 1


def set_session_sid(username, sid):
    '''
    Update sid of the session corresponding to the username.
    Return whether the operation is successful.
    '''
    username = MySQLdb.escape_string(username)
    sid = MySQLdb.escape_string(sid)
    sql = "UPDATE yagra_session SET sid='%s' \
           WHERE username='%s'" % (sid, username)
    n = cursor.execute(sql)
    return n == 1
