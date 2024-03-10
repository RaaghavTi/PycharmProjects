n, index = map(int, input().split())
pads = []

for _ in range(n):
    pad = list(map(int, input().split()))
    pads.append(pad)
index -=1
previousJump = None
targetsBroken = 0
if pads[index][0] == 1:
    targetsBroken += 1
    pads[index][0] = 2
    index += 1
power = 1
broken = []
#print(pads)
iter = 0
while index>=0 and index<n and iter<n*3:
   # print(f"index: {index}")

    if pads[index][0] == 0:
       # print("JUMP")
        if power <0:
            power -= pads[index][1]
        else:
            power += pads[index][1]
        power*=-1
      #  print(f"power: {power}")

    if pads[index][0] == 1:
        if abs(power) >=pads[index][1]:
            pads[index][0] = 2
            targetsBroken += 1
            broken.append(index)
    index += power
    iter += 1
print(targetsBroken)
#print(broken)


