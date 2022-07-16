from engine.game import Game
from nouns.items import Key, Ring
from nouns.locations import Kitchen, Cellar, Attic, Yard
from nouns.props import Door, Window


def start_game():
    setup = {
        'map': {
            Attic: {
                'exits': [Kitchen],
                'items': [Ring],
            },
            Cellar: {
                'exits': [Kitchen],
                'items': [Key],
            },
            Kitchen: {
                'exits': [Attic, Cellar],
                'props': [Door, Window]
            },
            Yard: {
                'exits': [Kitchen],
            },
        },
        'start': Kitchen
    }

    settings = {
        'debug': False
    }

    game = Game(settings, setup)
    game.run()


if __name__ == '__main__':
    start_game()
