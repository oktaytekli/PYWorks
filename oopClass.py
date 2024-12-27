#class

class Person:
    #class attributes
    address = 'no information'
    #constructor(yapıcı metod)
    def __init__(self, name, year): #self in anlamı classtan türetmiş olduğumuz herhangi bir objeyi temsil ediyor olmasıdır.
        #object attributes
        self.name = name
        self.birthyear = year
        print('init metodu çalıştı.')
    
    #method


#object (instance)
p1 = Person('ali', 1990) #Burada p1 objesi tanımlamış olduk.
p2 = Person(name = 'veli', year= 1989)

#updating
p1.name = 'ahmet'
p1.address = 'kocaeli'

# accessing object attributer
print(f'name: {p1.name} year: {p1.birthyear} address: {p1.address}') #obje 1
print(f'name: {p2.name} year: {p2.birthyear}') #obje 2


print(p1)
print(p2)

print (type(p1))
print(type(p2))