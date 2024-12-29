# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()


file = open("newfile.txt", "r", encoding = "utf-8")

# for döngüsü

# for i in file:
#     print(i, end="")
# read() fonksiyonu

# content1 = file.read()
# print("İçerik 1")
# print(content1)

# content2 = file.read()

# print("İçerik 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

#READLINE fonksiyonu
# print(file.readline(), end="") 
# print(file.readline()) #sadece bir satır okur

#READLINES fonksiyonu

liste = file.readlines()
print(liste)

file.close()