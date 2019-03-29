import sqlite3
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class slite:
    def connecttodb(self):
        dname = config.get('Sqlite','Database/URI')
        self.db = sqlite3.connect(dname)
        self.cur = self.db.cursor()

    def getphone(self):
        self.table = config.get('General','Table')
        phone = config.get('General','Phone_column')
        row = self.cur.execute("select "+phone+" from "+self.table)
        return row.fetchall()

    def getemail(self):
        email = config.get('General','Email_column')
        row = self.cur.execute("select "+email+" from "+self.table)
        row = row.fetchall()
        row = [item[0] for item in row]
        return row
