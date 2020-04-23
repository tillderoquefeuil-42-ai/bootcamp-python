import sys

errorMsg = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"

args = sys.argv[1:]
error = False

if len(args) < 2:
    error = True
elif len(args) > 2:
    print("InputError: too many arguments\n")
    error = True
elif not args[0].isdigit() or not args[1].isdigit():
    print("InputError: only numbers\n")
    error = True

if error == True:
    print(errorMsg)
    sys.exit(0)

nbr1 = int(args[0])
nbr2 = int(args[1])

# SUM
print("Sum:\t\t" + str(nbr1 + nbr2))
# DIFFERENCE
print("Difference:\t" + str(nbr1 - nbr2))
# PRODUCT
print("Product:\t" + str(nbr1 * nbr2))

# QUOTIENT
if nbr2 == 0:
    print("Quotient:\tERROR (div by zero)")
    print("Remainder:\tERROR (modulo by zero)")
else:
    print("Quotient:\t" + str(nbr1 / nbr2))
    print("Remainder:\t" + str(nbr1 % nbr2))
