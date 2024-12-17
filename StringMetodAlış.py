website= "http://www.oktaytekli.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

#result = ' Hello World '.strip()

# 2- 'www.oktaytekli.com' içindeki oktaytekli bilgisi haricindeki her karakteri silin.

#result = 'www.oktaytekli.com'.strip('w.moc')

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

#result = course.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

#result = website.count('a')

# 5- 'website' www ile başlayıp com ile bitiyor mu?

#result = website.startswith('www')
#result1 = website.endswith('com')

# 6- 'website' içinde '.com' ifadesi var mı?

#result = website.find('.com')

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# result = course.isalpha()
# result1 = course.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

#result  = 'Contents'.center(50, '*')

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

#result = course.replace('','-')

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

#result = 'Hello World'.replace('World', 'There')

# 11-'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split()

print(result)
#print(result1)
