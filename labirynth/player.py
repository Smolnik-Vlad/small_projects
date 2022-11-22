from imports import *
from room_door import Room

class Player (Room):
    def __init__(self, name, current_room):
        self.player_name = name
        self.current_room: Room = current_room

    def go_to_room(self):
        choose_room=int(input("Choose a room to go to: "))
        print(self.current_room._doors[choose_room])
        self.current_room = self.current_room._doors[choose_room].go_to_room(self.current_room)

        #_doors[choose_room].go_to_room(self)

    def play_the_game(self):
        while True:
            print(f"{self.player_name}, you are in the room {self.current_room.name}")
            print(f"Choose the action: 1. Look around 2. Go to the door: ")
            choose_action = int(input())
            if choose_action == 1:
                print(self.current_room.names_of_all_doors())
            elif choose_action == 2:
                self.go_to_room()
                if self.current_room._finish == True:
                    print("Вы выйшли из лабиринта")
                    return
