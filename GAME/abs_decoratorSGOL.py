from .abs_game import game

class AbsDecoratorSGOL(game):
    def __init__(self, jeu):
        self._jeu = jeu

    @property
    def jeu(self):
        return self._jeu