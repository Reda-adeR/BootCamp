import math

class Pagination:
    def __init__(self, items=[], size=10):
        self.items = items
        if size == 0:
            self.size = 1
        else:
            self.size = size
        self.currIdx = 2
        self.pages = math.ceil(len(self.items) / self.size)

    def get_visible_items(self):
        if not len(self.items):
            return print("empty list")
        if self.currIdx + 1 > self.pages:
            return print("Invalid index")
        start = self.size * self.currIdx
        stop  = start + self.size 
        return self.items[start:stop]
    
    def __str__(self):
        return "\n".join(self.get_visible_items())

    def go_to_page(self, page_num):
        if page_num == 0:
            raise ValueError("Error Page Number")
        self.currIdx = page_num - 1

    def first_page(self):
        self.currIdx = 0
        return self
    
    def last_page(self):
        self.currIdx = self.pages - 1
        return self

    def next_page(self):
        self.currIdx += 1
        if self.currIdx >= self.pages - 1 : self.last_page()
        return self

    def previous_page(self):
        self.currIdx -= 1
        if self.currIdx <= 0 : self.first_page()
        return self



gg = Pagination(["1","2","3","4","5","6","7","8","9","10","11","12"], 4)
gg.go_to_page(1)
gg.next_page().next_page().next_page().previous_page().first_page().last_page()
print(str(gg))


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.currIdx + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError
