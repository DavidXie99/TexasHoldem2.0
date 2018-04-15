

##Global Resources
suitTranslation = {
                    0 : 'Spades',
                    1 : 'Hearts',
                    2 : 'Clubs',
                    3 : 'Diamonds'
                  }

nameTranslation = {
                    0 : 'Ace',
                    1 : 'Two',
                    2 : 'Three',
                    3 : 'Four',
                    4 : 'Five',
                    5 : 'Six',
                    6 : 'Seven',
                    7 : 'Eight',
                    8 : 'Nine',
                    9 : 'Ten',
                    10 : 'Jack',
                    11 : 'Queen',
                    12 : 'King'
                  }
                    
##Object Definitions

class Card:
    def __init__(self,
                 suit_param = 'dunce',
                 name_param = '0',
                 value_param = -1,
                 raw_value_param = -1):
        self.suit = suit_param
        self.name = name_param
        self.value = value_param
        self.raw_value = raw_value_param

class Pot:
    def __init__(self,
                 ):
        self.stage_pot = {}
        self.total_pot = []
        
    def clear(self):
        self.stage_pot.clear()
        self.total_pot.clear()

    def stageAdd(self,betObject):
        if betObject.playerId in self.stage_pot:
            self.stage_pot[ betObject.player_id ].bet += betObject.amount
            self.stage_pot[ betObject.player_id ].allInBool = betObject.allInBool
            
    def totalAdd(self,player_id):
        if playerId in self.stage_pot:
            self.total_pot[-1] += self.stage_pot[ player_id ].bet 
            del self.stage_pot[ player_id ]

