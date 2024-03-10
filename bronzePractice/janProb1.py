t = int(input())

for _ in range(t):
    n = int(input())
    cows = input().split()
    n = len(cows)
    result_string = ""

    doubles = set()
    if cows[1] == cows[0]:
        doubles.add(cows[1])
    for x in range(2,n):
        if cows[x] == cows[x-1]:
            doubles.add(cows[x])
        if cows[x] == cows[x-2]:
            doubles.add(cows[x])
    final = list(doubles)

    final = set(final)
    final = list(final)
    final.sort()


    #print(final)
    if len(final)>0:
        result_string = ' '.join(final)
        print(result_string)
    else:
        print("-1")
