f = open("taming.in", "r")
n = int(f.readline())
counter = list(map(int, f.readline().split()))

counter[0] = 0

index = n-1
missingVal = -1
while index >= 0:
    if counter[index] != -1 and counter[index] != 0:
        missingVal = counter[index]
    if counter[index] == -1 and missingVal >=0:
        counter[index] = missingVal
    missingVal -= 1
    index -=1
min = 0
max = 0
for x in range(n):
    if counter[x] == 0:
        min += 1
        max += 1
    if counter[x] == -1:
        max += 1
#print(counter)
#print(counter)
out = open("taming.out", "w")
output = str(min) + " " + str(max)
out.write(output)