class Guest:
    def __init__(self, first_name, last_name, wallet, fav_song):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet = wallet
        self.fav_song = fav_song

    def pay_entry_fee(self, entry_fee):
        if self.wallet >= entry_fee:
            self.wallet -= entry_fee
        else:
            return "Insufficient funds"

    def fav_song_playing(self, current_song):
        if current_song == self.fav_song:
            return "Whoo!"

    def reduce_wallet(self, price):
        if self.wallet >= price:
            self.wallet -= price

    def buy_drink(self, price):
        self.reduce_wallet(price)

