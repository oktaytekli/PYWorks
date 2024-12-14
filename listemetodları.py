numbers = [1,10,5,16,4,9,10]
letters = ['a', 'g', 's','b','y','a','s']

val = min (numbers)
val = max (numbers)
val = max (letters)
val = min (letters)

val = numbers[3:6]#çıktı 16 4 9
val = letters[2:4]#çıktı s b

numbers[4] = 40

# numbers.append(49)#en sona sayı eklemek için kullanırız.
# numbers.insert(3, 78)#istediğimiz yere sayı eklemek için kullanırız.
# numbers.insert(-1,52)

# numbers.pop()#en sondaki sayıyı silmek için kullanırız.
# numbers.pop(-1)

numbers.remove(9)#istediğimiz elemanı kaldırmak için kullanırız.

numbers.sort()#küçükten büyüğe sıralar
numbers.reverse()#büyükten küçüğe

letters.sort()#alfabetik olarak sıralar
letters.reverse()#sondan sıralar

print(numbers.count(10))#kaç tane 10var diye sayar.

print(numbers)