class Room:
    def __init__(self, room_num, total_pop, entry_fee):
        self.room_num = room_num
        self.total_pop = total_pop
        self.entry_fee = entry_fee
        self.room_pop = []
        self.song_queue = []
        self.tab = 0

    def increase_room_pop(self, guest):
        if len(self.room_pop) < self.total_pop:
            self.room_pop.append(guest)
            return len(self.room_pop)
        else:
            return "Room is full"

    def play_song(self, song_to_play):
        self.song_queue.append(song_to_play)

    def remove_guest_from_room(self, guest):
        self.room_pop.remove(guest)

    def next_song_in_queue(self):
        return self.song_queue[1]

    def sell_drink(self, price):
        self.tab += price