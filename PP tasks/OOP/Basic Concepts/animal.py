class Animal:
    def __init__(self,s,n):
        self.__state = s
        self.__size = n
        
    def getState(self):
        return self.__state
        
    def getSize(self):
        return self.__size
        
    def feed(self):
        self.__size += 1
        print('Fish fed')
        if self.__size == 5:
            self.__state ='FISH'

thisFish=Animal('FISH', 1)
print(thisFish.getState(), 'is of size', thisFish.getSize())
while thisFish.getState() != 'FISH':
    thisFish.feed()
print('it is now a big', thisFish.getState())



'''
class thisFish(Animal):
    def __init__(self, s, n):
        super().__init__(s, n)

        print(thisFish.getState(), 'is of size', thisFish.getSize())

        while thisFish.getState() != 'FISH':
            thisFish.feed()
        
        print('It is now a big', thisFish.getState())
'''
