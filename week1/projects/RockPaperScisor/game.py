
r = "Rock"
p = "Paper"
s = "Scisor"

class Game:
    def __init__(self):
        self.res = [0,0,0]
    def get_user_item(self):
        dict = {"R" : r, "S" : s, "P": p}
        while 1:
            select = input("select : (R)ock   _   (P)aper   _   (S)cisor : ")
            if select.upper() in ["R","P","S"]:
                return dict[select.upper()]
            
    def get_computer_item(self):
        import random
        return random.choice([r,p,s])
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "Draw"

        dict = { r : s, s : p, p : r }
        if dict[user_item] == computer_item:
            return "Win"
        else:
            return "Loss"
        
    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()

        print(f"You selected          {user}.")
        print(f"the computer selected {computer}.")

        dict = { "Draw": 0, "Win": 1, "Loss": 2 }
        # print("------"+user +"------")
        # exit()
        result = self.get_game_result(user, computer)

        print(f"You {result} !")
        self.res[dict[result]] += 1
        return result
