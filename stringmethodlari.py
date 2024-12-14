message = 'Hello There. My name is Oktay Tekli'

# message  = message.upper() #bütün karakterler büyük harfe çevrilir.
# message  = message.lower() #bütün karakterler küçük harfe çevrilir.
# message  = message.title() #her kelimenin baş harfi büyük harfe çevrilir.
# message  = message.capitalize() #verilen string ifadenin sadece ilk harfi büyük harfe çevrilir.
# message  = message.strip()#başta ki boşluk karakteri gider.
# message  = message.split()#her bir boşluk kelime boşluk karakterlerinden ayrılır ve her boşluk bir dizi elemanı olarak bize sunulur.
# message  = message.split('.') # boşluklardan değil noktalardan ayır demek.
# message  = ''.join(message) # ayrı ayrı olan kelimeleri birleştirir.
# message  = '*'.join(message) #birleştirdiği kelimelerin arasına yıldız yerleştirir.
# index    = message.find('Oktay')#Cümle içerisinde sorduğumuz kelimeyi arar ve bulduğu takdirde cümle içerisinde ki karakter numarasını belirtir.
# isFound  = message.startswith('O')#Mesaj içerisinde O ile mi başlıyor diye sorarız evet ise true hayır ise false olarak döner.
# isFound  = message.endswith('i')#Mesaj i ile mi bitiyor diye sorarız evet ise true hayır ise false olarak döner.
# message  = message.replace('Oktay','Tekli')# ilk bilgiyi arar ve bulduğunda yerine ikinci parametrede yazılan şeyi yazar.
# message  = message.center(100)# vermiş olduğumuz string bilgisini 100 karakterlik sağ ve soluna boşluklar oluşturur.
# message  = message.center(100, '*')# boşluklara yıldız ekler.


print(message)