age_list = []

count = 0
while count < 20:
    age = int(input('Ingresa tu edad: '))
    age_list.append(age)
    count += 1


i=0
for e in age_list:
    if e > 20:
        i+=1

print(i) 
