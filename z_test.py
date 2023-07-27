def obtener_numeros_primos(n):
    """
    Función que devuelve un arreglo de números primos hasta el número n
    """
    numeros_primos = []  # Inicializar arreglo vacío para almacenar los números primos encontrados
    for num in range(2, n+1):  # Iterar sobre los números desde 2 hasta n (inclusive)
        es_primo = True  # Suponemos que num es primo hasta que se demuestre lo contrario
        for i in range(2, num):  # Iterar sobre los números desde 2 hasta num-1
            if num % i == 0:  # Si el número es divisible por i, entonces no es primo
                es_primo = False  # Marcar que num no es primo
                break  # Salir del loop interno
        if es_primo:  # Si num es primo (es_primo sigue siendo True), entonces agregar a la lista
            numeros_primos.append(num)
    return numeros_primos

# Ejemplo de uso
n = int(input("Introduce un número entero positivo: "))
print("Números primos hasta", n, ":", obtener_numeros_primos(n))
