from imports import *
#from doors import Doors



class Room:
    def __init__(self, name):
        self.name: str = name
        self._doors: List[Doors] = []

        # if previous_room is not None:
        #     self.__doors.append(previous_room)
        self._finish = False
    def names_of_all_doors(self) -> Dict[int, str]: #get the list of doors in the room
        list_of_doors = []
        for i in self._doors:
            if list(i.room_1.values())[0] != self.name:
                list_of_doors.append(list(i.room_1.values())[0])
            else:
                list_of_doors.append(list(i.room_2.values())[0])

        return dict(enumerate(list_of_doors))

    def create_labyrinth(self):
        while True:
            print(f"Вы находитесь в комнате {self.name}, что бы вы хотели сделать?:\n1. Добавить новую дверь в данную комнату"
                  f"\n2. Перейти в другую комнату\n3. Выйти из редактора лабиринта и сделать текущую комнату финишем"
                  f"\n4. Просмотреть все комнаты: ")
            choose = int(input())
            if choose == 1:
                self._doors.append(Doors(self, Room(input("Введите название комнаты: ")))) #добавить дверь обратно
            elif choose == 2:
                if len(self._doors)!=0:
                    print(self.names_of_all_doors())
                    choose_the_door=int(input())
                    self._doors[choose_the_door].go_to_room(self).create_labyrinth()
                    return
                else: print("Ни одной двери не создано! ")
                pass
            elif choose == 3:
                self._finish = True
                return
            elif choose == 4:
                print(self.names_of_all_doors())


class Doors:
    def __init__(self, room_1: Room, room_2: Room):
        self.room_1: Dict[Room, str] = {room_1 : room_1.name}
        self.room_2: Dict[Room, str] = {room_2 : room_2.name}
        room_2._doors.append(self)

    def go_to_room(self, current_room: Room)->Room:
        return list(self.room_1.keys())[0]  if current_room!=list(self.room_1.keys())[0] else list(self.room_2.keys())[0]


