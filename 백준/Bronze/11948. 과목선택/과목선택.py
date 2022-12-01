lst1 = []
lst2 = []
for i in range(6):
    n = int(input())
    if i < 4:
        lst1.append(n)
    else:
        lst2.append(n)

minlst1 = min(lst1)
lst1.remove(minlst1)
minlst2 = min(lst2)
lst2.remove(minlst2)

print(sum(lst1) + sum(lst2))