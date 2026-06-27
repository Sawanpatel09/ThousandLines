'''arr = [[7,8],[1,2]]
list1 = []
max_index = []
for i in range(len(arr[0])):
    max1 = arr[0][i]
    index1 = 0
    for j in range(len(arr)):
        if max1 < arr[j][i]:
            max1 = arr[j][i]
            index1 = j
    list1.append(max1)
    max_index.append(index1)
set1 = set(list1)
if len(set1) == 1:
    print(min(set1))
for i in max_index:
    min1 = arr[i][0]
    for j in range(len(arr[i])):
        if min1 > arr[i][j]:
            min1 = arr[i][j]
    if min1 in set1:
        print(min1)
        break'''











'''arr = [2,2,4,5]
k = 0
arr.sort()   #[1, 2, 3, 5, 6]
sub = 0
list1 = []
sam = k + arr[0]
list1.append(arr[0])
for i in range(1,len(arr)):
    if sam >= arr[i]:
        list1.append(arr[i])
    else:
        sam = arr[i] + k
        sub = sub + 1
        list1 = []
        list1.append(arr[i])



















if list1 != []:
    sub = sub + 1
print(sub)'''





'''arr = [2,2,4,5]
k = 0
check1 = 0
subsequence = 0
list1 = []
arr.sort()
i = len(arr) - 1
while i > -1:
    if list1 == []:
        if i > 0:
            diff = arr[i] - arr[i - 1]
            if diff <= k:
                check1 = arr[i]
                list1.append(arr[i])
                list1.append(arr[i-1])
                i = i - 2
            else:
                list1 = []
                subsequence = subsequence + 1
                i = i - 1
        else:
            subsequence = subsequence + 1
            i = i - 1
    elif list1 != []:
        diff = check1 - arr[i]
        if diff <= k:
            list1.append(arr[i])
            i = i - 1
        else:
            list1 = []
            subsequence = subsequence + 1
if list1 != []:
    subsequence = subsequence + 1
print(subsequence)
'''














'''arr = [7,7,7,7]
arr2 = arr.copy()
arr.sort()
hash2 = {}
list1 = []
for j in range(len(arr)):
    if arr[j] not in hash2:
        hash2[arr[j]] = j
for i in range(len(arr2)):
    list1.append(hash2[arr2[i]])
print(list1)'''











'''arr = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k = 14
arr.sort()
count = 0
matrix = []
list1 = []
for i in range(len(arr)):
    if count == 3:
        matrix.append(list1)
        list1 = []
        list1.append(arr[i])
        count = 0
        count = count + 1
    else:
        list1.append(arr[i])
        count = count + 1
matrix.append(list1)
for i in range(len(matrix)):
    if abs(matrix[i][0] - matrix[i][2]) <= k:
        pass
    else:
        print([])
        break
else:
    print(matrix)'''




# arr = [2,4,2,2,5,2]
# arr.sort()
# print(arr)
# count = 0
# matrix = []
# list1 = []
# for i in range(len(arr)):
#     if count == 3:
#         matrix.append(list1)
#         list1 = []
#         list1.append(arr[i])
#         count = 0
#         count = count + 1
#     else:
#         list1.append(arr[i])
#         count = count + 1
# matrix.append(list1)
# count1 = 0
# for i in range(len(matrix)):
#     if abs(matrix[i][0] )











'''arr = [1,3,4,8,7,9,3,5,1]
arr.sort()
print(arr)
k = 2
total = int(len(arr) / 3)
count = 0
i = 0
matrix = []
list1 = []
not_change = []
while i < len(arr)-1:
    if total == count:
        break
    if abs(arr[i] - arr[i+1]) >= k and arr[i] != arr[i+1]:
        list1.append(arr[i])
        list1.append(arr[i+1])
        list1.append(0)
        matrix.append(list1)
        list1 = []
        i = i + 2
        count = count + 1

    else:
        not_change.append(arr[i])
        i = i + 1
# if total != count:
#     print([])
if i == len(arr) - 1:
    not_change.append(arr[i])
elif i == len(arr) - 2:
    not_change.append(arr[i])
    not_change.append(arr[i+1])
list1 = not_change + arr[i:]
for j in range(len(matrix)):
    matrix[j][2] = list1[j]
    # matrix[j].sort()
matrix.append(not_change[j+1:])
print(matrix)'''









'''list1 = []
list2 = []
count = 0
for i in range(len(arr)):
    if count == 3:
        list1.append(list2)
        list2 = []
        count = 0
        list2.append(0)
        count = count + 1
    else:
        count = count + 1
        list2.append(0)
list1.append(list2)
k = 2
arr.sort()'''










'''math = int(input("enter number of math"))
phy = int(input("enter a number of phy"))
chem = int(input("enter a number of chem"))
percentage = (math + phy + chem)/3
if percentage < 33:
    print("Fail")
elif 33 <= percentage <= 60:
    print("B grade")
else:
    print("A grade")'''









'''year = int(input("enter a number"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("nOT leap year")
    else:
        print("Leap year")
else:
    print("Leap Year")
'''



'''arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr.sort()
list1 = []
for i in arr:
    id1 = str(bin(i))
    id1 = id1[2:]
    count = 0
    for j in range(len(id1)):
        if id1[j] == "1":
            count = count + 1
    list1.append(count)
hash1 = {}
for item in range(len(list1)):
    if list1[item] not in hash1:
        hash1[list1[item]] = [arr[item]]
    else:
        hash1[list1[item]].append(arr[item])
d = sorted(hash1)
list3 = []
for j in range(len(d)):
    list3 = list3 + hash1[d[j]]
print(list3)'''


















'''a = "python"
b = "python"
print(a is b)
print(id(a))
print(id(b))
'''



'''arr = [0,0]
hash1 = {}
for item in arr:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] = hash1[item] + 1
for item2 in arr:
    if (item2 * 2) in hash1 and item2 != 0:
        print(True)
        break
    elif item2 == 0 and hash1[item2] > 1:
        print(True)
        break
else:
    print(False)'''

















'''mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
target = 0
target1 = 1
for i in range(len(mat)):
    start = 0
    end = len(mat[i])
    mid = (start + end)//2
    while start <= end:
        mid = start + end // 2
        if mat[i][mid] == target and mat[i][mid - 1] == target1:
            break
        elif mid == 0 and mat[i][mid] != target1 and mat[i][mid + 1] != target:
            break
        elif mid == len(mat[i]) - 1 and mat[i][mid] != target1 and mat[i][mid - 1] != target:


        else:
            if mat[i][mid] == target and mat[i][mid-1] == target:
                end = mid
            elif mat[i][mid] == target1 and mat[i][mid-1] == target1:
                start = mid'''





















'''mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
list1 = []
for i in range(len(mat)):
    count = 0
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            count = count + 1
    list1.append(count)
list2 = list1.copy()
list1.sort()
set1 = set()
list5 = []
for j in range(k):
    for l in range(len(list2)):
        if list1[j] == list2[l]:
            if l not in set1:
                set1.add(l)
                list5.append(l)
                break
print(list5)
'''










'''arr = [1,5,2,10]
diff = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            diff1 = arr[j] - arr[i]
            if diff1 > diff:
                diff = diff1
if diff == 0:
    print(-1)
print(diff)'''













'''arr = [40,10,20,30]
arr2 = arr.copy()
arr.sort()
print(arr)
hash1 = {}
count = 1
for item in arr:
    if item not in hash1:
        hash1[item] = count
        count = count + 1
list1 = []
for item in arr2:
    list1.append(hash1[item])
print(list1)'''











'''# for i in range(len(arr)):
#     j = 0
#     k = 1
#     while j < len(arr) - (i - 1) and k < len(arr) - i:
#         if arr[j] > arr[k]:
#             arr[j],arr[k] = arr[k],arr[j]
#         j = j + 1
#         k = k + 1
# print(arr)
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while arr[j] > key and j >= 0:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
print(arr)'''













'''nums = [1,1,2,3]
list2 = []
i = 0
while i < len(nums):
        if (2 * i) < len(nums) and (2 * i + 1) < len(nums):
            list1 = [nums[2 * i], nums[2 * i + 1]]
            for j in range(list1[0]):
                list2.append(list1[1])
        i = i + 1
print(list2)'''



















'''n  = 5
list1 = []
if n % 2 != 0:
    check = int(n / 2)
    for i in range(1,check+1):
        list1.append(i)
        list1.append(-i)
    list1.append(0)
else:
    check = int(n / 2)
    for i in range(1,check+1):
        list1.append(-i)
        list1.append(i)
print(sum(list1))
print(list1)'''


'''ops = ["1","C"]
stack = []
for i in range(len(ops)):
    if ops[i] == "+":
        add = int(stack[len(stack) - 2]) + int(stack[len(stack) - 1])
        stack.append(add)
    elif ops[i] == "D":
        double = int(stack[len(stack) - 1]) * 2
        stack.append(double)
    elif ops[i] == "C":
        stack.pop()
    else:
        stack.append(int(ops[i]))
print(sum(stack))'''






















'''nums = [1,3,5,4,7]
maincount = 1
count = 1
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        count = count + 1
    else:
        if maincount < count:
            maincount = count
        count = 1

print(maincount)
'''













'''s = "aaa"
str1 = ""
list1 = []
for i in range(len(s)-1):
    list2 = []
    if s[i] == s[i+1]:
        str1 = str1 + s[i]
    elif s[i] == s[i-1] and i > 0:
        str1 = str1 + s[i]
        if len(str1) >= 3:
            list2.append(i - (len(str1)-1))
            list2.append(i)
            list1.append(list2)
        str1 = ""
    if i == len(s) - 2 and s[i] == s[len(s) - 1]:
        str1 = str1 + s[i+1]
        if len(str1) >= 3:
            list2.append(i+1 - (len(str1)-1))
            list2.append(i+1)
            list1.append(list2)
print(list1)'''











'''s = "I speak Goat Latin"
maintstr1 = ""
str2 = ""
vowel_flag = False
consonent = False
consonent_str = ""
count = 1
str5 = ""
for i in range(len(s)):
    if s[i] in {"a","e","i","o","u","A","E","I","O","U"} and str2 == "" and vowel_flag == False and consonent == False:
        vowel_flag = True
        str2 = str2 + s[i]
    elif vowel_flag == True and s[i] != " ":
        str2 = str2 + s[i]
    if s[i] not in {"a","e","i","o","u","A","E","I","O","U"} and str2 == "" and consonent == False:
        consonent = True
        consonent_str = s[i]
    elif consonent == True and s[i] != " " and consonent_str != "":
        str2 = str2 + s[i]
    if s[i] == " " or i == len(s) - 1:
        str5 = str5 + "a"
        if vowel_flag == True:
            str2 = str2 + "ma" + str5
            maintstr1 = maintstr1 + str2 + " "
            str2 = ""
            vowel_flag = False
        elif consonent == True:
            str2 = str2 + consonent_str + "ma" + str5
            maintstr1 = maintstr1 + str2 + " "
            str2 = ""
            consonent = False
            consonent_str = ""
print(maintstr1[:len(maintstr1)-1])'''

















'''s = "loveleetcode"
c = "e"
mainlist = []
for i in range(len(s)):
    if s[i] == c:
        mainlist.append(i)
mainlist.append(len(mainlist) - 1)
k = 0
index = 0
secolist = [100] * len(s)
for i in range(len(mainlist)-1):
    if i == 0:
        j = 0
    else:
        j = mainlist[i-1]
    while j < len(s):
        if j == mainlist[i+1]:
            break
        if j <= mainlist[i]:
            diff = abs(j - mainlist[i])
            if secolist[j] > diff:
                secolist[j] = diff
        elif j > mainlist[i]:
            diff = abs(j - mainlist[i])
            if secolist[j] > diff:
                secolist[j] = diff
        j = j + 1
print(secolist)
'''





























'''s = "loveleetcode"
c = "e"
sample_list = []
for i in range(len(s)):
    if s[i] == c:
        sample_list.append(i)
mainlist = []
j = 0
half = 0
for i in range(len(s)):
    if i >= sample_list[len(sample_list)-1]:
        diff = abs(i - sample_list[len(sample_list)-1])
        mainlist.append(diff)
    else:
        if i < sample_list[0]:
            diff = abs(i - sample_list[0])
            mainlist.append(diff)
        if i == sample_list[j]:
            half = (sample_list[j] + sample_list[j+1])//2
            j = j + 1
        if i >= sample_list[0]:
            if half != 0 and half < i:
                diff = abs(i - sample_list[j])
                mainlist.append(diff)
            elif half != 0 and half >= i:
                diff = abs(i - sample_list[j-1])
                mainlist.append(diff)
print(mainlist)

mainlist.insert(0,1)
print(mainlist)'''

#         elif half != 0 and i <= half:
#             diff = abs(i - sample_list[j-1])
#             mainlist.append(diff)
#         elif half != 0 and i > half:
#             diff = abs(i - sample_list[j])
#             mainlist.append(diff)
#         elif i == sample_list[j]:
#             half = sample_list[j] + sample_list[j+1]//2
#             mainlist.append(0)
#             j = j + 1
#         print(half)
# print(sample_list)
# print(mainlist)
















'''str1 = "2001:db8:0g00::1"
if "." in str1:
    l = str1.split(".")
    if len(l) == 4:
        for item in l:
            if item[0] == "0" and len(item) > 1:
                print("Neither")
                break
            elif item.isalpha():
                print("Neither")
                break
            elif item.isdigit():
                if 0 <= int(item) <= 255:
                    pass
                else:
                    print("NEITHER")
                    break
        else:
            print("IPv4")
elif ":" in str1:
    flag = False
    l2 = str1.split(":")
    if len(l2) == 8:
        for item2 in l2:
            if len(item2) == 4 and item2.isalnum() and flag == False:
                for j in item2:
                    if j.isalpha():
                        if "a" <= j <= "f" or "A" <= j <= "F":
                            pass
                        else:
                            print("Neither")
                            flag = True
                            break
            else:
                print("Neither")
                break
        else:
            print("IPv6")
    else:
        print("Neither")
else:
    print("Neither")
'''











'''# maxsubarray
list1 = [-11,-2,-3,-4]
count = float('-inf')
subarray = 0
for i in range(len(list1)):
    subarray = subarray + list1[i]
    if subarray > count:
        count = subarray
    if subarray < 0:
        subarray = 0
print(count)

count = float('-inf')
list1 = [-11,-2,-3,-4]

for i in range(len(list1)):
    subarraysum = 0
    for j in range(i, len(list1)):
        subarraysum += list1[j]
        if subarraysum > count:
            count = subarraysum
print(count)'''









'''x = ["www.a.com","www.b.com","www.c.com"]
list1 = []
for item in x:
    list1.append(item.split(".")[1] + "." + item.split(".")[2])
print(list1)'''











'''s = "abcabcbb"
str1 = ""
i = 0
str2 = ""
while i < len(s) - len(str1):
    if s[i] not in str2:
        str2 = str2 + s[i]
        i = i + 1
    else:
        str1 = str2[len(str1):len(str2)-1]
        i = i - len(str2) - 1'''








'''paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
banned = set(banned)
hash1 = {}
str1 = ""
for i in range((len(paragraph))):
    if paragraph[i] in {" ", "!", "?", "'", ",", ";", "."} and str1 != "":
        if str1 not in banned:
            if str1 not in hash1:
                hash1[str1] = 1
            else:
                hash1[str1] = hash1[str1] + 1
        str1 = ""
    elif paragraph[i] in {" ", "!", "?", "'", ",", ";", "."} and str1 == "":
        pass
    else:
        str1 = str1 + paragraph[i].lower()
if str1 != "" and str1 not in banned:
    if str1 not in hash1:
        hash1[str1] = 1
    else:
        hash1[str1] = hash1[str1] + 1
big = 0
ans = ""
for key,value in hash1.items():
    if value > big:
        big = value
        ans = key
print(ans)
print(big)'''




















        # d = paragraph[i][j].lower()
        # if d not in banned:
        #     if d not in hash1:
        #         hash1[d] = 1
        #     else:
        #         hash1[d] = hash1[d] + 1



















'''words = ["stars.bars.$"]
separator = "."
list1 = []
for i in range(len(words)):
    str1 = ""
    for j in range(len(words[i])):
        if words[i][j] == separator and str1 != "":
            list1.append(str1)
            str1 = ""
        elif words[i][j] == separator and str1 == "":
            pass
        else:
            str1 = str1 + words[i][j]
    if str1 != "":
        list1.append(str1)
        str1 = ""
print(list1)'''

















'''widths = [5,7,4,7,6,7,9,5,8,8,5,10,9,10,2,5,7,9,3,8,8,8,10,2,2,9]
s = "lgrnv"
hash1 = {}
for i in range(len(widths)):
    hash1[chr(97+i)] = widths[i]
list1 = []
lines = 1
total = 0
for item in s:
    total = total + hash1[item]
    if total <= 100:
        pass
    else:
        total = total - hash1[item]
        lines = lines + 1
        total = 0
        total = total + hash1[item]
last_wide = total
list1.append(lines)
list1.append(last_wide)
print(list1)'''










'''patterns = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabet = "abcdefghijklmnopqrstuvwxyz"
hash1 = {x:y for (x,y) in zip(alphabet,patterns)}
words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
list1 = []
for i in range(len(words)):
    str1 = ""
    for j in range(len(words[i])):
        str1 = str1 + hash1[words[i][j]]
    list1.append(str1)
print(len(set(list1)))
'''









'''s = "abcde"
goal = "abced"
for j in s:
    str1 = s[1:] + j
    s = str1
    if s == goal:
        print(True)
        break
else:
    print(False)
'''
'''s = "bbbacddceeb"
goal = "ceebbbbacdd"
str1 = s
str2 = ""
for i in range(len(s)):
    for j in range(1,len(s)):
        str2 = str2 + str1[j]
    str2 = str2 + s[i]
    if str2 == goal:
        print(True)
        break
    else:
        str1 = str2
        str2 = ""
else:
    print(False)'''










'''words = ["aa","ab"]
list1 = []
for item in words:
    d = sorted(item)
    str1 = d[0] + d[1]
    list1.append(str1)
lenght_list = len(list1)
lenght_set = len(set(list1))
total = lenght_list - lenght_set
print(total)'''









'''jewels = "aA"
stones = "aAAbbbb"
hash1 = {x : 0 for (x) in jewels}
for item in stones:
    if item in hash1:
        hash1[item] = hash1[item] + 1
sum1 = sum(hash1.values())
print(sum1)'''










'''num = "51230100"
print(num.strip("0"))'''








'''num = "51230000100"
str1 = ""
mainstr1 = ""
for i in range(len(num)):
    if num[i] == "0":
        str1 = str1 + num[i]
    elif num[i].isdigit() and str1 != "" and i != len(num) - 1:
        mainstr1 = mainstr1 + str1
        mainstr1 = mainstr1 + num[i]
        str1 = ""
    elif num[i].isdigit():
        mainstr1 = mainstr1 + num[i]
print(mainstr1)'''










'''d = "egcfe"
s = list(d)
i = 0
j = len(s) - 1
while i <= j:
    if s[i] == s[j]:
        pass
    elif s[i] < s[j]:
        s[j] = s[i]
    elif s[i] > s[j]:
        s[i] = s[j]
    i = i + 1
    j = j - 1
str1 = ""
for item in s:
    str1 = str1 + item
print(str1)'''











'''s = "CCDAABBDCD"
list1 = []
list1.append(s[0])
for i in range(1,len(s)):
    if list1 != [] and list1[len(list1)-1] + s[i] in {"AB","CD"}:
        list1.pop()
    else:
        list1.append(s[i])
print(list1)'''










# s = "BJKlDKABJ"
# i = 0
# str1 = s
# count = 0
# str2 = ""
# list1 = []
# for j in range(len(s)):
#     i = 0
#     flag = False
#     check = False
#     while i < len(str1) - 1:
#         store1 = (len(str1) - 1) - i
#         if str1[i + 1] == chr(ord(str1[i]) + 1) and store1 not in list1:
#             list1.append(i+1)
#             i = i + 2
#             check = True
#         else:
#             str2 = str2 + str1[i]
#             i = i + 1
#             if i == len(str1) - 2 and check:
#                 flag = True
#                 str2 = str2 + str1[i + 1]
#
#         if i > len(str1) - 2 and flag == False and i < len(str1):
#             str2 = str2 + str1[i]
#     str1 = str2
#     i = 0
#     str2 = ""
#     if check == False:
#         print(str1)
#         break

















'''licensePlate = "AN87005"
words = ["participant","individual","start","exist","above","already","easy","attack","player","important"]
mydict = {}
lenght = ""
for item in licensePlate:
    if item.isalpha():
        lower = item.lower()
        if lower not in mydict:
            mydict[lower] = 1
        else:
            mydict[lower] = mydict[lower] + 1
for i in range(len(words)):
    mydict1 = mydict.copy()
    for j in range(len(words[i])):
        if words[i][j] in mydict1:
            mydict1[words[i][j]] = mydict1[words[i][j]] - 1
            if mydict1[words[i][j]] == 0:
                mydict1.pop(words[i][j])
    if mydict1 == {}:
        if lenght == "":
            lenght = words[i]
        elif len(lenght) > len(words[i]):
            lenght = words[i]
print(lenght)'''





'''n = 5
count = 0
for i in range(n):
    sample = count+1
    manual = 2
    for j in range(n+count):
        if j < n-1 - count:
            print("  ",end="")
        else:
            if sample > 0:
                print("",sample,end="")
                sample = sample - 1
            else:
                print("",manual,end="")
                manual = manual + 1
    print()
    count = count + 1'''







'''s = "10101"
count = 0
for i in range(len(s)):
    balance = 0
    for j in range(i,len(s)):
        if s[j] == "0":
            balance = balance - 1
        else:
            balance = balance + 1
        if balance == 0:
            count = count + 1
            break
print(count)'''




'''s = "00011100"
sub_bin = 0
for i in range(len(s)):
    change = 1
    index = s[i]
    count_0 = 0
    count_1 = 0
    for j in range(i,len(s)):
        if index != s[j]:
            index = s[j]
            change = change + 1
        if change > 2:
            if count_0 == count_1:
                sub_bin = sub_bin + 1
            break
        if s[j] == "0":
            count_0 = count_0 + 1
        elif s[j] == "1":
            count_1 = count_1 + 1
        if count_0 == count_1:
            sub_bin = sub_bin + 1
            break
    else:
        if count_1 == count_0:
            sub_bin = sub_bin + 1
print(sub_bin)'''











'''s = "00110011"
store = 0
sub_bin = 0
index = 0
stack = list(s[0])
flag = True
for i in range(1, len(s)):
    if stack[index] != s[i] and flag == True:
        sub_bin = sub_bin + 1
        stack.append(s[i])
        if index > 0:
            index = index - 1
        else:
            flag = False
        store = len(stack) - 1
    else:
        stack.append(s[i])
        if stack[store] != s[i]:
            sub_bin = sub_bin + 1
            index = store - 1
        else:
            index = len(stack) - 1
        flag = True
print(sub_bin)'''







'''s = "eceec"
atmost = False
flag2 = False
store1 = 0
store2 = 0
i = 0
j = len(s) - 1
while j >= i:
    if s[i] == s[j]:
        i = i + 1
        j = j - 1
    elif atmost == False:
        store1 = i
        store2 = j
        atmost = True
        j = j - 1
        if s[i] == s[j]:
            i = i + 1
            j = j - 1
        elif s[i] != s[j]:
            i = i + 1
            j = j + 1
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
            else:
                print(False)
                break
    else:
        if flag2 == False:
            flag2 = True
            i = store1
            j = store2
            i = i + 1
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
            else:
                print(False)
                break
        else:
            print(False)
            break
else:
    print(True)'''














'''def count():
    count4 = 0
    def count1():
        nonlocal count4
        count4 = count4 + 1
        return count4
    if count4 < 3:
        count1()
    return

a = count()
print(a)
'''





'''def makecounter():
    count = 0
    def counter1():
        nonlocal count
        count = count + 1
        return count
    def counter2():
        nonlocal count
        count = count + 1
        return count
    return counter1(),counter2()
c1,c2 = makecounter()
print(c2)'''







'''details = ["1313579440F2036","2921522980M5644"]
count = 0
for item in details:
    str1 = item[11] + item[12]
    print(str1)
    if int(str1) > 60:
        count = count + 1
print(count)'''







'''s = "01000111"
substringlen = 0
zerocount = 0
count = 0
flag = False
for i in range(len(s)):
    if s[i] == "0" and flag == True:
        zerocount = zerocount - count
        count = 0
        if substringlen < zerocount:
            substringlen = zerocount
        count = count + 2
        flag = False
    elif s[i] == "0" and flag == False:
        count = count + 2
    elif s[i] == "1" and flag == False:
        flag = True
        zerocount = count
        count = count - 2
    elif s[i] == "1" and flag == True:
        count = count - 2
    if count < 0:
        count = 0
    if i == len(s) - 1:
        zerocount = zerocount - count
        count = 0
        if substringlen < zerocount:
            substringlen = zerocount
        count = count + 2
        flag = False
print(substringlen)'''








'''s = "00111"
stack = []
count = 0
maincount = 0
flag = False
for i in range(len(s)):
    if flag == True and s[i] == "0":
        stack = []
        count = 0
        stack.append(s[i])
        flag = False
    elif s[i] == "0":
        count = 0
        stack.append(s[i])
    elif s[i] == "1":
        flag = True
        if stack != []:
            stack.pop()
            count = count + 2
            if maincount < count:
                maincount = count
    # if stack == [] and maincount < count:
    #     maincount = count
    #     count = 0
print(maincount)
'''











'''moves = "UDDUURLRLLRRUDUDLLRLURLRLRLUUDLULRULRLDDDUDDDDLRRDDRDRLRLURRLLRUDURULULRDRDLURLUDRRLRLDDLUUULUDUUUUL"
hash1 = {"U" : 0,"D":0,"R":0,"L":0}
for i in range(len(moves)):
    hash1[moves[i]] = hash1[moves[i]] + 1
if hash1["R"] == hash1["L"] and hash1["D"] == hash1["U"]:
    print(True)
else:
    print(False)
print(hash1)'''




'''words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
count = 0
for i in range(left,right+1):
    if words[i][0] in {"a","e","i","o","u"} and words[i][len(words[i]) - 1] in {"a","e","i","o","u"}:
        count = count + 1

print(count)'''



'''s = "Let's take LeetCode contest"
list1 = s.split(" ")
str1 = ""
str2 = ""
for i in range(len(list1)):
    str1 = str1 + list1[i][::-1]
    if i == len(list1) - 1:
        pass
    else:
        str1 = str1 + " "
    str2 = str2 + str1
    str1 = ""
print(str2)'''



















'''s = "PPALL"
ab_count = 0
for i in range(len(s)):
    if i != 0 and i != len(s) - 1:
        if s[i] == "L" and s[i-1] == "L" and s[i+1] == "L":
            print(False)
            break
    if s[i] == "A" and ab_count < 2:
        ab_count = ab_count + 1
    elif ab_count >= 2:
        print(False)
        break

else:
    print(True)
'''




















'''words = ["bniieiayta","lepuduawhc","lepuduawhc","ipeusobtqm","xxdcknbaeu","okkbdtojsg","ipeusobtqm","ipeusobtqm","xxdcknbaeu","okkbdtojsg"]
target = "vdrvhwzwlm"
startIndex = 7
i = startIndex - 1
j = startIndex + 1
steps = 1
flag = True
while flag:
    if j > len(words) - 1:
        j = 0
    if words[i] == target:
        flag = False
        break
    if words[j] == target:
        flag = False
        break
    steps = steps + 1
    j = j + 1
    i = i - 1
    # if abs(i) == j:
    #     break
    if abs(i) > len(words):
        print(-1)
        flag = False
        break

print(steps)'''






'''words = ["hello","i","am","leetcode","hello"]
j = 0
count = 0
while count < len(words):
    if j > len(words) - 1 and count < len(words):
        print(words[j - len(words)],end=" ")
        count = count + 1
    else:
        print(words[j],end=" ")
    j = j + 1
'''


















'''words = ["nba","cba","dba"]
list1 = []
pair = 0
for i in range(len(words)):
    set1 = set()
    for j in range(len(words[i])):
        set1.add(words[i][j])
    str1 = ""
    for item in set1:
        str1 = str1 + item
    list1.append(str1)
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            pair = pair + 1
print(pair)
'''














'''strs = ["alic3","bob","3","4","00000"]
count = 0
for item in strs:
    if item.isdigit():
        if count < int(item):
            count = int(item)
    elif item.isalnum():
        if count < len(item):
            count = len(item)

print(count)'''




'''d = "onetwoten"
k = 3
s = []
for item1 in d:
    s.append(item1)
m = 0
str1 = ""
str2 = ""
str3 = ""
total = 0
rang1 = 0
while len(s) - m >= k:
    total = rang1
    rang1 = rang1 + 2 * k
    count1 = 0
    if rang1 < len(s):
        for i in range(total, rang1):
            if count1 >= k:
                str1 = str1 + s[i]
            else:
                str1 = s[i] + str1
            count1 = count1 + 1
    else:
        for i in range(total,len(s)):
            if count1 >= k:
                str1 = str1 + s[i]
            else:
                str1 = s[i] + str1
            count1 = count1 + 1
    str3 = str3 + str1
    str1 = ""
    m = m + 2 * k
for p in range(rang1,len(s)):
    str2 = s[p] + str2
str3 = str3 + str2
print(str3)'''









'''sentence ="Leetcode is cool"
list1 = sentence.split(" ")
for i in range(0,len(list1)):
    if list1[i-1][len(list1[i-1])-1] == list1[i][0]:
        pass
    else:
        print(False)
        break
else:
    print(True)'''


    # if i == len(list1) - 1:
    #     if list1[i][len(list1[i]) - 1] == list1[0][0]:
    #         print(True)
    #     else:
    #         print(False)







'''a = "aaa"
b = "aaa"
if a == b:
    print(-1)
flag_a = False
flag_b = False
difference_a = 0
difference_b = 0
subsequence_a = ""
subsequence_b = ""
str1 = ""
str2 = ""
for i in range(len(a) - 1):
    if flag_a == False:
        flag_a = True
        difference_a = abs(((ord(a[i]) - 97) - (ord(a[i+1]) - 97)))
        str1 = str1 + a[i] + a[i+1]
    else:
        if abs(((ord(a[i]) - 97) - (ord(a[i+1]) - 97))) == difference_a:
            str1 = str1 + a[i+1]
        else:
            if len(str1) > len(subsequence_a):
                subsequence_a = str1
            str1 = ""
            difference_a = abs(((ord(a[i]) - 97) - (ord(a[i + 1]) - 97)))
            str1 = str1 + a[i] + a[i+1]
    if flag_b == False:
        flag_b = True
        difference_b = abs(((ord(b[i]) - 97) - (ord(b[i+1]) - 97)))
        str2 = str2 + b[i] + b[i + 1]
    else:
        if abs(((ord(b[i]) - 97) - (ord(b[i + 1]) - 97))) == difference_b:
            str2 = str2 + b[i+1]
        else:
            if len(str2) > len(subsequence_b):
                subsequence_b = str2
            str2 = ""
            difference_b = abs(((ord(b[i]) - 97) - (ord(b[i + 1]) - 97)))
            str2 = str2 + b[i] + b[i+1]

if len(str1) > len(subsequence_a):
    subsequence_a = str1
if len(str2) > len(subsequence_b):
    subsequence_b = str2
if len(subsequence_a) >= len(subsequence_b):
    print(len(subsequence_a))
else:
    print(len(subsequence_b))'''






















'''word = "dbhf"
if word.isupper():
    print(True)
elif word.islower():
    print(True)
else:
    if word[0].isupper() and word[1:].islower():
        print(True)
    else:
        print(False)
'''











'''words = ["aaa","yyy","ggg","qwe"]
list1 = []
str1 = 0
for i in range(len(words)):
    camp3 = []
    for j in range(0,len(words[i])-1):
        str1 = ((ord(words[i][j+1]) - 97) - (ord(words[i][j]) - 97))
        camp3.append(str1)
    list1.append(camp3)
hash1 = {}
for k in range(1,len(list1)-1):
    if list1[k] != list1[k+1] and list1[k-1] == list1[k]:
        print(words[k+1])
        break
    elif list1[k] != list1[k-1] and list1[k+1] == list1[k]:
        print(words[k-1])
        break
    elif list1[k] != list1[k-1] and list1[k+1] == list1[k-1]:
        print(words[k])
        break
'''























'''n = 5
cun = 0
for i in range(n):
    for j in range(i+1):
        cun = cun + 1
        print(" ",cun,end="")
    print()
'''










'''event1 = ["10:00","11:00"]
event2 = ["14:00","15:00"]
str1_hh1 = event1[0][0] + event1[0][1]
str1_mm1 = event1[0][3] + event1[0][4]
str2_hh1 = event1[1][0] + event1[1][1]
str2_mm1 = event1[1][3] + event1[1][4]
str1_hh2 = event2[0][0] + event2[0][1]
str1_mm2 = event2[0][3] + event2[0][4]
str2_hh2 = event2[1][0] + event2[1][1]
str2_mm2 = event2[1][3] + event2[1][4]
flag = False
range1 = int(str1_hh1) * 60 + int(str1_mm1)
range2 = int(str2_hh1) * 60 + int(str2_mm1)
range3 = int(str1_hh2) * 60 + int(str1_mm2)
range4 = int(str2_hh2) * 60 + int(str2_mm2)
for i in range(range1 , range2+1):
    if range3 <= i <= range4:
        flag = True
print(flag)
'''














'''event1 = ["10:00","11:00"]
event2 = ["14:00","15:00"]
str_hh1 = event1[1][0] + event1[1][1]
str_mm1 = event1[1][3] + event1[1][4]
str_hh2 = event2[0][0] + event2[0][1]
str_mm2 = event2[0][3] + event2[0][4]
caltime1 = int(str_hh1) * 60 + int(str_mm1)
caltime2 = int(str_hh2) * 60 + int(str_mm2)
if caltime1 >= caltime2:
    print(True)
elif caltime1 < caltime2:
    print(False)
'''









'''s = "abcabcabcabc"
list1 = []
for item in s:
    list1.append(item)
    s = tuple(list1)
for i in range(len(s)//2):
    list1.insert(0,s[len(list1) - i - 1])
    list1.pop()
    if list(s) == list1:
        print(True)
        break'''









'''s = "abab"
list1 = []
len_str1 = 1
str1 = ""
for i in range(len(s)):
    l = 0
    for j in range(len(s)):
        str1 = str1 + s[j]
        l = l + 1
        if l == len_str1:
            list1.append(str1)
            str1 = ""
            l = 0
    len_str1 = len_str1 + 1
    l = 0
    if str1 != "":
        list1.append(str1)
    str1 = ""
    print(list1)
    if len(list1) == 1:
        print(False)
        break
    for k in range(len(list1) - 1):
        if list1[k] == list1[k+1]:
            pass
        else:
            break
    else:
        print(True)
        break
    list1 = []
else:
    print(False)'''
















'''word = "a"
list1 = []
for i in range(len(word)):
    for j in range(len(word)):
        if i == j:
            pass
        else:
            list1.append(word[j])
    hash1 = {}
    for item in list1:
        if item not in hash1:
            hash1[item] = 1
        else:
            hash1[item] = hash1[item] + 1
    list2 = []
    for value in hash1.values():
        list2.append(value)
    list2.sort()
    if list2[0] == list2[len(list2) - 1]:
        print(True)
        break
    list1 = []
else:
    print(False)'''





























'''s = "abcdabcdabcdabcdabcd"
print(len(s))
if len(s) % 2 == 0:
    half = int(len(s) / 2)
    str1 = s[:half]
    str2 = s[half:]
    if str1 == str2:
        print(False)
    else:
        i = 2
        k = 0
        str1 = s[:i]
        flag = True
        while i <= len(s):
            if str1 == s[k:i]:
                k = k + i
                i = i + 2
            else:
                k = 0
                i = i + 2
                str1 = s[:i]
            if str1 == s[k:i] and i == len(s):
                print(True)
            elif str1 != s[k:i] and i == len(s):
                print(False)

elif len(s) % 3 == 0:
    i = 3
    k = 0
    str1 = s[:i]
    flag = True
    while i <= len(s):
        if str1 == s[k:i]:
            k = k + 3
            i = i + 3
        else:
            k = 0
            i = i + 3
        if str1 == s[k:i] and i == len(s):
            print(True)
        elif str1 != s[k:i] and i == len(s):
            print(False)

'''








'''time = "??:??"
count = 0
list1 = []
for j in time:
    list1.append(j)
list2 = []
for i in range(24):
    sample_time = ["0", "0", ":", "0", "0"]
    for j in range(60):
        if len(str(i)) == 1:
            sample_time[1] = str(i)
        elif len(str(i)) == 2:
            str3 = str(i)
            sample_time[0] = str3[0]
            sample_time[1] = str3[1]
        if len(str(j)) == 1:
            sample_time[4] = str(j)
        elif len(str(j)) == 2:
            str4 = str(j)
            sample_time[3] = str4[0]
            sample_time[4] = str4[1]
        list2.append(sample_time)
        sample_time = ["0", "0", ":", "0", "0"]

for k in range(len(list2)):
    for l in range(len(list2[k])):
        if list1[l].isdigit():
            if list1[l] == list2[k][l]:
                pass
            else:
                break
    else:
        count = count + 1
print(count)'''





'''time = "?5:00"
list1 = []
for j in time:
    list1.append(j)
list2 = []
for i in range(24):
    sample_time = ["0","0",":","0","0"]
    for j in range(60):
        if len(str(i)) == 1:
            sample_time[1] = str(i)
        elif len(str(i)) == 2:
            str3 = str(i)
            sample_time[0] = str3[0]
            sample_time[1] = str3[1]
        if len(str(j)) == 1:
            sample_time[4] = str(j)
        elif len(str(j)) == 2:
            str4 = str(j)
            sample_time[3] = str4[0]
            sample_time[4] = str4[1]
        
        list2.append(sample_time)
        sample_time = ["0", "0", ":", "0", "0"]
'''













'''time = "?5:00"
list1 = []
for item in time:
    list1.append(item)
list2 = []
str1 = list1[:2]
if str1[0] == "?":
    str1[0] = "0"
if str1[1] == "?":
    str1[1] = "0"
count = 0
for i in range(23):
    str1[0] = str(i)
    if int(str1[0] + str1[1]) < 24:
        list2.append(int(str1[0] + str1[1]))
        count = count + 1
print(list2)
'''





'''s = "a0001afds-"
k = 4
list1 = s.split("-")
str1 = ""
for item in list1:
    str1 = str1 + item
str2 = ""
count = 0
rema = len(str1) % k
if rema > 0:
    str3 = str1[:rema].upper()
    if len(str1) == 1:
        str2 = str2 + str3
    else:
        str2 = str2 + str3 + "-"
for i in range(rema,len(str1)):
    if count == k:
        str2 = str2 + "-" + str1[i].upper()
        count = 0
        count = count + 1
    else:
        str2 = str2 + str1[i].upper()
        count = count + 1
print(str2)'''








'''time = "?5:00"
list1 = []
list2 = []
for item in time:
    list1.append(item)
    list2.append(item)
min_time = 0
max_time = 1440
str1 = ""
for i in range(len(list1)):
    if list1[i] == "?":
        list1[i] = str(0)
    if i == 1:
        str1 = list1[0] + list1[1]
        min_time = int(str1) * 60
    if i == 4:
        str1 = list1[3] + list1[4]
        min_time = min_time + int(str1)
print(min_time)
'''












'''s = "ababab"
str1 = s[0]
for i in range(1,len(s)):
    if str1 == s[:i]:
        str1 = s[:i]
    else:
        str1 = str1 + s[i]'''



















'''s = "ababab"
end = len(s)
mid = end//2
str1 = ""
str2 = ""
start = 0
for i in range(len(s)):
    str1 = s[:mid-1]
    str2 = s[mid+1:end+1]
    if str1 == str2:
        print(True)
        break
    else:
        end = mid
        mid = end//2
    print(str1)
print(str1)
print(str2)
'''







'''
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
hash1 = {}
for i in range(len(names)):
    hash1[heights[i]] = names[i]
heights.sort(reverse=True)
list1 = []
for j in range(len(heights)):
    value = hash1[heights[j]]
    list1.append(value)
print(list1)'''












'''arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-16"
list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list2 = []
count = 0
for item in list1:
    count = count + item
    list2.append(count)
alice_arrive_int = arriveAlice.split("-")
alice_arrive = list2[int(alice_arrive_int[0]) - 1] - (list1[int(alice_arrive_int[0]) - 1] - int(alice_arrive_int[1]))
alice_leave_int = leaveAlice.split("-")
alice_leave = list2[int(alice_leave_int[0]) - 1] - (list1[int(alice_leave_int[0]) - 1] - int(alice_leave_int[1]))
bob_arrive_int = arriveBob.split("-")
bob_arrive = list2[int(bob_arrive_int[0]) - 1] - (list1[int(bob_arrive_int[0]) - 1] - int(bob_arrive_int[1]))
bob_leave_int = leaveBob.split("-")
bob_leave = list2[int(bob_leave_int[0]) - 1] - (list1[int(bob_leave_int[0]) - 1] - int(bob_leave_int[1]))
diff = 0
print(alice_arrive)
print(alice_leave)
print(bob_arrive)
print(bob_leave)
if bob_arrive < alice_arrive < alice_leave < bob_leave:
    diff = alice_leave - alice_arrive + 1
elif alice_leave == alice_arrive == bob_arrive == bob_leave:
    diff = 1
elif alice_arrive < bob_leave == bob_arrive < alice_leave:
    diff = bob_leave - alice_arrive
elif alice_arrive < bob_arrive < bob_leave < alice_leave:
    diff = bob_leave - bob_arrive + 1
elif bob_arrive < alice_arrive < bob_leave < alice_leave:
    diff = bob_leave - alice_arrive + 1
elif alice_leave > bob_arrive and bob_leave > alice_arrive:
    diff = alice_leave - bob_arrive + 1
elif bob_leave > alice_arrive and alice_leave > bob_arrive:
    diff = bob_leave - alice_arrive + 1
else:
    diff = 0
print(diff)'''












'''s = "Hello, my name is John"
str1 = ""
list1 = []
for i in range(len(s)):
    if s[i] == " " and str1 != "":
        list1.append(str1)
        str1 = ""
    else:
        str1 = str1 + s[i]
list1.append(str1)
print(list1)'''






'''s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hash1 = {}
for i in range(len(s)):
    if s[i] not in hash1:
        hash1[s[i]] = i
    else:
        hash1[s[i]] = abs(hash1[s[i]] - i) - 1
for key,value in hash1.items():
    if distance[ord(key)-97] == value:
        pass
    else:
        print(False)
        break
else:
    print(True)'''







'''blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW"
k = 29
count  = 0
f = blocks[:k]
print(len(f))
for item in f:
    if item == "W":
        count = count + 1
print(count)'''






'''
blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW"
k = 29
window = ""
last_count = 0
local_count = 0
count = 0
for i in range(len(blocks)):
    if len(window) <= k-1:
        window = window + blocks[i]
        if blocks[i] == "W":
            count = count + 1
    elif len(window) >= k:
        if last_count == 0:
            local_count = count
        if last_count == 0:
            local_count = count
        if window[last_count] == "W" and blocks[i] == "B":
            count = count - 1
        elif window[last_count] == "B" and blocks[i] == "W":
            count = count + 1
        if last_count == 0 and local_count > count:
            local_count = count
        elif local_count > count:
            local_count = count
        last_count = last_count + 1
        window = window + blocks[i]

if last_count == 0:
    local_count = count
print(local_count)
'''



















'''pattern = "abba"
s = "dog dog dog dog"
list1 = s.split(" ")
mydict ={}
for i in range(len(list1)):
    if pattern[i] not in mydict:
        if list1[i] not in mydict.values():
            mydict[pattern[i]] = list1[i]
        else:
            print(False)
            break
    else:
        if mydict[pattern[i]] == list1[i]:
            pass
        else:
            print(False)
            break
else:
    print(True)
'''




'''number = "5646"
digit = "6"
str1 = ""
maxmized = 0
for i in range(len(number)):
    if int(number[i]) == int(digit):
        str1 = ""
        str1 = str1 + number[:i] + number[i+1:len(number)]
        if maxmized < int(str1):
            maxmized = int(str1)
print(maxmized)'''







'''arr = [1,2,10,15,18,19,22,90,875,1234,123453,1232156]
target = 10
start = 0
end = len(arr)
mid = (start + end)//2
i = 0
while arr[mid] != target:
    print(i)
    if target > arr[mid]:
        start = mid
    elif target < arr[mid]:
        end = mid
    # elif target == arr[mid]:
    #     print(mid)
    mid = (start+end)//2
    i = i + 1
print(mid)'''








'''s = "K1:L2"
alpha_list1 = []
combination_list = []
str1 = ""
for i in range(ord(s[0]),ord(s[3]) + 1):
    alpha_list1.append(chr(i))
for k in range(len(alpha_list1)):
    for j in range(int(s[1]), int(s[4]) + 1):
        str1 = str1 + alpha_list1[k] + str(j)
        combination_list.append(str1)
        str1 = ""
print(combination_list)'''








'''# 2185. Counting Words With a Given Prefix
words =  ["leetcode","win","loops","success"]
prefix = "code"
count = 0
for i in range(len(words)):
    j = 0
    k = 0
    while k < len(prefix) and len(words[i]) >= len(prefix):
        if prefix[k] == words[i][k]:
            k = k + 1
        else:

            j = j + 1
            break
    else:
        if len(prefix) <= len(words[i]):
            count = count + 1
print(count)'''





'''from collections import deque
d = deque()
d.append("dg")
list1 = []
list1.insert(1,"12")
list1.insert(1,"245")'''





'''s = "aacc"
t = "ccac"
list1 = [0]*26 
    list1[ord(s[i]) - 97] = list1[ord(s[i]) - 97] + 1
    list2[ord(t[i]) - 97] = list2[ord(t[i]) - 97] + 1
for i in range(len(list1)):
    if list1[i] == list2[i]:
        pass
    else:
        print(False)
        break
else:
    print(True)'''








'''s = "ab"
t = "a"

rang1 = ""
set1 = set()
if len(t) >= len(s):
    set1 = set(s)
    rang1 = t
else:
    set1 = set(t)
    rang1 = s
for item in rang1:
    print(item)
    if item not in set1:
        print(False)
        break
else:
    print(True)
'''
# 2138. Divide a String Into Groups of Size k
'''s = "abcdefghi"
list1 = []
str1 = ""
k = 4
fill = "x"
count = 0
for i in range(len(s)):
    count = count + 1
    str1 = str1 + s[i]
    if count == k:
        list1.append(str1)
        str1 = ""
        count = 0
    if i == len(s) - 1 and str1 != "":
        for j in range(count,k):
            str1 = str1 + fill
        list1.append(str1)
print(list1)'''














'''s = "badc"
t = "baba"
set1 = set(s)
set2 = set(t)
print(set1 == set2)'''



'''
s = "badc"
t = "baba"
mydict_s = {}
mydict_t = {}
for i in range(len(s)):
    if s[i] not in mydict_s:
        mydict_s[s[i]] = 1
    else:
        mydict_s[s[i]] = mydict_s[s[i]] + 1
    if t[i] not in mydict_t:
        mydict_t[t[i]] = 1
    else:
        mydict_t[t[i]] = mydict_t[t[i]] + 1
print(mydict_t)
print(len(mydict_s))
if len(mydict_t) != len(mydict_s):
    print("false")


i = 0
j = 0
mydict = {}
while i < len(s) and j < len(t):
    if s[i] not in mydict:
        mydict[s[i]] = t[j]
    else:
        if mydict[s[i]] == t[j]:
            pass
        else:
            print(False)
            break
    i = i + 1
    j = j + 1
else:
    print(True)
print(mydict)'''







'''def check(n):

n = [1,4,7,4,3]
print(check(n))
'''


'''n = 12
f1 = 1
f2 = 1
for i in range(n):
    if i < 2:
        print(1)
    else:
        res = f1 + f2
        f2 = f1
        f1 = res
        print(res)
'''









'''list1 = [12,8,10,666666,1,5,89]
for i in range(1,len(list1)):
    key = list1[i]
    j = i-1
    while key < list1[j] and j >= 0:
        list1[j+1] = list1[j]
        j = j - 1
    list1[j+1] = key
print(list1)'''




'''list1 = [4,10,1,3,2,9,8]
j = 0
backcounting = 1
for i in range(len(list1)):
    print(list1)
    if list1[j] < len(list1):
        if list1[j] != j + 1:
            list1[list1[j] - 1],list1[j] = list1[j], list1[list1[j] - 1]
        if list1[j] == j + 1:
            j = j + 1
    else:
        if list1[j] > list1[len(list1) - backcounting]:
            list1[len(list1)-backcounting],list1[j] = list1[j], list1[len(list1)-backcounting]
        elif list1[j] < list1[len(list1) - 1]:
            list1[len(list1)-(backcounting-1)],list1[j] = list1[j] ,list1[len(list1) - (backcounting-1)]
        backcounting  = backcounting + 1
print(list1)
'''





'''#implement cycle sorting
list1 = [5,2,3,1,4,6,8]
j = 0
for i in range(len(list1)):                                           #basic cycle sorting-------------------~~~~~~~~~~~~~~~~~~`==============
    if list1[j] != j + 1:
        list1[list1[j]-1],list1[j] = list1[j],list1[list1[j]-1]
    elif list1[j] == j + 1:
        j = j + 1
print(list1)
'''


'''
s = "ba"
str1 = s[0]
flag = False
if s[0] == "b":
    for i in range(len(s)):
        if s[i] != "b":
            print(False)
            break
        else:
            pass

for i in range(len(s)):
    if s[i] != str1 and flag == False:
        str1 = s[i]
        flag = True
    if flag == True and s[i] != str1:
        print(False)
        break
else:
    print(True)'''















'''title = "capiTalIze tHe of titLe"
list1 = title.split()
for i in range(len(list1)):
    if len(list1[i]) <= 2:
        d = list1[i].lower()
        list1[i] = d
    else:
        str1 = ""
        for j in range(len(list1[i])):
            if j == 0:
                d = list1[i][j].upper()
                str1 = str1 + d
            elif list1[i][j].isupper():
                d = list1[i][j].lower()
                str1 = str1 + d
            else:
                str1 = str1 + list1[i][j]
        list1[i] = str1
str2 = ""
for i in range(len(list1)):
    if i == len(list1) - 1:
        str2 = str2 + list1[i]
    else:
        str2 = str2 + list1[i] + " "

print(str2)'''










'''words = ["def","ghi"]
for i in range(len(words)):
    str1 = ""
    for j in range(len(words[i])):
        str1 = words[i][j] + str1
    if words[i] == str1:
        print(words[i])
        break
else:
    print("")'''









'''str1 = "B0B6G0R6R0R6G9G6R9B9"
mydict = {}
for i in range(1,len(str1),2):
    if str1[i] not in mydict:
        mydict[str1[i]] = [0]*3
        if str1[i-1] == "R":
            mydict[str1[i]][0] = 1
        elif str1[i-1] == "B":
            mydict[str1[i]][1] = 1
        elif str1[i-1] == "G":
            mydict[str1[i]][2] = 1
    else:
        if str1[i-1] == "R":
            mydict[str1[i]][0] = mydict[str1[i]][0] + 1
        elif str1[i-1] == "B":
            mydict[str1[i]][1] = mydict[str1[i]][1] + 1
        elif str1[i-1] == "G":
            mydict[str1[i]][2] = mydict[str1[i]][2] + 1
print(mydict)
count = 0
for value in mydict.values():
    if value[0] > 0 and value[1] > 0 and value[2] > 0:
        count = count + 1
print(count)'''





'''str1 =  "G4"
count = 0
str2 = ""
for i in range(1,len(str1),2):
    list1 = [0] * 3
    for j in range(1,len(str1),2):
        if str1[i] == str1[j] and str1[i] not in str2:
            if str1[j-1] == "R":
                list1[0] = 1
            elif str1[j-1] == "G":
                list1[1] = 1
            elif str1[j-1] == "B":
                list1[2] = 1
    str2 = str2 + str1[i]
    if list1[0] == 1 and list1[1] == 1 and list1[2] == 1:
        count = count + 1
print(count)'''







'''sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
list1 = []
for i in range(len(sentences)):
    str1 = sentences[i]
    d = str1.split()
    leng = len(d)
    list1.append(leng)
print(max(list1))
'''











'''columnTitle = "FXSHRXW"
n = len(columnTitle) - 1
m = columnTitle
multiple = 1
number = 0
g = 1
while n != -1:
    if n == len(columnTitle) - 1:
        number = number + (ord(m[n]) - 64)
        n = n - 1
    else:
        g = g * 26
        number = number + (g * (ord(m[n]) - 64))
        n = n - 1
print(number)'''




'''n = 89
str1 = ""
if n <= 26:
    print(chr(n + 64))
while n > 26:
    remainder = n % 26
    m = (n-remainder) / 26
    if remainder == 0:
        m = m - 1
        remainder = 26
        str1 = " " + str(remainder) + " " + str1
    else:
        str1 = " " + str(remainder) + " " + str1
    if m <= 26 and m != 0:
        str1 = " "+str(int(m))+" " + str1
    n = m
str2 = ""
list1 = str1.split()
for item in list1:
    str2 = str2 +  chr(int(item) + 64)
print(str2)'''



'''n = 2
j  = 0
k = 0
str1 = ""
str3 = ""
for i in range(n):
    ch1 = k + 97
    if k <= 25:
        k = k + 1
    if ch1 <= 122:
        str1 = ""
        str1 = str1 + chr(ch1)
    else:
        k = 0
        ch2 = j + 97
        str3 = str3 + chr(ch2)
        str1 = ""
        str1 = str1 + chr(k+97)
str3 = str3 + str1
print(str3)'''






'''word = "poazaeuioauoiioaouuouaui"
result = []
n = len(word)
for i in range(n):
    count = [0]*5
    curr = ""
    for j in range(i,n):
        ch = word[j]
        if ch not in "aeiou":
            break
        curr = curr + word[j]
        if ch == "a":
            count[0] = count[0] + 1
        elif ch == "e":
            count[1] = count[1] + 1
        elif ch == "i":
            count[2] = count[2] + 1
        elif ch == "o":
            count[3] = count[3] + 1
        elif ch == "u":
            count[4] = count[4] + 1
    for k in range(5):
        if count[k] == 0:
            break
    else:
        result.append(curr)

print(len(result))'''









'''words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
mydict1 = {}
mydict2 = {}
count = 0
for item in words1:
    if item not in mydict1:
        mydict1[item] = 1
    else:
        mydict1[item] = mydict1[item] + 1
for item in words2:
    if item  not in mydict2:
        mydict2[item] = 1
    else:
        mydict2[item] = mydict2[item] + 1
for key,value in mydict1.items():
    if value == 1 and key in mydict2 and mydict2[key] == 1:
        count = count + 1

print(count)'''











'''word = "aeiouu"
mainstr = ""
for i in range(len(word)):
    str1 = word[i:len(word)-i]
    list1 = list(str1)
    set1 = set(list1)
    list2 = list(set1)
    list2.sort()
    if ["a","e","i","o","u"] == list2:
        mainstr = str1
        break
print(mainstr)'''







'''word = "poazaeuioauoiioaouuouaui"
str1 = ""
for i in range(len(word)):
    if i != len(word) - 1:
        if word[i] in ("a","e","i","o","u"):
            if word[i+1] in ("a","e","i","o","u"):
                str1 = str1 + word[i]
            elif word[i-1] in ("a","e","i","o","u") and len(str1) >= 4:
                str1 = str1 + word[i]
            else:
                str1 = ""
    if i == len(word) - 1 and word[i] in ("a","e","i","o","u") and word[i-1] in ("a","e","i","o","u"):
        str1 = str1 + word[i]'''


















'''word1 = "abcdeef"
word2 = "abaaacc"
mydict_str1 = {}
mydict_str2 = {}
for i in range(len(word1)):
    if word1[i] not in mydict_str1:
        mydict_str1[word1[i]] = 1
    else:
        mydict_str1[word1[i]] = mydict_str1[word1[i]] + 1
    if word2[i] not in mydict_str2:
        mydict_str2[word2[i]] = 1
    else:
        mydict_str2[word2[i]] = mydict_str2[word2[i]] + 1
for i in range(len(word1)):
    if word1[i] not in mydict_str2:
        diff = abs(mydict_str1[word1[i]] - 0)
        if diff > 3:
            print(False)
            break
    else:
        diff = abs(mydict_str1[word1[i]] - mydict_str2[word1[i]])
        if diff > 3:
            print(False)
            break
    if word2[i] not in mydict_str1:
        diff = abs(mydict_str2[word2[i]] - 0)
        if diff > 3:
            print(False)
            break
        else:
            diff = abs(mydict_str2[word2[i]] - mydict_str1[word2[i]])
            if diff > 3:
                print(False)
                break
else:
    print(True)
'''






'''sentence =" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
s = sentence.split()
print(s)
count = 0
for i in range(len(s)):
    if s[i].isalpha():
        count = count + 1
    elif s[i].isdigit():
        pass
    else:
        count_hyph = 0
        count_punc = 0
        flag = False
        for j in range(len(s[i])):
            if s[i][j].isdigit():
                break
            if s[i][j] in ("!",",","."):
                if j == len(s[i]) - 1:
                    pass
                else:
                    break
            if s[i][j] == "-":
                if j != 0 and j != len(s[i]) - 1 and count_hyph < 1:
                    count_hyph = count_hyph + 1
                    if s[i][j+1].isalpha():
                        pass
                    else:
                        break
                    pass
                else:
                    break
            if j == len(s[i]) - 1:
                count = count + 1
                print(s[i])
print(count)'''












'''sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
d = sentence.split()
count = 0
str1 = ""
for i in range(len(d)):
    flag = False
    if i == 0 and d[i] in ("!",",",".") and len(d[i]) == 1:
        continue
    if d[i].isalpha():
        count = count + 1
        print(d[i])

    else:
        for j in range(len(d[i])):
            if d[i][j] == "-":
                if j == 0 or j == len(d[i]) - 1:
                    break
                elif flag == True:
                    flag = False
                    count = count - 1
                    break
                else:
                    flag = True
                    count = count + 1
            if d[i][j] in ("!",",","."):
                if j != len(d[i]) - 1:
                    break
                else:
                    count = count + 1
                    print(d[i])
            if d[i][j].isdigit():
                break
print(count)'''











'''sentence = ". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5"
d = sentence.split()
print(d)
count = 0
str1 = ""
for i in range(len(d)):
    count_punctutation = 0
    count_hyphrn = 0
    for j in range(len(d[i])):
        if d[i][j] in ("!",",","."):
            if j == 0 and len(d[i]) > 1:
                str1 = ""
                break
            elif j != len(d[i]) - 1:
                str1 = ""
                break
            else:
                count_punctutation = count_punctutation + 1
            if len(d[i]) == 1:
                str1 = str1 + d[i][j]
        elif d[i][j].isdigit():
            str1 = ""
            break
        elif d[i][j] == "-":
            if j == 0 or j == len(d[i][j]) - 1:
                str1 = ""
                break
            else:
                count_hyphrn = count_hyphrn + 1
        else:
            str1 = str1 + d[i][j]
    if str1 != "" and count_hyphrn < 2 and count_hyphrn < 2:
        print(str1)
        count = count + 1
    else:
        str1 = ""
print(count)'''







'''s = "A man, a plan, a canal: Panama"
d = s.replace(" ","")
f = d.split(".,:!@#$%^&*(){};'[]\|+_-~`<>?/", "")'''


'''s = "0P"
str1 = ""
for item in s:
    if item.isalpha():
        if item.isupper():
            str1 = str1 + item.lower()
        else:
            str1 = str1 + item
    elif item.isdigit():
        str1 = str1 + item
str2 = ""
for item2 in str1:
    str2 = item2 + str2
if str1 == str2:
    print(True)
else:
    print(False)'''






'''s = "2 3 4 6 7 8 10 royal reach 12"
d = s.split()
print(d)
'''



'''s = "2 3 4 6 7 8 10 royal reach 12"
str1 = ""
list1 = []
for i in range(len(s)):
    if "1" <= s[i] <= "9" and "1" <= s[i-1] <= "9":
        str1 = str1 + s[i]
    elif "1" <= s[i] <= "9":
        str1 = str1 + s[i]
    else:
        if "0" == s[i] and ("1" <= s[i-1] <= "9" or "1" <= s[i+1] <= "9"):
            str1 = str1 + s[i]
        if str1 != "":
            list1.append(int(str1))
            str1 = ""
    if i == len(s) - 1 and str1 != "":
        list1.append(int(str1))

i = 0
j = 0
while i < len(list1) - 1:
    j = i+1
    if list1[i] < list1[j]:
        pass
    else:
        print(False)
        break
    i = i + 1
else:
    print(True)
print(list1)'''




'''arr  = ["d","b","c","b","c","a"]
from collections import Counter
count = Counter(arr)
y = sorted(count.items(),key = lambda items:items[1])'''





'''arr  = ["d","b","c","b","c","a"]
k = 2
distinct = ""
mydict = {}
for i in range(len(arr)):
    if arr[i] not in mydict:
        mydict[arr[i]] = 1
    else:
        mydict[arr[i]] = mydict[arr[i]] + 1
for j in range(len(arr)):
    if mydict[arr[j]] == 1:
        k = k - 1
        distinct = arr[j]
    if k == 0:
        print(distinct)
        break
else:
    print(" ")'''












'''list2 = [56,89,12,89,6]
list1 = {9,2,12,14,56}
count = 0
for i in list1:
    if i in list2:
        count = count + 1
print(count)'''


'''s = "XXXXX"
move = 0
i = 0
while i < len(s):
    if s[i] == "X":
        move = move + 1
        i = i + 3
    else:
        i = i + 1
print(move)
'''


'''s = "XXXXX"
list1 = list(s)
move = 0
i = 0
flag = False
while i < len(list1):
    if i + 3 < len(list1) and list1[i] == "X":
       if "X" in (list1[i],list1[i+1],list1[i+2]):
           flag = True
           list1[i] = "0"
           list1[i+1] = "0"
           list1[i+2] = "0"
           move = move + 1
           i = i + 3
    else:
        if i == len(list1) - 1 and list1[i] == "X":
            flag = True
            list1[i] = "0"
            list1[i-1] = "0"
            list1[i-2] = "0"
            move = move + 1
            i = i + 3
        elif i == len(list1) - 2 and list1[i] == "X":
            flag = True
            list1[i] = "0"
            list1[i+1] = "0"
            list1[i-1] = "0"
            move = move + 1
            i = i + 3
    if flag == True:
        flag = False
    else:
        i = i + 1
print(move)'''














'''operations = ["--X","X++","X++"]
count = 0
for i in range(len(operations)):
    if operations[i] == "--X" or operations[i] == "X--":
        count = count - 1
    else:
        count = count + 1
print(count)
'''





'''list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = []
for i in range(len(list1)):
    list3 = []
    for j in range(len(list1[i])-1,-1,-1):
        list3.append(list1[j][i])
    list2.append(list3)


print(list2)'''







'''word = "abcdefd"
ch = "d"
str1 = ""
flag = False
for i in range(len(word)):
    if flag == False:
        str1 = word[i] + str1
    if word[i] == ch and flag == False:
        flag = True
        continue
    if flag == True:
        str1 = str1 + word[i]
    if flag == False and i == len(word) - 1:
        print(word)
print(str1)
'''













'''s = "abcdeaa"
freq_count = [0]*26
count = 0
count2 = 0
for i in range(len(s)):
    index = ord(s[i]) - ord("a")
    freq_count[index] = freq_count[index] + 1
    count = count + 1
for j in range(len(freq_count)):
    if count2 < count:
        index = chr(j + ord("a"))
        print(index, freq_count[j])
    count2 = count2 + 1

'''









'''def process(funct,text):
    return funct(text)

def check(text):
    return text.upper()


s = "sawan"
print(process(check,s))
'''




'''str1 = "abc123"
total = 0
for i in range(len(str1)):
    try:
        total = total + int(str1[i])
    except:
        pass

print(total)'''




'''def check(*args):
    print(args)
a = "a"
b = "b"
c = "d"
check(a,b,c)'''

'''def check2(**kwargs):
    print(kwargs)


check2(name = " sawan",surname = "patel")'''

'''list1 = [1,10,7,11,13,14]
first_largest = 0
second_laregst = 0
for i in range(len(list1)):
    if first_largest < list1[i] and second_laregst <= first_largest:
        second_laregst = first_largest
        first_largest = list1[i]
    if second_laregst < list1[i] and list1[i] < first_largest:
        second_laregst = list1[i]
print(second_laregst)'''



'''a = "11"
b = "1"
a_int = int(a,2)
b_int = int(b,2)
total = bin(a_int + b_int)[:]
# total = total[2:]
print(total)'''






'''def stringcheck(s):
    answer = 0
    previous_word_lenght = 0
    for i in range(len(s)):
        if s[i] != " ":
            answer = answer + 1
        else:
            if answer != 0:
                previous_word_lenght = answer
            answer = 0
    return answer if s[len(s)-1] != " " else previous_word_lenght

s = "Hello World"
print(stringcheck(s))'''





'''s =  "   fly me   to   the moon  "
print(s.strip().split())'''







'''s =  "Hello World"
str1 = ""
list1 = []
for i in range(len(s)):
    if str1 == " " and s[i] == " ":
        pass
    elif s[i].isalpha():
        str1 = str1 + s[i]
    elif str1 != "" and s[i] == " ":
        list1.append(str1)
        str1 = ""
    if str1 != "" and i == len(s)-1:
        list1.append(str1)
print(len(list1[len(list1)-1]))'''




'''arr = [1,1,1,4]
alextotal = 0
bobtotal = 0
arr2 = arr
while len(arr2) != 0:
    alextotal = alextotal + arr2[len(arr2)-1]
    arr2.pop()
    if len(arr2) != 0:
        bobtotal = bobtotal + arr2[len(arr2) - 1]
        arr2.pop()
abs_diff = abs(alextotal - bobtotal)
print(abs_diff)'''




'''patterns =  ["a","a","a"]
word = "ab"
count = 0
for patter in patterns:
    if patter in patterns:
        count = count + 1
print(count)'''




'''patterns =  ["a","a","a"]
word = "ab" 
str1 = ""
mydict = {}
for i in range(len(word)):
    j = i
    while j < len(word):
        str1 = str1 + word[j]
        j = j + 1
        mydict[str1] = 0
    str1 = ""
count = 0
for item in patterns:
    if item in mydict:
        count = count + 1
print(count)'''








'''s = "ccccccccc"
words = ["c","cc"]
str1 = ""
j = 0
slicing = 0
while slicing < len(s):
    if s[slicing : len(words[j])+slicing] == words[j]:
        slicing = slicing + len(words[j])
    else:
        print("False")
        break
    j = j + 1
    if j == len(words):
        break
'''


















'''str1 = "123abcd"
sum1 = 0
for item in str1:
    if "1" <= item <= "9":
        sum1 = sum1 + int(item)
print(sum1)
'''






'''word = "abc"
str1 = "abcdefghijklmnopqrstuvwxyz"
seconds = 0
for i in range(len(word)):
    if i == 0:
        j = 0
        k = 0
    else:
        j = str1.index(word[i - 1])
        k = str1.index(word[i - 1])
    count1 = 0
    count2 = 0
    while str1[j] != word[i]:
        count1 = count1 + 1
        if j == len(str1) - 1:
            j = 0
        else:
            j = j + 1
    while str1[k] != word[i]:
        count2 = count2 + 1
        k = k - 1
    if count1 >= count2:
        seconds = seconds + count2 + 1
    else:
        seconds = seconds + count1 + 1
    print(seconds)
print(seconds)
'''





'''seconds = 0
for i in range(len(word)):
    if i == 0 and word[i] == "a":
        seconds = seconds + 1
    else:
        count1 = 0
        count2 = 0
        j = 0
        while j < str1.index(word[i]):
            count1 = count1 + 1
            j = j + 1
        k = str1.index(word[i])-1
        while k > 0:
            count2 = count2 + 1
            k = k - 1
        i'''










'''word = "zjpc"
seconds = 0
str1 = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(word)):
    if i == 0 and word[i] == "a":
        seconds = seconds + 1
    else:
        count1 = 1
        count2 = 1
        if str1.index(word[i]) > 13:
            for j in range(str1.index(word[i]),len(str1)):
                if str1[j] != word[i]:
                    count1 = count1 + 1
                else:
                    break
        if str1.index(word[i]) < 12:
            for k in range(len(str1) - 1, str1.index(word[i]) - 1, -1):
                if str1[k] != word[i]:
                    count2 = count2 + 1
                else:
                    break
        if count1 >= count2:
            print(count2)
            seconds = seconds + count2 + 1
        else:
            print(count1)
            seconds = seconds + count1 + 1
print(seconds)'''










'''str1 = "leetcode"
str2 = ""
k = 2
times = 0
total = 0
for i in range(len(str1)):
    count = ord(str1[i]) - 96
    str2 = str2  + str(count)
while times < k:
    j = 0
    while j < len(str2):
        total = total + int(str2[j])
        j = j + 1
    times = times + 1
    str2 = str(total)
    total = 0
print(str2)
'''





'''# if i wnat to store a digit as string and float
variable = 17.909090
string = "in the digit foramat  %d \nthe float value of varibale is  %f" % (variable,variable)
print(string)'''



'''name = "patel"
string = f"hello guys me hu sawan {name}"
print(string)'''


'''name = "sawan"
string = ("hello my name is %s and my full name is %s" % (name,"patel"))
print(string)
'''




'''haystack = "sadbutsad"
needle = "sad"
str1 = ""
list1 = []
for i in range(len(haystack)):
    if len(needle) != len(str1):
        str1 = str1 + haystack[i]
    else:
        list1.append()'''










'''class Persons:
    name = "Sawan"
    @classmethod
    def print_name(cls,name1):
        cls.name = name1


p1 = Persons()
Persons.print_name("patel")
print(p1.name)
'''


'''haystack = "sadbutsad"
needle = "sad"
print(haystack.find(needle))'''





'''haystack = "sadbutsad"
needle = "sad"
list1 = []
str1 = ""
i = 0
j = 0
while i < len(haystack)-(len(needle)-1):
    str1 = str1 + haystack[j]
    j = j + 1
    if j == len(needle)+i:
        list1.append(str1)
        i = i + 1
        j = i
        str1 = ""
for i in range(len(list1)):
    if needle == list1[i]:
        print(i)'''









'''func = lambda a,b: a+b
print(func(2,3))
'''


'''class Car:
    class_engine = "Petrol"
    def __init__(self,engine1):
        self.instance_engine = engine1
    @classmethod
    def print_engine(cls,engine):
        cls.class_engine = engine
c1 = Car("Petrol1")
c1.print_engine("hdsghg")
print(c1.instance_engine)'''


'''s = "(])"
stack = []
for i in range(len(s)):
    if stack == [] and (s[i] == "]"  or s[i] == "}"  or s[i] == ")"):
        print(True)
        break
    if s[i] == ")" or s[i] == "]" or s[i] == "}":
        if stack[len(stack) -1] + s[i] == "()" or stack[len(stack) -1] + s[i] ==  "[]" or stack[len(stack) -1] + s[i] ==  "{}":
            stack.pop()
        else:
            stack.append(s[i])
    else:
        stack.append(s[i])
print(stack)'''





'''a = 5
b = 6
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)'''






'''a = 5
b = 6
a = a + b
b = a - b
a = a - b
print(a)
print(b)'''









'''import pickle
data = {"sawan" :"patel", "age":2}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
print("the data is dump")


with open("data.pkl", "rb") as file:
    file2 = pickle.load(file)
print(file2)
'''



'''key = ['a','b','c','d']
values = [1,2,3,4,9]
mydict = {k:v for k,v in zip(key,values)}
print(mydict)
'''



'''def decorator(func):
    def wrape():
        print(" hii am bot")
        func()
        print("good bye")
    return wrape
@decorator
def greet():
    print ( "hello sawan")
greet()'''



'''table = 2
list1 = [table*x for x in range(1,11)]
print(list1)'''













'''str1 =  "a@:1 b@:2 c@:3"
list1 = []
mydict = {}
str_store = ""
sum1 = 0
for i in range(len(str1)):
    try:
        mydict[str_store] = int(str1[i])
        list1.append(mydict)
        mydict = {}
        str_store = ""
    except:
        pass
    if str1[i].islower():
        mydict[str1[i]] = 0
        str_store = str1[i]

print(list1)'''






'''arr = [4,2,1,7,9,10]
for i in range(1,len(arr)):
    j = i-1
    key = arr[i]
    while j>= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
print(arr)'''




'''str1 = "123ABC"
sum1 = 0
for i in range(len(str1)):
    try:
        sum1 = sum1 + int(str1[i])
    except:
        pass
print(sum1)
'''




'''arr = [1,2,3,[4,5,6,[7,8]],[9,10],[11,12]]
list2 = []
list1 = arr
flag = False
i = 0
index = 0
while i < len(list1):
    if len(str(list1[i])) < 3:
        list2.append(list1[i])
        i = i + 1
        if flag == False:
            index = index + 1
    else:
        flag = True
        list1 = list1[i]
        i = 0
    if type(list1) == list:
        if flag == True and i == len(list1):
            index = index + 1
    if type(list1) == list:
        if index != len(arr) and i == len(list1):
            for k in range(index, index + 1):
                list1 = arr[k]
            i = 0

print(list2)'''





'''s = "()"
open_mydict = {}
closed_mydict = {}
for i in range(len(s)):
    if s[i] == "(" or s[i] == "[" or s[i] == "{":
        if s[i] not in open_mydict:
            open_mydict[s[i]] = 1
        else:
            open_mydict[s[i]] = open_mydict[s[i]] + 1

    if s[i] == ")" or s[i] == "]" or s[i] == "}":
        if s[i] not in closed_mydict:
            closed_mydict[s[i]] = 1
        else:
            closed_mydict[s[i]] = closed_mydict[s[i]] + 1
for j in range(len(s)):
    if s[j] == "(":
        if ")" in closed_mydict:
            if open_mydict[s[j]] == closed_mydict[")"]:
                pass
            else:
                print("false")
                break
        else:
            print("false")
            break
    elif s[j] == "[":
        if "]" in closed_mydict:
            if open_mydict[s[j]] == closed_mydict["]"]:
                pass
            else:
                print("false")
                break
        else:
            print("false")
            break
    elif s[j] == "{":
        if "}" in closed_mydict:
            if open_mydict[s[j]] == closed_mydict["}"]:
                pass
            else:
                print("false")
                break
        else:
            print("false")
            break
else:
    print("true")
'''














'''strs = ["flower","flow","flight"]
str1 = strs[0]
for i in range(len(strs)):
    str2 = ""
    j = 0
    while j < len(str1) and strs[i][j] == str1[j]:
        str2 = str2 + str1[j]
        j = j + 1
    else:
        str1 = str2
        str2 = ""
print(str1)'''




'''s = "D"
mydict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
addition = 0
i = 0
if len(s) == 1:
    print(mydict[s])
while i < len(s) - 1:
    if mydict[s[i]] > mydict[s[i+1]]:
        addition = addition + mydict[s[i]]
        if i == len(s)-2:
            addition = addition + mydict[s[i+1]]
        i = i + 1
    elif mydict[s[i]] < mydict[s[i+1]]:
        subtract = mydict[s[i+1]] - mydict[s[i]]
        if  subtract == 4 or subtract == 9 or subtract == 40 or subtract == 90 or subtract == 400 or subtract == 900:
            print(s[i])
            addition = addition + (mydict[s[i+1]] - mydict[s[i]])
            if i == len(s) - 3:
                addition = addition + mydict[s[i + 2]]
            i = i + 2
        else:
            addition = addition + mydict[s[i]]
            if i == len(s) - 2:
                addition = addition + mydict[s[i + 1]]
            i = i + 1
    else:
        addition = addition + mydict[s[i]]
        if i == len(s)-2:
            addition = addition + mydict[s[i+1]]
        i = i + 1

print(addition)'''






'''s = "aaabb"
mydict= {}
for i in s:
    if i not in mydict:
        mydict[i] = 1
    else:
        mydict[i] = mydict[i] + 1
sample = mydict[s[0]]
for values in mydict.values():
    if sample != values:
        print(values)
        print(False)
        break
else:
    print(True)'''
