from engine.words import Prop


class Door(Prop):
    def name(self):
        return "дверь"

    def describe(self):
        return "Массивная дверь с небольшой замочной скважиной"


class Window(Prop):
    def name(self):
        return "окно"

    def describe(self):
        return "Мутное окно с решёткой, сквозь которое ничего не видно. Похоже, оно не открывается"
