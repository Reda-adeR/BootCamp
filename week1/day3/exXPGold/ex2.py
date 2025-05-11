class MyList:
    def __init__(self, letterList):
        self.letList = letterList
    
    def rev_list(self):
        return self.letList[::-1]
    
    def sorted_list(self):
        return sorted(self.letList)
    
    def generate_list_nums(self):
        import random
        return [random.randint(1,100) for i in range(len(self.letList))]

gg = MyList(['a', 'b', 'c', 'd'])
print(gg.rev_list())
print(gg.sorted_list())
print(gg.generate_list_nums())