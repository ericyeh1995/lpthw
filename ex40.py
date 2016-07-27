class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def print_length(self):
        length = 0
        for line in self.lyrics:
            length += len(line)
        print length

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

love_story = Song(["You'll be the price",
                   "and I don't want to get sued either"])

happy_bday.sing_me_a_song()
happy_bday.print_length()

bulls_on_parade.sing_me_a_song()

love_story.sing_me_a_song()
love_story.print_length()
