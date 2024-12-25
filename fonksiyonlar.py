# #fonksiyon
# #Belirli amaçlara yönelik önceden oluşturulmuş bir yapıdır.

# # def sayHello(): #yazacağımız kodların sayHello'nun bir üyesi olacağı anlamına gelir.
# #     print('Hello')

# # sayHello() #3 kere print yazmak yerine bu tarz bir kullanım yapılır.
# # sayHello()
# # sayHello()

# def sayHello(name): #o anda fonksiyonu çağıran kişi name olarak ne yazarsa onu alacağız anlamına gelir.
#     print('Hello' + name)

# sayHello('Oktay') # argüman sunarak yazdırrız.
# sayHello('Olcay')



# #def sayHello(name = 'user'):#eğer name parametresi gönderilemdiyse vvarsayılan oalrak user yazdırır.

# def sayHello (name = 'user'):
#     return 'Hello' + name
# msg = sayHello('Oktay')
# print(msg)

# def total (num1,num2):
#     return num1+num2 #gönderdiğimiz 2 sayıyı toplayan bir fonksiyon

# result   = total(10,20)
# result   = total(15,20)

# print(result)

def yasHesapla(dogumYili):
     return 2019-dogumYili

# ageOktay = yasHesapla(1999)
# ageOlcay = yasHesapla(2000)

# print(ageOktay)

def emeklilikHesapla(dogumYili, isim):
    
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum Yılı
    OUTPU: Hesaplanan yıl
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
         print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
         print('Zaten emekli oldunuz.')

emeklilikHesapla(2002,'Damla')
emeklilikHesapla(2000,'Olcay')
emeklilikHesapla(1999,'Oktay')

print(help(emeklilikHesapla))

