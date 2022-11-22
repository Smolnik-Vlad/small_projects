from room_door import Room
from player import Player

class Create_and_Play():
    def __init__(self):
        print("Добро пожаловать в игру лабиринт. Игрок будет двигаться по лабиринту, переходя из комнаты в комнату, пока"
              " не найдет выход. После первого прохождения вы сможете задать лабиринт по желанию заново. А сейчас это "
              " необходимо.")

        current_room = Room(name="Start")
        current_room.create_labyrinth()
        player_name = input("Имя игрока: ")
        Player(player_name, current_room).play_the_game()

Create_and_Play()