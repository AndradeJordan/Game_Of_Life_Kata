from GAME.abs_decoratorSGOL import AbsDecoratorSGOL
from .neighbors_program import Neighbors
from .displayer import Displayer
import copy

class StrategieGameOfLife(AbsDecoratorSGOL):
    
    @property
    def description(self):
        return self.jeu.description + " with Strategie "
    
    @property
    def strategie(self):
        
        return_matrix = Neighbors(self.jeu.n_lignes,self.jeu.n_cols, self.jeu.n_repet,self.jeu.people)
    
        while return_matrix.n_repet > 0 :
            n,m,M = return_matrix.n_lignes,return_matrix.n_cols, return_matrix.people 
            
            temp_matrix = copy.deepcopy(return_matrix)
            for i in range(n):
                for j in range(m):
                    neighbors = return_matrix.call_neighbors(i,j)
                    if M[i][j]==1 :
                        if ( sum(neighbors) == 2 ) or ( sum(neighbors) == 3 ) :
                            pass
                        else :
                            temp_matrix.people[i][j] = 0
                    elif M[i][j]== 0 :
                        if sum(neighbors) == 3 :
                            temp_matrix.people[i][j] = 1
 
            return_matrix = temp_matrix
            Displayer.display_element(temp_matrix)   
            return_matrix.n_repet -= 1
            