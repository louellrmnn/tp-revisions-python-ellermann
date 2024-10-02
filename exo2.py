#2a
a = input("Un nombre:")
converted_a = int(a)

if converted_a < 0:
    print("nombre negatif")

elif converted_a == 0: 
    print("nombre nul")

else: 
    print("nombre positif")


#2b
for i in [1, 2, 3, 4, 5]:
    print(i)


#2c
somme = 0
for i in range(100):
    if i % 2 == 0:
        somme += i
print (somme)