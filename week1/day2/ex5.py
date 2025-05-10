

def randomizer(num):
    if not isinstance(num, int):
        print("Invalid Number.")
        return
    num = int(num)
    import random
    comp = random.randint(1, 100)
    if num == comp:
        print("You win")
    else:
        print("you lose ", "your number is ", num,
              "and the computer's number is ", comp)

randomizer(50)