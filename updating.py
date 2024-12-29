# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     file.write("Deneme")


# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())


with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nOktay Tekli 2")

with open("newfile.txt", "r+", encoding="utf-8") as file:
     print(file.read())
