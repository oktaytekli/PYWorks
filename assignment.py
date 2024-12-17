# x = 5
# y=10
# z= 20

#x, y, z = 5, 10, 20
#x, y = y, x #yerler değişir

# x += 5 # x = x+5 demenin farklı yoludur.
# x -= 5 # x= x -5 demenenin farklı yoludur.
# x*= 5 # x = x * 5 demenin farklı yoludur.
# x /= 5 # x = x / 5 demenin farklı yoludur.
# x %=5 #x = x % 5 demenin farklı yoludur. (MOD)
# x //= 5 # x = x // 5 demenin farklı yoludur. (TAM BÖLME)
# y **= 5 # y = y ** 5 demenin farklı yoludur. (üslü sayı)


#print(x,y,z)

values = 1, 2, 3, 4, 5
print(values)
print(type(values))

x, y, *z = values # kalan dizi elemanları z ye gider demek yani z için bir dizi oluşturur.


print(x,y,z)