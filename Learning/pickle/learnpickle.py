import pickle

listtodump=['cheese',13,12.2]

with open('picklefile.txt','wb')as f:
    pickle.dump(listtodump,f)

with open('picklefile.txt','rb') as f:
    print(f.read())
    data=pickle.load(f)
    print(data)