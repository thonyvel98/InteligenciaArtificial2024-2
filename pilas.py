containerPila = []

containerPila.append(23)
containerPila.append(100)
containerPila.append(25)

for item in containerPila:
    print(item)

auxl=containerPila.pop()

print(f'El ultimo elemento mostrado {auxl} ')

print ('Actualizacion despues del pop')
for elem in containerPila:
    print(elem)

auxl2=containerPila[-1]
print ( 
    'Actualizacion de contenedor despues de [-1]')
for elem in containerPila:
    print(elem)