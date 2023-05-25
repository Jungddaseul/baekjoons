word = input().upper()
dict_word = {}

for i in list(word):
    if i in dict_word:
        dict_word[i] += 1
    else:
        dict_word[i] = 1

max_count = max(dict_word.values())

max_char = []
for char, count in dict_word.items():
    if count == max_count:
        max_char.append(char)

if len(max_char) > 1:
    print("?")
else:
    print(max_char[0])