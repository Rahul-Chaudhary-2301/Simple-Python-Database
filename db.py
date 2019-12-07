import database
import table
import dbobj 
import session
import rwobj

#Language
db_obj = dbobj.DBOBJ()            
class Interpreter:
    def use(self,DBName,Password = "root"):
        #
        db = session.CreateSession(DBName,Password)

    def create(self,mode,name,secure='standard',value=None):
        print(value)
        if mode == "database":
            db.DBcreate(name,security = secure)
            db_obj.dblist[name] = db.DBKEY
            db_obj.tblist[db.DBKEY] = {}
        elif mode == "table":

            if session.SESSION is True:
                tb.TBCreate(name,value,db.DBKEY)
                print("--------------------------------")
                db.Table.append(tb.Keys)
                db_obj.tblist[db.DBKEY][tb.TBName] = tb.TBKEY
            else:
                print("No Database Selected")

    def commit(self):
        db_obj.dbobjs[db.DBKEY] = db
        db_obj.tbobjs[tb.TBKEY] = tb
        rwobj.write(db_obj)
           
    def __init__(self,command):
        cmdlist = command.split(' ')
        print(cmdlist)
        print(len(cmdlist))
        if cmdlist[0] == "create":
            if cmdlist[1] == "database":
                if len(cmdlist) > 3:
                    if cmdlist[3] == "secure":
                        getPass = input("Enter Password : ")
                        self.create("database",cmdlist[2],secure=True,value = [getPass])
                else:
                    self.create("database",cmdlist[2])
            elif cmdlist[1] == "table":
                self.create("table",cmdlist[2],cmdlist[3:])
        elif cmdlist[0] == "use":
            self.use(cmdlist[1])
        elif cmdlist[0] == "commit":
            self.commit()
        elif cmdlist[0] == "exit":
            exit()

        
        
        
db = database.Database()
tb = table.Table()
        
print("Welcome to database ")

command = None    
while True:
    command = input("DB> ")
    Interpreter(command)
    
