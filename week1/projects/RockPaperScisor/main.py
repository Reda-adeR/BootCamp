from game import Game

def get_user_menu_choice():
    while 1:
        choice = input("***RPS GAME*** | (P)lay game | (S)how scores | (Q)uit | ***RPS GAME***\n ===> ")
        if choice.upper() in ["P","S","Q"] : return choice

def print_results(results):
    print("Game Results : " , results)
    print(f"You Drew {results[0]} times")
    print(f"You Won {results[1]} times")
    print(f"You Lost {results[2]} times")
    print()
    print("Thank You For Playing !")


if __name__ == "__main__":
    obj = Game()
    while 1:
        c = get_user_menu_choice()
        if c.upper() == "P":
            obj.play()
        elif c.upper() == "S":
            print_results(obj.res)
        else:
            exit("See next Time")

#     obj = None
#     while 1:
#        g = showMenu()
#        if g.upper() == "G":
#            obj = 