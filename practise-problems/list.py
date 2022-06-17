#square = [expression: i**2 iteration: for i in range (1, 12, 2) condition: if i**2 <= 100]
square =[]
for i in range (1, 12, 2):
    if i**2 <= 100:
        square.append(i**2)

print(square)