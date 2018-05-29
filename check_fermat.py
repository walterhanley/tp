def check_fermat(a, b, c, n):
    if ((a**n + b**n) == c**n) and n > 2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def input_hasher():
    a = int(input("Define a value for a.\n"))
    b = int(input("Define a value for b.\n"))
    c = int(input("Define a value for c.\n"))
    n = int(input("Define a value for n.\n"))
    check_fermat(a, b, c, n)


input_hasher()
