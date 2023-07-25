from getkey import getkey, keys

decision = "Y"

print("Press enter when you are done \n")

while decision == "Y":
    key = getkey()
    if key == "a":
        print("01100001", end=" ")
    elif key == "A":
        print("01000001", end=" ")
    elif key == "b":
        print("01100010", end=" ")
    elif key == "B":
        print("01000010", end=" ")
    elif key == "c":
        print("01100011", end=" ")
    elif key == "C":
        print("01000011", end=" ")
    elif key == "d":
        print("01100100", end=" ")
    elif key == "D":
        print("01000100", end=" ")
    elif key == "e":
        print("01100101", end=" ")
    elif key == "E":
        print("01000101", end=" ")
    elif key == "f":
        print("01100110", end=" ")
    elif key == "F":
        print("01000110", end=" ")
    elif key == "g":
        print("01100111", end=" ")
    elif key == "G":
        print("01000111", end=" ")
    elif key == "h":
        print("01101000", end=" ")
    elif key == "H":
        print("01001000", end=" ")
    elif key == "i":
        print("01101001", end=" ")
    elif key == "I":
        print("01001001", end=" ")
    elif key == "j":
        print("01101010", end=" ")
    elif key == "J":
        print("01001010", end=" ")
    elif key == "k":
        print("01101011", end=" ")
    elif key == "K":
        print("01001011", end=" ")
    elif key == "l":
        print("01101100", end=" ")
    elif key == "L":
        print("01001100", end=" ")
    elif key == "m":
        print("01101101", end=" ")
    elif key == "M":
        print("01001101", end=" ")
    elif key == "n":
        print("01101110", end=" ")
    elif key == "N":
        print("01001110", end=" ")
    elif key == "o":
        print("01101111", end=" ")
    elif key == "O":
        print("01001111", end=" ")
    elif key == "p":
        print("01110000", end=" ")
    elif key == "P":
        print("01010000", end=" ")
    elif key == "q":
        print("01110001", end=" ")
    elif key == "Q":
        print("01010001", end=" ")
    elif key == "r":
        print("01110010", end=" ")
    elif key == "R":
        print("01010010", end=" ")
    elif key == "s":
        print("01110011", end=" ")
    elif key == "S":
        print("01010011", end=" ")
    elif key == "t":
        print("01110100", end=" ")
    elif key == "T":
        print("01010100", end=" ")
    elif key == "u":
        print("01110101", end=" ")
    elif key == "U":
        print("01010101", end=" ")
    elif key == "v":
        print("01110110", end=" ")
    elif key == "V":
        print("01010110", end=" ")
    elif key == "w":
        print("01110111", end=" ")
    elif key == "W":
        print("01010111", end=" ")
    elif key == "x":
        print("01111000", end=" ")
    elif key == "X":
        print("01011000", end=" ")
    elif key == "y":
        print("01111001", end=" ")
    elif key == "Y":
        print("01011001", end=" ")
    elif key == "z":
        print("01111010", end=" ")
    elif key == "Z":
        print("01011010", end=" ")
    elif key == keys.SPACE:
        print(" ", end=" ")
    elif key == keys.ENTER:
        break
