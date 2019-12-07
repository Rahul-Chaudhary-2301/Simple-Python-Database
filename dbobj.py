import pickle
#object
dblist = {}
#dblist
#dblist = {DBNAME : DBKEY,}
#tblist
#tblist = {DBKEY : {TBNAME : TBKEY},}
class DBOBJ:
    def __init__(self):
        self.dblist = {}
        self.tblist = {}
        self.dbobjs = {}
        self.tbobjs = {}


