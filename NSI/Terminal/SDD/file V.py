from collections import deque

d = deque("mule")

for i in range(len(d)):
    print(d[i].capitalize())
print()

d.appendleft("e")
d.append("r")

for i in range(len(d)):
    print(d[i].capitalize())
print()

d.popleft()
d.appendleft("i")
d.appendleft("s")

for i in range(len(d)):
    print(d[i].capitalize())
