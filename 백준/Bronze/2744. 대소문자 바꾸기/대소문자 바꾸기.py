data = input()

for i in range(len(data)):
    if 65 <= ord(data[i]) <= 90:
        print(chr(ord(data[i])+32), end='')
    else:
        print(chr(ord(data[i])-32), end='')