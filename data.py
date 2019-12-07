import database
import table

class Data(database,table):
    def __init__(self,DBKEY,TKEY):
        pass

    def insert(self,column,data):
        self.data[column].append(data)
