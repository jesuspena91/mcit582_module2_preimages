# Use a brute-force algorithm to find a partial preimage.
# Using the template “hash_preimage.py” write a function called “hash_preimage” that takes a single input, target_string, 
# where target_string is a string of bits. The function “hash_preimage” should return a single variable x such that the 
# trailing bits of SHA256(x) matches the target string (not the hash of the target string).
# Your algorithm should be randomized, i.e., hash_preimage(target_string) should not always return the same partial preimage.

import hashlib
import os
import math

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    random_base = 64

    while True:
    	random_num = os.urandom(random_base)
    	hash_random_num = hashlib.sha256(random_num).hexdigest()
    	int_random_num = int(hash_random_num, base=16)
    	binary_random_num = bin(int_random_num)[2:]

    	if (binary_random_num[-len(target_string):] == target_string):
    		break

    # print(target_string)
    # print(binary_random_num)
    # print(binary_random_num[-len(target_string):])
    # print(type(binary_random_num))
    # print(binary_random_num.encode('utf-8'))
    # print(type(binary_random_num.encode('utf-8')))

    #print(random_num)
    return(random_num)

#hash_preimage('011010')