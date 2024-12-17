
# #VALUE TYPE 
# x = 5
# y = 25

# x = y #bunu ortak bir değer olarak algılar.

# y = 10 #bunu da diğer bir değer olarak algılar.
# print(x,y)

#REFERENCE TYPE => list

a = ["apple", "banana"]
b = ["apple", "banana"]

a=b
b[0]= "grape"
print(a,b)  #burada tanımlamış olduğumuz listeyi değiştirme iki adrestede otomatik olarak yapılır.

#value type larda verinin kendisi, referrence type larda ise listenin kendisi ile ilgilenilir.
