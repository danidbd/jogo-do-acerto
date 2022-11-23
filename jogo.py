print("bem vindo ao meu jogo de acerto, tu tem 3 tentaivas para acertar o numero certo")
resp=8
tt=3
rj=""
while rj!=resp and tt!=0:
    rj=int(input("insira sua tentativa de 1 a 10:"))
    tt=tt-1
    if rj>resp:
        print("menor")
    elif rj<resp:
        print("maior")

if rj!=resp:
    print("errou")
else:
    print("parabens")