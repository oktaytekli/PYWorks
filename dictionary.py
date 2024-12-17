# # key - value

# # 41 => kocaeli 

# sehirler = ['istanbul', 'kocaeli']
# plakalar = ['34', '41']

# print(plakalar[sehirler.index('kocaeli')]) # kocaeli bilgisini getiricez.

# #print(plakalar['kocaeli']) => 41
# #print(plakalar['istanbul']) => 34
 
# plakalar = {'kocaeli' : 41, 'istanbul' : 34} 
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)


user = {
    'oktaytekli' :{
    'age' : 25 , 
    'roles': ['user'],  
    'email' : 'oktaytekli@hotmail.com',
    'address' : 'istanbul',
    'phone' : '538085614'
    },
    'olcaytekli' : {
    'age' : 25 , 
    'roles' : ['admin', 'user'],
    'email' : 'olcaytekli@hotmail.com',
    'address' : 'istanbul',
    'phone' : '538875614'
    }
}

print(user['olcaytekli'])
print(user['olcaytekli']['roles'])
print(user['olcaytekli']['roles'][0])
