# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)    

# numbers = [x for x in range(10)]
# print(numbers)

for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10)]
print(numbers)

myString = 'Hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList) #çıktısı ['H', 'e', 'l', 'l', 'o']

years = [1983,1999,2008,1956,1986]
ages = [2019-year for year in years]
print(ages) #çıktısı [36, 20, 11, 63, 33]

result = [x if x%2 == 0 else 'Tek' for x in range (1,10)]
print(result) #çıktısı ['Tek', 2, 'Tek', 4, 'Tek', 6, 'Tek', 8, 'Tek']

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y)) #çıktısı [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print(result)

numbers = [(x,y) for x in range(3) for y in range(3) for z in range (3)]
print(numbers) #çıktısı [(0, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 2), (0, 2), (0, 2), (1, 0), (1, 0), (1, 0), (1, 1), (1, 1), (1, 1), (1, 2), (1, 2), (1, 2), (2, 0), (2, 0), (2, 0), (2, 1), (2, 1), (2, 1), (2, 2), (2, 2), (2, 2)]



