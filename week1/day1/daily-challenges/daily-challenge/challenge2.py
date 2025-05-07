word = input("Enter a word: ")
letter = ''
new_word = ''
for i in word:
    if i != letter:
        new_word += i
    elif i == letter:
        pass
    letter = i
print(new_word)
    