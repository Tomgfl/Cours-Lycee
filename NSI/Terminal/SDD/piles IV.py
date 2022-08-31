
p1 = [2,3,5,7,11,13,17,19,23,24,25]

p1.pop()
p1.pop()


for nb in range(24,40):
    i,premier = 2,True
    while i < nb and premier:
        if nb%i == 0: premier = False
        i+=1
    if premier:p1.append(nb)


while p1[-1] > 20:
    p1.pop()


for i in range(1,len(p1)+1):
    print(" ------- ")
    if len(str(p1[-i])) == 2:
        print(f"|  {p1[-i]}   |")
    else:
        print(f"|   {p1[-i]}   |")
print(" ------- ")


