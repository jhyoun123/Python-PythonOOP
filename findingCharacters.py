def find(words, char):
    new_list = []
    for word in words:
        if char in word:
            new_list.append(word)
    print new_list
find(['hello','world','my','name','is','Anna'], "o")