class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def printname(self):
        print(self.first_name, self.last_name)



class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year
    
    def Welcome(self):
        print('Welcome', self.first_name, self.last_name, 'to the class of', self.graduation_year)