
from src.biblioteca import Biblioteca

#inicia a biblioteca
qtd = int(input("Quantos Livros quer adicionar: "))
library = Biblioteca()

for a in range (qtd):
    title = input("Titulo do livro: ")
    author = input("Autor: ")
    dt = input("Data de Publicação dd/mm/aaaa: ")
    price = float(input("Preço: "))
    library.add_books(title, author, dt, price)


def menu():
    print("1...Exibir Detalhes\n0...Sair")
    esc = int(input("Digite uma opção: "))

    return esc

while True:
    print("Livros\n----------------------")
    library.imprimir_titles()
    print("----------------------")
    op = menu()

    if op == 1:
        chave = int(input("Escolha o livro: "))
        print("----------------------")
        library.imprimir_infos(chave)
        print("----------------------")
    if op == 0:
        break;