import random
# Varianta I cu while
# contor=0
# while contor<6:
#     contor+=1
#     nr=random.randint(1,49)
#     print(nr)
    
# print('Contor nu mai este mai mic ca 6')

# Varianta II cu for

# for i in range(6):
#     nr=random.randint(1,49)
#     print(nr)

# Varianta pythonica
# numere=[random.randint(1,49) for i in range(6)]
# print(numere)

numere=[]

while len(numere)<6:
    nr=random.randint(1,49)
    if nr not in numere:
        numere.append(nr)
    
print(numere)
