n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False
count = 0


while min(a) > -1:
    a_min = min(a)
    if len(set(a)) == 1:
        print(count)
        break

    for j in range(len(a)):
        if a[j] > a_min:
            a[j] = a[j] - b[j]
            count += 1
else:
    print(-1)