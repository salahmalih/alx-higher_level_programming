#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum number."""
    import sys

    sum = 0
    count = len(sys.argv) - 1
    if count == 0:
        print("0")
    elif count == 1:
        print("{}".format(sys.argv[count]))
    else:
        for i in range(count):
            sum = sum + int(sys.argv[i + 1])
        print("{}".format(sum))
