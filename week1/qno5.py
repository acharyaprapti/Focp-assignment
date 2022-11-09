Lab_group=24
full=0
Num=[113,175,12]
left=0
for i in range(len(Num)):
    group=Num[i]//24
    full=full+group
    group2=Num[i]%24
    left=left+group2
print("Full group=%d"%full)
print("Leftover group=%d"%(left//Lab_group))