from RSA import *
from matrix import *


k = RSA()
N = int(k[2])
d = int(k[1])
c = int(k[0])
H = []
H = mat(H)
G = []
G = gam(G)
r = random.randint(0, 100)
print("Матрица графа G")
for i in range(len(H)):
    for j in range(len(H[i])):
        print(H[i][j], end=' ')
    print()
print("Мартрица изоморфного графа G - H")
pos = [0, 1, 2, 3, 4, 5]
random.shuffle(pos)
for i in range(len(H)):
    for j in range(len(H[i])):
        H[i][j]=H[pos[i]][pos[j]]
        G[i][j]=G[pos[i]][pos[j]]
for i in range(len(H)):
    for j in range(len(H[i])):
        print(H[i][j], end=' ')
    print()
for i in range(len(H)):
    for j in range(len(H[i])):
        H[i][j] = str(r) + str(H[i][j])
        H[i][j] = int(H[i][j])
        r = random.randint(1, 100)
print("Закодированная матрица графа H")
for i in range(len(H)):
    for j in range(len(H[i])):
        print(H[i][j], end=' ')
    print()
for i in range(len(H)):
    for j in range(len(H[i])):
        H[i][j] = pow(H[i][j], d, N)
print("Зашифрованная матрица графа H")
for i in range(len(H)):
    for j in range(len(H[i])):
        print(H[i][j], end=' ')
    print()
print(pos, "использованная нумерация")
print('ответ на 1-ый вопрос:')
for i in range(len(H)):
    for j in range(len(H[i])):
        if G[i][j]== 1:
            H[i][j] = pow(H[i][j],c,N)
for i in range(len(H)):
    for j in range(len(H[i])):
        print(H[i][j], end=' ')
    print()





