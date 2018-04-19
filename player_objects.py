##Imports
import constants
import misc_functions

##Object Definitions

class Player:
    def __init__(self,
                 first_name_param = 'Parker',
                 middle_name_param = '',
                 last_name_param = 'Lee',
                 money_param = 100000):
        self.first_name = first_name_param
        self.middle_name = middle_name_param
        self.last_name = last_name_param
        self.money = money_param
        self.id = misc_functions.generateId( constants.player_const)

class PlayerStats:
    def __init__(self,
                 number_param1 = 3.1415926):
        self.random_attribute = number_param1 #just to initialize the object

class Bet:
    def __init__(self,
                player_id_param =   misc_functions.generateId(-1),
                money_amount_param = 100,
                all_in_bool_param = False,
                action_param = 'Sleep'):
        self.player_id = player_id_param
        self.amount = money_amount_param
        self.all_in_bool = all_in_bool_param
        self.action = action_param
        self.id = misc_functions.generateId( constants.bet_const)
