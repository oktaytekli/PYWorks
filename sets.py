fruits = {'orange', 'apple', 'banana'}

#print(fruits[0]) indekslenemez.

for x in fruits:
    print(x)

fruits.add('cherry') # yeni bir eleman eklenir.
fruits.update(['mango', 'grape', 'apple']) #yeni bir liste yollayabiliriz.
fruits.remove('mango') #silmeye yarar.
fruits.discard('apple') # çıkartmaya yarar.
fruits.pop() # eğer içine bir şey yazmazsak herhangi bir eleman silinebilir.

fruits.clear()#tüm elemanlar silinir.

print(fruits)

myList = [1,2,5,4,4,2,1]

print(set(myList)) # set e çevirdiğimizde tekrarlayan elemanlar liste içerisinden gider.
