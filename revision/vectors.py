import numpy as np

working=True


def sumvectors(v1,v2):
    return v1+v2

def scalevectors(v1,v2,s):
    return v1*s,v2*s


while working==True:
    vector1=list(input("enter 2 numbers for vector 1 eg 12\n>"))
    vector2=list(input("enter 2 numbers for vector 2 eg 23\n>"))
    scaler=int(input("enter variable for scaling eg 2\n>"))
    vector1=np.array(vector1)
    vector2=np.array(vector2)

    menu=True
    while menu==True:
        print("1 | sum vectors\n2 | scale vectors")
        menu_choice=int(input("\n>"))

        if menu_choice==1:
            print("sum of vectors ",vector1,vector2, "is", sumvectors(vector1,vector2))
        elif menu_choice==2:
            print("vectors",vector1,vector2,"scaled to",scaler,"is",scalevectors(vector1,vector2,scaler))