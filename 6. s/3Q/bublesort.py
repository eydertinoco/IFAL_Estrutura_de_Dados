def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):

            if lista[i] > lista[j]:
                temp = lista[j]
                lista[j] = lista[i]
                lista[i] = temp
            print(lista)


lista = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]

bubble_sort(lista)

print("Sorted array is:")
for i in range(len(lista)):
    print("%d" % lista[i])