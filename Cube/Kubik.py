import random


class Cube:
    i=1
    def __init__(self, amount=6):

        self.number=self.__class__.i
        self.amount=amount
        self.__class__.i+=1

    def throw(self):
        return random.randint(1, self.amount)


class List_of_cubes:
    def __init__(self):
        self.cubes = list()

    def add_cubes(self, *new_cube):
        self.a=list(new_cube)
        self.cubes.extend(new_cube)

    def select_to_throw(self):
        print("Выберите кубики: ")
        for i in self.cubes:
            print(f"{i.number}: {i.amount}")

        selection=list(map(int, input().split(', ')))

        for i in self.cubes:
            if i.number in selection:
                yield i.throw()


a1=Cube(10)
a2=Cube(4)
a3=Cube(5)
a4=Cube()

cubes=List_of_cubes()
cubes.add_cubes(a1, a2)
cubes.add_cubes(a3, a4)
list_of_values=list(cubes.select_to_throw())
print(list_of_values)



