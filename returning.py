# def usAlma(number):
#     # two = usalma(2)
#     # three = usalma(3)

#     def inner(power):
#         return number ** power
    
#     return inner 

# two = usAlma(2)
# three = usAlma(3)

# print(two(3))
# print(three(4))


# def yetkiSorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolünün {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamz.".format(role,page)
#     return inner   

# user1 = yetkiSorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))

def islem(islemAdi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if islemAdi == "toplama":
        return toplam
    else:
        return carpma
    
toplama = islem("toplama")
print(toplama(1,3,5,6,7))

carpma = islem("carpma")
print(carpma(1,2,4,5))    
