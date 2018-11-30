import os               #this was added for challenge 
from string import ascii_uppercase
from random import choice

SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__)) #this was added for challenge

def make_grid(width, height):
    
    #create a grid that will hold all the tiles for a boggle game
    #this function creates a dictionary with a row/column tupple as the key and a space as the value
    return {(row, col): choice(ascii_uppercase)     #choice(ascii_uppercase) replaced ' ' which was blank space
        for row in range(height)
        for col in range(width)
}

def neighbours_of_position(coords):
                                                                  # x = row, y = column
    #get neighbours of a given position                           #  <-1,-1> <-1,0> <-1,+1>
                                                                  #  < 0,-1> <0, 0> <0, +1>
    row = coords[0]                                               #  <+1,-1> <+1,0> <+1,+1>           
    col = coords[1]
    
    #assign each of the neighbours
    #top left to top right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col )
    top_right = (row - 1, col + 1)
    
    #left to right
    left = (row, col - 1)
    #the (row,col) coordinates passed to this 
    #function are situated here
    right = (row, col + 1)
    
    #bottom left to bottom right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)

    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]


def all_grid_neighbours(grid):
    
    #get all posible neighbours for each position in the grid
    
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
        
    return neighbours
    
    
def path_to_word(grid, path):
    
    #add all of the letters on the path to a string
    
    return ''.join([grid[p] for p in path]) #gets list of letters from position in path and joins them imto a string


def search(grid, dictionary):    #function that accepts a grid and a dictionary
    
    #search through the paths to locate words by matching strings to words in a dictionary
    
    neighbours = all_grid_neighbours(grid)  #1st get neighbours of every position in the grid
    paths = []                              #then get paths list to capture all paths that form valid words
#store words as paths rather than strings to distinguish between letters. by location. could be 2 A's in the grid

    #this function is nested inside main search function.cant be called directly
    #has access to other variables within search function(eg paths list..which it can add to)
    #do_search function can be called by the search function and can call itself recursively to build up paths
    #search func starts a search by passing a single position to the do_search. this is a path of 1 letter
    #do_search function converts whatever path its given into a word and checks if is in dictionary
    #if path makes a word its added to the paths list. whether the path is a word or not..do_search gets 
    #each of the neighbours of the last letter,checks to make sure neighbouring letter isnt already 
    #in the path and then continues the searching from that letter
    #do_search could call itself 8 times for each starting position and again for each of the various neighbours
    #of each neighbour and so on.
    def do_search(path): 
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)    

#for each position in the grid we do a search and convert all the paths to make valid words and return them in a list
#



def get_dictionary(dictionary_file):
    
    #load dictionary file
    
    if not dictionary_file.startswith('/'):                         #added this for challenge 2x2
        #if not absolute, then make path relative to our location
        dictionary_file = os.path.join(SCRIPT_PATH, dictionary_file)    #added this for challenge 2x2
    
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]
        
def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
    
def main():
    #this is the function that will run the whole project
    
    grid = make_grid(2, 2)  #change here from (3,3) to (2,2) to check runtimes
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    # for word in words:        this was inserted into function display_words above
    #     print(word)
    # print("Found %s words" % len(words))
    
    display_words(words)
    
if __name__ == "__main__":  #to avoid running code when file is imported we use this if statement
                            #code within this statement will only execute when the file is run directly
    main()
    
    
    