x = 5

hak = 5
devam = 'e' 

result = 5 < x < 10
#and

result = (x > 5) and (x < 10) #true değeri için her iki tarafında true olması gerekiyor
result = (hak > 0) and (devam == 'e') #hak sıfırdan büyük ise ve eğer oyuncu devam için e yazmışsa 

#or
result = (x>0) or (x % 2 == 0) # x 0dan büyük ise ya da çift sayı ise true verir. Bir tarafın true olması yeterlidir.

#not

result = not (x > 0) #tam tersini alabilirsiniz.


# x, 5-10 arasında olan bir çift sayı mı ?
((x>5) and (x<10) and (x%2==0)) # x 5 ten büyük ya da 10dan küçük ya da sonuç mod alımında sıfır ise çift sayıdır.

print(result)