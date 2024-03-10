n = int(input())
bacteria = list(map(int, input().split()))
uses = 0

for x in range(n):
    #print(bacteria)
    multiplier = bacteria[x] * -1
    uses += abs(multiplier)
    factor = 0
    for y in range(x,n):
        factor +=1
        bacteria[y] += multiplier*factor
print(uses)













'''
start from beginning,
index is multiplier
carrying addition
carrying remover

multiply both by the index
add the two
add the total of the two to the current bacteria level
don't actually change the carrying addition and remover
'''