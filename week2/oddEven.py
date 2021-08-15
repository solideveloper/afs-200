
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num, " is an EVEN number.")
else:
   print(num, " is an ODD number.")
if (num % 4) == 0:
    print(num, " is a multiple of four")

