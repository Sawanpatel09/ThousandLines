l = [2,5,7,6,9,4]
k = 8
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == k:
            print(l[i],l[j])
        break

