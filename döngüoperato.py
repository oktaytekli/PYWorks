#RANGE METODU

# for item in range(10): # 0dan başlar ve 9a kadar sayıları yazmasını sağlar.
#     print(item)

# for item in range(5, 10): # 5den başlar ve 9a kadar sayıları yazmasını sağlar.
#     print(item)

# for item in range(5,100,20): # 5den başlar ve 100e kadar sayıları yazmasını sağlar sondaki 20 sayısı artış miktarıdır.
#     print(item)


# print(list(range(5,100,20)))  



#ENUMERATE METODU

# index = 0
# greeting = 'Hello There'

# for letter in greeting:
#     print(f'index: {index} letter: {letter}')
#     index +=1 #index numarasıda gelir.

# greeting = 'Hello There'

# for item in enumerate(greeting):
#     print(item)

#ZIP METODU

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']

#print(list(zip(list1,list2))) #index numaralarına göre eşleştirmemizi/birleştirmemizi sağlar.

for item in zip(list1, list2):
    print(item)

for a, b in zip(list1, list2):
    print(a, b)
    