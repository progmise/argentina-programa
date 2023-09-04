def sumar(num1: int, num2: int) -> int:
    return num1 + num2


def restar(num1: int, num2: int) -> int:
    return num1 - num2


def multiplicar(num1: int, num2: int) -> int:
    return num1 * num2


def dividir(num1: int, num2: int) -> int:
    return num1 // num2


def main() -> None:
    num1 = int(input("Ingrese el 1° número: "))
    num2 = int(input("Ingrese el 1° número: "))

    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es {resultado}")

    resultado = restar(num1, num2)
    print(f"El resultado de la resta es {resultado}")

    resultado = multiplicar(num1, num2)
    print(f"El resultado de la multiplicación es {resultado}")

    resultado = dividir(num1, num2)
    print(f"El resultado de la división es {resultado}")


main()