#!/usr/bin/env python

import MySQLdb

class database(object):

    __HOST = '127.0.0.1'
    __USER = 'root'
    __PWD = '2112'
    __DB = 'yagra'
    __CHARACSET = 'utf-8'

    def __init__(self):
        
        # self.conn = MySQLdb.connect('127.0.0.1', 'root', '2112', 'yagra')
        self.conn = MySQLdb.connect(self.__HOST, self.__USER, self.__PWD, self.__DB)
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor()
        
        
    def add_user(self, username, password, salt):
        username = MySQLdb.escape_string(username)
        password = MySQLdb.escape_string(password)
        salt = MySQLdb.escape_string(salt)
        sql = "INSERT INTO yagra_user(username, password, salt) VALUES('%s', '%s', '%s')" % (username, password, salt)
        n = self.cursor.execute(sql)
        # self.conn.commit()
        return n == 1
        
    def get_user(username):
        username = MySQLdb.escape_string(username)
        sql = 'SELECT * FROM user WHERE username=%s' % username
        return exec_sql(sql)

