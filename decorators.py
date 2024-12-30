# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello()

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + str(finish-start) + " saniye sürdü.")
    return inner
    
@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usAlma(2,3)
faktoriyel(4)

# def usAlma(a,b):
#     start = time.time()
#     time.sleep(1)
#     print(math.pow(a,b))
#     finish = time.time()
#     print("Fonksiyon" + str(finish-start)+ "saniye sürdü.")

# def faktoriyel(num):
#     start = time.time()
#     time.sleep(1)
#     print(math.factorial(num))
#     finish = time.time()
#     print("fonksiyon" + str(finish-start) + "saniye sürdü.")

# usAlma(2,3)
# faktoriyel(4)