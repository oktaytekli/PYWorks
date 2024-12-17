# 1. Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# a = float(input('bir sayı giriniz: '))
# result = (a>=0) and (a<=100)
# print(f'Girdiğiniz sayının 0 ile 100 arasında olma durumu: {result} ')


# 2. Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# a = float(input('bir sayı giriniz: '))
# result = (a>=0) and (a % 2 == 0)
# print(f'Girdiğiniz sayının pozitif çift sayı olma durumu: {result}')

# 3. Email ve parola bilgileri ile giriş kontrolü yapınız.

# email, password = 'email@oktaytekli.com' , '1234'
# a =(input('epostasınız girin: '))
# b =(input('şifrenizi girin: '))

# result = (a == email) and (b == password)
# print(f'Girdiğiniz bilgilerin doğru olma durumu: {result}')


# 4. Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = float(input('bir sayı giriniz: '))
# b = float(input('bir sayı giriniz: '))
# c=  float(input('bir sayı giriniz: '))

# result = (a > b) and (a > c)
# print(f'a en büyük sayı olmasının doğruluk durumu: {result}')

# result = (b > a) and (b > c)
# print(f'b en büyük sayı olmasının doğruluk durumu: {result}')

# result = (c > a) and (c > b)
# print(f'c en büyük sayı olmasının doğruluk durumu: {result}')



# 5. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırınız.
#    - a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    - b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('1.Vize notunuzu giriniz: '))
# vize2 = float(input('2.Vize notunuzu giriniz: '))
# final = float(input('Final  notunuzu giriniz: '))

# ortalama =(((vize1+vize2))/2 *0.6) + (final * 0.4)
# result = (ortalama >= 50) and (final>=50)
# result = (ortalama > 50) or (final >=70)
# print(f'Geçme durumunuz: {result}')




# 6. Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    - Formül: (Kilo / boy uzunluğunun karesi)
#    - Aşağıdaki tabloya göre kişi hangi gruba girmektedir:
#      - 0-18.4 = Zayıf
#      - 18.5-24.9 = Normal
#      - 25.0-29.9 = Fazla Kilolu
#      - 30.0-34.9 = Şişman (Obez)

ad       =    input('Lütfen adınızı girin: ')
kilo     =    float(input('Lütfen kilonuzu girin: '))
boy      =    float(input('Lütfen boyunuzu girin: '))

index = (kilo) / (boy**2)
zayif = (index >=0) and (index<=18.4)
normal = (index >18.4) and (index<=24.9)
fazlakilo = (index >24.9) and (index<=29.9)
obez= (index >29.9) and (index<=34.9)

print(f'{ad} kilo endeksin {index} ve kilo değelendirme {zayif}')
print(f'{ad} kilo endeksin {index} ve kilo değelendirme {normal}')
print(f'{ad} kilo endeksin {index} ve kilo değelendirme {fazlakilo}')
print(f'{ad} kilo endeksin {index} ve kilo değelendirme {obez}')





