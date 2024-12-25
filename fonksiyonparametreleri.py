# def changeName(n):
#     n ='Olci'
# name = 'oktay'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul' #0.elemanı istanbul yaptırır.
# sehirler = ['ankara', 'izmir']
# change(sehirler)
# print(sehirler)


# def change(n):
#     n[0] = 'istanbul' #0.elemanı istanbul yaptırır.
# sehirler = ['ankara', 'izmir']
# n = sehirler #veriler üzerinde güncelleme yapmış oluruz istersek yukarıdaki gibi istersek buradaki gibi

# n[0] = 'istanbul'
# print(sehirler)

# def change(n):
#     n[0] = 'istanbul'
# sehirler = ['ankara', 'izmir']
# change(sehirler[:])
# print(sehirler)

# def add(a, b, c = 0): #buradaki c = 0 demek eğer c belirtilmemişse 0 olarak al demektir.
#     return sum((a, b, c)) #liste veya tuple içindeki tüm elemanların toplamını hesaplayan yerleşik fonksiyondur.
# print(add(10,20))
# print(add(10,20,30))

# #eğer 6 ve daha fazla parametre göndermek istersem

# def add(*params):#params = parametleri temsil eden
#     print(params)#liste şeklinde 10,20 gibi yazdırır.
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30, 50, 60))

# def add(*params): #bir tuple kullanacaksak tek yıldız.
#     sum = 0
    
#     for n in params:
#         sum = sum + n
#     return sum

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50))

def displayUser(**args): #2 tane yıldız dictionary geleceğini belirtmemiz.
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

displayUser(name = 'Oktay', age = 2, city = 'istanbul')
displayUser(name = 'Olcay', age = 22, city = 'istanbul', phone = '123123')
displayUser(name = 'Damla', age = 12, city = 'istanbul', phone = '123123', email= 'mailcom')


def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50, key = ' value 1', key2 = 'value 2')

