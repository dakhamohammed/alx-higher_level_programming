#!/usr/bin/python3

# or index = 0
index: int = 0
for chars in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(chars - index)), end="")
    index = 32 if index == 0 else 0
