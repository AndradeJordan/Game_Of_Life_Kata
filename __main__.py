
from STRATEGY.game_of_life import GameOfLife
from STRATEGY.strategie_of_game_of_life import StrategieGameOfLife

def main():
    jeu = GameOfLife(5,5,2)
    jeu.description()
    st = StrategieGameOfLife(jeu)
    st.strategie
    
if __name__ == '__main__':
    main()
