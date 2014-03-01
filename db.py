#!/usr/bin/env python

import MySQLdb

HOST = '127.0.0.1'
USER = 'root'
PWD = '2112'
DB = 'yagra'
CHARACSET = 'utf-8'

conn = MySQLdb.connect(HOST, USER, PWD, DB)
conn.autocommit(1)
cursor = conn.cursor()


def add_user(username, password, salt):
    username = MySQLdb.escape_string(username)
    password = MySQLdb.escape_string(password)
    salt = MySQLdb.escape_string(salt)
    sql = "INSERT INTO yagra_user(username, password, salt) VALUES('%s', '%s', '%s')" % (username, password, salt)
    n = cursor.execute(sql)
    return n == 1

def get_user(username):
    username = MySQLdb.escape_string(username)
    sql = "SELECT id,password,salt FROM yagra_user WHERE username='%s'" % username
    n = cursor.execute(sql)
    if n == 0:
        return None
    row = cursor.fetchone()
    result = {}
    result['id'] = row[0]
    result['password'] = row[1]
    result['salt'] = row[2]
    return result
    
def get_avatar_ext(md5):
    md5 = MySQLdb.escape_string(md5)
    sql = "SELECT ext FROM yagra_avatar WHERE md5='%s'" % md5
    n = cursor.execute(sql)
    if n==0:
        return None
    row = cursor.fetchone()
    return row[0]
    
def update_avatar_ext(md5, ext):
    md5 = MySQLdb.escape_string(md5)
    ext = MySQLdb.escape_string(ext)
    sql = "UPDATE yagra_avatar SET ext='%s' WHERE md5='%s'" % (ext, md5)
    n = cursor.execute(sql)
    return n == 1
    
def add_avatar(md5, ext):
    md5 = MySQLdb.escape_string(md5)
    ext = MySQLdb.escape_string(ext)
    sql = "INSERT INTO yagra_avatar(md5, ext) VALUES('%s', '%s')"  % (md5, ext)
    n = cursor.execute(sql)
    return n == 1
