class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print('{} is now sitting'.format(self.name))
    def roll_over(self):
        print('{} rolled over!'.format(self.name))

class new_Dog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def run(self):
        print('{} is running'.format(self.name))
mine = new_Dog('amier',6)
mine.run()