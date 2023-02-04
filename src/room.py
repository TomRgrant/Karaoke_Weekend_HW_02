class Room:
    def __init__(self, room_num, total_pop, entry_fee):
        self.room_num = room_num
        self.total_pop = total_pop
        self.entry_fee = entry_fee
        self.room_pop = []
        self.current_song = ''

    def increase_room_pop(self, guest):
        if len(self.room_pop) < self.total_pop:
            self.room_pop.append(guest)
            return len(self.room_pop)
        else:
            return "Room is full"

    def play_song(self, song_to_play):
        self.current_song = song_to_play