from GAME.abs_game import game
import numpy as np

class GameOfLife(game):

    def __init__(self,n_lignes,n_cols,n_repet):
        self.n_lignes,self.n_cols,self.n_repet = n_lignes,n_cols,n_repet
        self.people = np.random.randint(2, size = (self.n_lignes, self.n_cols))
        

    def description(self):
        print(f"\n  Game Name : Game of Life \n With nb_rows : {self.n_lignes}, nb_cols : {self.n_cols}, nb_repetitions : {self.n_repet}")
        print("The initialisation of the Matrix :")
        print(self.people)

    def strategie(self):
        pass

    def call_neighbors_first_rows(self,i,j):
        pass

    def call_neighbors_last_rows(self,i,j):
        pass

    def call_neighbors_between_first_and_last_rows(self,i,j):
        pass

    def call_neighbors(self,i,j) -> list:
        pass

    