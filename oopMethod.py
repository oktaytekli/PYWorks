# #class

# class Person:
#     #class attributes
#     address = 'no information'

#     #constructor(yapıcı metod)
#     def __init__(self, name, year): #self in anlamı classtan türetmiş olduğumuz herhangi bir objeyi temsil ediyor olmasıdır.
        
#         #object attributes
#         self.name = name
#         self.birthyear = year
    
    
#     #instance method 
#     def intro(self):
#         print('Hello There. I am ' + self.name)
    
#     #instance method 
#     def calculateAge(self):
#         return 2019 - self.birthyear


# #object (instance)
# p1 = Person('ali', 1990) #Burada p1 objesi tanımlamış olduk.
# p2 = Person(name = 'veli', year= 1989)

# p1.intro()
# p2.intro()

# print(f'yaşım : {p1.calculateAge()}')
# print(f'yaşım:  {p2.calculateAge()}')



class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.r = yaricap
    
    #methods
    def cevreHesapla(self):
        return 2*self.pi*self.r
    
    def alanHesapla(self):
        return self.pi*(self.r**2)
    
c1 = Circle() #yaricap = 1
c2 = Circle(5)

print(f'c1: alan = {c1.alanHesapla()} ve çevresi = {c1.cevreHesapla()}')
print(f'c2: alan = {c2.alanHesapla()} ve çevresi = {c2.cevreHesapla()}')