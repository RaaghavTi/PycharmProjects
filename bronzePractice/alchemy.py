n = int(input())
inventory = [''] + list(map(int, input().split()))

k = int(input())
recipes = [''] + [0] * n
for _ in range(k):
    recipe = list(map(int, input().split()))
    recipe.pop(1)
    a = recipe[0]
    recipe.pop(0)
    recipes[a] = recipe
#print(recipes)
ans = -1
craftable = True

while craftable:
    ans += 1
    need = [''] + [0] * n
    need[n] = 1
    metalsInUse = [n]
    index = 0
    while True:
        #print(inventory)
        if len(metalsInUse) == 0:
            break
        # sees if we have enough to satisfy one metal requirement

        if inventory[metalsInUse[index]] >= need[metalsInUse[index]]:
            inventory[metalsInUse[index]] -= need[metalsInUse[index]]
            #print(f"inventory[metalsInUse[index]]: {inventory[metalsInUse[index]]} - need[metalsInUse[index]]: {need[metalsInUse[index]]}")
            need[metalsInUse[index]] = 0
            metalsInUse.pop(index)
            index = 0
        else:

            if recipes[metalsInUse[index]] == 0:
                craftable = False
                break
            else:

                substitute =  recipes[metalsInUse[index]].copy()
                for x in substitute:
                    need[x] += 1
                metalsInUse.pop(index)
                metalsInUse+= substitute
                index = 0
                #print(metalsInUse)
                #print(f"recipe:{recipes[metalsInUse[index]]}")
                #print(f"metals:{metalsInUse}")
        #print(metalsInUse)
        #print(inventory)
print(ans)
'''
5
2 0 0 1 0
3
5 2 3 4
2 1 1
3 1 2

'''