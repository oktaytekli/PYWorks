# #IDENTITY OPERATOR: IS eşitlik operatörleri

# x = y = [1,2,3]
# z = [1,2,3]

# print(x==y)
# print(x==z)
# print(x is y) # true bilgisini alırız.
# print(x is z) # farklı referansları olmasına rağmen false getirir. objeler aynı olmalı.

# x = [1,2,3]
# y = [2,4]

# del x[2] # 2.elemanı sil demek
# y[1] = 1 
# y.reverse()

# print(x == y) #yukarıdaki işlemlerden sorna aynı olacağını için true bilgisi karşımıza gelir.
# print (x is y)
# print(x is not y) 

# MEMBERSHIP OPERATOR: IN

x = ['apple', 'banana']
print('banana' in x) 

name = 'Oktay'
print('a' in name) # içerisinde var mı sorusu
print('a' not in name) # içerisinde yok mu sorusu
