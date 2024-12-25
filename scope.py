# #global scope
# x = 'global x'

# def function():
#     #local scope
#     #x = 'local x'

# function()
# print(x)

############################

name = 'Oktay'
def changeName(new_name):
    name = new_name
    print(name)

changeName('Damla')
print(name)

#####################

name = 'global string'

def greeting():
    #name='Oktay'
    
    def hello():
        #name = 'Okti'
        print('Hello'+ name)
    hello()

greeting()


################

x = 50
def test():
    global x #dışarıda tanımlanmış x bilgisini içeride kullanmak için
    print(f'x  : {x}')
    
    x=100
    print(f'Changed x to {x}')
test()
print()