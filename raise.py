# x = 10
# if x > 5:
#     raise Exception("X, 5ten büyük değer alamaz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 7 karakter olmalı.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola alfa numerik karakter içermelidir.")
#     elif not re.search("\s", psw):
#         raise Exception("Parola boşluk içermelidir.")
#     else:
#         print("Geçerli parola girdiniz.")
    
# password = "123456"
# password = "12345678" #en az 7 karakter şartı
# password = "1234567a" #küçük harf karakter şartı
# password = "1234567aA" #büyük harf karakter şartı
# password = "1234567aA_" #alfa numerik şartı karakter şartı
# password = "12345678 " #boşluk şartı karakter şartı

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli Parola")
# finally:
#     print("Validation tamamlandı.")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiiiiiiiii" , 1989)