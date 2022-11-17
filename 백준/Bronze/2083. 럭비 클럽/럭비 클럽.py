while True:
    name, age, weight = map(str, input().split())
    age, weight = int(age), int(weight)
    if name == '#' and age == 0 and weight == 0:
        break

    if 17 < age or 80 <= weight:
        print(name, 'Senior')
    else:
        print(name,'Junior') 