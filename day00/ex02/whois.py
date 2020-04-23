import sys

args = sys.argv[1:]

if len(args) != 1 or not args[0].isdigit():
    print('ERROR')
    sys.exit(0)

nbr = int(args[0])

if nbr == 0:
    print("I'm Zero.")
elif nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
