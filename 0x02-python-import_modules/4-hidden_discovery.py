#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    defined_names = dir(hidden_4)

    for name in defined_names:
        if defined_names[:2] != "__":
            print(defined_names)
