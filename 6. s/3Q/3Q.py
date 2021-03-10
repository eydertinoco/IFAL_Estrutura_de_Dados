import time

from mergesort import MergeSort
from quicksort import QuickSort


class terceiraQuestao:

    def printInformacoes(self, lista, bubble, temp1, merge, temp2, quick, temp3, insertion, temp4):
        print("====================================")
        print("A lista atualmente {}".format(lista))
        print("====================================")
        print("Bubblesort {} ms: {}".format(temp1, bubble))
        print("Mergesort {} ms: {}".format(temp2, merge))
        print("Quicksort {} ms: {}".format(temp3, quick))
        print("Insertionsort {} ms: {}".format(temp4, insertion))
        print("====================================")

    def mergesort(self, vetor):
        merge = MergeSort.mergesort(self, vetor, 0, len(vetor)-1)
        return merge

    def quicksort(self, vetor):
        quick = QuickSort.quicksort(self, vetor, 0, len(vetor) - 1)
        return quick

if __name__ == "__main__":
    x = int(0)
    while x < 4:
        if x > 0 and x <= 3:
            if x == 0: list = [2, 4, 6, 8, 10, 12]
            if x == 1: list = [11, 9, 7, 5, 3, 1]
            if x == 2: list = [2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 3, 1]
            if x == 3: list = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
        inicio = time.time()
        bubblesort = terceiraQuestao.(list)
        final = time.time()
        tempbubblesort = final - inicio

        inicio = time.time()
        mergesort = terceiraQuestao.mergesort(list)
        final = time.time()
        tempmergesort = final-inicio

        inicio = time.time()
        quicksort = terceiraQuestao.mergesort(list)
        final = time.time()
        tempquicksort = final - inicio

        inicio = time.time()
        insertionsort = terceiraQuestao.mergesort(list)
        final = time.time()
        tempinsertionsort = final - inicio

        terceiraQuestao.printInformacoes(list,bubblesort, tempbubblesort, mergesort, tempmergesort,
                                         quicksort, insertionsort, tempinsertionsort)