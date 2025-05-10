def throw_dice():
    import random
    return random.randint(1, 6)

def throw_until_double():
    count = 0
    while 1:
        d1 = throw_dice()
        d2 = throw_dice()
        count += 1
        if d1 == d2:
            print(f"--> ({d1}, {d2})")
            break
        print(f"({d1}, {d2}),", end="")
    return count

def throw_until_100():
    throws = 0
    for i in range(100):
        throws += throw_until_double()
    print(f"Total throws until double in 100 rounds: {throws}")
    print(f"Average throws until double: {throws / 100:.2f}")



throw_until_100()