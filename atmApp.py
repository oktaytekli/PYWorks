#Bankamatik uygulaması

oktayHesap = {
    'ad' : 'Oktay Tekli',
    'hesapNo' : '1234567',
    'bakiye': 1000,
    'ekHesap': 20000
}

olcayHesap = {
    'ad' : 'Olcay Tekli',
    'hesapNo' : '145567',
    'bakiye': 10000,
    'ekHesap': 100
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye']+ hesap['ekHesap']

        if (toplam >=miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h)')

            if  ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar * hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır.')
        else:
            print('Bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(oktayHesap, 1000)
bakiyeSorgula(oktayHesap)

print('*********')

paraCek(oktayHesap, 1000)
bakiyeSorgula(oktayHesap)
