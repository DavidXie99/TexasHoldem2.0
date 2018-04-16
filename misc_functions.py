##Imports
import random
import constants


##Function Definitions

def addFillerChars(string_param,
                   length_param,
                   char_param = '0'):
    return char_param * ( length_param - len(string_param)) + string_param
                   

def generateId(number_param):
    p_num_val1 = pow( number_param, number_param, constants.global_prime)
    p_num_val2 = max( p_num_val1,
                     pow( p_num_val1, 2, constants.global_prime),
                     (p_num_val1 * 2) % constants.global_prime)
    
    random_number = pow( number_param,
                        random.randint( p_num_val1, p_num_val2),
                         constants.global_prime)

    prefix_string = constants.id_Prefix[ number_param ] if number_param in constants.id_Prefix else 'un'
    return prefix_string + addFillerChars( str( random_number), 10)

