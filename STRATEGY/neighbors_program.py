from .game_of_life import GameOfLife 
import copy

class Neighbors(GameOfLife):
    def __init__(self,n_lignes,n_cols,n_repet,people_old):
        super().__init__(n_lignes,n_cols,n_repet)
        self.people  =  copy.deepcopy(people_old)

    def call_neighbors_first_rows(self,i,j):
        n,m,M = self.n_lignes,self.n_cols,self.people
        neighbors = []
        
        if i==0 :
            if j != m-1 :
                neighbors = [M[i][j+1],M[i+1][j],M[i+1][j+1]]
            if j !=0 :
                if j == m-1 :
                    l = [M[i][j-1],M[i+1][j],M[i+1][j-1]]
                else :
                    l = [M[i][j-1],M[i+1][j-1]]
                [neighbors.append(elt) for elt in l]
        else :
            raise "This not an element's first rows"
        return neighbors
    
    def call_neighbors_last_rows(self,i,j):
        n,m,M = self.n_lignes,self.n_cols,self.people
        neighbors = []
        
        if i==n-1 :
            if j != m-1 :
                neighbors = [M[i-1][j],M[i][j+1],M[i-1][j+1]]
            if j !=0 :
                if j == m-1 :
                    l = [M[i][j-1],M[i-1][j],M[i-1][j-1]]
                else :
                    l = [M[i][j-1],M[i-1][j-1]]
                [neighbors.append(elt) for elt in l]
        else :
            raise "This not an element's last rows"
        return neighbors
    
    def call_neighbors_between_first_and_last_rows(self,i,j):
        n,m,M = self.n_lignes,self.n_cols,self.people
        neighbors = [M[i-1][j],M[i+1][j]] # always up and down on ]n,m[
        
        if j == 0 :
            l = [M[i][j+1],M[i-1][j+1],M[i+1][j+1]]
            [neighbors.append(elt) for elt in l]
        elif j == m-1 :
            l = [M[i][j-1],M[i-1][j-1],M[i+1][j-1]]
            [neighbors.append(elt) for elt in l]
        else :
            l = [M[i][j+1],M[i-1][j+1],M[i+1][j+1],M[i][j-1],M[i-1][j-1],M[i+1][j-1]]
            [neighbors.append(elt) for elt in l]
        return neighbors
    
    def call_neighbors(self,i,j) -> list: #methode pour importer tous les voisins de l'élément Matrix[i][j]
        n,m,M = self.n_lignes,self.n_cols,self.people
        neighbors = []
        
        if i==0 : #first rows
            neighbors = self.call_neighbors_first_rows(i,j)
        elif i==n-1 : #last rows
            neighbors = self.call_neighbors_last_rows(i,j)
        else :
            neighbors = self.call_neighbors_between_first_and_last_rows(i,j)# always up and down on ]n,m[
            
        return neighbors
    
   

