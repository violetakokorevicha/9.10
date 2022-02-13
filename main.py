import sys
n = int(input('Your number:'))
if n == 0:
    sys.exit("Stop")
if n % 2 == 0:
    print('even')
else:
    print('odd')
