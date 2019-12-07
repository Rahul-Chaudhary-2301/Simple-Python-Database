import rwobj

SESSION = False
def CreateSession(DBName,password):
    print(DBName,password)
    db_obj = rwobj.read()
    if DBName in db_obj.dblist.keys():
        DBKey = db_obj.dblist[DBName]
    print(DBKey,password)
    if db_obj.dbobjs[DBKey].DBAuthtication(DBKey,password) is True:
        SESSION = True

    if SESSION is True:
        db = db_obj.dbobjs[DBKey]

    return db




