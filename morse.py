#
# Partly inspired by https://morsle.fun/
# 

import argparse
import sys

# TODO
# Allow strings of words as input
# Read from file
# Output to file
# Read from STDIN

ap = argparse.ArgumentParser()
mode_arg = ap.add_mutually_exclusive_group()
mode_arg.add_argument("-e","--encode", default=True, action="store_true", required=False, help="Output Morse code for input string. This is the default.")
mode_arg.add_argument("-d", "--decode", default=False, action="store_true", required=False, help="Output text from Morse code input.")
#ap.add_argument("-e","--encode", default=True, required=False, help="Output Morse code for input string. This is the default.")
#ap.add_argument("-d", "--decode", default=False, required=False, help="Output text from Morse code input.")
ap.add_argument("cmdargs", nargs=argparse.REMAINDER)
args = vars(ap.parse_args())

#print(args)

if (args["encode"] == True):
    mode = "encode"
if (args["decode"] == True):
    mode = "decode" 

#print(mode)

# From Wikipedia:
# https://en.wikipedia.org/wiki/Morse_code
# The length of a dot is one unit
# Dash is three units
# Space between parts of same letter is one unit
# Space between letters is three units
# Space between words is seven units
# See also https://en.wikipedia.org/wiki/Prosigns_for_Morse_code for punctuation etc
morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "-",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "   ",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

# reverse keys and values, easier than looking through each time
reverse_m_dict = {v: k for k, v in morse_dict.items()}

test_string = "HELLO WORLD!"
test_morse = ".... . .-.. .-.. ---     .-- --- .-. .-.. -.."

def encode_letter(l):
    l = l.upper()
    # return the value from the key
    if(l in morse_dict):
        return morse_dict[l]
    return l

def decode_morse(m):
    # spaces already stripped out
    #if(m in morse_dict.values()):
    if(m in reverse_m_dict):
        return reverse_m_dict[m]
    return m

#print(encode_letter("e"))
#print(decode_morse(test_morse))

# if(args["cmdargs"]):
#     input_string = args["cmdargs"][0]
# else:
#     input_string = test_string
output_string = ''
#print(input_string)
if(mode == 'encode'):
    if(args["cmdargs"]):
        input_string = args["cmdargs"][0]
    else:
        input_string = test_string
    for c in input_string:
        #print(encode_letter(c) + " ", end="") # leaves trailing space
        output_string += (encode_letter(c) + " ")
    print(output_string)
    sys.exit()

if(mode == 'decode'):
    if(args["cmdargs"]):
        #input_string = args["cmdargs"][0] # will only decode one character
        input_string = args["cmdargs"] # now an array
    else:
        input_string = test_morse
    #for m in input_string.split(" "):
    for m in input_string:
        #print(decode_morse(c), end="") # space between words gets consumed
        output_string += (decode_morse(m))
    print(output_string)
    sys.exit()