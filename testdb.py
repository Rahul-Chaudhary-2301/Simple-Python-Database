import database
import table
db = database.Database()
db.DBcreate("rahul")
DBKEY = db.DBKEY
table = table.Table(DBKEY)
table.create("student",["name","color"])
print("-------- Database --------- ")
print("DBNAME : ",db.DBName)
print("DBKEY: ",db.DBKEY)

print("Password : ",db.Password)
print("DBAUTH : ",db.DBAuth)
print("TableDetail : ",db.TableDetail)
print("---------- Table ------------ ")
print("TNAME : ",table.Name)
print("TKEY : ",table.TKEY)
print("TableDetail :",table.detail)

