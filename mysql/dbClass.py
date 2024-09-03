#!/usr/bin/python3

import MySQLdb

class MyDBClass:
    
    def __init__(self):
        
        self.db = MySQLdb.connect(
            "192.168.1.1", 
            "readonly", 
            "readonly", 
            "test"
        )
        self.cursor = self.db.cursor()
   
    def getTickers(self):
        
        self.cursor.execute(
            "SELECT DISTINCT ticker FROM fund_info ORDER BY ticker limit 5"
        )
        result = self.cursor.fetchall()  
        self.cursor.close()
        self.db.close()
        
        return  result    