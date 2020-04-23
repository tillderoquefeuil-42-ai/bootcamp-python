import sys

str = ""
output = ""

for i in range(len(sys.argv)):
    if i == 1:
        str += sys.argv[i]
    if i > 1:
        str += " " + sys.argv[i]

j = len(str) - 1
while j >= 0:
    ascii = ord(str[j])
    if 65 <= ascii and ascii <= 90:
        output += chr(ascii + 32)
    elif 97 <= ascii and ascii <= 122:
        output += chr(ascii - 32)
    else:
        output += str[j]
    j = j - 1

print(output)