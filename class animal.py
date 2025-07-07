from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class human(animal):

    def move(self):
        print("I can walk and run lol")

class snake(animal):

    def move(self):
        print("I can slide.")

class elephant(animal):

    def move(self):
        print("I can trumpet and stampede")

class peacock(animal):

    def move(self):
        print("Can't fly but I have nice feathers.")


# after creation of all the classes, call them w the driver function

p = human()
p.move()

s = snake()
s.move()

y = elephant()
y.move()

k = peacock()
k.move()
