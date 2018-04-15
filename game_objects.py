##Imports
import constants

                    
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
    def __init__(self):
        self.stage_Pot = {}
        self.total_Pot = []
        
    def clear(self):
        self.stage_Pot.clear()
        self.total_Pot.clear()

    def stageAdd(self,
                 betObject):
        if betObject.playerId in self.stage_Pot:
            self.stage_Pot[ betObject.player_id ].bet += betObject.amount
            self.stage_Pot[ betObject.player_id ].allInBool = betObject.allInBool
            
    def totalAdd(self,
                 player_id):
        if playerId in self.stage_Pot:
            self.total_Pot[-1] += self.stage_Pot[ player_id ].bet 
            del self.stage_Pot[ player_id ]

