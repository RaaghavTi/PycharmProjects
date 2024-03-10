n, m = map(int, input().split())
directions = input()
buckets = list(map(int, input().split()))

lost = 0
total = sum(buckets)

diffs = []
pos = []
if n >= 3:
    for x in range(n):
        current = -1
        if x == 0:
            if directions[x+1] == 'L':
                current += 1
            if directions[-1] == 'R':
                current += 1
        elif x == n-1:
            if directions[x-1] == 'R':
                current += 1
            if directions[0] == 'L':
                current += 1
        else:
            if directions[x-1] == 'R':
                current += 1
            if directions[x+1] == 'L':
                current += 1
        if current == 1:
            pos.append(x)
        diffs.append(current)
    #print(diffs)
    for x in pos:
        if x == 0:
            if diffs[-1] == -1:
                lost += min(m,buckets[-1])
            elif diffs[1] == -1:
                lost += min(m,buckets[1])
            else:
                lost += m
        elif x == n-1:
            if diffs[0] == -1:
                lost += min(m,buckets[0])
            elif diffs[-2] == -1:
                lost += min(m,buckets[-2])
            else:
                lost += m
        else:
            if diffs[x+1] == -1:
                lost += min(m,buckets[x+1])
            elif diffs[x-1] == -1:
                lost += min(m,buckets[x-1])
            else:
                lost += m


if n <3:
    lost = 0

print(total - lost)
