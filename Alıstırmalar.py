'''
(f''fonk)
Kullanıcıdan alınan isim ve soyismi birleştirip, baş harflerini büyük harf yaparak ekrana yazdırın.
'''
# ad = input('Adınızı girin:')
# soyad = input('Soyadınız girin:')

# result = (f"{ad.capitalize()} {soyad.capitalize()}")
# print(result)

'''
Bir sayının çift olup olmadığını kontrol eden kod dizini yazınız.
'''
# sayi = int(input('Bir sayı giriniz: '))
# if (sayi >=0) and (sayi %2  == 0):
#     print('Girdiğiniz Sayı çifttir.')
# else:
#     print('Girdiğiniz sayı tektir.')

'''
Girilen bir cümledeki kelime sayısını hesaplayın.
'''
# cumle = (input('Bir cümle giriniz: '))
# kelimeSay = len(cumle.split()) #Burada ki split metodu kelimeleri ayırıp hesaplanmasına yardımcı olur.
# print(f'Girdiğiniz cümlenin kelime sayısı: {kelimeSay}')

'''
(fordöngüsü)
sayilar = [12, 7, 9, 14, 18, 21, 4, 10]
Bir listedeki çift sayıları filtreleyip yeni bir liste oluşturun.
'''

# sayilar = [12, 7, 9, 14, 18, 21, 4, 10]
# ciftSay = []
# tekSay = []
# for sayi in sayilar:
#     if sayi %2 == 0:
#         ciftSay.append(sayi)
#     else:
#         tekSay.append(sayi)
# print(f'Çift Sayılar: {ciftSay}, Tek sayılar: {tekSay}')

'''
(fordöngüsü)
Bir sayının faktöriyelini hesaplayın.
'''

# sayi = int(input('Bir sayı giriniz: '))
# faktoriyel = 1

# for i in range(1, sayi +1):
#     faktoriyel *= i

# print(f'Girdiğiniz {sayi} sayısının faktoriyeli {faktoriyel}')



'''
Kullanıcıdan alınan üç sayının toplamını ve ortalamasını hesaplayın.
'''

# a = float(input('Bir sayı giriniz: '))
# b = float(input('Bir sayı giriniz: '))
# c = float(input('Bir sayı giriniz: '))

# toplam = a + b + c
# ortalama = toplam / 3

# print(f'Girdiğiniz sayıların toplamı : {toplam} ve ortalaması {ortalama}')

'''
Manavdaki elma,armut,muz ve çilek fiyatlarını sözlük özelliğini kullanarak rastgele fiyatlar vererek değerlerin toplamını hesaplayın.
'''
# menu = {
#     'elma' : 5,
#     'armut' : 7,
#     'muz' : 9,
#     'çilek': 11,
# }

# toplamFiy = sum(menu.values()) #Buradaki sum bir dizinin tüm elemanlarının toplamını hesaplar.
# print(toplamFiy)

'''
sayilar = [45, 23, 67, 12, 89, 34, 56]
Bu listedeki en büyük ve en küçük eleman arasındaki farkı hesaplayın.
'''
# sayilar = [45, 23, 67, 12, 89, 34, 56]
# fark = max(sayilar) - min(sayilar)
# print(fark)

'''
(ifelse konusu)
Girilen sayının pozitif, negatif veya sıfır olduğunu kontrol eden program.
'''

# sayi= int(input('Bir sayı giriniz: '))

# if (sayi > 0):
#     print('Girdiğiniz sayı pozitifir.')
# elif (sayi == 0):
#     print('Girdiğiniz sayı sıfıra eşittir.')
# else:
#     print('Girdiğiniz sayı negatiftir.')

'''
(ifelse konusu)
Bir öğrencinin not ortalamasına göre geçme veya kalma durumunu belirleyen program
Ortalama 90 ve üzeri ise: "Pekiyi"
Ortalama 70-89 arası ise: "İyi"
Ortalama 50-69 arası ise: "Orta"
Ortalama 50'nin altı ise: "Kaldı"
'''

# ad = input('Lütfen isminizi girin: ')
# not1 = int(input('Lütfen ilk sınav notunuzu girin: '))
# not2 = int(input('Lütfen ikinci sınav notunuzu girin: '))

# ort = (not1 + not2) / 2

# if (ort >=90):
#     print(f'Öğrencimiz {ad}, ortalamanız {ort} ve geçme durumunuz: Pekiyi')
# elif (ort > 69) and (ort < 90):
#     print(f'Öğrencimiz {ad}, Ortalamanız {ort} ve geçme durumunuz: İyi')
# elif (ort > 49) and (ort < 70):
#     print(f'Öğrencimiz {ad}, Ortalamanız {ort} ve geçme durumunuz: Orta')
# else:
#     print(f'Öğrencimiz {ad}, Ortalamanız {ort} ve geçme durumunuz: Kaldı')

'''
(ifelse konusu)
Girilen saatteki çalışma durumuna göre mesaj veren program
Saat 9-17 arası: "Mesai saatleri içindesiniz."
Saat 17-22 arası: "Çalışma saatleri dışında, dinlenme zamanı."
Saat 22-9 arası: "Gece vakti, uyuma zamanı."

'''

# saat = int(input('Lütfen işe başlama saatinizi yazın: '))

# if (saat > 8 ) and (saat < 18):
#     print(f'Giriş saatiniz {saat} ve  çalışma durumunuz: Mesai saatleri içindesiniz.')
# elif (saat > 16) and (saat < 23):
#     print(f'Giriş saatiniz {saat} ve  çalışma durumunuz: Çalışma saatleri dışında, dinlenme zamanı')
# else:
#     print(f'Giriş saatiniz {saat} ve  çalışma durumunuz: Gece vakti, uyuma zamanı.')

