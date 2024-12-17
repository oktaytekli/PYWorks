'''
öğrenciler = {
    '120': {
        'ad': 'Oktay',
        'soyad': 'Tekli',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Olcay',
        'soyad': 'Tekli',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Damla',
        'soyad': 'İriz',
        'telefon': '532 000 00 03'
    }
}

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''

ogrenciler = {}

number = input("öğrenci no:")
name = input("öğrenci adı:")
surname= input("öğrenci soyadı: ")
phone= input("öğrenci telefonu:")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }

ogrenciler.update({ #bu metodu kullanarak birden fazla veriyi üst üste ekleyebiliriz.
    number: {
        'ad':name,
        'soyad': surname,
        'telefon': phone
    }

})

ogrenciler.update({ #bu metodu kullanarak birden fazla veriyi üst üste ekleyebiliriz.
    number: {
        'ad':name,
        'soyad': surname,
        'telefon': phone
    }

})
ogrenciler.update({ #bu metodu kullanarak birden fazla veriyi üst üste ekleyebiliriz.
    number: {
        'ad':name,
        'soyad': surname,
        'telefon': phone
    }

})

print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[number]

print(f'Aradığınız {ogrNo} nolu öğrencini adı: {ogrenci['ad']} soyadı:{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}')