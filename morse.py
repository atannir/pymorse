#
# Partly inspired by https://morsle.fun/
# 

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-e","--encode", default=True, required=False, help="Output Morse code for input string. This is the default.")
ap.add_argument("-d", "--decode", default=False, required=False, help="Output text from Morse code input.")
args = vars(ap.parse_args())

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
}

test_string = "HELLO WORLD"

def decode_letter(l):
    # return the value from the key
    #if()
    return ""
