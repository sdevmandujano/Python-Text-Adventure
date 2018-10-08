import enemies
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You wake up from a bed that its not yours, in a unknown room.
        You can make out four black doors, each leading to a different direction.
        """

class TextTile(MapTile):
    def intro_text(self):
        return """
        You find something.....an old newspaper article. it reads:

        "Jury finds William Napier guilty of first-degree"

"It took a jury only four hours of deliberation to return a guilty verdict against William Napier
 at the Brahms Courthouse this afternoon. Napier, 42, had been accused of abducting, and murdering Rachel Stephens, 
 an 16-year-old local girl whose parents had reported her missing in January of last year. 
 Napier misteriously vanished after the hearing......" 
        """

class UnknownTile(MapTile):
    def intro_text(self):
        return """

        A Missing Poster is placed on the wall....
        
        Ariadne Johnson

        DOB: January 6th, 1996

        Height: 4' 2"

        Eyes: Brown

        Race: Caucasian

        Age: 8

        Sex: Female

        Weight: 48 lbs

        Hair: Dark Brown

        Ariadne was last seen on April 11, around 2:15pm while walking home from the Hillside Middle School. 
        She suffers from severe autism and is prone to wandering away from home. She follows a fixed route home 
        from her bus stop, marked by a series of colored ribbons placed by her mother. Ariadne has a strong aversion 
        to the color blue and has been known to alter her route to avoid the color.

        Anyone having information should contact the Maine Police Department's missing persons hotline.

        1-800-555-LOST

        """
class SomethingTile(MapTile):
    def intro_text(self):
        return """
        You hear whispers........ something lays ahead.
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.AbstractFigure()
            self.alive_text = """
            A figure comes from out of nowhere,
                              its in front of you now!
                              """
            self.dead_text = """
            The corpse rots on the ground.
            """
        elif r < 0.80:
            self.enemy = enemies.FacelessMan()
            self.alive_text = """
            A Faceless Man is blocking your path!
            """
            self.dead_text = """
            A body and a pool of blood lays on the floor.
            """
        elif r < 0.95:
            self.enemy = enemies.Mannequin()
            self.alive_text = """
            You hear a squeaking noise growing louder
                              ...suddenly a mannequin strikes at you!
                              """
            self.dead_text = """
            A bleeding mannequin.......
            """
        else:
            self.enemy = enemies.TorturedMan()
            self.alive_text = """
            A disfigured man is yelling 
                              kill me....end my suffering!
                              """
            self.dead_text = """
            The disfigured man rests in peace.
             """ 
                             

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("""
            Enemy does {} damage. You have {} HP remaining.
            """.
                  format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! 


            Time to wake up again.....
        """


world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |EN|  |EN|
|EN|SS|TT|UT|EN|
|EN|EN|ST|EN|EN|
|EN|  |EN|  |EN|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "EN": EnemyTile,
                  "TT": TextTile,
                  "UT": UnknownTile,
                  "SS": SomethingTile,
                  "EN": EnemyTile,
                  "  ": None}


world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
