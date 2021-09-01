from src.livro import Livro
class Biblioteca:
    qtd =0
    def __init__(self):
        self._books = {}

    @property
    def books(self):
        return self._books

    def add_books(self, title, author, dt, price):
        b = Livro(title, author, dt, price)
        self._books[Biblioteca.qtd] = b
        Biblioteca.qtd += 1

    def imprimir_titles(self):
        for key, a in self._books.items():
            print(key,"- Titulo:", a._title)

    def imprimir_infos(self, key):
        if key in self._books.keys():
            print("Titulo:", self._books[key]._title)
            print("Autor:",  self._books[key]._author)
            print("Data de Publicação:",  self._books[key]._dt_publish)
            print("Preço:",  self._books[key]._price_target)