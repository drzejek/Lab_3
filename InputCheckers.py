import sys
import string
from Exceptions import *

def doQuitGame(position):
    if position == 'q':
        print("Goodbye!")
        sys.exit()

def isInputLengthCorrect(position):
    if len(position) != 2:
        raise WrongStringLength


def isInputSyntaxCorrect(position):
    if not position[0] in string.ascii_lowercase:
        raise NotString

