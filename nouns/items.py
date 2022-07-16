from engine.words import Item


class Key(Item):
    def name(self):
        return "ключ"

    def describe(self):
        return "Небольшой латунный ключ. Кажется, им можно открыть какую-то дверь?"


class Ring(Item):
    def name(self):
        return "кольцо"

    def describe(self):
        return "Маленькое колечко из жёлтого металла. Кто знает, кому оно принадлежало ранее?"
