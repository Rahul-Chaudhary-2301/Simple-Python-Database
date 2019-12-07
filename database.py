import time
import hashlib

#import status
#Database Core Class
class Database():
    def __init__(self):
        #Database Name
        self.DBName = None
        #Database Security defination
        self.security = None
        #Database U key
        self.ADBKEY = None
        #Database Key 
        self.DBKEY = None
        #Password
        self.Password = None
        #auth
        self.DBAuth = None
        #Table detail
        self.Table = []


    def DBAuthtication(self,DBKEY,password):
        #password sha512 conversion
        encPass = hashlib.sha512(password.encode()).hexdigest()
        string = encPass + self.DBKEY
        
        encPDBKEY = hashlib.sha512(string.encode()).hexdigest()
        if self.DBKEY == DBKEY and self.ADBKEY == encPDBKEY:
            return True
        else:
            return False

    #Database Security and Key Genration
    def DBSecurity(self,SecurityMode,value=None):
        def setSecurity(password):
           
            #password sha512 conversion
            self.Password = hashlib.sha512(password.encode()).hexdigest()
            
            #UDBKey sha512 conversion - dbname + security + time
            self.DBKEY = hashlib.sha512(self.DBName.encode() + self.security.encode() + str(time.time()).encode()).hexdigest()
            
            #DBKEY  sha512 conversion - password + DBKEY
            string = self.Password + self.DBKEY 
            self.ADBKEY = hashlib.sha512(string.encode()).hexdigest()
        
        if SecurityMode == "standard":
            setSecurity("root")
            self.DBAuthtication(self.DBKEY,"root")
            
        if SecurityMode == "secure":
            setSecurity(value[0],value[1])
            self.DBAuthtication(value[0],value[1])
            
    

    #Database Creation
    def DBcreate(self, DBName, security = "standard",value=None):
        self.DBName = DBName
        self.security = security
        self.DBSecurity(security,value)
        
        

    #Database ALter Changes
    # def alter(command,value):
    #     if command == "DBRename":
    #         self.DBName = value
    #     if command == "ChgSecurity":
    #         self.security = value
    #         self.DBSecurity(value)

    #Database Delete
    # def delete():
    #     pass


        

