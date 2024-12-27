#Inheritance (Kalıtım): Miras alma

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person) bu durumda person için tanımladığımız özellikelr student ve teacher içinde geçerli olacaktır.


#Animal => Dog(Animal), Cat(Animal) burada yaptığımız şey de dog ve cat in animaldan miras alması

class Person():
    def __init__(self, fname, lname,):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')
    
    def who_am_i(self):
        print('I am a person')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number 
        print('Student Created')
    
    def who_am_i(self):
        print('I am a student') #aynı bir sınıfta ki metod temel sınıfta ki metodu ezer. override

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname) #super ı yazınca self i çağırmaya gerek kalmıyor. 
        self.branch = branch
        def who_am_i(self):
            print(f'I am a {self.branch} teacher')   


p1 = Person('Ali', 'Yılmaz')
p2 = Student('Oktay', 'Olcay', '12')
t2 = Teacher('Oktay', 'Tekli', 'Ogrenci')

print(p1.firstName + '' + p1.lastName)
print(p2.firstName + '' + p2.lastName + '' + p2.studentNumber)

p1.who_am_i()
p2.who_am_i()