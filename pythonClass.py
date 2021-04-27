#class cannot be empty add pass to avoid error
class Baraka:
    def __init__(self,name, age):
        self.name=name
        self.age=age

#create an object of the clas person
personOne=Baraka("Uphoro Kimambo",46)
print(personOne.name, personOne.age)