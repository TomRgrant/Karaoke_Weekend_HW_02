class Guest:
    def __init__(self, first_name, last_name, wallet, fav_song, fav_song_artist):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet = wallet
        self.fav_song = fav_song, fav_song_artist

    def pay_entry_fee(self, entry_fee):
        if self.wallet >= entry_fee:
            self.wallet -= entry_fee
        else:
            return "Insufficient funds"

    def fav_song_playing(self, current_song):
        if current_song == self.fav_song:
            return "Whoo!"