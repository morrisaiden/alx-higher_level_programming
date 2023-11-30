#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, 's' if argc > 1 else ''))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
