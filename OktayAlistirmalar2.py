#### IF, ELSE, ELIF ALIŞTIRMALARI ####

'''
1. Kullanıcıdan Yaş Bilgisi Alarak İzin Verme
Kullanıcının yaşını soran ve belirli yaş aralıklarına göre farklı izinler veren bir örnek.
0-14 yaş arası: çocuklar ve ergenler
15-64 yaş arası: aktif nüfus veya çalışan nüfus
65 ve üzeri: yaşlı ve bağımlı nüfus

'''
# name = input('Lütfen isminizi giriniz: ')
# age = int(input('Lütfen yaşınızı giriniz: '))

# if (age >=0) and (age <15):
#     print(f'Sayın {name}, yaşınıza göre bulunduğunuz kategori: Çocuklar ve Ergenler.')
# elif (age >14) and (age <65):
#     print(f'Sayın {name}, yaşınıza göre bulunduğunuz kategori: Aktif nüfus veya Çalışan nüfus.')
# else:
#     print(f'Sayın {name}, yaşınıza göre bulunduğunuz kategori: Yaşlı ve bağımlı nüfus.')

'''
2. Saat Dilimi ve Günün Zamanına Göre Selamlaşma 
Kullanıcıdan saat bilgisini alarak günün zamanına göre uygun bir selamlaşma mesajı yazan bir örnek.
'''

# saat = int(input('Saat giriniz(0-23 arası): '))

# if (saat >=6 ) and (saat <12):
#     print('Günaydın!')
# elif (saat > 11) and (saat <17):
#     print('İyi öğlenler.')
# elif (saat > 17) and (saat < 23):
#     print('İyi akşamlar.')
# else:
#     print('İyi geceler.')


'''
3. Birim Fiyatına Göre İndirim Uygulama
Bir ürünün fiyatını alıp, belirli bir fiyat aralığına göre indirim uygulayan bir örnek.
'''
# fiyat = float(input('Lütfen ürünün fiyatını giriniz: '))

# if (fiyat >=0) and (fiyat < 2000):
#     indirim = fiyat * 0.1
#     yenifiyat= fiyat - indirim
#     print(f'Harcama tutarınız {fiyat}TL , harcama tutarınıza göre %10 indirim uygulandı ve yeni harcama tutarınız {yenifiyat}. İyi günler')
# elif fiyat >= 2000:
#     indirim = fiyat * 0.3
#     yenifiyat = fiyat - indirim
#     print(f'Harcama tutarınız {fiyat}TL , harcama tutarınıza göre %30 indirim uygulandı ve yeni harcama tutarınız {yenifiyat}. İyi günler')
# else:
#     print(f'Harcama tutarınız {fiyat}TL , harcama tutarınıza göre indirim uygulanamadı. İyi günler')



#### FOR DÖNGÜSÜ ####
'''
1. Alışveriş Listesindeki Ürünleri Yazdırma
Bir alışveriş listesinde bulunan ürünleri yazdırmak için for döngüsü kullanabilirsiniz.
alisveris_listesi = ["Ekmek", "Süt", "Peynir", "Yumurta", "Elma"]. Her ürünü yazdıralım.
'''

# alisveris_listesi = ["Ekmek", "Süt", "Peynir", "Yumurta", "Elma"]

# for urun in alisveris_listesi:
#     print(f"Alınacak ürün: {urun}")


'''
2. Saatlik Aktivite Planı
Bir gün boyunca yapılacak aktiviteleri saat saat listeleyip yazdırmak için for döngüsü kullanabilirsiniz.
aktivite_planı = [
    "07:00 - Kahvaltı",
    "08:00 - İşe başlama",
    "12:00 - Öğle yemeği",
    "15:00 - Ara",
    "18:00 - Eve dönüş",
    "20:00 - Akşam yemeği",
    "22:00 - Uyuma"
]
'''
# aktivite_planı = [
#     "07:00 - Kahvaltı",
#     "08:00 - İşe başlama",
#     "12:00 - Öğle yemeği",
#     "15:00 - Ara",
#     "18:00 - Eve dönüş",
#     "20:00 - Akşam yemeği",
#     "22:00 - Uyuma"
# ]

# for plan in aktivite_planı:
#     print(f"Aktive planınız {plan}")


'''
3. Sınıftaki Öğrencilerin Notlarını Yazdırma
Bir sınıftaki öğrencilerin isimlerini ve notlarını yazdırmak için for döngüsü kullanılabilir.
ogrenci_notları = {"Ali": 85, "Ayşe": 92, "Mehmet": 78, "Zeynep": 88}
'''
# ogrenci_notları = {"Ali": 85, 
#                    "Ayşe": 92, 
#                    "Mehmet": 78, 
#                    "Zeynep": 88}

# for kisi, notu in ogrenci_notları.items(): #items kullanma nedenimiz anahtar değer çiftini döndürmek istememizdendir. ogrenci anahtar kısmını temsil eder not ise değeri
#     print(f"{kisi} : {notu} puan")
    



'''
4. Kredi Kartı Harcama Özetini Yazdırma
Bir kişinin kredi kartı harcamalarını listeleyip toplam harcamayı hesaplamak için for döngüsü kullanılabilir.
harcamalar = [50, 100, 200, 75, 120]
'''
harcamalar = [50, 100, 200, 75, 120]

toplam = 0
for harcama in harcamalar:
    toplam += harcama
print(f"Toplam harcamanız : {toplam}") 


### WHILE DÖNGÜSÜ ###

'''
1. Kullanıcıdan Doğru Şifreyi Alana Kadar Girdi Alma
Bir uygulamada kullanıcıdan doğru şifreyi girene kadar şifre girmesi istenebilir. Bu işlem için while döngüsü kullanılır.
dogru_sifre = "1234"
'''



'''
2. Kullanıcıdan Pozitif Bir Sayı İsteme
Kullanıcıdan pozitif bir sayı girmesi istenebilir. Kullanıcı yanlış bir sayı girerse, doğru sayıyı girene kadar tekrar istenebilir.
'''

'''
3. Kullanıcıdan 0'ı Girmesiyle Durdurulan Harcama Listesi
Bir kişinin yaptığı harcamalar listelenip, kullanıcı 0'ı girdiğinde listeleme durdurulabilir.
'''

'''
4. Kullanıcının Sayı Girerek Toplama Yapması
Kullanıcıdan sürekli sayı girmesi istenebilir ve bu sayılar toplanır. 0 girildiğinde işlem sonlandırılır.
'''

'''
5. Sınıfın Ortalama Notunu Hesaplama
Bir sınıftaki öğrencilerin notlarını girip, ortalamayı hesaplayabilirsiniz. Kullanıcı 0 girene kadar notları almaya devam eder.
'''