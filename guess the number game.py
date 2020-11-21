import random
#PP
intentos=n=0
num=random.randint(1,500)
while n!=num:
    try:
        n=int(input("Adivine el numero: "))
    except ValueError:
        print("Dato no válido.Debe ingresar un numero entero.")
        intentos+=1
    else:
        if n>num:
            print("Te pasaste.")
        elif n<num:
            print("Te quedaste corto.")
        intentos+=1      
print(f"Adivinaste en {intentos} intentos")    