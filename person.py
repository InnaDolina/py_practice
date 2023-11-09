import random


class Person:
    def __init__(self, first_name, last_name, health, status):
        """Initialize attributes to be used in/available for all class methods in this class, and for class objects
        created by this class."""

        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves."""
        print("Hello, my name is {} {}.".format(self.first_name, self.last_name))

    def emotion(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy".format(self.first_name))
        elif emotion == 2:
            print("{} is sad right now".format(self.first_name))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.first_name))
        elif self.health >= 76:
            print("{} is a bit tired today.".format(self.first_name))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.first_name))
        elif self.health >= 40:
            print("{} goes to see a doctor.".format(self.first_name))
        else:
            print("{} is unconscious.".format(self.first_name))


Maria = Person("Maria", "Guttierez", 95, status=True)
Olga = Person("Olga", "Pugatsiova", 52, status=False)
Lee = Person("Lee", "Joe", 38, status=True)

people = [Maria, Olga, Lee]

for person in people:
    print("{} is my friend? {}".format(person.first_name, person.status))

Maria.introduce()
Maria.status_change()
Olga.introduce()
Olga.status_change()
Lee.introduce()
Lee.status_change()


# inheritance example
class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "knife":
            other.health -= 15
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak!".format(other.first_name))

    def steal(self, other):
        print("Ha ha ha, I have your stuff {}!".format(other.first_name))
        if other.status == True:
            other.status = False


Alex = Enemy("rock", "Alex", "Wayne", 75, status=False)
Alex.hurt(Maria)
Alex.insult(Maria)
Alex.insult(Lee)
Alex.steal(Lee)
Alex.introduce()
