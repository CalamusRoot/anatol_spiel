import Game_Character


class Player(Game_Character):
    def __init__(self):
        self.name = "b"
        self.hp = 100
       
        # self.xp = 0
        # self.dmg = 1
        # self.defense = 1
        # self.location_x = 0
        # self.location_y = 0
        
        
hans = Player()

print(hans.name)
 
        

    # def am_leben(self):
    #     return self.hp > 0
    #
    # def zeige_inventar(self):
    #     for item in self.iventar:
    #         print(item, '\n')
    #
    # def get_name(self):
    #     return self.name
    #
    # def bewege(self, dx, dy):
    #     self.location_x += dx
    #     self.location_y += dy
    #
    # def bewege_norden(self):
    #     self.bewege(dx=0, dy=-1)
    #
    # def bewege_süden(self):
    #     self.bewege(dx=0, dy=1)
    #
    # def bewege_osten(self):
    #     self.bewege(dx=1, dy=0)
    #
    # def bewege_westen(self):
    #     self.bewege(dx=-1, dy=0)