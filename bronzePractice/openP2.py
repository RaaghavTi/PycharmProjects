import copy

n, p = map(int, input().split())

posts = []
for _ in range(p):
    post = list(map(int, input().split()))
    posts.append(post)
if posts[0] == posts[-1]:
    posts.pop(-1)

for _ in range(n):
    journey = list(map(int, input().split()))
    start = [journey[0], journey[1]]
    end = [journey[2], journey[3]]
    current = copy.deepcopy(posts)
    if start not in posts:
        for x in range(p):
            x1 = current[x][0]
            y1 = current[x][1]

            x2 = current[x + 1][0]
            y2 = current[x + 1][1]
            if start[0] == x1 and start[0] == x2:
                if start[1] > min(y1, y2) and start[1] < max(y1, y2):
                    current.insert(x + 1, start)
                    si = x
                    break
            # print(current)
            # print(current[x], current[x+1], end, x)
            if start[1] == y1 and start[1] == y2:

                if start[0] > min(x1, x2) and start[0] < max(x1, x2):
                    current.insert(x + 1, start)
                    si = x
                    break
        x1 = current[0][0]
        y1 = current[0][1]

        x2 = current[-1][0]
        y2 = current[-1][1]
        if start[0] == x1 and start[0] == x2:
            if start[1] > min(y1, y2) and start[1] < max(y1, y2):
                current.insert(x + 1, start)
                si = x
        # print(current)
        # print(current[x], current[x+1], end, x)
        if start[1] == y1 and start[1] == y2:

            if start[0] > min(x1, x2) and start[0] < max(x1, x2):
                current.insert(x + 1, start)
                si = x
    # print(current)
    if end not in posts:

        for x in range(len(current) - 1):
            x1 = current[x][0]
            y1 = current[x][1]

            x2 = current[x + 1][0]
            y2 = current[x + 1][1]
            if end[0] == x1 and end[0] == x2:
                if end[1] > min(y1, y2) and end[1] < max(y1, y2):
                    current.insert(x + 1, end)
                    ei = x
                    break
            # print(current)
            # print(current[x], current[x+1], end, x)
            if end[1] == y1 and end[1] == y2:

                if end[0] > min(x1, x2) and end[0] < max(x1, x2):
                    current.insert(x + 1, end)
                    ei = x
                    break

        x1 = current[0][0]
        y1 = current[0][1]

        x2 = current[-1][0]
        y2 = current[-1][1]
        if end[0] == x1 and end[0] == x2:
            if end[1] > min(y1, y2) and end[1] < max(y1, y2):
                current.insert(0, end)
                ei = x

        # print(current)
        # print(current[x], current[x+1], end, x)
        if end[1] == y1 and end[1] == y2:

            if end[0] > min(x1, x2) and end[0] < max(x1, x2):
                current.insert(0, end)
                ei = x

    si = current.index(start)

    ei = current.index(end)
    total = 0

    # print(current, si, ei)
    for x in range(min(si, ei), max(si, ei)):
        total += abs(current[x][0] - current[x + 1][0])
        total += abs(current[x][1] - current[x + 1][1])
    new = 0
    for x in range(max(si, ei), len(current) - 1):
        new += abs(current[x][0] - current[x + 1][0])
        new += abs(current[x][1] - current[x + 1][1])
    new += abs(current[0][0] - current[-1][0])
    new += abs(current[0][1] - current[-1][1])
    for x in range(min(si, ei)):
        new += abs(current[0][0] - current[x + 1][0])
        new += abs(current[0][1] - current[x + 1][1])
    print(min(new, total))






