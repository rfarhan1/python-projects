from typing import ItemsView


n = 3
a = [5, 1, -2, 1, -2]
ab = []

"creating a list without duplicate values"
for i in range (0, len(a), 1): 
    if (a[i] not in ab):
        ab.append(a[i])

print(ab) 

b = -100

"highest value of the list:"                   
for i in range (0, len(ab), 1):
    if ab[i] >= b:
        b = ab[i]
        
print(b)  

"Remove the heighest value"
ab.remove(b)

c = -100

"Find the new heighest value"
for i in range (0, len(ab), 1):
    if ab[i] >= c:
        c = ab[i]

print(c)


"""for i in range (0, len(ab), 1):
    for j in range (i+1, len(ab) , 1): 
        if ab[i] > ab[j]:
            b = ab[i]
            ab[i] = ab[j]
            ab[j] = b 

k = 0
for i in range (0, len(ab), 1):
    for j in range (i+1, len(ab), 1):
        if ab[i] == ab[j]:
            k = i

ab.remove(ab[k])"""

