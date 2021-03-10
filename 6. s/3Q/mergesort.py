class MergeSort:

    def mergesort(self, v, p, r):
        if p < r:
            q = (p + r) // 2
            MergeSort.mergesort(v, p, q)
            MergeSort.mergesort(v, q+1, r)
            MergeSort.intercalar(v, p, q, r)

    def intercalar(self, v, p, q, r):
        temp = v.copy()
        i = p
        j = q+1
        k = p

        while k <= r:
            if i > q:
                v[k] = temp[j]
                j += 1
            elif j > r:
                v[k] = temp[i]
                i+= 1
            elif temp[i] <= temp[j]:
                v[k] = temp[i]
                i += 1
            else:
                v[k] = temp[j]
                j+= 1

            k += 1