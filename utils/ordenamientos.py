def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Extraemos el número del ID (C1 -> 1), tecnicamente convertimos el ID a entero para comparar
            num_j = int(''.join(filter(str.isdigit, lista[j]["id"])))
            num_j1 = int(''.join(filter(str.isdigit, lista[j + 1]["id"])))
            if num_j > num_j1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
