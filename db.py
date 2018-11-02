#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:36:32 2018

@author: jan
"""

import sqlite3


class DB():
    """
    connection to application database
    """
    def __init__(self, initializeNewDB=False):
        self.conn = sqlite3.connect('users.db')
        self.cur = self.conn.cursor()
        if initializeNewDB:
            self.cur.execute("""
                     create table users(user text, password text) 
                     """)
            self.conn.commit()
        
    def addUser(self, user, password):
        self.cur.execute("""
                        insert into users values(?, ?)                 
                        """, (user, password))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
    @property
    def users(self):
        self.cur.execute("""
                         select * from users
                         """)
        print(self.cur.fetchall())
        
    def deleteUser(self, user):
        self.cur.execute("""
                         delete from users where user=?                         
        """, (user,))
    
if __name__ == '__main__':
    db = DB()
    

    