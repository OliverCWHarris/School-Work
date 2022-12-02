from animal import animal

class land(animal):
    def __init__(self, name, age, blood, size, sound, legs):
        super().__init__(name, age, blood, size, sound)

        self.legs=legs
    
    def get_legs(self):
        return self.legs
    
    def emote(self):
        print(self.sound)

class sea(animal):
    def __init__(self, name, age, blood, size, sound, fins):
        super().__init__(name, age, blood, size, sound)

        self.fins=fins
    
    def get_fins(self):
        return self.fins
    
    def emote(self):
        print(self.sound)

class air(land):
    def __init__(self, name, age, blood, size, sound, legs, wings):
        super().__init__(name, age, blood, size, sound, legs)

        self.wings=wings
    
    def get_wings(self):
        return self.wings
    
    def emote(self):
        print(self.sound)