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
        if gi_chara.age <= 19 and gi_chara > 12:
            return print("This character is a teenager.")
        elif gi_chara.age <= 12:
            return print("This character is a child.")
        elif gi_chara.age > 19:
            return print("This character is an adult.")
        else:
            return print("Invalid inputted age.")