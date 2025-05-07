my_fav_numbers = {2,7,11,9}
my_fav_numbers.add(3)
my_fav_numbers.add(6)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers = {1,4,6,5}
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)