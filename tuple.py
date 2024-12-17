list = [1, 2, 3]

tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

list = ['oktay','olcay']
tuple = ('damla','ayşe', 'damla')
names  = ('demet', 'emel', 'ayşe') + tuple # bu tarz kullanımda names in üzerinde tuple da tanıttığımzı elemanalrı eklemeyi sağlarız.


list[0] = 'ahmet'
tuple[0] = 'deniz' #tuple da eleman atandık sonra yeni bir eleman ataması yapamıyoruz.



print(tuple.count('damla'))
print(tuple.index('damla'))


print(list)
print(tuple)

