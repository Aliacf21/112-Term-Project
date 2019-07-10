import pickle

#Citing Eddie - not my own
def write(megaList):
    o = open("myData.p", "wb")
    pickle.dump(megaList,o)
    o.close()

def read():
    o = open("myData.p", "rb")
    L = pickle.load(o)
    return L
    
    
#print(read())
    
    
