'''
Crie um programa que receba duas listas e retorne 
uma terceira lista com a interseção dos elementos das duas listas.
'''

lista1=['A',2,'Pedro',4]
lista2=[5,True,7,['b',5]]
lista3=[]

'''
for item in lista1:
    lista3.append(item)
for item in lista2:
    lista3.append(item)
print(lista3)
'''

lista3.extend(lista1)
print(lista3.extend(lista2))
print(lista3)