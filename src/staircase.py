def gen_staircase(n: int, display: str):
    staircase = []
    space = ' ' * len(display)

    if 0 < n <= 30:
        for i in range(1,n+1):
            step = (space * (n-i)) + (display * i)
            staircase.append(step)
    return staircase


# print(gen_staircase(5, '*'))