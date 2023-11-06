class hsr_chara:
    def __init__(self, name, path, age, is_dead):
        self.name = name
        self.path = path
        self.age = age
        self.is_dead = is_dead

class gi_chara:
    def __init__(self, name, element, weapon, age):
        self.name = name
        self.element = element
        self.weapon = weapon
        self.age = age

    def age_range(self):
        if self.age <= 19 and self.age > 12:
            return print("This character is a teenager.")
        elif self.age <= 12:
            return print("This character is a child.")
        elif self.age > 19:
            return print("This character is an adult.")
        else:
            return print("Invalid inputted age.")