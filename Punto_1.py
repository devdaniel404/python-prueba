#Fizz, Buzz y FizzBuzz

Numero = int(input("Digite el numero a evaluar: "))

if Numero%3 == 0 and Numero%5 == 0:
    print("FizzBuzz")
elif Numero%5 == 0:
    print("Buzz")
elif Numero%3 == 0:
    print("Fizz")
else:
    print(f"El numero es {Numero} ")