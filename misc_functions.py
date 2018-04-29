##Imports
import random
import constants


##Function Definitions

def addFillerChars(string,
                   length,
                   char = '0'):
    return char * ( length - len(string)) + string


def generateId(number):
    p_num_val1 = pow( number, 2 * abs( number), constants.global_prime)
    p_num_val2 = max( p_num_val1,
                     pow( p_num_val1, 2, constants.global_prime),
                     (p_num_val1 * 2) % constants.global_prime)

    random_number = pow( number,
                         abs( random.randint( 1, p_num_val2)),
                         constants.global_prime)

    prefix_string = constants.id_Prefix[ number ] if number in constants.id_Prefix else 'un'
    return prefix_string + addFillerChars( str( random_number), 10)
