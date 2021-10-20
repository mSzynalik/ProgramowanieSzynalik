"""
zad 1
def hello(name: str, surname: str) -> str:
    x = (f"Cześć {name} {surname}!")
    return x

print(hello("Mati", "Szynal"))
"""

"""
zad 2
def multiply(a: int, b: int) -> int:
    result = a * b
    return result

print(multiply(3, 4))
"""

"""
zad 3
def checking(a: int) -> bool:
    if a % 2 == 0:
        y = True
    else:
        y = False
    if y:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")

checking(6)
checking(5)
"""
"""
zad 4
def check(a: int, b: int, c: int) -> bool:
    if a + b >= c:
        return True
    else:
        return False

print(check(4, 3, 6))
print(check(4, 3, 20))
"""

"""
zad 5
def sprawdzenie(lista: list, a: int) -> bool:
    if a in lista:
        return True
    else:
        return False

print(sprawdzenie([2, 3, 4], 2))
print(sprawdzenie([2, 3, 4], 1))
"""

"""
zad 6
def modify(lista_a: list, lista_b: list) -> list:
    lista_wynikowa = []
    for elem in lista_a:
        lista_b.append(elem)
    temp_set = set()
    for elex in lista_b:
        temp_set.add(elex)
    for el in temp_set:
        lista_wynikowa.append(el)
    for i in range(len(lista_wynikowa)):
        lista_wynikowa[i] = lista_wynikowa[i] ** 3
    return lista_wynikowa

print(modify([2, 3, 4], [1, 2, 3, 4, 5]))
"""

class Brawery()


