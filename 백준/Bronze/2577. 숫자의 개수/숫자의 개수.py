a = int(input())
b = int(input())
c = int(input())

result = a * b * c
dic_num = {'0' : 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0
        , '7': 0, '8': 0, '9': 0}

for i in str(result):
    if i == '0':
        dic_num['0'] += 1
    elif i == '1':
        dic_num['1'] += 1
    elif i == '2':
        dic_num['2'] += 1
    elif i == '3':
        dic_num['3'] += 1
    elif i == '4':
        dic_num['4'] += 1
    elif i == '5':
        dic_num['5'] += 1
    elif i == '6':
        dic_num['6'] += 1
    elif i == '7':
        dic_num['7'] += 1
    elif i == '8':
        dic_num['8'] += 1
    elif i == '9':
        dic_num['9'] += 1

for key, value in dic_num.items():
    print(value)