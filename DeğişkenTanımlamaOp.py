"""
    1-Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    
    Müşteri adı
    Müşteri soyadı
    Müşteri ad+soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı

"""
musteriAdi= 'Oktay'
musteriSoyad= 'Tekli'
musteriAdSoyad= musteriAdi + '' + musteriSoyad
musteriCinsiyet = True #Erkek
musteriTcKim= '4876153272'
musteriDogumYil= 1999
musteriAdres = 'İstanbul Esenyurt'
musteriYasi= 2024 - musteriDogumYil

"""
    2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    Sipariş 1 => 110 TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 2187.95 TL

"""
order1=110
order2=1100.5
order3=2187.95

total=order1+order2+order3
print(total)



