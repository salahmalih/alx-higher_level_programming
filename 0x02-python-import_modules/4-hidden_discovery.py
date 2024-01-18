#!/usr/bin/Python3
if __name__ == "__main__":
    """prints all the names defined by the compiled."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
