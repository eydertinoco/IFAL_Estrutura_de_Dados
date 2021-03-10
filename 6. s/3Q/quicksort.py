class QuickSort:

    def quicksort(self, v, p, r):
        if p < r:
            q = QuickSort.particionar(v, p, r)
            QuickSort.quicksort(v, p, q-1)
            QuickSort.quicksort(v, q+1, r)

    def particionar(self, v, p, r):
        x = v[p]
        i = p
        j = p + 1

        while j <= r:
            if v[j] < x:
                i += 1
                QuickSort.trocar(v, i, j)
            j += 1
        QuickSort.trocar(v, p, i)

        return i

    def trocar(self, v, n, m):
        temp = v[n]
        v[n] = v[m]
        v[m] = temp