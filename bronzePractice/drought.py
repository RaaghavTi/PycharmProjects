t = int(input())
for _ in range(t):
    n = int(input())
    hunger = list(map(int, input().split()))
    count = 0
   # leftFail = False
    #rightFail = False
    for x in range(n-2):

      goal = hunger[x+1]
      if hunger[x]>goal:
        #print(f"x:{x}")
        '''if you need to decrease the current one, and the ones before it...the first up to
        x are too big'''
        if (x+1)%2 == 1:
            '''if the # of hunger levels that you have to make equal to the goal is odd,
            then not possible'''
            break
        else:
            difference = hunger[x] - goal
            for y in range(x):
                count += difference
                hunger[y] = goal
      else:
        goal = hunger[x]
        ''' if you need to decrease the two ahead of it...the one directly in front is too big '''
        if x<n-2:

            removing = hunger[x+1] - hunger[x]

            if hunger[x+2] - removing <0:
                break
            count += removing*2
            hunger[x+1] = goal
            hunger[x+2] -= removing
        else:
            break
    print(hunger)
    for x in reversed(range(2,n)):

        goal = hunger[x -1]
        if hunger[x] > goal:
            if n-x % 2 == 1:
                # leftFail = True
                break
            else:
                difference = hunger[x] - goal
                for y in range(x,n):
                    count += difference
                    hunger[y] = goal
        else:
            goal = hunger[x]
            if x >1:
                removing = hunger[x - 1] - hunger[x]
                if hunger[x - 2] - removing < 0:
                    break
                count += removing * 2
                hunger[x - 1] = goal
                hunger[x - 2] -=removing
            else:
                break
        previous = hunger[0]
        same  = 0
        print(hunger)
        for x in hunger:
            if x==previous:
                same +=1
            previous = x
        if same == n:
            print(count)
        else:
            print("-1")






