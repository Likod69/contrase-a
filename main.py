import random
contra=""
caracteres="/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cant=int(input("ingrese un numero:"))
for i in range(cant):
    contra+=random.choice(caracteres)
print(contra)
