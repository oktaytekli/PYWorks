# 1- Girilen 2 sayıdan hangisi büyüktür?

# a = int(input('1.sayıyı giriniz: '))
# b = int(input('2.sayıyı giriniz: '))

# result = (a > b)
# print(f'birinci sayı {a} ikinci sayıdan {b} büyüktür. {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti, değil ise kaldı yazdırın.

# vize1 = float(input('1.vize: '))
# vize2 = float(input('2.vize: '))
# final = float(input('Final notunuz: '))

# ortalama = (((vize1+vize2))/2 *0.6) + (final * 0.4)
# result = (ortalama >= 50)
# print(f' Ortalamanız {ortalama} geçtiniz. Tebrikler {result}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input('sayı: '))

# tekcift = (sayi % 2 == 0)
# print(f'Girilen sayının çift olma durumu {tekcift}')

# 4- Girilen bir sayının negatif mi pozitif mi olduğunu yazdırın.

# sayi = int(input('sayı:'))
# pozitifmi= sayi > 0
# print(f'Girilen sayının pozitif olma durumu {pozitifmi}')


# 5- Parolo ve email bilgisini isteyip doğruluğunu kontrol edin.
# (email: email@oktaytekli.com parolo:abc123)

# email = 'email@oktaytekli.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenSifre = input('Parolo: ')

# isEmail = (email == girilenEmail.lower().strip())
# isSifre = (password == girilenSifre.lower())

# print(f'Email bilgisi doğru mu: {isEmail} Girilen şifre doğru mu: {isSifre}')
