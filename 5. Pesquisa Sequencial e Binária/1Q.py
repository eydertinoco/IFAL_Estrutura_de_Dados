x = int(input("Adicione um valor positivo: "))
y = int(0)
media = int(0)

# Pegando metade por metade até encontrar onde está a raiz. Ex o X = 30
# 15*15 - 30 < 0,000001
# 7,5*7,5 - 30 < 0,000001
# 3,75*3,75 = 30 < 0,000001

# 5,625*5,625 = 30 < 0,000001
# 4.6875*4.6875 = 30 < 0,000001

# 5.15625*5.15625 = 30 < 0,000001
# 5.390625*5.390625 = 30 < 0,000001

# 5,5078125*5,5078125 = 30 < 0,000001
# 5,4492187*5,4492187 =


while y < x:
    if (y*y) == x:
        print("A raiz de {} é igual a {}".format(x,y))
    elif (y*y) > media and (y*y) < x:
        media = (y*y)
        print("A raiz de {} é próxima a {}".format(x, media))
    elif y == (x/2)+1:
        if (y*y) > media:
            media = (y * y)
    elif (y*y) > x:
        break;
    y += 1


