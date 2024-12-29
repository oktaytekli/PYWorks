# Dosya  açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (Write) yazma modu. Dosyayı konumda oluşturur.

# file = open("newfile.txt", "w")
# file.close()

# file = open("C:\users\USER\Desktop\newfile.txt", "w")
# file.close()

# file = open("newfile.txt", "w", encoding='utf-8')
# file.write("OktayTekli")
# file.close()

# "a" : (Append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt", "w", encoding='utf-8')
# file.write("Oktay Tekli")
# file.write("\nOktay Tekli")
# file.close() 

# "x" : (Create) oluşturma. Dosya zaten varsa hata verir.

file = open("newfile2.txt", "w", encoding='utf-8')

# "r" : (Read) okuma. Varsayılan. Dosya konumda yoksa verir.