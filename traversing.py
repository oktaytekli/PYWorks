with open("newfile.txt" , "r", encoding="utf-8") as file:
    content = file.read(10) # sadece 10 tanesini oku deriz bu şekilde
    print(content)
    file.seek(0) #bu metod ile birlikte cursor u en başa gönderip baştan yazdırdı
    print(file.tell())
    content2 = file.read()
    print(content2)


file.close()