def is_triangle(a, b, c):
    if (a + b) > c:
        print('These three lengths can make a triangle.')
    elif (a + c) > b:
        print('These three lengths can make a triangle.')
    elif (b + c) > a:
        print('These three lengths can make a triangle')
    else:
        print('These three lengths cannot make a triangle.')


def input_hasher():    
    inp = []
    for n in range(3):
        inp.append(int(input("Define a value.\n")))
    is_triangle(inp[0], inp[1], inp[2])


input_hasher()
