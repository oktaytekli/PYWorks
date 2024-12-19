# #1-100e kadar çift olarak yazdırma

# x= 1
# while x <= 100:
#     if x % 2 == 0:
#         print(x)
#     x += 1
# print('bitti..')

# #1-100e kadar tek olarak yazdırma

# x= 1
# while x <= 100:
#     if x % 2 == 1:
#         print(x)
#     x += 1
# print('bitti..')

# #1-100e kadar yazdırma
# x= 1
# while x <= 100:
#     if x % 2 == 1:
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1
# print('bitti..')

name = '' #false
while not name.strip(): #strip boşluk karakteri girmemize rağmen bunun önüne geçmesini sağlar.
    name = input('isminizi giriniz: ') #isim girmedikçe false değer döndürmesi ve bu nedenle yazdırmaması demektir.
print(f'Merhaba {name}')