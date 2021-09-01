from src.televisao import Televisao, ControleRemoto

tv = Televisao(15, 1)
controle = ControleRemoto(tv)


while True:

    op = controle.opcoes()

    if op == 1:
        res = controle.aumentar_volume()
        if res:
            print("Ok")
        else:
            print("Volume no maximo!")
    elif op == 2:
        res  = controle.diminuir_volume()
        if res:
            print("Ok")
        else:
            print("Volume no minimo!")
    elif op == 3:
        controle.prox_canal()
        print("Ok")
    elif op == 4:
        controle.ante_canal()
        print("Ok")
    elif op == 5:
        print("Canal: ", controle.consulta_canal)
    elif op == 6:
        print("Volume: ", controle.consulta_volume)
    elif op ==  0:
        break
    else:
        print("Opção inválida")