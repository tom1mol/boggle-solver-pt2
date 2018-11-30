import unittest     #unittest framework uses classes and inherritance
                    #to create tests we create a class that iherrits from test case class and the framework
                    #then we write methods inside that class for the actual tests
import boggle
from string import ascii_uppercase      #26 uppercase characters A-Z
"""
class test_boggle(unittest.TestCase):       #class that inherrits from TestCase
    def test_is_this_thing_on(self):        #method..starts with test_
        self.assertEqual(1, 1)       #method assertEqual..method inherrited from test_case class. is 1 = 0? 1=1?
                                    #test command python3 -m unittest((in the command line))
"""
class TestBoggle(unittest.TestCase):
    #Our test suite for boggle solver
    
    
    def test_can_create_an_empty_grid(self):
        
        #Test to see if we can create an empty grid
        grid = boggle.make_grid(0,0)        ##(0,0) height/with or row/column. (0,0)=no rows or columns
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        
        #test to ensure total size of grid = width x height
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
        
    def test_grid_coordinates(self):
        
        #test 2 ensure all coordinates inside grid can be accessed
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)     #assertIn method to check if (0,0) is in a 2x2 grid
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)  #assertNot in to check (2,2) is not in a 2x2 grid
        
        
    def test_grid_is_filled_with_letters(self):
        
        #ensure that each of the coordinates in the grid contains letters
        
        grid = boggle.make_grid(2, 3)  #test creates grid and asserts every value in grid is uppercase
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
            
    def test_neighbours_of_a_position(self):
        
        #ensure that a position has 8 neighbours
        
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
        
    def test_all_grid_neighbours(self):
        
        #ensure that all grid positions have neighbours
        
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))    #assert correct length of neighbours dictionary
        for pos in grid:            #for loop will iterate through positions in the grid
            others = list(grid)     #creates a new list from dictionarys keys. full list
            others.remove(pos)      #minus position in question
            self.assertListEqual(sorted(neighbours[pos]), sorted(others)) # asserts position of neighbours is 
                                                                         #position being checked
                                                                         
    
    def test_converting_a_path_to_a_word(self):
    
        #ensure that paths can be converted to words
        #test checks that path to word function returns same strings we manually construct in the test
        grid = boggle.make_grid(2, 2)                       #turn list of positions into string of letters
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)]) #can access any leter in grip by its position
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
        
        
    def test_search_grid_for_words(self):
        
        #ensure that certain patterns can be found in a path_to_word
        #create mock grid so we can control the letters. `2x2  grid containing a,b,c,d
        grid = {(0, 0): 'A' , (0, 1): 'B' , (1, 0): 'C' , (1, 1): 'D' }
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
        
    def test_load_dictionary(self):
        
        #test that the 'get_dictionary' function returns a dictionary that has a length > 0
        
        dictionary = boggle.get_dictionary('words.txt') #create new file in boggle project called words.txt
        self.assertGreater(len(dictionary), 0)
        
        
        
        
        
        
        