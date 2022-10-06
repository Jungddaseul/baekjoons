num = list(map(int, input().split()))
num_sqr = []
for i in num:
    num_sqr.append(i**2)

sum = 0

for i in num_sqr:
    sum += i
print(sum % 10)
