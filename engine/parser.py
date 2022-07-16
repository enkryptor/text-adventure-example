from engine.words import Verb, Noun, Unknown


class Parser:
    def __init__(self, game):
        self.verbs = [*game.verbs]
        self.nouns = [*game.locations, *game.items, *game.props]

    def parse(self, phrase: str) -> (Verb, Noun):
        words = phrase.lower().strip(" ,.\"").split()
        verb_str = words[0]
        noun_str = words[-1]
        verb = next((x for x in self.verbs if x.match(verb_str)), None)
        noun = None if verb_str == noun_str else next((x for x in self.nouns if x.match(noun_str)), Unknown(noun_str))
        return verb, noun
