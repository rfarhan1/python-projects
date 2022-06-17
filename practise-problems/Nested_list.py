name = ["Rahman", "Farhana", "Sudip", "Podder", "Partho"]
score = [55, 7, 55, 8, 7]
records = []

'creats a nested loop with names associated with the scores'
for i in range (0, len(name), 1):
    records.append ([name[i], score[i]])
print(records)

'sorting list to descending'
for i in range (0, len(records), 1):
    for j in range (i+1, len(records), 1):
        if records[i][1] <= records[j][1]:
            b = records[i]
            records [i] = records [j]
            records [j] = b
print(records)

print("lowest value of the list:", records[len(records)-1])

records1 = []
'creating a list without the lowest values(if there is any duplicate)'
for i in range (0, len(records), 1):
    if records [i][1] != records[len(records)-1][1]:
        records1.append(records [i])


print(records1)


'creating a list with all the names with second heighest scores'
result = []
for i in range (0, len(records1), 1):
    if records1[len(records1)-1][1] == records1[i][1]:
        result.append(records1[i][0])

'sorting list alphabetically'
result.sort()

'printing the elements separatelly of the alphabetically sorted list'
for i in range (0, len(result), 1):
    print(result[i])
