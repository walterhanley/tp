def do_twice(f, g):
    f(g)
    f(g)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(h, i):
    do_twice(h, i)
    do_twice(h, i)
