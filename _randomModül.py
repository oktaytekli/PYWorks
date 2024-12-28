import random

# result = dir(random)# içine bakmak için
# result = help(random) # metodların kullanımları


result = random.random() # böyle yaparsak 0.0 ile 1.0 arasında random sayılar üretilecek
result = random.random() * 100 # 100 ile çarpar
result = random.uniform(1 , 10) # 1 ile 10 arasında ondalıklı sayılar üretir.
result = int(random.uniform(1 , 10)) # ondalıklı kısmı atar
result = random.randint(1,100) # 1 ile 100 arasında integer sayı üretir.


greeting = 'Hello There'
names  = ['ali', 'yağmur', 'deniz', 'cenk', 'atilla', 'oktay']
result = names[random.randint(0,len(names)-1)] #database den isim aldığımızı varsayarak len(names) yazarak isim listesinin uzunluğuna göre sınır belirtmeden otomatik olarak isim sınırı belirlemiş oluruz.
result = random.choice(names) #choice metoduna biz listeyi veriyoruz ve liste içerisinden bize rastgele kişileri getiriyor.
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste) #orjinal liste içerisinde ki elemanları karıştırmamıza yarar
result = liste


liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2) #names dizesi içerisinden rastgele 2 tane getir demek.

print(result)