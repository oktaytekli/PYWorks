# name = 'Oktay Tekli'

# # for letter in name:
# #     if letter == 'a':
# #         break #a ya geldiği an durdur demek
# #     print(letter)


# for letter in name:
#     if letter == 'a':
#         continue #sadece o an ki döngü durumunu devam ettiriyor.
#     print(letter)

# x = 0
# while x < 5:
#     if x == 2:
#         break #2 ye geldiği an döngüden çık demek
#     print(x)
#     x +=1

#1 den 100e kadar tek sayıların toplamı

x = 1
result = 0
while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x
   

print(f'Toplam {result}')