import pickle

def write(objs):
    file = open("DBOBJ","wb")
    pickle.dump(objs,file)

def read():
    try:
        file = open("DBOBJ","rb")
    except FileNotFoundError:
        print("NO Database Found")

    return pickle.load(file)