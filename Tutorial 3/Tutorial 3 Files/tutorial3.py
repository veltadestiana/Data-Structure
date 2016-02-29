# Data Structures & Algorithms
# Tutorial 3: Recursion
# Name: TODO Write your name here
# NPM: TODO Write your NPM here

class Dungeon:
    '''This class represents the layout of a dungeon.'''

    def __init__(self, width=1, height=1, dmap=None):
        if dmap is not None:
            self._dmap = dmap
        else:
            self._dmap = self._initDMap(width, height)

        # Think width as 'column' and height as 'row' in 2D array POV
        self._width = len(self._dmap[0])
        self._height = len(self._dmap)

        # Count the number of clues in the dungeon
        # This is the number of clues before being picked up by Wade
        self._clues = self._countClues()
    
    def get(self, row, col):
        '''Returns the element located at position (row,col) in the map.'''
        return self._dmap[row][col]

    def set(self, row, col, val):
        '''Sets the element at position (row,col) in the map.'''
        self._dmap[row][col] = val
    
    def getWidth(self):
        '''Returns the width of the map.'''
        return self._width

    def getHeight(self):
        '''Returns the height of the map.'''
        return self._height

    def getClues(self):
        '''Returns the number of clues in the map.'''
        return self._clues;

    def _countClues(self):
        '''Counts the number of clues in the map.'''
        # TODO Implement me!
        pass
    
    def _initDMap(self, width, height):
        dmap = [['.' for column in range(width)] for row in range(height)]
        return dmap

    def __str__(self):
        output = ''
        rows = len(self._dmap)

        for row in range(rows):
            cols = len(self._dmap[row])

            for col in range(cols):
                output = output + self._dmap[row][col]

            # Do not append new line at the last row's string representation
            if row < rows - 1:
                output = output + '\n'

        return output

class Wade:
    '''This class represents Wade the Dungeon Explorer.'''

    def __init__(self, dungeon):
        self._dungeon = dungeon
        self._startRow, self._startCol = self._initStartPosition()
        self._curRow, self._curCol = self._startRow, self._startCol
        self._foundClues = 0
    
    def getStartRow(self):
        return self._startRow

    def getStartCol(self):
        return self._startCol

    def getCurrentRow(self):
        return self._curRow

    def getCurrentCol(self):
        return self._curCol
    
    def explore(self, row, col):
        '''Makes Wade to explore given (row, col) position at the dungeon.'''
        # TODO Implement me!

        # (Base case)
        # Check if current position is out of boundary, a cell that 
        # has an obstacle, or a cell that has been visited
        # If true, then return immediately

        # (Explore current cell)
        # - Does Wade found a clue at current visited cell?
        # - Do not forget to keep track of cells that have been visited

        # (Recursive calls)
        # Move Wade to the rest of unvisited cells. The order is:
        # North - East - South - West
        pass

    def report(self):
        '''Prints the output as specified in the problem description.'''
        # TODO Implement me!

        # (Print first line of the output)
        # e.g.: Wade can explore all areas in Dungeons :)
        
        # (Print second line of the output)
        # e.g.: Clues obtained: 1 / 2
        pass
    
    def _initStartPosition(self):
        startRow, startCol = -1, -1
        for row in range(self._dungeon.getHeight()):
            for col in range(self._dungeon.getWidth()):
                if self._dungeon.get(row, col) is 'A':
                    startRow, startCol = row, col
                    break

        return startRow, startCol

def main():
    '''Main program. It reads the name of input file, then parses the content into dungeon representation. The implementation is left for tutorial exercise.'''

    # 1. Create 2D array
    # 2. Parse the input file and use the data to fill in the 2D array
    # 3. Create dungeon instance backed by the 2D array as the map
    # 4. Create Wade instance, pass the dungeon instance as the dungeon
    # that will be explored by Wade
    # 5. Start exploring from Wade's initial position
    # 6. Print the output

    file = input('Enter the name of the input file (e.g. 1.in, 2.in): ')
    f = open(file, 'r')

    # TODO Implement me!

    f.close()

if __name__ == '__main__':
    main()
