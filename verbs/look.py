from engine.words import Verb, Prop, Scene


class Look(Verb):
    def name(self):
        return "осмотреться"

    def get_synonyms(self):
        return ["смотреть", "посмотреть", "осмотреть", "рассмотреть", "изучить"]

    def run(self, noun):
        match noun:
            case None:
                print("Вы осматриваетесь вокруг...\n")
                self.look_around()
            case Prop():
                self.look_at_prop(noun)
            case Scene():
                if noun is self.game.get_current_scene():
                    self.look_around()
                else:
                    print(noun.name().capitalize(), "сейчас слишком далеко отсюда")
            case _:
                print("Я не вижу рядом ничего похожего")

    def look_around(self):
        print(self.game.get_current_scene().describe())

        items = self.game.get_nearby_items()
        if items:
            print("В поле вашего зрения:")
            for item in items:
                print("\t", item.name())

        exits = self.game.get_nearby_exits()
        if exits:
            print("Выходы:")
            for loc in exits:
                print("\t", loc.name())

    def look_at_prop(self, item):
        if item in self.game.get_nearby_props():
            print(item.describe())
        else:
            print("Здесь нет ничего похожего на", item.name())
