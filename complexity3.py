'''str1 = "aaabbc"
hash1 = {}
for item in str1:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item]+=1
flag = True
count_lenght = 0
str2 = ""
while flag:
    for key, value in hash1.items():
        if value > 0:
            str2 = str2 + key
            hash1[key] -= 1
        count_lenght += 1
        if count_lenght-1 == len(str1):
            flag = False
print(str2)'''





'''l = [8,15,17,69,71,76,45,46,54,]
k = []
for i in range(len(l)):
    if l[i]%2 == 0:
        k.append(l[i])
print(k)
total = 0
for j in range(len(k)):
    total = total + k[j]
print(total)'''