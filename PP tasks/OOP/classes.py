class Person:
    def __init__(self, name='', age=''):
        self.name=name
        self.age=age
    
    def prnt_data(input):
        print('Hello my name is',input.name,'\n and im',input.age,'years old!')

p1=Person('Joe',30)
p2=Person('James',28)
p3=Person()

while True:
    choice=int(input("Enter person number\n0 for quit\n>"))
    try:
        if choice==0:
            break
        elif choice==1:
            if (p1.name=='') or (p1.age==''):
                break
            p1.prnt_data()
        elif choice==2:
            if (p2.name=='') or (p2.age==''):
                break
            p2.prnt_data()
        elif choice==3:
            if (p3.name=='') or (p3.age==''):
                break
            p3.prnt_data()
    except:
        print('please enter a number')