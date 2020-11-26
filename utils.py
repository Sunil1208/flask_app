import pymysql
import os

DEBUG = os.environ.get("FLASK_DEBUG") == "1"

class DBManager(object):
    def __init__(self, dbconfig):
        self.db = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], passwd=dbconfig['passwd'], db=dbconfig['db'], autocommit=True)
        self.cursor = self.db.cursor(pymysql.cursor.DictCursor)

    def fetchData(self, sql, args=()):
        self.cursor.execute(sql, args)
        print(self.cursor._last_executed)
        return self.cursor

    def runQuery(self, sql, args=()):
        try:
            self.cursor.execute(sql, args)
            print(self.cursor._last_executed)
            return self.cursor
        except Exception as err:
            if hasattr(self.cursor, '_last_executed'):
                print("Unexpected error: SQL runQuery: Exception: ", err, ", SQL_executed: ", self.cursor._last_executed)
            else:
                print("Unexpected error: SQL runQuery: Exception: ", err, ", SQL_sent: ", sql, ", args: ", args)
            return None
        
    def close(self):
        self.db.close()