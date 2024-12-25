# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdir(kelime, adet):
#     print(kelime * adet)
# yazdir('Selam Dünya', 10)
    
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

# def add(*args):
#     liste = []
    
#     for arg in args:
#         liste.append(arg)
#     return liste
# result = add(10,20,30,'Hello')
# print(result)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.



# def asalSay(sayi1,sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#                 else:
#                     print(sayi)

# sayi1 = int(input('sayı 1: '))
# sayi2 = int(input('sayı 2: '))

# asalSay(sayi1, sayi2)



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür.


def tambolenlerBul(sayi):
    tambolenler =[]
    for i in range(2, sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler

print(tambolenlerBul(20))