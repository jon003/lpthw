class Song(object):

  def __init__(self, lyrics):
    self.lyrics = lyrics
    
  def sing_me_a_song(self):
    for line in self.lyrics:
      print line
      
  def song_lines(self):
    return len(self.lyrics)
      
# create a song object, preload the lyrics with the variable passed to it.
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

# create another song object, preload the lyrics.                   
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
                        
# invoke the sing object's sing_me_a_song function.  the object already had
# the lyrics loaded into it.
happy_bday.sing_me_a_song()

# again.
bulls_on_parade.sing_me_a_song()

""" study drills """
# 1.
dumb_song = Song(["This song is short", "so I don't have to type", "more than 1 line"])
dumb_song.sing_me_a_song()

other_song_lyrics = ["one", "two", "three"]
other_song = Song(other_song_lyrics)
other_song.sing_me_a_song()
print "This song has %d lines." % other_song.song_lines()


