
class Song:
    def __init__(self, lyrics=[]):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print("End of song")

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right here"])
happy_bday.sing_me_a_song()