class Guest:
    
    def __init__(self, name, wallet, favourite_song, favourite_artist):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.favourite_artist = favourite_artist


    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def favourite_song_playing(self, song_list):
        for song in song_list:
            if song.name == self.favourite_song:
                return "This is my favourite song!"
            else:
                return False
    
    def favourite_artist_playing(self, song_list):
        for song in song_list:
            if song.artist == self.favourite_artist:
                return f"I love {song.artist}!"
            else:
                return f"I hate {song.artist}"
