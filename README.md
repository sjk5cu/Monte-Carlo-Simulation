# sjk5cu_ds5100_montecarlo
Final Project

## montecarlo

In this simulator, a “die” can be any discrete random variable associated with a stochastic process, such as using a deck of card, flipping a coin, rolling an actual die, or speaking a language.

## Installation

Use package installer pip to install

```bash
pip install montecarlo
```

## Usage (Die Class)

```python
from montecarlo.montecarlo import Die, Game, Analyzer

#Create an array of faces to pass to Die object
a = np.array([1,2,3,4,5,6])
die1 = Die(a)

#Roll Die, number of rolls defaults to 1
die1.roll_dice()

#Change Weights of a Face
die1.change_weights(6,2)

#Return a dataframe showing die faces and weights
die1.show_die()
```

## Usage (Game Class)


```python

# Call a game Object
game = Game([die1,die1])

#Play a game
game.play(1000)

#Show results of the game
game.show_results()
```

## Usage (Analyzer Class)

```python

#Create an Analyzer object
analyzer = analyzer(game)


#Jackpot Counter
analyzer.jackpot()

#Count the number of faces that showed each roll
analyzer.face_counts()

#Compute the number of combinations
analyzer.combo_counts()

#Computer the number of permutations
analyzer.permu_count()
```

## Docstrings

```python
help(Die)
```
```python
Help on class Die in module montecarlo.montecarlo:

class Die(builtins.object)
 |  Die(sides)
 |  
 |  This is a class to model a generalized n-sided 'die'. It can be a two sided coin, a 6 sided die, a deck of cards, etc.
 |  
 |  Attributes
 |  -----------
 |  sides: a numpy array of the sides of the generalised die. 
 |  
 |  Methods
 |  ------------
 |  roll_dice(): Intiializes a Die object. Takes a NumPy Array as a parameter. Default weights are 1 for every face
 |  change_weights(): A function to change one weight of the generalized die. Takes two arguments: the side to be changed, and the new weight
 |  show_die(): Function to return the copy of the die dataframe showing sides and weights
 |  
 |  Methods defined here:
 |  
 |  __init__(self, sides)
 |      Intiializes a Die object. Takes a NumPy Array as a parameter. Default weights are 1 for every face
 |  
 |  change_weights(self, side, new_weight: int)
 |      A function to change one weight of the generalized die. Takes two arguments: the side to be changed, and the new weight
 |  
 |  roll_dice(self, n_rolls=1)
 |      a function to roll the generalized die. Takes an argument n_rolls and returns a list of the output
 |  
 |  show_die(self)
 |      Function to return the copy of the die dataframe showing sides and weights
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```
```python
help(Game)
```

```python
Help on class Game in module montecarlo.montecarlo:

class Game(builtins.object)
 |  Game(list_of_dice: list)
 |  
 |  Class to simulate a monte carlo game. Takes in a list of generalized Die objects 
 |  
 |  Attributes
 |  -------------
 |  dice: list of die objects. Must be list data type
 |  
 |  
 |  Methods
 |  ------------
 |  play(): method to play a game for a given number of trials
 |  show_results(): method to show results of the game
 |  
 |  Methods defined here:
 |  
 |  __init__(self, list_of_dice: list)
 |      Initializes a Game object. Takes a list of Die objects as a parameter
 |      
 |      Inputs
 |      -----------
 |      list_of_dice = list of Die objects. Must be list. No default value
 |  
 |  play(self, trials: int)
 |      Method to play a game for a given number of trials
 |      
 |      Inputs
 |      -------
 |      trials: integer of how many rolls each die will be rolled.
 |      
 |      Stores results in object attribute and returns a copy
 |  
 |  show_results(self, format='wide')
 |      Method to show results of the game. Returns a dataframe of the results
 |      
 |      Input
 |      -------
 |      format: str value. Can be wide or narrow. 
 |      
 |      Returns a dataframe of the game results
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

```
```python
help(Analyzer)
```
```python
Help on class Analyzer in module montecarlo.montecarlo:

class Analyzer(builtins.object)
 |  Analyzer(gameObject)
 |  
 |  Initializes an Analyzer object
 |  
 |  Attributes
 |  --------------
 |  game: the game object passed into the init
 |  data: the results of the game object to be analyzed
 |  
 |  Methods
 |  --------------
 |  jackpot(): returns the number of jackpots, where jackpot is defined as the same face for all die cast in the same roll. All 1's, for example.
 |  face_counts(): returns a dataframe of each face count present per roll
 |  combo_count(): Computes the distinct combinations for each game and stores it in a dataframe
 |  permu_count(): Computes the distinct permutations for each game and stores it in a dataframe
 |  
 |  Methods defined here:
 |  
 |  __init__(self, gameObject)
 |      Initializes an Analyzer object. Takes a single Game object as a parameter
 |      
 |      Input: a Game object. Must be a game object.
 |  
 |  combo_count(self)
 |      Computes distinct combinations of faces rolled along with their counts. Returns a dataframe of results
 |  
 |  face_counts(self)
 |      Computes how many times a given face is rolled in each event. Returns a dataframe of results
 |  
 |  jackpot(self)
 |      Returns the number of jackpots in a given game. Jackpot is defined as all 1's on a roll, for example.
 |  
 |  permu_count(self)
 |      Computes distinct permutations of faces rolled along with their counts. Returns a dataframe of results
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```









