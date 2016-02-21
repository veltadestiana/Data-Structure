# Data Structures & Algorithms
# Tutorial 2: Abstract Data Type
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


class Track:
    def __init__(self, title, artist, genre, is_fav):
        # TODO Implement me!
        self.title = title
        self.artist = artist
        self.genre = genre
        self.is_fav = True if is_fav == 'True' else False


class Playlist:
    def __init__(self, queue=None):
        if not queue:
            queue = []
        self.queue = queue

    def add(self, track=None):
        # TODO Implement me!
        if track in self.queue:
            print("{} - {} already in playlist.".format(track.artist, track.title))
            return False
        self.queue.append(track)
        print("{} - {} added to playlist.".format(track.artist, track.title))
        return True

    def delete_title(self, title):
        # TODO Implement me!
        for track in self.queue:
            if track.title == title:
                print("{} - {} deleted from playlist.".format(track.artist, track.title))
                del track
                return True
        print("{} not found in playlist.".format(title))
        return False

    def delete_position(self, pos):
        # TODO Implement me!
        if pos in range(1, len(self.queue)+1):
            del self.queue[pos-1]
            print("Track {} deleted from playlist.".format(pos))
            return True
        else:
            print("Cannot delete track at position {}.".format(pos))
            return False

    def move(self, n, m):
        # TODO Implement me!
        if n in range(1, len(self.queue)+1) and m in range(1, len(self.queue)+1):
            self.queue.insert(m-1, self.queue.pop(n-1))
            print("{} moved into position {}.".format(self.queue[m-1].title, m))
        else:
            print("Invalid track position.")
        return True

    def count_genre(self, genre):
        # TODO Implement me!
        count = 0
        for track in self.queue:
            if track.genre == genre:
                count += 1
        print("Number of {} tracks: {}".format(genre, count))

    def count_favourite(self):
        # TODO Implement me!
        count = 0
        for track in self.queue:
            if track.is_fav is True:
                count += 1
        print("Number of favourited tracks: {}".format(count))

    def print_playlist(self):
        # TODO Implement me!
        for track in self.queue:
            print("{} - {}".format(track.artist, track.title))


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
