import sys
import re

args = sys.argv[1:]
error = False

if len(args) < 2:
    error = True
elif len(args) > 2:
    error = True
elif args[0].isdigit() or not args[1].isdigit():
    error = True

if error == True:
    print("ERROR")
    sys.exit(0)

string = args[0]
nbr = int(args[1])

string = re.sub(r"[!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", "", string)
shortword = re.compile(rf'\W*\b\w{{1,{nbr}}}\b')
string = shortword.sub('', string)

string = string.strip()

print(string.split(' '))