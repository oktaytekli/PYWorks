# 1. Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# ad  = input('İsminizi giriniz: ')
# yas = int(input('Yaşınızı giriniz: '))
# egtm= input('Eğitim durumunuz: ')

# if yas >=18:
#     if egtm >= ('lise') or ('üniversite'):
#         print(f'Sayın {ad}. Ehliyet almaya uygunsunuz.')
# else:
#     print(f'Sayın {ad}. Ehliyet almaya uygun değilsiniz.')



# 2. Bir öğrencinin 2 yazılı ve 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#    - 0 - 24  => 0
#    - 25-44  => 1
#    - 45-54  => 2
#    - 55-69  => 3
#    - 70-84  => 4
#    - 85-100 => 5

# adsoyad = input('Lütfen adınız ve soyadınız giriniz: ')
# yazili1= int(input('Lütfen birinci yazılı notunuzu giriniz: '))
# yazili2= int(input('Lütfen ikinci yazılı notunuzu giriniz: '))
# sozlu = int(input('Lütfen sözlü notunuzu giriniz: '))

# ortalama = (yazili1+yazili2+sozlu)/3 

# if (ortalama >=0) and (ortalama<25):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 0 dır.')
# elif (ortalama >=25) and (ortalama<45):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 1 dir.') 
# elif (ortalama >=45) and (ortalama<54):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 2 dir.')       
# elif (ortalama >=55) and (ortalama<70):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 3 tür.')
# elif (ortalama >=70) and (ortalama<84):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 4 tür.')
# elif (ortalama >=85) and (ortalama<100):
#     print(f'{adsoyad}, not ortalamanız {ortalama} ve not aralığınız 5 tir.')
# else:
#     print(f'{adsoyad}, yanlış bir bilgi girdiniz.')                        


# 3. Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    - 1. Bakım => 1. yıl
#    - 2. Bakım => 2. yıl
#    - 3. Bakım => 3. yıl

# **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# *** datetime modülünü kullanmanız gerekiyor.


# adsoyad = input('Lütfen adınızı ve soyadınız girin: ')
# days = int(input('Aracınız kaç gündür trafiktedir: '))

# if days <= 365:
#     print(f'Sayın {adsoyad} 1.servis aralığı.')
# elif days > 365 and days <=365*2:
#     print(f'Sayın {adsoyad} 2.servis aralığı.')
# elif days > 365*2 and days <=365*3:
#     print(f'Sayın {adsoyad} 3.servis aralığı.')
# else:
#     print('Eksik veya hatalı bilgi girdiniz. Lütfen kontrol ediniz.')

#DATETIME

import datetime

adsoyad = input('Lütfen adınızı ve soyadınız girin: ')
tarih = input('Aracınız hangi tarihte trafiğe çıktı(2019/8/9): ')
tarih = tarih.split('/')
# print (tarih[0])#Gün ay yıl olarak ayırır
# print (tarih[1])
# print (tarih[2])
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now() #şuan ki tarihi alır.
fark = simdi - trafigeCikis
days = fark.days
#print(fark)#kullanıcıdan aldığımız tarih bilgisinden şimdi ki tarihi çıkararak kaç gün olduğunuda hesaplayabiliriz.


if days <= 365:
    print(f'Sayın {adsoyad} aracınız 1.servis aralığı.')
elif days > 365 and days <=365*2:
    print(f'Sayın {adsoyad} aracınız 2.servis aralığı.')
elif days > 365*2 and days <=365*3:
    print(f'Sayın {adsoyad} aracınız 3.servis aralığı.')
else:
    print('Eksik veya hatalı bilgi girdiniz. Lütfen kontrol ediniz.')
