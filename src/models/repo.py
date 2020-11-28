class Repo:

    def __init__(self, ident, name, stars):
        self._id = ident
        self._name = name
        self._stars = stars

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def stars(self):
        return self._stars

    def __str__(self):
        return f'id: {self._id}, {self._name}, {self._stars}'
