import database
import hashlib
class Table():
    def __init__(self):
        self.DBKEY = None
        self.TBName = None
        self.TBKEY = None
        self.TBData = {}
        
    def TBreate(self, TName, columns,DBKEY):
        
        self.Name = TName
        
        self.DBKEY = DBKEY
        if self.DBKEY is None:
            print("No Database Selected")
        else:
            TBKEY = hashlib.sha512(TName.encode()).hexdigest()
            self.TBKEY = TBKEY
            self.detail = {"KEY": TBKEY, "Name" : TName, "ColumnsDetail" :{"Count":len(columns),"Heading":columns}}
        
    
        
