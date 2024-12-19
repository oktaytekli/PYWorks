numbers = [1,2,3,4,5]

for num in numbers:
    print(num) #listenin içerisinden tek tek elemanları al num değişkeni içerisine at ve her seferinde her for döngüsü döndüğünde içine at demek

for num in numbers:
    print('Hello') #burada da listede ki sayı kadar hello döndür işlemini yapıyoruz.

names = ['oktay', 'olcay', 'damla']

for name in names:
    print(f'my name is {name}') # tek tek her ismi yazdırır.

name= 'Oktay Tekli'
for n in name:
    print(n) #her bir eleman bir dizi elemanı şeklinde değerlendirdiği için tek tek yazdırır.

tuple = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b) #her bir liste elemanı bir tuple listesi elemanına karşılık geliyor yani 1,2 vb gibi yazdırır.

d = {'k1':1, 'k2':2, 'k3':3}  
for item in d:
    print(item) #bu tarz yazımda sadece key bilgileri gelir.
for key,value in d.items():
    print(key, value) #bu tarz yazımda hem key hem value sunu yazdırabiliriz.   