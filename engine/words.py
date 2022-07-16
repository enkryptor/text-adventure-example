from abc import abstractmethod, ABC


class Word(ABC):
    game = None

    @abstractmethod
    def name(self):
        ...

    def get_synonyms(self):
        return []

    def match(self, word) -> bool:
        if word == self.name():
            return True
        return word in self.get_synonyms()


class Unknown(Word):
    def __init__(self, word):
        self.unknown_word = word

    def name(self):
        return self.unknown_word


class Verb(Word, ABC):
    @abstractmethod
    def run(self, noun):
        ...


class Noun(Word, ABC):
    def accusative(self):
        return self.name()

    def match(self, word) -> bool:
        return super().match(word) or word == self.accusative()


class Scene(Noun, ABC):
    @abstractmethod
    def describe(self):
        ...
    exits = {}
    items = []
    props = []


class Prop(Noun, ABC):
    @abstractmethod
    def describe(self):
        ...


class Item(Prop, ABC):
    ...
    location = None
