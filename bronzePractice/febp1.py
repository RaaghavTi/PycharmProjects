def findNextPal(n):
    if str(n) == str(n)[::-1]:
        return n
    for num in reversed(range(1,n + 1)):
        strPile = str(n-num)
        potential = n-num
        strNum = str(num)
        # print(strPile,strNum)
        if strNum == strNum[::-1] and strPile != strPile[::-1]:
            if str(potential-10) != str(potential-10)[::-1]:
                return num


    for num in range(1,n+1):
        if str(num) == str(num)[::-1]:
            return num


t = int(input())
result = 0
for _ in range(t):
    turn = 0
    stones = int(input())
    while stones != 0 and result != -1:
        print(stones)
        result = findNextPal(stones)
        stones -= result
        turn += 1
    print(stones)
    if turn % 2 == 1:
        print("B")
    else:
        print("E")