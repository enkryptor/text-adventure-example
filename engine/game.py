import importlib
import pkgutil

from engine.parser import Parser
from engine.words import Verb, Scene, Item, Prop


def get_words(pkg_name, word_class):
    modules = [name for _, name, _ in pkgutil.iter_modules([pkg_name])]
    for module_name in modules:
        module = importlib.import_module(f"{pkg_name}.{module_name}")
        for class_name in dir(module):
            class_ = getattr(module, class_name)
            try:
                if word_class in class_.__bases__ and class_ not in [Scene, Prop, Item]:
                    yield class_()
            except AttributeError:
                pass


class Player:
    def __init__(self, location=None):
        self.current_location = location
    current_location = None


class Game:
    def __init__(self, settings, setup):
        self.verbs = list(get_words("verbs", Verb))
        self.locations = list(get_words("nouns", Scene))
        self.props = list(get_words("nouns", Prop))
        self.items = list(get_words("nouns", Item))
        self.flags = {}
        self.inject_game([*self.verbs, *self.locations, *self.props, *self.items])
        debug = settings.get('debug')

        if debug:
            print("Loaded verbs:", list(map(lambda x: x.name(), self.verbs)))
            print("Loaded locations:", list(map(lambda x: x.name(), self.locations)))
            print("Loaded props:", list(map(lambda x: x.name(), self.props)))
            print("Loaded items:", list(map(lambda x: x.name(), self.items)))

        scenes = setup['map']
        for scene_class in scenes:
            scene = self.get_scene(scene_class)
            if debug:
                print('Loading scene:', scene.name())
            exits = scenes[scene_class].get('exits')
            scene.exits = set([x for x in self.locations if x.__class__ in exits]) if exits else {}
            props = scenes[scene_class].get('props')
            scene.props = [x for x in self.props if x.__class__ in props] if props else []
            items = scenes[scene_class].get('items')
            if items:
                for item in items:
                    assert not item.location
                    item.location = scene

        start_scene_class = setup['start']
        start_scene = self.get_scene(start_scene_class)
        self.player = Player(start_scene)

    def inject_game(self, words):
        for word in words:
            word.game = self

    def run(self):
        parser = Parser(self)
        print('Введите слово "справка", если играете впервые')
        while True:
            print()
            phrase = input("> ")
            verb, noun = parser.parse(phrase)
            if verb:
                verb.run(noun)
            else:
                print("Что, простите?")

    def get_scene(self, scene_class):
        return next(s for s in self.locations if s.__class__ is scene_class)

    def get_verb(self, verb_class):
        return next(s for s in self.verbs if s.__class__ is verb_class)

    def change_scene(self, scene):
        self.player.current_location = scene

    def get_current_scene(self):
        return self.player.current_location

    def take_item(self, item: Item):
        item.location = self.player

    def get_inventory(self):
        return [item for item in self.items if item.location is self.player]

    def has_item(self, item_class):
        item = next(x for x in self.items if x.__class__ is item_class)
        return False if not item else item in self.get_inventory()

    def get_nearby_items(self):
        return [item for item in self.items if item.location is self.player.current_location]

    def get_nearby_exits(self):
        return self.get_current_scene().exits

    def get_nearby_props(self):
        return [*self.get_nearby_items(), *self.get_current_scene().props]

    def is_nearby(self, noun):
        return noun in [*self.get_nearby_props(), *self.get_inventory(), self.get_current_scene()]
