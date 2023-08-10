import numpy as np
import pandas as pd
import random


class Die():
    '''
    This is a class to model a generalized n-sided 'die'. It can be a two sided coin, a 6 sided die, a deck of cards, etc.

    Attributes
    -----------
    sides: a numpy array of the sides of the generalised die. 

    Methods
    ------------
    roll_dice(): Intiializes a Die object. Takes a NumPy Array as a parameter. Default weights are 1 for every face
    change_weights(): A function to change one weight of the generalized die. Takes two arguments: the side to be changed, and the new weight
    show_die(): Function to return the copy of the die dataframe showing sides and weights
    
    '''
    
    def __init__(self,sides):
        ''' Intiializes a Die object. Takes a NumPy Array as a parameter. Default weights are 1 for every face'''

        if type(sides) == type(np.array([0])):
            if len(sides) == len(np.unique(sides)):
                self.sides=len(sides)
                self._weight= pd.DataFrame({"side": [i for i in sides],
                                            "weights": [1 for i in sides],
                                            })
                
                self._die = self._weight.set_index('side')
                                    
            else: raise ValueError("Values must be distinct")
        else: raise TypeError("Input must be a Numpy Array")

    def roll_dice(self,n_rolls=1):
        '''a function to roll the generalized die. Takes an argument n_rolls and returns a list of the output'''

        for i in range(n_rolls):
            result = random.choices(self._die.index,k=n_rolls,weights = self._die.weights)
            
        return result
    
    def change_weights(self,side,new_weight:int):
        '''A function to change one weight of the generalized die. Takes two arguments: the side to be changed, and the new weight'''

        if side in self._die.index:
            self._die.loc[side] = new_weight
        else: raise IndexError("Side Not Found")
        

    def show_die(self):
        '''Function to return the copy of the die dataframe showing sides and weights'''
        
        return self._die.copy(deep=True)
    
    



class Game():
    ''' 
    Class to simulate a monte carlo game. Takes in a list of generalized Die objects 

    Attributes
    -------------
    dice: list of die objects. Must be list data type


    Methods
    ------------
    play(): method to play a game for a given number of trials
    show_results(): method to show results of the game
    '''
    
    def __init__(self,list_of_dice:list):
        ''' 
        Initializes a Game object. Takes a list of Die objects as a parameter
        
        Inputs
        -----------
        list_of_dice = list of Die objects. Must be list. No default value
    
        '''
        
        if type(list_of_dice) == type([]):
            self.dice = list_of_dice
            self._results = []
        else: raise TypeError("Value must be a list")

    def play(self,trials:int):
        '''
        Method to play a game for a given number of trials

        Inputs
        -------
        trials: integer of how many rolls each die will be rolled.

        Stores results in object attribute and returns a copy
        '''

        gameResults = {f'Die{i+1}': die.roll_dice(trials) for i,die in enumerate(self.dice)}
        self._results = pd.DataFrame(gameResults)   
        return self._results.copy(deep=True)

    def show_results(self, format="wide"):
        '''
        Method to show results of the game. Returns a dataframe of the results
        
        Input
        -------
        format: str value. Can be wide or narrow. 

        Returns a dataframe of the game results
        '''
        
        if type(format) == str:
            if format.lower() == "wide":
                return self._results.copy()
            elif format.lower() == "narrow":
                return self._results.copy().melt(ignore_index=False).rename_axis("Roll",axis=0).rename({"variable":"Die","value":"Value"},axis=1).reset_index().set_index(["Roll","Die"])
            else: raise ValueError("Please select Wide or Narrow for format")
        else: raise TypeError("Value must be a string")

class Analyzer():
    ''' 
    Initializes an Analyzer object

    Attributes
    --------------
    game: the game object passed into the init
    data: the results of the game object to be analyzed

    Methods
    --------------
    jackpot(): returns the number of jackpots, where jackpot is defined as the same face for all die cast in the same roll. All 1's, for example.
    face_counts(): returns a dataframe of each face count present per roll
    combo_count(): Computes the distinct combinations for each game and stores it in a dataframe
    permu_count(): Computes the distinct permutations for each game and stores it in a dataframe
    
    '''
    def __init__(self,gameObject):
        ''' 
        Initializes an Analyzer object. Takes a single Game object as a parameter
        
        Input: a Game object. Must be a game object.
        '''

        if not isinstance(gameObject,Game):
            raise TypeError("Must take a Game Object")
        
        self.game = gameObject
        self.data = self.game.show_results()

    def jackpot(self):
        '''
        Returns the number of jackpots in a given game. Jackpot is defined as all 1's on a roll, for example.

        '''

        data = self.game.show_results()
        jackpot_counter = 0
        
        for index in data.index:
            if len(data.iloc[index].value_counts()) == 1:
                jackpot_counter += 1
        return jackpot_counter

    def face_counts(self):
        '''Computes how many times a given face is rolled in each event. Returns a dataframe of results'''
        
        lists = [self.data.iloc[row].value_counts().reset_index() for row in self.data.index]
        final = pd.concat(lists,axis=0).groupby("index").sum().T
    
        return final

    def combo_count(self):
        '''Computes distinct combinations of faces rolled along with their counts. Returns a dataframe of results'''
        
        sort = np.sort(self.data.values,axis=1)
        df =  pd.DataFrame(sort,columns = self.data.columns).value_counts()
        return df

    def permu_count(self):
        '''Computes distinct permutations of faces rolled along with their counts. Returns a dataframe of results'''

        return self.data.value_counts().to_frame()
    

