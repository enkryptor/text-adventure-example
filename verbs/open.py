from engine.words import Verb
from nouns.items import Key
from nouns.locations import Yard
from nouns.props import Door


class Open(Verb):
    def name(self):
        return "открыть"

    def run(self, noun):
        if noun and not self.game.is_nearby(noun):
            print("Здесь этого нет")
            return
        match noun:
            case None:
                print("Что конкретно открыть?")
            case Door():
                if self.game.flags.get('kitchen_door_is_open'):
                    print("Дверь уже открыта!")
                    return
                print("Вы попытались открыть дверь")
                if self.game.has_item(Key):
                    print("Дверь получилось открыть с помощью имеющегося у вас ключа")
                    self.game.flags['kitchen_door_is_open'] = True
                    self.game.get_current_scene().exits.add(self.game.get_scene(Yard))
                else:
                    print("Заперто... Наверное, нужен ключ?")
            case _:
                print("Не получилось открыть")
