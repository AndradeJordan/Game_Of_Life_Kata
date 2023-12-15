class Displayer :
    Compteur = 1
    @staticmethod
    def display_element(matrix):
        print("Cycle iteration:",Displayer.Compteur)
        print(matrix.people)
        print(f"\n  Number of cycles remaining : {matrix.n_repet-1}")
        Displayer.Compteur +=1
        