class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class AbstractFigure(Enemy):
    def __init__(self):
        self.name = "Abstract Figure"
        self.hp = 10
        self.damage = 2


class FacelessMan(Enemy):
    def __init__(self):
        self.name = "Faceless Man"
        self.hp = 30
        self.damage = 10


class Mannequin(Enemy):
    def __init__(self):
        self.name = "Mannequin"
        self.hp = 100
        self.damage = 4


class TorturedMan(Enemy):
    def __init__(self):
        self.name = "Tortured Man"
        self.hp = 80
        self.damage = 15
