'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('sayi: '))
result = (sayi > 0) and (sayi <= 100)
print(f'sayi 0-100 arasında mı: {result}')

'''

# sayi = float(input('Bir sayı giriniz: '))
# if (sayi > 0) and (sayi <= 100):
#     print('Sayı 0 ile 100 arasındadır.')
# else:
#     print('Sayı 0 ile 100 arasında değildir.')



'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('sayi: '))
result = (sayi > 0) and (sayi % 2 == 0)
print(f'girilen sayı pozitif çift sayı mı: {result}')

'''
# sayi = int(input('Bir sayı giriniz: '))
# if (sayi >= 0) and (sayi % 2 == 0):
#     print('Girdiğiniz sayı pozitif çift sayıdır..')
# elif (sayi < 0) and (sayi % 2 == 0):
#     print('Girdiğiniz sayı negatif çift sayıdır.')
# elif (sayi < 0) and (sayi % 2 !=0):
#     print('Girdiğiniz sayı negatif tek sayıdır.')
# else:
#     print('Girdiğiniz sayı pozitif tek sayıdır.')



'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@oktaytekli.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

result = (girilenEmail == email) and (girilenPassword == password)
print(f'uygulamaya giriş başarılı mı: {result}')

'''

# email = 'email@oktaytekli.com'
# password = 'abc123'

# girilenEmail= input('Bir email giriniz: ')
# girilenPassword= input('Bir şifre giriniz: ')

# if (girilenEmail == email) and (girilenPassword == password):
#     print('Giriş başarılı. Hoş geldiniz.')
# elif (girilenEmail != email) and (girilenPassword == password):
#     print('Email yanlış, tekrar deneyiniz.')
# elif (girilenEmail == email) and (girilenPassword != password):
#     print('Şifre yanlış, tekrar deneyiniz.')
# else:
#     print('Email ve şifre yanlış, tekrar deneyiniz.')

'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (a > c)
print(f'a en büyük sayıdır : {result}')

result = (b > a) and (b > c)
print(f'b en büyük sayıdır : {result}')

result = (c > a) and (c > b)
print(f'c en büyük sayıdır : {result}')

'''

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a > b) and (a > c):
#     print('A sayısı en büyük sayıdır.')
# elif (b > a) and ( b > c):
#     print('B sayısı en büyük sayıdır.')
# else:
#     print('C sayısı en büyük sayıdır.')        


'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız.
   - a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
   - b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)

result = (ortalama>=50) and (final>=50)
result = (ortalama >=50) or (final>=70)

print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')

'''
# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final : '))

# ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)

# if (ortalama >= 50) and (final >=50):
#     print(f'Öğrencinin ortalaması {ortalama} ve geçme durumu: GEÇTİ. ')
# elif (final >= 70):
#     print(f'Öğrencinin ortalaması {ortalama} fakat final notu {final}, 70 ten yukarıda olduğu için geçme durumu: GEÇTİ.')
# elif (ortalama >=50) and (final <50):
#     print(f'Öğrencinin ortalaması {ortalama} fakat final notu {final}, 50 den aşağıda olduğu için geçme durumu: KALDI. ')
# else:
#     print(f'Öğrencinin ortalaması {ortalama} ve geçme durumu: KALDI. ')



'''
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
Formül: (Kilo / boy uzunluğunun karesi)
Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
0-18.4        => Zayıf
18.5-24.9     => Normal
25.0-29.9     => Fazla Kilolu
30.0-34.9     => Şişman (Obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)
index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayif: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')

'''

# name = input('adınız: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))

# index = (kg) / (hg ** 2)
# index = (kg) / (hg ** 2)

# if (index >= 0) and (index <= 18.4):
#     print(f'Sayın {name}, girdiğiniz boy ve kilonuza göre vücut kitle indeksiniz {index} ve durumunuz: ZAYIF')
# elif (index > 18.4) and (index <= 24.9):
#     print(f'Sayın {name}, girdiğiniz boy ve kilonuza göre vücut kitle indeksiniz {index} ve durumunuz: NORMAL KİLO')
# elif (index > 24.9) and (index <= 29.9):
#     print(f'Sayın {name}, girdiğiniz boy ve kilonuza göre vücut kitle endeksiniz {index} ve durumunuz: FAZLA KİLOLU')
# else:
#     print(f'Sayın {name}, girdiğiniz boy ve kilonuza göre vücut kitle endeksiniz {index} ve durumunuz: OBEZ')
