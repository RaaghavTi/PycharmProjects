f = open("sleepy.in", "r")
n = int(f.readline())
order = list(map(int, f.readline().split()))
index = 0
#print(order)
previous = n-1

for x in reversed(range(n)):
    #print(x)
    if order[x]>order[previous]:
        index = x+1
        break
    previous = x
out = open("sleepy.out", "w")
#print(index)
out.write(str(index))