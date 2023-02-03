class Room:
    def __init__(self, room_num, total_pop, entry_fee):
        self.room_num = room_num
        self.total_pop = total_pop
        self.entry_fee = entry_fee
        self.room_pop = []

    def increase_room_pop(self, guest):
        if len(self.room_pop) < self.total_pop:
            self.room_pop.append(guest)