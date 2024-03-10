def reverse(myList, start, end):
    myList[start:end] = reversed(myList[start:end])
    return myList


f = open("swap.in", "r")
n, k = map(int, f.readline().split())
f1, f2 = map(int, f.readline().split())
s1, s2 = map(int, f.readline().split())

original = []

directory = []
for x in range(n):
    original.append(x+1)
changed = original.copy()

changed = reverse(changed, f1-1, f2)
changed = reverse(changed, s1-1, s2)
directory.append(changed)
while changed!=original:
    changed = reverse(changed, f1-1, f2)
    changed = reverse(changed, s1-1, s2)

    directory.append(changed.copy())


fout = open("swap.out", "w")
array = []
array = directory[k%len(directory) - 1]
for element in array:
    fout.write(str(element) + '\n')
