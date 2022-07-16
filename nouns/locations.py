from engine.words import Scene


class Kitchen(Scene):
    def name(self):
        return "кухня"

    def accusative(self):
        return "кухню"

    def describe(self):
        details = "\nДверь открыта" if self.game.flags.get('kitchen_door_is_open') else ""
        return "Грязная обшарпанная кухня. Маленькое зарешётченное окно и одна дверь" + details


class Cellar(Scene):
    def name(self):
        return "подвал"

    def describe(self):
        return "Тесный и мрачный погреб"


class Attic(Scene):
    def name(self):
        return "чердак"

    def describe(self):
        return "Пыльный чердак с паутиной"


class Yard(Scene):
    def name(self):
        return "улица"

    def accusative(self):
        return "улицу"

    def describe(self):
        return "Выход во двор. Собственно, здесь заканчивается демонстрация игры"
