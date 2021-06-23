arr = [7,8,17,18,9,1,3,5,11,15,21]

target = 21

"""
# Sol 1
for i in arr:
    for j in arr:
        if (i + j) == target:
            print(i, j)
"""
"""
# Sol 2
arr.sort()
last = (len(arr) - 1)
first = 0
found = False
while last > first and not found:
    if (arr[first] + arr[last]) > target:
        last -= 1
    elif (arr[first] + arr[last]) < target:
        first += 1
    else:
        print(first, last)
        found = True
"""
"""
d = dict()
for i in arr:
    x = target - i
    if x in d:
        print(i,d[x])
    else:
        d[i] = i
"""