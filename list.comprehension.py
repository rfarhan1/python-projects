x = 1
y = 1
z = 2
n = 3
list = []

'using for loop'
for i in range (0, x+1, 1):
    for j in range (0, y+1, 1):
        for k in range (0, z+1, 1):
            if i+j+k != n: 
                list.append([i,j,k])

print(list)

'using list comprehension'
list_comp = [[i, j, k] for i in range (0, x+1, 1) for j in range (0, y+1, 1) for k in range (0, z+1, 1) if i+j+k != n]

print(list_comp)