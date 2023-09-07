#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    argv_result = 0

    for i in range(argc):
        argv_result = argv_result + int(sys.argv[i + 1])

    print("{}".format(argv_result))
