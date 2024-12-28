 # error => hata

 
# print(a) #tanımlamadan yazdırırsak NameError
# int('1a2') #ValueError
# print(10/0) #sıfıra bölünemez hatası olan ZeroDivisionError
# print('denem'e) #SyntazError yani yazım hatası 

#Bunlar başlıca hatalar bundan farklı hataları python ın docs kısmında bulabiliriz.


# error handling => hata yönetimi

# YÖNTEM 1 #
# try: 
#     x = int(input('X:  '))
#     y = int(input('Y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için 0 girilemez.')
# except ValueError:
#     print('x ve y için sayısal değer girmelisiniz.') 


# YÖNTEM 2 #
# try: 
#     x = int(input('X:  '))
#     y = int(input('Y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz.')
#     print(e)


# YÖNTEM 3 #

while True:
    try: 
        x = int(input('X:  '))
        y = int(input('Y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz.', ex)       
    else:       
        break
    finally:
        print('try except sonlandı.')