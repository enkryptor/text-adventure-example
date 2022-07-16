from engine.words import Verb, Unknown, Scene
from verbs.look import Look


class Go(Verb):
    def name(self):
        return "идти"

    def get_synonyms(self):
        return ["пойти", "уйти", "пройти", "бежать", "спуститься", "подняться", "вернуться"]

    def run(self, noun):
        match noun:
            case None:
                print("Напишите, куда конкретно вы хотите идти")
            case Unknown():
                print("Я не понимаю, куда вы хотите идти")
            case Scene():
                if noun in self.game.get_nearby_exits():
                    print("Вы направились в", noun.accusative())
                    self.game.change_scene(noun)
                    self.game.get_verb(Look).look_around()
                else:
                    print("Отсюда нельзя попасть в", noun.name())
            case _:
                print(f"Непонятное направление движения \"{noun.name()}\"")
