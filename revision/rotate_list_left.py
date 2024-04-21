mylist=[1,2,3,4,5]
rotation=3

def rotate_list_left(mylist, rotation):
    for i in range(0,rotation):
        mylist=mylist.append(mylist[0])
        del mylist[0]
    print(mylist)

rotate_list_left(mylist, rotation)