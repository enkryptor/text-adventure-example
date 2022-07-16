from engine.words import Verb, Item, Unknown


class Take(Verb):
    def name(self):
        return "взять"

    def get_synonyms(self):
        return ["поднять", "забрать"]

    def run(self, noun):
        match noun:
            case None:
                print("Напишите, что конкретно вы хотите взять")
            case Unknown():
                print("Ничего подобного здесь нет")
            case Item():
                self.take_item(noun)
            case _:
                print("Нельзя взять с собой", noun.accusative())

    def take_item(self, item):
        inventory_items = self.game.get_inventory()
        if item in inventory_items:
            print("У вас это уже с собой")
            return

        available_items = self.game.get_nearby_items()
        if item in available_items:
            print("Вы решили взять с собой", item.name())
            self.game.take_item(item)
        else:
            print("Нигде рядом вы не видите", item.name())
