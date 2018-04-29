##Imports
import constants
import misc_functions
import random
from collections import deque

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
        self.id = misc_functions.generateId( constants.card_const)

class Pot:
    def __init__(self):
        self.stage_Pot = {}
        self.total_Pot = []
        self.id = misc_functions.generateId( constants.pot_const)

    def clear(self):
        self.stage_Pot.clear()
        self.total_Pot.clear()

    def stageAdd(self,
                 BetObject):
        if BetObject.player_id not in self.stage_Pot:
            self.stage_Pot[ BetObject.player_id ] = SomeObject ## this needs to be declared

        self.stage_Pot[ BetObject.player_id ].bet += BetObject.amount
        self.stage_Pot[ BetObject.player_id ].all_in_bool = BetObject.all_in_bool

    def totalAdd(self,
                 player_id):
        if playerId in self.stage_Pot:
            self.total_Pot[-1] += self.stage_Pot[ player_id ].bet
            del self.stage_Pot[ player_id ]

class Dealer:
    def __init__(self):
        self.deck = [ Card( constants.suit_Translation[ i//13 ],
                            constants.name_Translation[ i%13 ],
                            i%13,
                            i) for i in range(52) ]
        self.index = 0
        self.id = misc_functions.generateId( constants.dealer_const)

    def shuffleDeck(self):
        for i in range(random.randint(1,10)):
            random.shuffle(self.deck)

    def deal(self,
             PlayerObject):
        playerObject.hand.append( self.deck[ self.index ])
        self.index += 1

class Seat:
    def __init__(self,
                 PlayerObjectParam,
                 position_param,
                 buy_in_param):
        self.PlayerObject = PlayerObjectParam
        self.hand = []
        self.money = buy_in_param
        self.cur_position = position_param
        self.all_in = False
        self.next_position = None
        self.prev_position = None

class Table:
    def __init__(self,
                 buy_in_param = 10000):
        self.Pot = Pot()
        self.Dealer = Dealer()
        self.buy_in = buy_in_param
        self.player_List = {}
        self.available_Position_List = deque(i for i in range(10))
        self.id = misc_functions.generateId( constants.table_const)

    def addPlayer(self,
                  PlayerObject,
                  buy_in):
        position = self.available_Position_List.popleft()
        SeatObject = Seat(PlayerObject, position, buy_in)
        next_pos = position
        prev_pos = position
        if len(self.player_List):
            for i in range(position + 1, position + 10):
                if i%10 in self.player_List:
                    next_pos = i%10
                    prev_pos = self.player_List[ next_pos ].prev_position
                    self.player_List[ next_pos ].prev_position = position
                    self.player_List[ prev_pos ].next_position = position
                    break
        SeatObject.next_position = next_pos
        SeatObject.prev_position = prev_pos
        self.player_List[ position ] = SeatObject

    def removePlayer(self,
                     position):
        next_pos = self.player_List[ position ].next_position
        prev_pos = self.player_List[ position ].prev_position

        self.player_List[ next_pos ].prev_position = prev_pos
        self.player_List[ prev_pos ].next_position = next_pos
        del self.player_List[ position ]

        self.available_Position_List.append( position)
