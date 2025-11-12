def saludo(nombre: str) -> str:
    return f"Hola, {nombre}! Bienvenido a Git."

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))
    print("editar desde GitHub")
    a = eval(input("Ingrese un numero: "))
    b = eval(input("Ingrese un numero: "))
    total = a + b
    print("La suma de",a , "+", b, "es: ", total)
