from string import ascii_lowercase
list_ = list(ascii_lowercase)
word = input()

for i in range(len(list_)):
    if(list_[i] in word):
        print(word.index(list_[i]), end=' ')
    else:
        print(-1, end=' ')