import unittest
from montecarlo import Die,Game,Analyzer
import numpy as np
import pandas as pd

class monteCarloTestSuite(unittest.TestCase):
    
    def test_1_roll_dice(self):

        a = np.array([1,2,3,4,5,6])
        test = []
        die1 = Die(a)
        ans = die1.roll_dice()
        self.assertTrue(type(ans)==type(test))


    def test_2_change_weights(self):
         
         a = np.array([1,2,3,4,5,6])
         die1 = Die(a)
         die1.change_weights(2,2)
         test = 2
         ans = die1.show_die().iloc[1].item()
         self.assertTrue(ans,test)

    def test_3_show_die(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        test = die1.show_die()
        ans = pd.DataFrame()
        self.assertTrue(type(ans) == type(test))
       

    def test_4_play(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        game.play(5)
        answer = 5
        test = len(game.show_results())
        self.assertEqual(answer,test)

    def test_5_show_results(self):
        
        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        game.play(5)
        ans = pd.DataFrame()
        test = game.show_results()
        self.assertTrue(type(test)==type(ans))
              
    def test_6_jackpot(self): 
       
       a = np.array([1,2,3,4,5,6])
       die1 = Die(a)
       die2 = Die(a)
       list = [die1,die2]
       game = Game(list)
       game.play(5)
       analyzer = Analyzer(game)
       a = 8
       b = analyzer.jackpot()
       self.assertTrue(type(a)==type(b)) 

    def test_7_combo_count(self): 
       
       a = np.array([1,2,3,4,5,6])
       die1 = Die(a)
       die2 = Die(a)
       list = [die1,die2]
       game = Game(list)
       game.play(5)
       analyzer = Analyzer(game)
       ans = pd.DataFrame()
       test = analyzer.combo_count()
       self.assertTrue(type(test)==type(ans))

    def test_8_permu_count(self): 

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        game.play(5)
        analyzer = Analyzer(game)
        ans = pd.DataFrame()
        test = analyzer.permu_count()
        self.assertTrue(type(test)==type(ans))

    def test_9_face_counts(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        game.play(5)
        analyzer = Analyzer(game)
        ans = pd.DataFrame()
        test = analyzer.face_counts()
        self.assertTrue(type(test)==type(ans))

    def test_10_die_object(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        self.assertTrue(type(die1)==Die)

    def test_11_game_object(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        self.assertTrue(type(game)==Game)

    def test_12_analyzer_object(self):

        a = np.array([1,2,3,4,5,6])
        die1 = Die(a)
        die2 = Die(a)
        list = [die1,die2]
        game = Game(list)
        game.play(5)
        analyzer = Analyzer(game)
        self.assertTrue(type(analyzer)==Analyzer)

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
