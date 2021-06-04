class Livro:

    def __init__(self, title, author, dt_publish, price_target):
        self._title = title
        self._author = author
        self._dt_publish = dt_publish
        self._price_target = price_target

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author

    @property
    def dt_publish(self):
        return self.adt_publish
    @dt_publish.setter
    def title(self, dt_publish):
        self._dt_publish = dt_publish

    @property
    def price_target(self):
        return self._price_target
    @price_target.setter
    def price_target(self, price_target):
        self._price_target = price_target
