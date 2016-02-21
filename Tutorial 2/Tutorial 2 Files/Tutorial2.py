# Data Structures & Algorithms
# Tutorial 2: Abstract Data Type
# Name: TODO Write your name here
# NPM: TODO Write your NPM here

# TODO list:
# 1. Implement the Track class by assigning track attributes
#    on the __init__ method.
# 2. Complete the Playlist class by implementing the class
#    methods so that they perform their respective operations.
# 3. Done

class Track:
    def __init__(self, title, artist, genre, is_fav):
        # TODO Implement me!
        pass


class Playlist:
    def __init__(self, queue=None):
        if not queue:
            queue = []
        self.queue = queue

    def add(self, track=None):
        # TODO Implement me!
        pass

    def delete_title(self, title):
        # TODO Implement me!
        pass

    def delete_position(self, pos):
        # TODO Implement me!
        pass

    def move(self, n, m):
        # TODO Implement me!
        pass

    def count_genre(self, genre):
        # TODO Implement me!
        pass

    def count_favourite(self):
        # TODO Implement me!
        pass

    def print_playlist(self):
        # TODO Implement me!
        pass


def main():
    """
    Main function to run the program. Instantiates a Playlist object,
    opens test case files and parses each line as an operation on the
    playlist object.
    """

    for i in range(1, 4):
        print("\nSAMPLE INPUT {}".format(i))

        playlist = Playlist()

        filename = "testinput{}.txt".format(i)

        with open(filename, 'r') as testfile:
            operation_list = testfile.read().splitlines()

        for line in operation_list:
            operation = line.split(',')
            op_type = operation[0]
            if op_type == 'ADD':
                title, artist, genre, is_fav = operation[1:]
                playlist.add(Track(title, artist, genre, is_fav))
            elif op_type == 'DELTITLE':
                title = operation[1]
                playlist.delete_title(title)
            elif op_type == 'DELPOS':
                position = int(operation[1])
                playlist.delete_position(position)
            elif op_type == 'MOVE':
                old_pos, new_pos = int(operation[1]), int(operation[2])
                playlist.move(old_pos, new_pos)
            elif op_type == 'COUNTGENRE':
                genre = operation[1]
                playlist.count_genre(genre)
            elif op_type == 'COUNTFAV':
                playlist.count_favourite()
            elif op_type == 'PRINT':
                playlist.print_playlist()


# Runs the program if executed via command prompt
if __name__ == '__main__':
    main()
