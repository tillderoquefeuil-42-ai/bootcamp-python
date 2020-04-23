import sys

alphanum = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--',
    'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'
}

args = sys.argv[1:]

if len(args) == 0:
    sys.exit(0)

strings = []

for i in args:
    tmp = i.replace(" ", "")
    if not tmp.isalnum():
        print("ERROR")
        sys.exit(0)

    upper = i.upper()
    upper = upper.replace(" ", " / ")

    morse = ""
    for j in upper:
        if j in alphanum:
            morse += alphanum[j] + " "
        else:
            morse += j

    strings.append(morse.strip())

print(" / ".join(strings))