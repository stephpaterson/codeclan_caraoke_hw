class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.songs = []
        self.guests = []
        self.capacity = capacity
        self.entry_fee = 10
        self.till = 100

    def add_song_to_room(self, song_name):
        self.songs.append(song_name)

    def add_individual_guest_to_room(self, guest):
        if not self.capacity_check():
            self.guests.append(guest)

    def remove_all_guests_from_room(self):
        self.guests.clear()

    def remove_guest_by_name(self, guest_name):
        self.guests.remove(guest_name)

    def capacity_check(self):
        if len(self.guests) >= 6:
            return "Sorry, room full"
       
    def add_money_to_till(self):
        self.till += self.entry_fee
    
    def take_entry_fee_from_guest(self, guest):
        guest.remove_money_from_wallet(self.entry_fee)
        self.add_money_to_till()
