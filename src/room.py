class Room:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guests = []

    def add_song_to_room(self, song_name):
        self.songs.append(song_name)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_all_guests_from_room(self):
        self.guests.clear()

    def remove_guest_by_name(self, guest_name):
        self.guests.remove(guest_name)