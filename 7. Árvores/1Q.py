class No:

    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

def altura(self, atual):
    if atual == None or atual.esq == None and atual.dir == None:
        return 0
    else:
        if self.altura(atual.esq) > self.altura(atual.dir):
            return 1 + self.altura(atual.esq)
        else:
            return 1 + self.altura(atual.dir)