# 120190101_Văn-Hữu-An Bài 2

V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
E = [[0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 0, 1, 0, 1, 0]]
# Trả lời: Dán code vào bên dưới
start = 0
open = [start]
close = []
success = False
count = 0
dinhcha = {}
while len(open) >= 1:
    count += 1
    O = open.pop(0)
    close.append(O)
    if O == 8:
        success = True
        break
    khampha = []
    for y in range(0, 9):
        if E[O][y] == 0:
            continue
        if y in close or y in open:
            continue
        khampha.append(y)
    dinh = []
    for i in khampha:
        dinh.append(V[i])
        dinhcon = i
        open.insert(0, dinhcon)
        dinhcha[dinhcon] = O
    print("Kham pha ra dinh: ", dinh)
if success == False:
    print("Khong tim thay duong di")
else:
    truyvet = [V[O]]
while dinhcha.get(O) != None:
    O = dinhcha.get(O)
    truyvet.append(V[O])
    truyvet.reverse()
    print("Duong di: ")
    print(*truyvet)
