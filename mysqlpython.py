from pymysql import *

class Mysqlpython:
    def __init__(self,database,host='192.168.43.249',user='root',
                    password='123456',port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.database = database
    def open(self):
        self.db = connect(host=self.host,user=self.user,password=self.password,
                        port=self.port,database=self.database,charset=self.charset)
        self.cur = self.db.cursor()
    def close(self):
        self.cur.close()
        self.db.close()
    def zhixing(self,sql,L=[]):#相当于pymysql.execute(sql)
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            self.close()
            return 'OK'
        except Exception as e:
            self.db.rollback()
            self.close()
            return e
            
    def all(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            self.close()
            return result
        except Exception as e:
            print('failed',e)
        self.close()


















