# FYI uses ACIll encoding
import struct

def TextToBinary():
    # Asks for a word from the user
    user = input("Type a word to convert into binary: ")

    # Formats the word in base 2
    res = ''.join(format(ord(i), '08b') for i in user)

    # Prints binary
    print(res)

def NumberToBinary():
    # Asks for a Whole Number from the user
    user = int(input("Type a Whole Number to convert into binary: "))
    
    # Formats the word into Binary
    res = '{0:08b}'.format(user)

    # Prints Binary
    print(res)

def FloatToBinary():
    user = float(input("Type a Float Number to convert into binary: "))
    s = struct.pack('!f', user)
    b = ''.join(format(c, '08b') for c in s)
    print(b)

FloatToBinary()