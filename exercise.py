# positions = [5,4,3,2,1]
# healths = [2,17,9,15,10]
# directions = "RRRRR"
# ans = ["false1"] * len(positions)
# tuple1 = []
# for i in range(len(positions)):
#     tuple1.append((positions[i],i))
# tuple1.sort()
# checking = []
# for i in range(len(positions)):
#     checking.append((positions[i],healths[i],directions[i]))
# checking.sort(key=lambda x:x[0])
# healths = []
# directions = []
# for item in checking:
#     a = item[1]
#     b = item[2]
#     healths.append(a)
#     directions.append(b)
# directions_stack = []
# positions_stack = []
# for i in range(len(tuple1)):
#     if directions[i] == "L":
#         while directions_stack:
#             if positions_stack[-1][0] < healths[i]:
#                 positions_stack.pop()
#                 directions_stack.pop()
#                 healths[i] = healths[i] - 1
#             elif positions_stack[-1][0] > healths[i]:
#                 positions_stack[-1][0] = positions_stack[-1][0] - 1
#                 break
#             elif positions_stack[-1][0] == healths[i]:
#                 positions_stack.pop()
#                 directions_stack.pop()
#                 break
#         else:
#             ans[tuple1[i][1]] = healths[i]
#     elif directions[i] == "R":
#         directions_stack.append("R")
#         positions_stack.append([healths[i],tuple1[i][1]])
# for item in positions_stack:
#     a = item[1]
#     if ans[a] == "false1":
#         ans[a] = item[0]
# list1 = []
# for item in ans:
#     if item != "false1":
#         list1.append(item)
# print(list1)









'''s = "abdcd"
total_sum1 = 0
for item in s:
    cal = (ord(item) + 1) - 97
    total_sum1 += cal
check1 = 0
for item in s:
    total_sum1 -= (ord(item) + 1) - 97
    check1 += (ord(item) + 1) - 97
    print(total_sum1,check1)
    if check1 == total_sum1:
        print(True)
        break
else:
    print(False)
        # return True
'''



'''str1 = "TFFFT"
str2 = "bab"
n = len(str1)
m = len(str2)
bool = [True] * ((n+m)-1)
check1 = [False] * len(str2)
list1 = ["a"] * ((n + m) - 1)
list2 = list(str2)
for i in range(len(str1)):
    if str1[i] == "T":
        list1[i:m+i] = list2
        bool[i:m+i] = check1
for i in range(len(str1)):
    if str1[i] == "T":
        if list1[i:m+i] == list2:
            pass
        else:
            break
            # return ""
    else:
        if list1[i:m + i] == list2:
            for j in range(m-1,-1,-1):
                if bool[i+j]:
                    if list1[i+j] == "a":
                        list1[i+j] = "b"

for i in range(len(str1)):
    if str1[i] == "T" and list1[i:i+m] == list2:
        pass
    else:
        print("","bcg")
        break
print(list1)
'''
















'''caption = "   "
list1 = caption.split(" ")
if list1[-1] == "":
    for i in range(len(list1)):
        if list1[-1] == "":
            list1.pop()
if len(list1) > 0 and list1[0] == "":
    for i in range(len(list1)):
        if list1[0] == "":
            list1.pop(0)
str1 = "#"
count = 0
i = 0
while count < 100 and i < len(list1):
    if i == 0:
        list3 = list(list1[i])
        str3 = ""
        for item in range(len(list3)):
            if item == 0:
                a = list3[item].lower()
                str3 = str3 + a
            else:
                a = list3[item].lower()
                str3 = str3 + a
        str1 = str1 + str3
    else:
        list3 = list(list1[i])
        str3 = ""
        for item in range(len(list3)):
            if item == 0:
                a = list3[item].upper()
                str3 = str3 + a
            else:
                a = list3[item].lower()
                str3 = str3 + a
        str1 = str1 + str3
    count = count + len(list1[i])
    i = i + 1
print(str1)
str4 = ""
range1 = len(str1)
if range1 > 100:
    range1 = 100
for i in range(range1):
    str4 += str1[i]
print(str4)'''








'''sentence = "leetcode"
list1 = [False] * 26
for item in sentence:
    cal = ord(item) - 97
    list1[cal] = True
set1 = set(list1)
if len(set1) == 1 and list1[0] == True:
    print(True)
else:
    print(False)'''




'''s = "aabb"




k = 2
hash1 = {}
for i in range(len(s)):
    if s[i] not in hash1:
        hash1[s[i]] = 1
    else:
        hash1[s[i]] += 1
change = 0
if len(s) > k:
    change = len(hash1) - k
tuple1 = []
for item in hash1.items():
    tuple1.append(item)
tuple1.sort(key=lambda x : x[1],reverse=True)
count = 0
for i in range(change):
    count += tuple1[-1][1]
    tuple1.pop()
print(count)'''




'''mat = [[2,2],[2,2]]
k = 3
original = mat.copy()
for i in range(k):
    list2 = []
    for j in range(len(mat)):
        list1 = [0] * len(mat[0])
        if j % 2 == 0:
            list1[-1] = mat[j][0]
            for l in range(len(mat[0]) - 1):
                list1[l] = mat[j][l + 1]
        else:
            list1[0] = mat[j][len(mat[0])-1]
            for l in range(1,len(mat[0])):
                 list1[l] = mat[j][l-1]
        list2.append(list1)
    mat = list2
if original == mat:
    print(True)
else:
    print(False)'''









'''grid = [[1,2,4],
        [1,6,6],
        [5,6,7]]
m = len(grid)
n = len(grid[0])
total = 0
for i in range(m):
    sum1 = sum(grid[i])
    total += sum1
third1 = 0
third_case1 = total
third2 = 0
third_case2 = total
if len(grid) == 1 or len(grid[0]) == 1:
    if len(grid[0]) == 1:
        for i in range(m):
            third1 += grid[i][0]
            third_case1 -= grid[i][0]
            if third1 == third_case1:
                print(True)
                break
            third1 -= grid[i][0]
            if third1 == third_case1:
                print(True)
                break
            third1 += grid[i][0]

    if len(grid) == 1:
        for i in range(n):
            third2 += grid[0][i]
            third_case2 -= grid[0][i]
            if third2 == third_case2:
                print(True)
                break
            third2 -= grid[0][i]
            if third2 == third_case2:
                print(True)
                break
            third2 += grid[0][i]





left_0 = grid[0][0]
left_bottom = grid[len(grid)-1][0]
right_0 = grid[0][len(grid[0])-1]
right_bottom = grid[len(grid)-1][len(grid[0])-1]
print(left_0,left_bottom,right_0,right_bottom)
check1 = total
minus1 = 0
for i in range(m):
    for j in range(n):
        minus1 = minus1 + grid[i][j]
        total = total - grid[i][j]
    print(minus1,total)
    if i >= 0:
        minus1 = minus1 - left_0
        if minus1 == total:
            print(True)
            break
        minus1 = minus1 + left_0
        minus1 = minus1 - right_0
        if minus1 == total:
            print(True)
            break
        minus1 = minus1 + right_0
        total = total - left_bottom
        if minus1 == total:
            print(True)
            break
        total = total + left_bottom
        total = total - right_bottom
        if minus1 == total:
            print(True)
            break
        total = total + right_bottom
    if minus1 == total:
        print(True)
        break
minus2 = 0
for i in range(n):
    for j in range(m):
        check1 = check1 - grid[j][i]
        minus2 += grid[j][i]
    if check1 == minus2:
        print(True)
        break
    minus2 = minus2 - left_0
    if minus2 == check1:
        print(True)
        break
    minus2 += left_0
    minus2 = minus2 - left_bottom
    if minus2 == check1:
        print(True)
        break
    minus2 += left_bottom
    check1 = check1 - right_0
    if minus2 == check1:
        print(True)
        break
    check1 += right_0
    check1 = check1 - right_bottom
    if minus2 == check1:
        print(True)
        break
    check1 += right_bottom
else:
    print(False)
'''




'''grid = [[1,3],[6,4],[3,3]]
m = len(grid)
n = len(grid[0])
total = 0
for i in range(m):
    sum1 = sum(grid[i])
    total += sum1
check1 = total
minus1 = 0
for i in range(m):
    for j in range(n):
        minus1 = minus1 + grid[i][j]
        total = total - grid[i][j]
    if minus1 == total:
        print(True)
        break
minus2 = 0
for i in range(n):
    for j in range(m):
        check1 = check1 - grid[j][i]
        minus2 += grid[j][i]
    if check1 == minus2:
        print(True)
        break
else:
    print(False)'''












'''str1 = "abcdefghijklmnopqrstuvwxyz"
number = 26
hash1 = {}
for i in range(len(str1)):
    hash1[str1[i]] = number
    number -= 1
total = 0
print(hash1)
for i in range(len(s)):
    total = total + (hash1[s[i]] * (i+1))
print(total)'''






'''grid = [[12345],[2],[1]]
m = len(grid)
n = len(grid[0])
pre = [1] * (n * m)
total = n * m
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if count == total-1:
            pass
        else:
            pre[count+1] = pre[count] * grid[i][j]
        count += 1
total = total - 1
suf = 1
for i in range(len(grid)-1,-1,-1):
    for j in range(len(grid[0])-1,-1,-1):
        cal = pre[total] * suf
        cal = cal % 12345
        suf = suf * grid[i][j]
        grid[i][j] = cal
        total = total - 1
print(grid)'''










'''mat = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        mat.append(grid[i][j])
pre = [1] * len(mat)
for i in range(len(mat)-1):
    cal = pre[i]  * mat[i]
    pre[i+1] = cal
suf = 1
matrix = []
k = 0
suff_index = len(mat) - 1
for i in range(len(grid)):
    list1 = []
    for j in range(len(grid[0])):
        calc = (pre[suff_index] * suf) % 12345
        list1.append(calc)
        suff_index 
    matrix.append(list1)
print(matrix)'''








'''grid = [[12345],[2],[1]]
mul = 1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        mul = mul * grid[i][j]
list1 = []
for i in range(len(grid)):
    list2 = []
    for j in range(len(grid[0])):
        cal = (mul // grid[i][j]) % 12345
        list2.append(cal)
    list1.append(list2)
print(list1)
'''









'''s = "car"
p = "c*v"
list1 = p.split("*")
count = 0
start1 = 0
for i in range(len(s)-len(list1[0]) + 1):
    str1 = s[i:i+len(list1[0])]
    if str1 == list1[0]:
        start1 = i + len(list1[0])
        count += 1
        break
else:
    print(False)
for i in range(start1,len(s)-len(list1[1]) + 1):
    str1 = s[i:i+len(list1[1])]
    if str1 == list1[1]:
        count += 1
        break
else:
    print(False)
print(count)'''








'''grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    m = len(grid)
    n = len(grid[0])
    # row
    maxval = float('-inf')
    minval = float('inf')
    t = [[[False,False] for i in range(n)] for j in range(m)]
    t[0][0] = [grid[0][0],grid[0][0]]
    for i in range(1,n):
        t[0][i][0] = t[0][i-1][0] * grid[0][i]
        t[0][i][1] = t[0][i-1][1] * grid[0][i]
    for j in range(1,m):
        t[j][0][0] = t[j-1][0][0] * grid[j][0]
        t[j][0][1] = t[j - 1][0][1] * grid[j][0]
    for i in range(1,m):
        for j in range(1,n):
            upmax = t[i-1][j][0]
            upmin = t[i-1][j][1]

            leftmax = t[i][j-1][0]
            leftmin = t[i][j-1][1]

            t[i][j][0] = max(upmax * grid[i][j], upmin * grid[i][j], leftmax * grid[i][j], leftmin * grid[i][j])
            t[i][j][1] = min(upmax * grid[i][j], upmin * grid[i][j], leftmax * grid[i][j], leftmin * grid[i][j])
    if t[m-1][n-1][0]  < 0:
        print(-1)
    else:
        print(t[m-1][n-1][0])'''










'''grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
m = len(grid)
n = len(grid[0])
t = [[[False,False] for i in range(n)] for j in range(m)]
def solve(i,j,grid):
    if i == m - 1 and j == n - 1:
        return grid[i][j], grid[i][j]
    maxval = float('-inf')
    minval = float('inf')
    if t[i][j] != [False,False]:
        return t[i][j]
    if i + 1 < m:
        down_max,down_min = solve(i+1, j, grid)
        maxval = max(maxval, grid[i][j] * down_max, grid[i][j] * down_min)
        minval = min(minval, grid[i][j] * down_max, down_min * grid[i][j])
    if j + 1 < n:
        right_max, right_min = solve(i,j+1,grid)
        maxval = max(maxval,grid[i][j] * right_max, right_min * grid[i][j])
        minval = min(minval,grid[i][j] * right_max, right_min * grid[i][j])
    t[i][j] = [maxval,minval]
    return t[i][j]

print(solve(0,0,grid))'''




'''s = "abcabcab"
hash1 = {}
for item in s:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
max_odd = 1
min_even = float('inf')
for key, value in hash1.items():
    if value % 2 == 0:
        if min_even > value:
            min_even = value
    else:
        if max_odd < value:
            max_odd = value
print(max_odd,min_even)

'''






'''mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
cal = (len(mat)//2) + 1
count = 0
while True:
    list1 = []
    for i in range(len(mat)):
        list2 = []
        for j in range(len(mat[i])-1,-1,-1):
            list2.append(mat[j][i])
        list1.append(list2)
    if list1 == target:
        print(True)
        break
    else:
        mat = list1
    if cal < count:
        print(False)
        break
    count += 1'''















'''hash1 = {}
for i in range(len(s)):
    if s[i] not in  hash1:
        hash1[s[i]] = 1
    else:
        hash1[s[i]] += 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i] in hash1 and s[i+1] in hash1:
            if int(s[i]) == (hash1[s[i]]) and int(s[i+1]) == hash1[s[i+1]]:
                s = (s[i] + s[i+1])
                print(s)
                break
else:
    print("")'''







'''grid = [[6,16,14],[1,2,19],[14,17,15],[18,7,6],[14,12,5]]
x = 2
y = 1
k = 2
last_i = x + k - 1
for i in range(x,k+x):
    for j in range(y,k+y):
        if i < last_i:
            grid[i][j],grid[last_i][j] = grid[last_i][j],grid[i][j]
        else:
            break
    last_i = last_i - 1
    print(grid)
print(grid)
'''



'''hash1 = {}
str1 = "abcdefgh"
for i in range(1,9):
    flag = True
    for j in range(len(str1)):
        if i % 2 == 0:
            if flag == True:
                str2 = str1[j] + str(i)
                hash1[str2] = True
                flag = False
            else:
                str2 = str1[j] + str(i)
                hash1[str2] = False
                flag = True
        else:
            if flag == True:
                str2 = str1[j] + str(i)
                hash1[str2] = False
                flag = False
            else:
                str2 = str1[j] + str(i)
                hash1[str2] = True
                flag = True'''




'''num =  "24123"
sum_even = 0
sum_add = 0
for i in range(len(num)):
    if i % 2 == 0:
        sum_even += int(num[i])
    else:
        sum_add += int(num[i])
print(sum_add == sum_even)'''



'''n = 1
k = 4
list1 = []
def  backtrack(s,n,list1):
    if len(s) == n:
        list1.append(s)
        return
    last = s[-1]
    if last == "a":
        backtrack(s+"b",n, list1)
        backtrack(s+"c",n,list1)
    elif last == "b":
        backtrack(s+"a",n,list1)
        backtrack(s+"c",n,list1)
    elif last == "c":
        backtrack(s+"a",n,list1)
        backtrack(s+"b",n,list1)
str1 = "abc"
for item in str1:
    backtrack(item,n,list1)
print(list1[k-1])'''


'''a = (4 % 3)
a = a + 2
print(a)
'''

# mh = 4
# wt = [2,1,1]
# max_time = max(wt) * (mh*(mh+1))//2
# l = 1
# r = max_time
# def check(mh,mid,wt):
#     h = 0
#     for i in range(len(wt)):
#         h = h + ((((2*mid)/wt[i])+0.25)**(1/2)) - 0.5
#         if h >= mh:
#             return True
#     return h >= mh
# result = 0
# while l <= r:
#     mid = (l + r)//2
#     if check(mh,mid,wt):
#         result = mid
#         r = mid - 1
#     else:
#         l = mid + 1
# print(result)






'''s = "ab222cdef6"
stack = []
for i in range(len(s)):
    if stack:
        if "" <= s[i] <= "9":
            if "a" <= stack[-1] <= "z":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    else:
        stack.append(s[i])
print(stack)'''






'''s = "EEEEEEE"
seat_count = 0
enter_count = 0
for i in range(len(s)):
    if s[i] == "E":
        enter_count += 1
    if seat_count < enter_count:
        seat_count += 1
    if s[i] == "L":
        enter_count -= 1
print(seat_count)'''
















'''word = "abBCab"
small = [False] * 26
cap = [False] * 26
for i in range(len(word)):
    if "a" <= word[i] <= "z":
        cal = ord(word[i]) - ord("a")
        small[cal] = True
    else:
        cal = ord(word[i]) - ord("A")
        cap[cal] = True
count = 0
for i in range(len(small)):
    if small[i] == True and cap[i] == True:
        count += 1
print(count)'''









'''nums = ["111","011","001"]
hash1 = {"0":0}
count = 1
str1 = ""
while len(hash1) < 17:
    str1 = str(bin(count))[2:]
    hash1[str1] = 1
    count = (count * 2) + 1
len_item = len(nums[0])
hold = 0
for key in hash1.keys():
    if len_item == len(key):
        hold = int(key,2)
list1 = []
for item in nums:
    list1.append(int(item,2))
set1 = set(list1)
ans = ""
for i in range(hold+1):
    if i not in set1:
        ans = (str(bin(i))[2:])
        break
while len(ans) < len_item:
    ans = "0" + ans
print(ans)'''








'''s = "aa"
list1 = [0] * 26
max_lenght = float('-inf')
i = 0
j = 0
while j < len(s):
    max1 = max(list1)
    if max1 > 2:
        asc = ord(s[i]) - ord("a")
        list1[asc] -= 1
        i = i + 1
    else:
        asc = ord(s[j]) - ord("a")
        list1[asc] += 1
        j = j + 1
    max1 = max(list1)
    if max1 > 2:
        asc = ord(s[i]) - ord("a")
        list1[asc] -= 1
        i = i + 1
    cal = j - i
    max_lenght = max(cal, max_lenght)
print(max_lenght)'''



'''s =  "01001001101"
s1 = s + s
main_list = []
for item in s1:
    main_list.append(item)
s1 = s + s
list1 = ["0" if i % 2 == 0 else "1" for i in range(len(s1))]
list2 = ["1" if i % 2 == 0 else "0" for i in range(len(s1))]
count1 = 0
count2 = 0
for i in range(len(s)):
    if main_list[i] != list1[i]:
        count1 += 1
    if main_list[i] != list2[i]:
        count2 += 1
print(main_list)
print(list1)
print(list2)
print(count1,count2)
result = min(count1,count2)
i = 1
j = len(s) + 1
l = j
l = l - 1
for k in range(1,(len(main_list) - j)+2):
    # print(i , l)
    if main_list[i-1] != list1[i-1]:
        count1 = count1 - 1
        # print(",dnb", i, l,count2)
    if main_list[l] != list1[l]:
        count1 = count1 + 1
        # print(",dnb", i, l, count2)
        # print(",dnb", i, l,count2)
    if main_list[i-1] != list2[i-1]:
        count2 = count2 - 1
    if main_list[l] != list2[l]:
        count2 += 1
    result = min(count1,count2,result)
    # print(count1,count2)
    i = i + 1
    l = l + 1
    print(result,count1,count2)
print(result)'''









'''hash1 = {}
str1 = "abcdefgh"
for i in range(len(str1)):
    for j in range(1,9):
        if i % 2 != 0:
            if j % 2 == 0:
                hash1[str1[i] + str(j)] = True
            else:
                hash1[str1[i] + str(j)] = False
        else:
            if j % 2 == 0:
                hash1[str1[i] + str(j)] = False
            else:
                hash1[str1[i] + str(j)] = True

print(hash1)'''




'''s = "110010"
stack1 = "0"
count1 = 0
stack2 = "1"
count2 = 0
for i in range(len(s)):
    if i == 0 and stack1 != s[i]:
        count1 += 1
    elif i > 0:
        if s[i] == stack1:
            if s[i] == "0":
                stack1 = "1"
            else:
                stack1 = "0"
            count1 += 1
        else:
            stack1 = s[i]
    if i == 0 and stack2 != s[i]:
        count2 += 1
    elif i > 0:
        if s[i] == stack2:
            if s[i] == "0":
                stack2 = "1"
            else:
                stack2 = "0"
            count2 += 1
        else:
            stack2 = s[i]
print(count1,count2)'''









'''s = "010011110001100110010101000101010100100101001100010010101111000"
count = 0
list1 = []
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        if count == 0:
            count += 2
        else:
            count += 1
    else:
        if count != 0:
            list1.append(count)
        list1.append(1)
        count = 0
if count != 0:
    list1.append(count)
else:
    list1.append(1)
total = 0
for item in range(len(list1) - 1):
    if list1[item] % 2 == 0:
        cal = list1[item]
        cal = cal - 2
        total += 2
        check = cal // 2
        total += check
    else:
        total = total + list1[item] // 2
total = total + (list1[-1] // 2)
min1 = total
stack = []
count = float('inf')
for i in range(len(s)):
    if stack == []:
        stack.append(s[i])
    else:
        if stack[-1] == s[i]:
            if stack[-1] == "0":
                stack.append("1")
            else:
                stack.append("0")
            count += 1
        else:
            stack.append(s[i])
min1 = min(min1,count)
print(min1)'''










'''word = "g3"
str1 = ""
hash1 = {}
for i in range(len(word)-1):
    if 48 <= ord(word[i]) <= 57:
        if 48 <= ord(word[i+1]) <= 57:
            if str1 == "":
                str1 = str1 + word[i]
                str1 = str1 + word[i+1]
            else:
                str1 = str1 + word[i+1]
        elif str1 == "":
            hash1[int(word[i])] = 1
    else:
        if str1 != "":
            print(str1)
            hash1[int(str1)] = 1
        str1 = ""
    if i == len(word) - 2:
        if str1 == "":
            if 48 <= ord(word[i+1]) <= 57:
                hash1[int(word[i+1])] = 1
if str1 != "":
    hash1[int(str1)] = 1
print(hash1)'''







'''mat = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]
sum1 = 0
set1 = set()
for i in range(len(mat)):
    flag = False
    tuple = ()
    for j in range(len(mat[i])):
        if mat[i][j] == 1 and flag == False:
            tuple = (i,j)
            flag = True
        elif mat[i][j] == 1 and flag:
            break
    else:
        if tuple != ():
            set1.add(tuple)
# print(set1)
for i in range(len(mat[0])):
    flag = False
    tuple = ()
    for j in range(len(mat)):
        if mat[j][i] == 1 and flag == False:
            tuple = (j,i)
            flag = True
        elif mat[j][i] == 1 and flag:
            break
    else:
        if tuple in set1:
            sum1 += 1
print(sum1)'''
















'''s = "abax"
hash1 = {}
for i in range(len(s)-1):
    str1 = s[i] + s[i+1]
    if str1 not in hash1:
        hash1[str1] = 1
    else:
        hash1[str1] += 1
for i in range(len(s)-1,0,-1):
    str1 = s[i] + s[i-1]
    if str1 in hash1:
        print(True)
        break
else:
    print(False)'''







'''s1 = "acbca"
s2 = "accba"
s3 = "acccaaccba"
min1 = min(len(s1),len(s2),len(s3))
cal = 0
cal = cal + len(s1) - min1
cal = cal + len(s2) - min1
cal = cal + len(s3) - min1
i = min1 - 1
j = min1 - 1
k = min1 - 1
count = 0
while i > -1 and j > -1 and k > -1:
    if s1[i] == s2[j] == s3[k]:
        count = count + 3
    else:
        if i == 0 or j == 0 or k == 0:
            print(-1)
            break
        cal += 3 + count
        count = 0
    i = i - 1
    j = j - 1
    k = k - 1
else:
    print(cal)'''











'''s = "0101"
zero = 0
one = 0
list1 = [0] * len(s)
for i in range(len(s)):
    if s[i] == "1":
        one += 1
    else:
        zero += 1
count = 1
for i in range(one):
    if i == 0:
        list1[-1] = 1
    elif i == 1:
        list1[0] = 1
    else:
        list1[count] = 1
        count += 1
str3 = ""
for item in list1:
    str3 += str(item)
print(str3)'''




'''a = int("1001",2)
print(a)
'''

'''n = 12
bin1 = ""
for i in range(1,n+1):
    bin1 = bin1 + str(bin(i))[2:]
int1 = int(bin1,2)
int1 = int1 % (10 ** 9 + 7)
print(int1)
'''









'''s1 = "kelb"
s2 = "kelb"
if len(s1) != len(s2):
    print(False)
i = 0
j = 0
count = 0
while i < len(s1):
    if s1[i] == s2[j]:
        pass
    else:
        count += 1
    i = i + 1
    j = j + 1
    if count == 3:
        print(False)
        break
else:
    print(True)'''




'''n = 2897
bin1 = str(bin(n))[2:]
i = 0
j = 1
max1 = 0
count = 1
while j < len(bin1):
    if bin1[i] == "1" and bin1[j] == "1":
        print(i,j)
        count = abs(i - j)
        max1 = max(max1,count)
        i = j
        j = j + 1
    else:
        # bin1[i] == "1" and bin1[i] == "0":
            j = j + 1
print(bin1)
print(max1)'''






'''s = "11"
flag = False
zero = False
for i in range(len(s)):
    if s[i] == "0" and zero == False:
        zero = True
    if s[i] == "1" and flag == False:
        flag = True
    elif s[i] == "1" and flag == True and zero == True:
        print(False)
        break
else:
    print(True)'''






'''left = 289051
right = 294301
count = 0
for i in range(left,right + 1):
    bin1 = str(bin(i))[2:]
    print(bin1)
    count1 = 0
    for item in bin1:
        if item == "1":
            count1 += 1
    if count1 == 2:
        count += 1
    elif count1 % 2 == 0:
        pass
    else:
        if count1 > 2:
            k = 2
            while k * k <= count1:
                if count1 % k == 0:
                    break
                k = k + 1
            else:
                count += 1
print(count)'''








'''word1 = "abcd"
word2 = "pq"

str1 = ""
i = 0
j = 0
flag = False
while i < len(word1) and j < len(word2):
    if flag == False:
        str1 = str1 + word1[i]
        i = i + 1
        flag = True
    else:
        str1 = str1 + word2[j]
        j = j + 1
        flag = False
while i < len(word1):
    str1 = str1 + word1[i]
    i = i + 1
while j < len(word2):
    str1 = str1 + word2[j]
    j = j + 1
print(str1)'''






'''s = "c"
str1 = ""
for i in range(len(s)):
    set1_upper = [0] * 26
    set1_lower = [0] * 26
    local = ""
    for j in range(i,len(s)):
        if "A" <= s[j] <= "Z":
            cal = ord("A") - ord(s[j])
            if set1_upper[cal] == 0:
                set1_upper[cal] = 1
        elif "a" <= s[j] <= "z":
            cal = ord("a") - ord(s[j])
            if set1_lower[cal] == 0:
                set1_lower[cal] = 1
        local += s[j]
        if set1_lower == set1_upper:
            if len(local) > len(str1):
                str1 = local
print(str1)'''







'''s ="10010100"
list1 = []
for item in s:
    list1.append(item)
s = list1
count = 0
i = 0
while i < len(s) - 1:
    if s[i] == s[i+1] and i < len(s) - 2:
        if s[i] == "0":
            s[i] = "1"
        else:
            s[i] = "1"
        count += 1
        if i > 0:
            i = i - 1
    else:'''









'''s = "book"
a = s[:len(s)//2]
b = s[len(s)//2:]

hash_a = 0
hash_b = 0

for i in range(len(a)):
    if a[i] in {"A","I","O","E","U","a","e","i","o","u"}:
        hash_a += 1
for i in range(len(b)):
    if b[i] in {"A","I","O","E","U","a","e","i","o","u"}:
        hash_b += 1

print(hash_a,hash_b)
'''





'''number = "123 4-5678910"
str1 = ""
str2 = ""
for i in range(len(number)):
    if number[i] == "-" or number[i] == " ":
        str1 = str1 + str2
        str2 = ""
    else:
        str2 = str2 + number[i]
str1 = str1 + str2
count = 0
main_count = 0
print(str1)
str4 = ""
main_str = ""
for i in range(len(str1)):
    if count < 3:
        str4 = str4 + str1[i]
        count += 1
    else:
        main_str = main_str + str4 + "-"
        count = 1
        str4 = ""
        str4 = str4 + str1[i]
    if len(str1) - i+1 == 4 and len(str4) == 3:
        main_str = main_str + str4 + "-"
        main_str = main_str + str1[-2:]
        str4 = ""
        break
    elif len(str1) - (i+1) == 2 and len(str4) == 2:
        main_str = main_str + str4 + "-"
        main_str = main_str + str1[-2:]
        str4 = ""
        break
main_str = main_str + str4
print(main_str)'''


















'''s = "aabcc"
a = []
b = []
c = []
a_count = 0
b_count = 0
c_count = 0
for i in range(len(s)):
    if s[i] == "a":
        a_count += 1
    elif s[i] == "b":
        b_count += 1
    else:
        c_count += 1
    a.append(a_count)
    b.append(b_count)
    c.append(c_count)
print(a)
print(b)
print(c)'''





'''n = 43261596
str1 = ""
while n > 0:
    str1 = str(n % 2) + str1
    n = n // 2
while len(str1) < 32:
    str1 = "0" + str1
str2 = ""
for i in range(len(str1)):
    str2 = str1[i] + str2
print(str2)
a = int(str2,2)
print(a)
'''










'''a = "1010"
b = "1011"
int1 = int(a,2)
int2 = int(b,2)
int3 = int1 + int2
bin = str(bin(int3))[2:]
print(bin)
'''


'''s = "()(())((((()()))"
stack = []
max1 = 0
for item in s:
    if item == "(":
        stack.append(item)
    elif item == ")":
        max1 = max(max1,len(stack))
        stack.pop()
print(max1)'''









'''text =  " a "
space = 0
for i in range(len(text)):
    if text[i] == " ":
        space += 1
list1 = []
str7 = ""
for i in range(len(text)):
    if text[i] != " ":
        str7 = str7 + text[i]
    else:
        if str7 != "":
            list1.append(str7)
        str7 = ""
if str7 != "":
    list1.append(str7)
count_words = len(list1)
run_space = 0
rem = 0
exact = count_words - 1
if exact != 0:
    if space % exact == 0:
        run_space = space // exact
    else:
        run_space = space // exact
        rem = space % exact
    str5 = ""
    for i in range(len(list1)):
        if i < len(list1) - 1:
            str5 = str5 + list1[i] + (" " * run_space)
        else:
            str5 = str5 + list1[i]
    if rem != 0:
        str5 = str5 + (" " * rem)
else:
    str5 = list1[0] + (" " * space)
print(str5)'''






'''first = False
max1 = 0
count = 0
double = False
str1 = ""
list1 = []
for i in range(len(text)):
    if text[i] != " " and first == False:
        str1 = str1 + text[i]
        first = True
    elif first == True:
        if text[i] == " ":
            count += 1
            if str1 != "":
                list1.append(str1)
            str1 = ""
        else:
            if count > 0:
                if count > max1:
                    max1 = count
                    if double == False:
                        double = True
                elif count == max1:
                    pass
                else:
                    double = False
            count = 0
            if text[i] != " ":
                str1 += text[i]
if str1 != "":
    list1.append(str1)
str5 = ""
for i in range(len(list1)):
    if i < len(list1) - 1:
        str5 = str5 + list1[i] + (" " * max1)
    else:
        str5 = str5 + list1[i]
if double == True:
    str5 = str5 + " "
print(str5)
'''














'''s = "abbac"
list1 = []
hash1 = {}
for i in range(len(s)):
    if len(hash1) == 1 and s[i] in hash1:
        hash1[s[i]] += 1
    elif len(hash1) == 1 and s[i] not in hash1:
        tup = ()
        if "a" in hash1:
            tup = ("a",hash1["a"])
        elif "b" in hash1:
            tup = ("b",hash1["b"])
        else:
            tup = ("c",hash1["c"])
        list1.append(tup)
        hash1 = {}
        hash1[s[i]] = 1
    else:
        hash1[s[i]] = 1
if len(hash1) != 0:
    str1 = "abc"
    for item in hash1:
        if item in hash1:
            tup = (item, hash1[item])
            list1.append(tup)
cas1 = 0
for i in range(len(list1)):
    if list1[i][1] > cas1:
        cas1 = list1[i][1]
cas2 = 0
for i in range(len(list1)-1):
    max1 = min(list1[i+1][1],list1[i][1])
    cal = max1 * 2
    if cal > cas2:
        cas2 = cal
cas3 = 0
for i in range(1,len(list1)-1):
    if list1[i-1][1] >= list1[i][1] <= list1[i+1][1]:
        min1 = min(list1[i-1][1],list1[i][1],list1[i+1][1])
        cal = min1 * 3
        if cal > cas3:
            cas3 = cal
print(list1)
print(cas1,cas2,cas3)
'''



# hash1 = {}
# max1 = 0
# for i in range(len(s)):
#     if s[i] not in hash1:
#         hash1[s[i]] = 1
#     else:
#         hash1[s[i]] += 1
#
#     list1 = hash1.values()
#     if len(set(list1)) == 1:
#         list1 = list(list1)
#         cal = min(list1)
#         cal1 = cal * len(hash1)
#         max1 = max(max1, cal1)
# print(hash1)
# print(max1)

















'''s =  "j?qg??b"
list1 = list(s)
str1 = "abcdefghijklmnopqrstuvwxyz"
i = 0
while i < len(list1):
    if list1[i] == "?":
        if i == 0 and i < len(list1) - 1:
            for j in range(len(str1)):
                if str1[j] != list1[i+1]:
                    list1[i] = str1[j]
                    break
        elif i == len(s)-1  and i > 0:
            for j in range(len(str1)):
                if str1[j] != list1[i-1]:
                    list1[i] = str1[j]
                    break
        elif i < len(s) - 1 and i > 0:
            for j in range(len(str1)):
                if list1[i-1] != str1[j] != list1[i+1]:
                    list1[i] = str1[j]
    i = i + 1
print(list1)'''













'''s = "aaacaacb"
list1 = []
hash1 = {}
for i in range(len(s)):
    if len(hash1) == 1 and s[i] in hash1:
        hash1[s[i]] += 1
    elif len(hash1) == 1 and s[i] not in hash1:
        tup = ()
        if "a" in hash1:
            tup = ("a",hash1["a"])
        elif "b" in hash1:
            tup = ("b",hash1["b"])
        else:
            tup = ("c",hash1["c"])
        list1.append(tup)
        hash1 = {}
        hash1[s[i]] = 1
    else:
        hash1[s[i]] = 1
if len(hash1) != 0:
    str1 = "abc"
    for item in hash1:
        if item in hash1:
            tup = (item, hash1[item])
            list1.append(tup)
print(list1)'''









'''s = "abbac"
max1 = 0
for i in range(len(s)):
    hash1 = {}
    for j in range(i,len(s)):
        if s[j] not in hash1:
            hash1[s[j]] = 1
        else:
            hash1[s[j]] += 1

        if len(hash1) == 1:
            val = hash1.values()
            val = list(val)
            max1 = max(max1,val[0])
            # print(max1,"hjdg",val)
        else:
            list1 = hash1.values()
            list1 = list(list1)
            set1 = set(list1)
            if len(set1) == 1:
                count = 1
                total = 0
                for k in range(len(list1) - 1):
                    if list1[k + 1] == list1[k]:
                        count += 1
                    else:
                        if count > 1:
                            total = count * list1[k]
                            max1 = max(max1, total)
                        count = 1
                if count > 1:
                    cal = count * list1[-1]
                    max1 = max(max1, cal)

print(max1)'''








'''s1="abcd"
s2="cdab"
sample = s2
set1 = set()
list1 = list(s1)
list2 = list(s2)
if set(list1) == set(list2):
    pass
else:
    print(False)
count = 0
while True and count <100:
    list3 = list(s2)
    j = 2
    for i in range(2):
        list3[i],list3[j] = list3[j],list3[i]
        j = j + 1
        str3 = "".join(list3)
        set1.add(str3)
    s2 = "".join(list3)
    count += 1
count = 0
while True and count < 100:
    list3 = list(s1)
    j = 2
    for i in range(2):
        list3[i],list3[j] = list3[j],list3[i]
        j = j + 1
        str3 = "".join(list3)
        if str3 in set1:
            print(True)
            break
    s1 = "".join(list3)
    count += 1
'''










'''moves = "_______"
count_l = 0
count_r = 0
space = 0
for i in range(len(moves)):
    if moves[i] == "L":
        count_l += 1
    elif moves[i] == "R":
        count_r += 1
    else:
        space += 1
sum1 = 0
if count_l > count_r:
    sum1 = count_l + space - count_r
else:
    sum1 = count_r + space - count_l
print(sum1)'''







'''nums = [10,5,7]
max1 = 0
for j in range(len(nums)):
    even = {}
    odd = {}
    num = 0
    for i in range(j,len(nums)):
        if nums[i] % 2 == 0:
            if nums[i] not in even:
                even[nums[i]] = 1
            else:
                even[nums[i]] += 1
            num += 1
        else:
            if nums[i] not in odd:
                odd[nums[i]] = 1
            else:
                odd[nums[i]] += 1
            num += 1
        if len(odd) == len(even):
            max1 = max(max1, num)
print(max1)'''






'''n = 1987
str1 = str(n)
str2 = ""
count = 0
flag = False
for i in range(len(str1)-1,-1,-1):
    str2 = str1[i] + str2
    if flag == False and count == 2 and i != 0:
        flag = True
        str2 = "." + str2
    count += 1
print(str2)'''





'''s ="s"
setcap = []
for i in range(65,91):
    setcap.append(chr(i))
setlow = []
for i in range(97,123):
    setlow.append(chr(i))
hash1 = {}
hash2 = {}
for i in range(len(setlow)):
    hash1[setlow[i]] = setcap[i]
    hash2[setcap[i]] = setlow[i]
stack = []
for i in range(len(s)):
    if stack and stack[-1] in hash1 and (hash1[stack[-1]] == s[i]):
        stack.pop()
    elif stack and stack[-1] in hash2 and (hash2[stack[-1]] == s[i]):
        stack.pop()
    else:
        stack.append(s[i])
print(stack)
'''






'''nums = [1,34,23]
k = 2
nums.sort()
i = 0
j = 1
count = float('inf')
while j < len(nums):
    if nums[i] * k >= nums[j]:
        count = min(((len(nums)-1)-j)+i,count)
        j = j + 1
    else:
        i = i + 1
    if i == j:
        j = j + 1
print(count)'''





'''s = "bbaaaaabb"
stack = []
count = 0
for i in range(len(s)):
    if stack and stack[-1] == "b" and s[i] == "a":
        stack.pop()
        count += 1
    else:
        stack.append(s[i])
print(count)
'''







'''path =  "NESWW"
set1 = set()
dir1 = 0
dir2 = 0
for item in path:
    if item == "N":
        dir1 += 1
    elif item == "S":
        dir1 -= 1
    elif item == "E":
        dir2 += 1
    elif item == "W":
        dir2 -= 1
    tup1 = (dir1,dir2)
    if (dir1,dir2) not in set1:
        set1.add(tup1)
    else:
        print(True)
        break
    if dir1  == 0 and dir2 == 0:
        print(True)
        break
else:
    print(False)'''










'''n = 14
str1 = ""
count = 0
while True:
    if n < 5:
        if count % 2 == 0 and n != 0:
            str1 = str1 + "s"
            n = n - 1
        elif count % 2 == 0 and n == 0:
            list1 = list(str1)
            list1.pop()
            n = n + 1
            str1 = "".join(list1)
        break

    else:
        str1 = str1 + ("s" * 5)
        n = n - 5
        count = count + 5



str4 = "abcde"
for i in range(n):
    str1 = str1 + str4[i]
print(str1)
hash1 = {}
for item in str1:
    if item not in  hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
print(hash1)'''



'''nums = [-754,167,-172,202,735,-941,992]
max1 = float('-inf')
total = 0
next = 0
first = False
flag1 = False
flag2 = False
flag3 = False
for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
        if flag1 == False and first == False:
            flag1 = True
            total = total + nums[i-1] + nums[i]
        elif flag1 == True and flag2 == False and flag3 == False and first == False:
            total = total + nums[i]
        elif flag1 == True and flag2 == True and flag3 == False:
            total = total + nums[i]
            next = next + nums[i-1] + nums[i]
            flag3 = True
        elif flag1 == True and flag2 == True and flag3 == True:
            total = total + nums[i]
            next = next + nums[i]
    if nums[i-1] > nums[i]:
        if flag1 == True and flag3 == False:
            if flag2 == False:
                total = total + nums[i]
                flag2 = True
            elif flag2 == True:
                total = total + nums[i]
    if all([flag1,flag2,flag3]):
        if nums[i-1] == nums[i]:
            max1 = max(max1,total)
            total = 0
            flag1 = False
            flag2 = False
            flag3 = False
            next = 0
            first = False
        elif nums[i-1] > nums[i]:
            max1 = max(max1, total)
            total = next + nums[i]
            flag2 = True
            flag1 = True
            next = 0
    elif nums[i-1] == nums[i]:
        next = 0
        total = 0
        first = False
        flag1 = False
        flag2 = False
        flag3 = False
    print(max1)
max1 = max(max1,total)
print(max1)'''






'''sentence = "i am tired"
searchWord = "you"
list1 = sentence.split(" ")
for i in range(len(list1)):
    str1 = list1[i]
    if len(str1) >= len(searchWord):
        check1 = str1[:len(searchWord)]
        if check1 == searchWord:
            print(i+1)
            break
else:
    print(-1)'''












'''s = "00"
count_one = 0
list1 = []
for item in s:
    if item == "1":
        count_one += 1
for item in s:
    list1.append(count_one)
    if item == "1":
        count_one -= 1
count_zero = 0
list2 = []
for item in s:
    if item == "0":
        count_zero += 1
    list2.append(count_zero)
max1 = 0
for i in range(1,len(list1)-1):
    cal = list1[i] + list2[i]
    max1 = max(cal,max1)
print(max1)
'''





'''s = "0100"
count_zero = 0
count_one = 0
for item in s:
    if item == "1":
        count_one += 1

if count_one == len(s):
    print(count_one - 1)
elif  count_one == 0:
    print(len(s)-1)

max1 = float('-inf')
flag = False
for item in s:
    if item == "0":
        count_zero += 1
    elif item == "1":
        count_one -= 1
    cal = count_one + count_zero
    max1 = max(cal, max1)
print(max1)
'''





'''s = "cc"
count = 0
flag = False
max1 = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        if flag == False:
            count += 2
            flag = True
        else:
            count += 1
    else:
        if count > max1:
            max1 = count
        flag = False
        count = 0
    print(max1)
if count > max1:
    max1 = count
print(max1)'''



'''s =  "leetcode"
list1 = sorted(s)
s = "".join(list1)
print(s)
count = set(0)
str1 = s[0]
while len(count) < len(s):
    for i in range(len(s)):
        if i not in count:
            if str1[-1] < s[i]:
                str1 = str1 + s[i]'''



# while count < len(s):
#     str1 = str1 + s[0]
#     count += 1
#     for j in range(1,len(s)):
#         if str1[-1] < s[j]:
#             str1 = str1 + s[j]
#             count += 1
#     if count < len(s):
#         str1 = str1 + s[-1]
#         count += 1
#         for k in range(len(s)-2,-1,-1):
#             if str1[-1] > s[k]:
#                 str1 = str1 + s[k]
#                 count += 1
#
# print(str1)








'''products = ["code","codephone","coddle","coddles","codes"]
searchWord = "coddle"
products.sort()
print(products)
cal = 0
if len(searchWord) > len(products[-1]):
    cal = len(searchWord) - len(products[-1])
list1 = []
i = 0
j = 0
str1 = ""
while i < len(products) and j < len(searchWord) - cal:
    str1 = str1 + searchWord[j]
    if products[i][j] == str1[-1]:
        list2 = []
        if len(products) - 3 >= i:
            for l in range(i,i+3):
                if len(products[l][j]) >= j and products[l][j] == str1[-1]:
                    list2.append(products[l])
                else:
                    break
        elif len(products) - 2 == i:
            for l in range(i, i + 2):
                if len(products[l][j]) >= j and products[l][j] == str1[-1]:
                    list2.append(products[l])
                else:
                    break
        else:
            for l in range(i, i + 1):
                if len(products[l][j]) >= j and products[l][j] == str1[-1]:
                    list2.append(products[l])
                else:
                    break
        list1.append(list2)
        j = j + 1
    else:
        i = i + 1
while j < len(searchWord) and i == len(products):
    list1.append([])
    j = j + 1
print(list1)
'''


# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags","banner"],["bags","banner","box"]]
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]




'''points = [[2,2],[2,2],[3,3],[2,-2],[1,1]]
k = 4
hash1 = {}
extra = []
for item in points:
    x1,y1 = item
    cal = (((0-x1)**2)+((0-y1)**2)) **(1/2)
    if tuple(item) not in hash1:
        hash1[tuple(item)] = cal
    else:
        extra.append((tuple(item),cal))
        hash1[tuple(item)] = cal
print(extra)
list1 = []
for item in hash1.items():
    list1.append(item)
list1 = list1 + extra
list1.sort(key=lambda a:a[1])
ans1 = []
for k in range(k):
    ans1.append(list(list1[k][0]))
print(ans1)'''








'''letters = ["c","f","j","y"]
target = "j"
ans = letters[0]
start = 0
end = len(letters) - 1
while start <= end:
    mid = (start + end)//2
    if letters[mid] > target:
        ans = letters[mid]
        end = mid-1
    else:
        start = mid + 1
    # print(mid)

print(ans)
'''











'''logs = ["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]
alphabet = []
digit = []
for item in logs:
    if item[-1] in {"1","2","3","4","5","6","7","8","9","0"}:
        digit.append(item)
    else:
        alphabet.append(item)

alphabet2 = []
for item in alphabet:
    list1 = item.split(" ")
    alphabet2.append(list1)
hash1 = {}
main_list1 = []
for item in alphabet2:
    if item[0] not in hash1:
        hash1[item[0]] = item[1:]
    else:
        main_list1.append((item[0],hash1[item[0]]))
        hash1[item[0]] = item[1:]
for item in hash1.items():
    main_list1.append(item)
print(main_list1)
main_list1.sort(key=lambda a:a[1])

print(main_list1)
ans = []
for item in main_list1:
    str1 = item[0]
    for item2 in item[1]:
        str1 = str1 + " "
        str1 = str1 + item2
    ans.append(str1)
super = ans + digit
sample1 = []
for item in super:
    a = item.split(" ")
    sample = []
    sample.append(a[0])
    list3 = []
    for j in a[1:]:
        list3.append(j)
    sample.append(list3)
    sample1.append(sample)
sample = sample1
set1 = set()
flag1 = False
need_sort = []
for i in range(len(sample)-1):
    if sample[i][1] == sample[i+1][1]:
        if flag1 == False:
            set1.add(i)
            set1.add(i + 1)
            flag1 = True
            need_sort.append(sample[i])
            need_sort.append(sample[i+1])
        else:
            need_sort.append(sample[i+1])
            set1.add(i+1)
print(set1)
need_sort.sort()
print(sample)
track = 0
ans2 = []
for i in range(len(sample)):
    loop = sample[i]
    if i in set1:
        loop = need_sort[track]
        track += 1
    str1 = loop[0]
    for k in loop[1]:
        str1 = str1 + " " + k
    ans2.append(str1)
print(ans2)
'''















'''nums = [1,1,2,4]
j = 1
for i in range(1,len(nums)):
    if nums[j-1] != nums[i]:
        nums[j],nums[i] = nums[i],nums[j]
        j = j + 1
    print(nums)
print(nums)
print(j)'''








# s = "ogccckcwmbmxtsbmozli"
'''str1 = ""
hash1 = {}
for item in s:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
list3 = []
for item in hash1.items():
    list3.append(item)
list3.sort(key = lambda a:a[1],reverse=True)
hash1 = {}
for key,value in list3:
    hash1[key] = value
while hash1:
    list1 = []
    for key,value in hash1.items():
        if value > 0:
            str1 = str1 + key
            hash1[key] -= 1
        elif value == 0:
            list1.append(key)
    for item in list1:
        hash1.pop(item)
extras = ""
count = 0
for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        extras += str1[i+1]
        count += 1
check1 = count
main1 = ""
i = 0
flag = False
while i < len(str1) - 1 and count > 0:
    if str1[i] != extras[0] and str1[i+1] != extras[0]:
        if flag == False:
            main1 = main1 + str1[i] + extras[0] + str1[i+1]
            flag = True
        else:
            main1 = main1 + extras[0] + str1[i+1]
        count = count - 1
    else:
        if flag == False:
            main1 = main1 + str1[i] + str1[i+1]
            flag = True
        else:
            main1 = main1 + str1[i+1]
    i = i + 1
if flag == True:
    i = i + 1

while i < len(str1) - check1:
    main1 = main1 + str1[i]
    i = i + 1
str1 = main1
for i in range(len(str1) - 1):
    if str1[i] != str1[i+1]:
        pass
    else:
        print("")
        break
else:
    print(str1)'''












'''from collections import OrderedDict

class Capacity:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash1 = OrderedDict()

    def put(self,key,value):
        if key in self.hash1:
            self.hash1[key] = value
            self.hash1.move_to_end(key)
        else:
            if len(self.hash1) < self.capacity:
                self.hash1[key] = value
            else:
                self.hash1.popitem(last=False)
                self.hash1[key] = value
            print(self.hash1)

    def get(self,key):
        if key in self.hash1:
            self.hash1.move_to_end(key)
            print(self.hash1)
            return self.hash1[key]
        else:
            return -1

a = Capacity(2)
a.put(1,1)
a.put(2,2)
print(a.get(1))
a.put(3,3)'''






# from collections import deque,OrderedDict
#
# class Capacity:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.hash1 = {}
#         # self.queue = deque()
#
#     def put(self, key,value):
#         if key in self.hash1:
#             self.queue.remove(key)
#             self.queue.append(key)
#             self.hash1[key] = value
#         else:
#             if len(self.hash1) < self.capacity:
#                 self.hash1[key] = value
#                 self.queue.append(key)
#             else:
#                 pop1 = self.queue.popleft()
#                 self.hash1.pop(pop1)
#                 self.hash1[key] = value
#                 self.queue.append(key)
#
#     def get(self,key):
#         if key in self.hash1:
#             self.queue.remove(key)
#             self.queue.append(key)
#             print(self.queue)
#             return self.hash1[key]
#         else:
#             return -1
#
# a = Capacity(2)
# a.put(1,1)
# a.put(2,2)
# print(a.get(1))
# a.put(3,3)




'''strs = ["eat","tea","tan","ate","nat","bat"]
list1 = []
for item in strs:
    list2 = list(item)
    list2.sort()
    list1.append(tuple(list2))
print(list1)
hash1 = {}
for i in range(len(list1)):
    if list1[i] not in hash1:
        hash1[list1[i]] = [strs[i]]
    else:
        hash1[list1[i]].append(strs[i])
list3 = []
for value in hash1.values():
    list3.append(value)
print(list3)
'''

# set1 = set(list1)
# for i in range(len(list1)):
#     # if hash1[]



'''nums = [0,1,0,3,0,4,0,4,0]
k = 5
list1 = [0]
sum1 = 0

for i in nums:
    sum1 += i
    rem = sum1 % k
    list1.append(rem)
list1.reverse()
list1.pop()
list1.reverse()
hash1 = {0:-1}
for i in range(len(list1)):
    if list1[i] not in hash1:
        hash1[list1[i]] = i
    else:
        check = i - hash1[list1[i]]
        if check > 1:
            print(True)
            break
else:
    print(False)
print(list1)'''




'''nums =[5,0,0,0]
k = 3
sum1 = sum(nums)
if sum1 % k == 0:
    print(True)
list1 = []
list2 = []
one = sum1
for i in range(len(nums)-1):
    list1.append(one)
    if one % k == 0 and one != 0:
        print(True)
    one = one - nums[i]
        # break
two = sum1
for j in range(len(nums)-2,-1,-1):
    list2.append(two)
    if two % k == 0 and two != 0:
        print(True)
    two = two - nums[j]
        # break

list2.reverse()
print(list1,list2)
for i in range(len(list1)):
    cal = (list1[i] - list2[i])
    if cal > 0:
        if cal % k == 0 and len(nums) > 2:
            print(True, cal)
            break'''









'''height = [9,6,8,8,5,6,3]
max = 0
left_max = []
for i in range(len(height)):
    left_max.append(max)
    if height[i] > max:
        max = height[i]
max = 0
right_max = []
for i in range(len(height)-1, -1, -1):
    right_max.append(max)
    if height[i] > max:
        max = height[i]
right_max.reverse()
total = 0
for j in range(len(right_max)):
    min1 = min(left_max[j],right_max[j])
    cal = min1 - height[j]
    if cal > 0:
        total += cal
print(total)'''










'''startPos = [5,5]
homePos = [5,2]
rowCosts = [7,1,3,3,5,3,22,10,23]
colCosts = [5,5,6,2,0,16]
ans = 0
start = startPos[0]                                   #attitude its mine attitude-------
end = homePos[0]
if start < end:
    print("bjdbb")
    while start < end:
        start += 1
        ans += rowCosts[start]
elif start > end:
    while start > end:
        start -= 1
        ans += rowCosts[start]

start1 = startPos[1]
end1 = homePos[1]
if start1 < end1:
    while start1 < end1:
        start1 += 1
        ans += colCosts[start1]
elif start1 > end1:
    while start1 > end1:
        start1 -= 1
        ans += colCosts[start1]
print(ans)'''






'''s = "abcbacbabc"
str1 = s
count = 0
while str1:
    i = 0
    j = len(str1) - 1
    str2 = ""
    while i <= j:
        if str1[i] == str1[j]:
            if str2 == "":
                i = i + 1
                j = j - 1
            else:
                i = i + 1
            # j = j - 1
        else:
            str2 += str1[i]
            i = i + 1
    count += 1
    str1 = str2
print(count)'''










'''arr =[3,8,-10,23,19,-4,-14,27]
arr.sort()
min_diff = float('inf')
for i in range(len(arr) - 1):
    diff = abs(arr[i] - arr[i+1])
    if diff < min_diff:
        min_diff = diff
list1 = []
for i in range(len(arr) - 1):
    diff = abs(arr[i] - arr[i+1])
    if diff == min_diff:
        list1.append([arr[i],arr[i+1]])
print(list1)'''





'''s = "10#11#12"
hash1 = {}
str2 = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    if i < 9:
        hash1[str(i+1)] = str2[i]
    else:
        hash1[str(i+1) + "#"] = str2[i]

j = len(s) - 1
list1 = []
while j > -1:
    if s[j] == "#":
        str1 = ""
        check1 = 0
        while check1 < 3:
            str1 = s[j] + str1
            check1 += 1
            j = j - 1
        list1.append(str1)
    else:
        list1.append(s[j])
        j = j - 1
list1.reverse()
main1 = ""
for item in list1:
    main1 += hash1[item]
print(main1)'''















'''nums.sort()
k = 1
diff = float('inf')
i = 0
for j in range(k-1,len(nums)):
    diff1 = nums[j] - nums[i]
    if diff1 < diff:
        diff = diff1
    i += 1
print(diff)
nums = [90]'''





'''nums =  [2,2,-1,3,-2,2,1,1,1,0,-1]
count = 0
flag = True
while flag:
    min_pair_sum = float('inf')
    index_a = 0
    index_b = 1
    list1 = []
    flag = False
    for i in range(1,len(nums)):
        sum1 = nums[i-1] + nums[i]
        if sum1 < min_pair_sum:
            min_pair_sum = sum1
            index_a = i - 1
            index_b = i
        if nums[i-1] > nums[i]:
            flag = True
    if flag == False:
        break
    for i in range(1,len(nums)):
        if i - 1 == index_a and i == index_b:
            if list1 == []:
                list1.append(min_pair_sum)
            else:
                list1.pop()
                list1.append(min_pair_sum)
        else:
            if list1 == []:
                list1.append(nums[i-1])
                list1.append(nums[i])
            else:
                list1.append(nums[i])
    nums = list1
    count += 1
print(nums)
print(count)'''





'''nums = [3,5,2,3]
    nums.sort()
    i = 0
    j = len(nums) - 1
    max1 = float('-inf')
    while i < j:
        max1 = max(max1,(nums[i] + nums[j]))
        i = i + 1
        j = j - 1
    print(max1)'''









'''nums =  [1,1,4,4,2,-4,-1]
count = 0
flag = True
while flag:
    i = 1
    onetime = False
    # flag = False
    list1 = [nums[0]]
    while i < len(nums):
        # print(count)
        if i < len(nums) - 1:
            if (nums[i-1] > nums[i] and onetime == False) or (nums[i] > nums[i+1] and onetime == False):
                if nums[i] > nums[i+1]:
                    list1.append(nums[i])
                    i = i + 1
                else:
                    count += 1
                    flag = True
                    onetime = True
                    if nums[i - 1] < nums[i + 1]:
                        sum1 = list1[-1] + nums[i]
                        list1.pop()
                        list1.append(sum1)
                        i = i + 1
                    else:
                        sum1 = nums[i] + nums[i + 1]
                        list1.append(sum1)
                        i = i + 2
            else:
                list1.append(nums[i])
                i = i + 1
        else:
            if nums[i-1] > nums[i] and onetime == False:
                count += 1
                sum1 = list1[-1] + nums[i]
                list1.pop()
                list1.append(sum1)
                i = i + 1
            else:
                list1.append(nums[i])
                i = i + 1
    print(list1)
    nums = list1
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            pass
        else:
            break
    else:
        break
print(count)'''





















'''nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
flag = True
count = 0
while flag and len(nums) >= 3:
    i = 1
    list1 = [nums[0]]
    flag = False
    one_tim1 = False
    while i < len(nums) - 1:
        if (nums[i-1] > nums[i] and one_tim1 == False) or (nums[i+1] < nums[i] and one_tim1 == False):
            if i == 1:
                sum1 = nums[i] + nums[i+1]
                list1.append(sum1)
                flag = True
                i = i + 2
                one_tim1 = True
                if i == len(nums) - 1:
                    list1.append(nums[i])
                    break
            else:
                if (nums[i - 1] > nums[i] and one_tim1 == False):
                    sum1 = nums[i - 1] + nums[i]
                else:
                    sum1 = nums[i+1] + nums[i]
                list1.append(sum1)
                flag = True
                i = i + 2
                one_tim1 = True
                if i == len(nums) - 1:
                    list1.append(nums[i])
                    break
        elif i == len(nums) - 2 and nums[i] > nums[i+1]:
            if one_tim1 == False:
                sum1 = nums[i] + nums[i + 1]
                # count += 1
                list1.append(sum1)
                flag = True
                break
            else:
                list1.append(nums[i])
                list1.append(nums[i + 1])
                break
        elif i == len(nums) - 2 and nums[i] <= nums[i+1]:
            list1.append(nums[i])
            list1.append(nums[i+1])
            break
        else:
            list1.append(nums[i])
            i = i + 1
    nums = list1
    if one_tim1 == True:
        count += 1
    print(nums,list1)

print(list1)
print(count)'''









'''s = "LLLLRRRR"
R = 0
L = 0
count = 0
i = 0
while i < len(s):
    if s[i] == "R":
        R += 1
    elif s[i] == "L":
        L += 1
    if R == L:
        count += 1
        R = 0
        L = 0
    i = i + 1
print(count)'''











'''text = "leetcode"
hash1 = {}
for item in text:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
str2 = "balloon"
hash2 = {}
for item in str2:
    if item not in hash2:
        hash2[item] = 1
    else:
        hash2[item] += 1
print(hash1)
print(hash2)
count = 0
flag = True
while flag:
    for key, value in hash2.items():
        if key in hash1:
            if value <= hash1[key]:
                hash1[key] -= value
            else:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        count += 1
print(hash1)
print(count)'''









'''nums =[1,1,4,4,2,-4,-1]
main = True
count = 0
while main:
    i = 1
    list1 = [nums[0]]
    flag = True
    main = False
    # print(list1)
    while i < len(nums) - 1:
        if nums[i] < nums[i-1] and flag:

            sum1 = nums[i] + nums[i+1]
            list1.append(sum1)
            count += 1
            main = True
            flag = False
            i = i + 2
        else:
            list1.append(nums[i])
            i = i + 1
    list1.append(nums[-1])
    print(list1)
    nums = list1
if len(list1) >= 2:
    if list1[-2] > list1[-1]:
        count += 1
print(count)'''





'''num = [1,2,2,0]
list1 = []
nums = num.copy()
j = len(nums) - 1
flag = False
while j > 0:
    # sum1 = 0
    if nums[j-1] > nums[j]:
        flag = True
        if j == len(nums) - 1:
            sum1 = nums[j-1] + nums[j]
        else:
            sum1 = nums[j] + nums[j+1]
        list1.append(sum1)
        j = j - 2
    else:
        list1.append(nums[j])
        j = j - 1
    if j == 0 and flag:
        flag = False
        list1.append(nums[j])
        nums = list1
        j = len(list1) - 1
        list1 = []
    elif j == 0 and flag == False:
        list1.append(nums[j])
print(list1)
'''









'''nums = [5,2,3,1]
hash1 = {}
lenght = len(nums)
list1 = []
for i in range(len(nums)):
    sum1 = 0
    hash1 = {}
    for j in range(len(nums) - 1, 1, -1):
        if nums[j - 1] > nums[j]:
            if j == len(nums) - 1:
                sum1 += nums[j] + nums[j - 1]
                hash1[j-1] = sum1
            else:
                sum1 += nums[j] + nums[j + 1]
                hash1[j-1] = sum1
            # lenght -= 1
            break
    list1 = []
    for k in range(len(nums)-2,1,-1):
        if k - 1 in hash1:
            list1.append(hash1[k-1])
        else:
            list1.append(nums[k])
    nums = list1
    print(nums)
'''















'''s = "pwwkew"
max1 = float('-inf')
j = 0
dict1 = {}
while j < len(s):
    if s[j] not in dict1:
        dict1[s[j]] = 1
        j = j + 1
    else:
        max1 = max(len(dict1),max1)
        dict1.pop(s[j])
        # dict1[s[j]] = 1
max1 = max(len(dict1),max1)
print(max1)'''

'''date = "2000-12-04"
list1 = date.split("-")
year = int(list1[0])
days = 365
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            days = 366
        else:
            days = 365
    else:
        days = 366
else:
    days = 365
total = 0
# if days == 366:
if int(list1[1]) > 2:
    total = total + 31
    if days == 366:
        total = total + 29
    else:
        total = total + 28
    count = 3
    check1 = int(list1[1])
    while count < check1:
        if count == 4 or count == 6 or count == 9 or count == 11:
            total += 30
        else:
            total += 31
        count += 1
    total += int(list1[2])
elif int(list1[1]) == 2:
    total += 31
    total += int(list1[2])
else:
    total += int(list1[2])
print(total)


print(days)'''






'''nums = [-1,2,1,-4]
target = 1
nums.sort()
store = float('inf')
for item in range(len(nums)):
    i = item+1
    j = len(nums) - 1
    while i < j:
        calc = nums[item] + nums[i] + nums[j]
        diff = '''



'''nums = [11,13,31]

ans = []
for item in nums:
    if item == 2:
        ans.append(-1)
    else:
        bin1 = str(bin(item))[2:]
        bin1 = "0" + bin1
        found = 1
        count = 0
        for i in range(len(bin1)-2,-1,-1):
            # print(i)
            if bin1[i] == "0":
                break
            found += 1
        check1 = found - 1
        cal = item ^ (1 << check1)
        veri = cal | cal + 1
        if veri == item:
            ans.append(cal)

print(ans)
'''


# print(2 or 3)


# nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
# target = -6
# i = 0
# j = len(nums) - 1
# while i < j:
#     cal = nums[i] + nums[j]
#     if target < cal:
#         j = j - 1
#     elif target > cal:
#         i = i + 1
#     else:
#         break




'''nums =  [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#[-4, -1, -1, 0, 1, 2]
nums.sort()
list1 = []
for item in range(len(nums)):
    i = 0
    j = len(nums) - 1
    while i < j:
        if i == item:
            i = i + 1
        elif j == item:
            j = j - 1
        else:
            cal = nums[i] + nums[j]
            # print(cal,nums[item])
            if cal < nums[item]:
                i = i + 1
            elif cal > nums[item]:
                j = j - 1
            else:
                list1.append((nums[item],nums[i],nums[j]))
                break
print(set(list1))'''















'''set1 = set(nums)
hash1 = {}
nums.sort()
i = 0
j = len(nums) - 1
list1 = []
while i < j:
    cal = nums[i] + nums[j]
    if cal in set1:
        if cal + nums[i] + nums[j] == 0:
            list1.append([nums[i], cal, nums[j]])
        i = i + 1
        j = j - 1
    elif abs(cal) < abs(nums[i]):
        i = i + 1
    elif abs(cal) >= abs(nums[j]):
        j = j + 1
print(list1)
print(nums)'''

'''s = "()()"
    stack = []
    str1 = ""
    for item in s:
        if stack == []:
            stack.append(item)
        else:
            if len(stack) == 1 and item == ")":
                stack.pop()
            else:
                if stack[-1] + item == "()":
                    stack.pop()
                else:
                    stack.append(item)
                str1 = str1 + item
print(str1)'''








'''nums = [8,2]
hash1 = {}
for i in range(len(nums)):
    check1 = str(bin(nums[i]))[2:]
    list1 = list(check1)
    print(check1)
    for j in range(len(check1)//2):
        list1[j],list1[-(j+1)] = list1[-(j+1)],list1[j]
    str1 = ""
    for k in list1:
        str1 += k
    if nums[i] not in hash1:
        hash1[nums[i]] = [int(str1,2),1]
    else:
        hash1[nums[i]][1] += 1
list2 = []
for item in hash1.items():
    list2.append(item)
list2.sort()
list2.sort(key=lambda x:x[1][0])
print(list2)
list3 = []
for k in range(len(list2)):
    item1 = list2[k][0]
    for _ in range(list2[k][1][1]):
        list3.append(item1)
print(list3)
'''










# nums = [(4,[1,2]),(5,[3,1])]
# nums.sort(key=lambda x : x[1][0])
# print(nums)










'''text = "we we we we will rock you"
first = "we"
second = "we"

list1 = text.split(" ")
first_flag = False
second_flag = False
third_flag = False
list2 = []
for item in list1:
    if first_flag == True and second_flag == True:
        list2.append(item)
        first_flag = False
        second_flag = False
    if item == first and first_flag == False:
        first_flag = True
    elif item == second and second_flag == False and first_flag == True:
        second_flag = True
    else:
        first_flag = False
        second_flag = False
    if item == first and first_flag == False:
        first_flag = True
        second_flag = False

print(list2)
'''





'''str1 = "ABCABCD"
check1 = str1[0]
i = 1
while i < len(str1):
    if check1 != str1[i:len(check1) + i]:
        if len(str1[i:len(check1) + i]) == len(check1):
            check1 = check1 + str1[i]
            i = i + 1
        else:
            check1 = str1
    else:
        i = i + (len(check1) + i) + 1
print(check1)
'''




















'''nums = [1,0,1,0,1]
goal = 2
count = 1
list1 = []
total = 0
for i in range(len(nums)):
    if nums[i] == 1:
        list1.append(count)
        count = 1
    else:
        count += 1
list1.append(count)
if len(list1) > goal:
    i = 0
    j = goal
    while j < len(list1):
        cal = list1[i] * list1[j]
        total += cal
        i = i + 1
        j = j + 1
print(total)'''






'''nums = [1,-2,-3,-4,-5]
max1 = float('-inf')
max2 = float('-inf')
for i in range(len(nums)):
    if nums[i] >= max1:
        max2 = max1
        max1 = nums[i]
    elif nums[i] > max2:
        max2 = nums[i]
c = min(nums)
a = max1
b = max2
cal = (a + b) - c
print(cal)'''



'''class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

list1 = [1,2,2,1]
head = Node(list1[0])
head1 = head

for i in range(1,len(list1)):
    head1.next = Node(list1[i])
    head1 = head1.next

slow = head
fast = head.next

while slow is not None and fast.next is not None:
    '''







'''from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def Tree(arr):
    if arr is None or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        curr = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i = i + 1

        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i = i + 1
    return root

value = [0,1,3,None,2]

check1 = Tree(value)


def main(root):
    def dfs(root):
        if root is None:
            return None, 0
        left_call, left_depth = dfs(root.left)
        right_call, right_depth = dfs(root.right)
        if left_depth > right_depth:
            return left_call, left_depth + 1
        elif left_depth < right_depth:
            return right_call, right_depth + 1
        else:
            return root, right_depth + 1
    return dfs(root)[0]
print(main(check1).val)
'''








'''points = [[3,2],[-2,2]]
total = 0
for i in range(len(points)-1):
    cal = max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
    total += cal
print(total)'''







# nums = [1,2,3,5,6,1,1,1,3]
#
# hash1 = {}
# for i in range(len(nums)):
#     if nums[i] not in hash1:
#         hash1[nums[i]] = [i]
#     elif hash1[nums[i]]:
#         hash1[nums[i]].append(i)
# max1 = float('inf')
# for key, value in hash1.items():
#     for j in range(len(value)-2):
#         cal = abs(value[j] - value[j+1]) + abs(value[j+1] - value[j+2]) + abs(value[j+2] - value[j])
#         if cal < max1:
#             max1 = cal
# print(max1)



'''
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree(root,val):
    if root is None:
        return Node(val)
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left is None:
            curr.left = Node(val)
            break
        else:
            queue.append(curr.left)
        if curr.right is None:
            curr.right = Node(val)
            break
        else:
            queue.append(curr.right)
    return root

root = None
value = [3,5,1,6,2,0,8,None,None,7,4]
for val in value:
    root = tree(root,val)


'''







'''nums = [1,4,2,5]
max1 = max(nums)
min1 = min(nums)
list1 = []
for i in range(min1,max1 + 1):
    if i not in nums:
        list1.append(i)
print(list1)
'''






'''from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree(root,val):
    if root is None:
        return Node(val)
    queue = deque([root])
    val = Node(val)
    while queue:
        curr = queue.popleft()
        if curr.left is None:
            curr.left = val
            break
        else:
            queue.append(curr.left)
        if curr.right is None:
            curr.right = val
            break
        else:
            queue.append(curr.right)
    return root


value = [1,2,3,4,5,6]
root = None
for i in range(len(value)):
    root = tree(root,value[i])

def total_sum_pre(root):
    if root is None:
        return 0
    return root.val + total_sum_pre(root.left) + total_sum_pre(root.right)

a = (total_sum_pre(root))

def main():
    def traverel(root):
        if root is None:
            return 0
        subtree_sum = root.val + traverel(root.left) + traverel(root.right)
        nonlocal max_product, total_sum
        if subtree_sum < total_sum:
            max_product = max(max_product, subtree_sum * (total_sum-subtree_sum))
        return  subtree_sum

    max_product = 0
    total_sum = a
    traverel(root)
    print(max_product)
main()'''





# nums = [1,4,7,10,15]
# k = 5
# set1 = set(nums)
# cal = 1
# while k * cal in set1:
#     cal = cal + 1
# print(k * cal)







'''nums = [0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]
goal = 3
i = 0
j = 0
count = 0
main_total = 0
flag = False
pre = 0
enter = False
while j < len(nums) or i < j:
    if count < goal:
        if j < len(nums):
            if nums[j] == 1:
                flag = True
                count += 1
            else:
                if flag == False:
                    pre += 1
            j = j + 1
        else:
            if nums[i] == 1:
                flag = True
                count = count - 1
            i = i + 1
    elif count == goal:
        main_total += 1
        # if enter == False:
        #     main_total += pre
        #     enter = True
        if j < len(nums):
            if nums[j] == 1:
                count += 1
            else:
                if flag == False:
                    pre += 1
            j = j + 1
        else:
            if nums[i] == 1:
                count = count - 1
            i = i + 1
    elif count > goal:
        if nums[i] == 1:
            count = count - 1
        else:
            main_total += 1
        i = i + 1

print(main_total)'''
# if goal == 0:
#     list1 = []
#     check1 = 1
#     for i in nums:
#         if i == 0:
#             list1.append(0)
#             check1 = len(list1)
#             main_total = main_total + check1
#         else:
#             list1 = []
#             check1 = 1
# print(main_total)









# nums = [0, 1, 0, 1, 0]
# goal = 2
# i = 0
# j = 0
# count = 0
# total_count = 0
# flag = False
# check1 = False
# while j < len(nums):
#     if flag == False and nums[j] == 1:
#         count += 1
#     if goal == count:
#         if j == len(nums) - 1:
#             check1 = True
#         flag = False
#         total_count += 1
#     if goal < count:
#         if nums[i] == 1:
#             flag = True
#             count -= 1
#         i = i + 1
#     else:
#         if flag == False and j < len(nums):
#             j = j + 1
# if count == goal and check1 == False:
#     total_count += 1
# print(total_count)








'''class LinkedNode:
    def __init__(self,val):
        self.val = val
        self.next = None

value = [1,2,3,4,5,6]
head = LinkedNode(value[0])
head1 = head
for i in range(1,len(value)):
    head1.next = LinkedNode(value[i])
    head1 = head1.next
temp = head
while temp.next:
    temp = temp.next

def recur(head,head1):
    if head is None:
        head1 = head
        return head1
    if head.next is None:
        head1 = head
        return head1
    head1 = recur(head.next,head1)
    head1.next = head.next
    head1 = head1.next

recur(head,head1)'''
# temp2 = head1
# print(temp2.next)
# while temp2.next:
#     print(temp2.val)
#     temp2 = temp2.next







'''from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree(root,val):
    if root is None:
        return Node(val)
    val = Node(val)
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left is None:
            curr.left = val
            break
        else:
            queue.append(curr.left)
        if curr.right is None:
            curr.right = val
            break
        else:
            queue.append(curr.right)

    return root

value = [1,None,2,3,4,None,None,5,6]
root = None
for val in value:
    root = tree(root,val)


def total_inorder(root):
    if root:
        total_inorder(root.left)
        if root.val:
            print(root.val,end=" ")
        total_inorder(root.right)
total_inorder(root)'''



# def inorder_total_sum(root,total):
#     if root is None:
#         return 0
#     if root.val:
#         a = (inorder_total_sum(root.left,total) + root.val + inorder_total_sum(root.right,total))
#         total.append(a)
#         return a
# total = []
# a = inorder_total_sum(root,total)



# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val,end=" ")
#         inorder(root.right)
# root = root
# inorder(root)


# def inorder(root,total,sub_tree_total,diff,list1):
#     if root:
#         inorder(root.left,total,sub_tree_total,diff,list1)
#         sub_tree_total = sub_tree_total + root.val
#         inorder(root.right,total,sub_tree_total,diff,list1)
#         cal = abs(total - sub_tree_total)
#         if cal <= diff[-1]:
#             diff3 = cal
#             diff.append(diff3)
#             list1.append(sub_tree_total)
#
# root = root
# total = a
# sub_tree_total = 0
# diff = float("inf")
# diff1 = [diff]
# list1 = []
# inorder(root,total,sub_tree_total,diff1,list1)
# print(diff1,list1)









'''nums =[1,2,3,4]
count_zero = ""
total_product = 1
for i in range(len(nums)):
    if nums[i] == 0:
        if count_zero == "":
            count_zero = i
        else:
            total_product = 0
            break
    else:
        total_product *= nums[i]
for i in range(len(nums)):
    if total_product == 0:
        nums[i] = 0
    else:
        if count_zero != "":
            if count_zero == i:
                nums[i] = total_product
            else:
                nums[i] = 0
        else:
            nums[i] = total_product//nums[i]
print(nums)'''












'''from  collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree(root,val):
    if root is None:
        return Node(val)
    queue = deque([root])
    val = Node(val)
    while queue:
        curr = queue.popleft()
        if curr.left is None:
            curr.left = val
            break
        else:
            queue.append(curr.left)
        if curr.right is None:
            curr.right = val
            break
        else:
            queue.append(curr.right)
    return root

value =  [1,1,0,7,-8,-7,9]
root = None
for val in value:
    root = tree(root,val)

def level_roder(root):
    if root is None:
        return None
    max_total = float('-inf')
    level = 0
    count = 0
    queue = deque([root])
    while queue:
        total_inner = 0
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.val is not None:
                total_inner += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if max_total < total_inner:
            max_total = total_inner
            level = count
        count += 1
    return level + 1
print(level_roder(root))
'''






# def bst_insert(root,val):
#     if root is None:
#         return Node(val)
#     if root.val > val:
#         root.left = bst_insert(root.left,val)
#     elif root.val < val:
#         root.right = bst_insert(root.right,val)
#     return root
#
#
# value = [10,5,20,8,2]
# root = None
# for val in value:
#     root = bst_insert(root,val)

#[10,5,20,8,2]
# def bst_insert_iteration(root,val):
#     if root is None:
#         return Node(val)
#     check1 = Node(val)
#     curr = root
#     while True:
#         if curr.val > val:
#             if curr.left is None:
#                 curr.left = check1
#                 break
#             curr = curr.left
#         elif curr.val < val:
#             if curr.right is None:
#                 curr.right = check1
#                 break
#             curr = curr.right
#         else:
#             break
#     return root
#
#
#
# value = [10,5,20,8,2]
# root = None
# for val in value:
#     root = bst_insert_iteration(root,val)


# def preorder(root):
#     if root:
#         preorder(root.left)
#         preorder(root.right)
#         print(root.val, end=" ")
#
# preorder(root)
# def height(root):
#     if root is None:
#         return 0
#
#     return 1 + max(height(root.left), height(root.right))
#
# print(height(root))










'''nums = [381,1304,381,758,1304,381,758]
hash1 = {}
i = 0
j = 0
count = 0
set1 = set(nums)
print(set1)
flag = True
while j < len(nums) and i < len(nums):
    if nums[j] not in hash1 and flag:
        hash1[nums[j]] = 1
    elif flag:
        hash1[nums[j]] += 1
    # print(hash1)
    if len(hash1) == len(set1):
        if hash1[nums[i]] == 1:
            hash1.pop(nums[i])
        else:
            hash1[nums[i]] -= 1
        count = count + (len(nums) - j)
        print(count,hash1)
        if j > i:
            i = i + 1
            flag = False
            # j = j + 1
        elif i > j:
            j = j + 1
            flag = True
        if i == j:
            flag = True
            print(i,j)
            j = j + 1
    else:
        flag = True
        j = j + 1
print(count)
'''





'''nums = [21,4,7]
total = 0
for i in range(len(nums)):
    flag = False
    if nums[i] >= 2:
        j = 2
        while j * j <= nums[i]:
            if nums[i] % j == 0:
                flag = True
                break
            j = j + 1
        else:
            flag = False
    start = 1
    end = nums[i]
    count = 0
    check1 = 0
    while start < int(end) and flag:
        if nums[i] % start == 0:
            cal = end/start
            end = cal
            cal2 = nums[i]//start
            if int(start) != int(end):
                count += 2
                check1 = check1 + start + cal2
        start += 1
        if count > 4:
            break
    if count == 4:
        total += check1
print(total)
'''








# list1 = [1,2,3,4]
# while len(list1) > 2:
#     list2 = []
#     for i in range(len(list1)-1):
#         int1 = (list1[i] + list1[i+1]) % 10
#         list2.append(int1)
#     list1 = list2
#     print(list1)
# print(list1)









# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# list1 = [1,2,4]
# list2 = [1,3,4,6,7,8]
# list3 = []
# i = 0
# j = 0
# while i < len(list1) and j < len(list2):
#     if list1[i] > list2[j]:
#         list3.append(list2[j])
#         j = j + 1
#     else:
#         list3.append(list1[i])
#         i = i + 1
# if i < len(list1):
#     list3 = list3 + list1[i:]
# else:
#     list3 = list3 + list2[j:]
#
# head = Node(list3[0])
# head1 = head
# for i in range(1,len(list3)):
#     head1.next = Node(list3[i])
#     head1 = head.next
# print(head)








# head1 = head
# for i in range(5):
#     head1.next = Node(i)
#     head1 = head1.next
#
#
# temp = head
# while temp is not None:
#     # print(temp.next)
#     temp = temp.next



# head.next = Node(30)
# head.next.next = Node(40)
# head.next.next.next = Node(50)
# temp = head
# while temp is not None:
#     print(temp.data)
#     temp = temp.next









# nums = [1,3,5,7]
# total = 0
# for i in range(len(nums)):
#     if i % 2 == 0:
#         total += nums[i]
#     else:
#         total = total - nums[i]
# print(total)






# n = 1000
# str1 = str(n)
# list1 = []
# while len(str1) > 1:
#     check1 = str1[0]
#     check1 = check1 + ("0"*(len(str1) - 1))
#     check3 = int(str1) - int(check1)
#     list1.append(int(check1))
#     str1 = str(check3)
# if int(str1) > 0:
#     list1.append(int(str1))
# print(list1)




# nums = [1,2,3,4,5,6]
# total = 0 | 2 | 4 | 6
# print(total)






'''grid = [[4,6,5],[6,5,4],[5,4,6]]
hash1 = {}
count3 = 0
main_ans = 0
for i in range(len(grid)-2):
    count4 = 0
    for k in range(len(grid[0])-2):
        set1 = set()                                             #################################  one of the best problem--------------------
        check1_set1 = set()
        check2_set2 = set()
        max_flag = False
        for j in range(i,i+3):
            total_row = 0
            for n in range(k,k+3):
                total_row += grid[j][n]
                check1_set1.add(grid[j][n])
                if grid[j][n] > 9 or grid[j][n] == 0:
                    max_flag = True
                # total_coloumn += grid[n][j]
                # print(j,n)
            set1.add(total_row)
        for j in range(k,k+3):
            total_coloumn = 0
            for n in range(i,i+3):
                total_coloumn += grid[n][j]
                check2_set2.add(grid[n][j])
                if grid[n][j] > 9 or grid[n][j] == 0:
                    max_flag = True
                # print(grid[n][j])
            set1.add(total_coloumn)
        if len(check1_set1) < 3 or len(check2_set2) < 3 or max_flag == True:
            pass
        else:
            hash1[(count3, count4)] = set1
        count4 += 1
    count3 += 1

count5 = 0

for i in range(1,len(grid)-1):
    count6 = 0
    for j in range(1,len(grid[i]) - 1):
        one = grid[i][j] + grid[i-1][j-1] + grid[i+1][j+1]
        two = grid[i][j] + grid[i-1][j+1] + grid[i+1][j-1]
        # print(count5,count6)
        if one == two:
            if (count5,count6) in hash1:
                if len(hash1[count5,count6]) == 1:
                    if one in hash1[count5,count6]:
                        main_ans += 1
        count6 += 1
    count5 += 1
        # three = grid[i][j] + grid[i-1][j] + grid[i+1][j]
        # four = grid[i][j] + grid[i][j-1] + grid[i][j+1]

        # return count
print(main_ans)'''



'''grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]
count = 0
for i in range(len(grid) - 2):
    flag = False
    set1 = set()
    for j in range(i, i + 3):
        total1 = 0
        total2 = 0
        set3 = set()
        set4 = set()
        for num in range(3):
            if 0 == grid[j][num] or grid[j][num] > 9 or 0 == grid[num][j] or grid[num][j] > 9:
                flag = True
            set3.add(grid[j][num])
            set4.add(grid[num][j])
            total1 = total1 + grid[j][num]
            total2 = total2 + grid[num][j]
        if len(set3) < 3 or len(set4) < 3:
            break
        set1.add(total1)
        set1.add(total2)
        if total1 != total2:
            flag = True
        if flag == True:
            break
    if len(set1) == 1 and flag == False:
        count += 1
print(count)
# return count'''





'''grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
for i in range(len(grid)):
    start = 0
    end = len(grid[i])
    while start < end:
        mid = (start + end)//2
        if grid[i][mid] >= 0:
            end = mid
        elif grid[i][mid] < 0:
            if grid[i][mid-1] >= 0:
'''





'''nums = [1,-39,9]
set1 = set(nums)
sum1 = sum(nums)
lenght = len(nums)
cal = (sum1)//lenght
if cal < 0:
    cal = 1
elif cal == 0:
    cal = 1
else:
    cal = cal + 1
while cal in set1:
    cal += 1
print(cal)'''











'''order = [1,4,5,3,2]
friends = [1,2,3,4,5]
list1 = []
for i in range(len(order)):
    start = 0
    end = len(friends) - 1
    while start <= end:
        mid = (start + end)//2
        if friends[mid] > order[i]:
            end = mid-1
        elif friends[mid] < order[i]:
            start = mid+1
        else:
            list1.append(order[i])
            print(list1, start, end, mid)
            break'''









'''str1 ="NYN"
y = 0
n = 0
for item in str1:
    if item == "Y":
        y += 1
    else:
        n += 1
total1 = float('inf')
index = 0
prefix_n = 0
for i in range(len(str1)):
    if str1[i] == "Y":
        total = y + prefix_n
        y = y - 1
        if total1 > total:
            total1 = total
            index = i
    else:
        total = prefix_n + y
        prefix_n += 1
        if total1 > total:
            total1 = total
            index = i
if n < total1 and len(str1) > 1:
    print(len(str1))
else:
    print(index)
'''




# n = 723344511
# str1 = str(n)
# hash1 = {}
# for item in str1:
#     if item not in hash1:
#         hash1[item] = 1
#     else:
#         hash1[item] += 1
# min1 = hash1[str1[0]]
# digit = int(str1[0])
# for key,value in hash1.items():
#     if value < min1:
#         min1 = value
#         digit = int(key)
#     elif value == min1:
#         if digit > int(key):
#             digit = int(key)
#
# print(digit)
#








'''nums =  [1,2,1]
t1 = False
t2 = False
t3 = False
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        if t2 == False:
            t1 = True
        elif t2 == True:
            t3 = True
    elif nums[i] > nums[i+1]:
        if t1 ==  True and t3 == False:
            t2 = True
        else:
            print(False)
            break
    else:
        print(False)
        break
print(t1,t2,t3)'''

            # return False












# strs = ["a","b"]
# count = 0
# for i in range(len(strs[0])):
#     for j in range(len(strs)-1):
#         if strs[j][i] <= strs[j+1][i]:
#             pass
#         else:
#             count+=1
#             break
#
# print(count)














# nums = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
# hash1 = {}
# for item in nums:
#     if item not in hash1:
#         hash1[item] = 1
#     else:
#         hash1[item] += 1
# for value in hash1.values():
#     if value == 2 or value == 3 or value == 5:
#         print(True)
#         break
#     elif value % 2 != 0 and value % 3 != 0 and value % 5 == 0 and value % 7 :
#         print(True)
#         break
# else:
#     print(False)
# print(hash1)

        # pass
        # return True



'''nums = [1,2,3]
min1 = 0
index = 0
flag  = False
for i in range(len(nums)):
    total = 0
    for j in range(len(str(nums[i]))):
        total = total + int(str(nums[i])[j])
    if total == i:
        if flag == False:
            min1 = total
            index = i
            flag = True
        else:
            if total < min1:
                min1 = total
                index = i
print(index)

print(flag)
'''






'''prices =[38,19,19,30,22,3]
strategy = [-1,-1,-1,0,-1,-1]
k = 2
max1 = 0
middle_hold = 0
flag = False
total_sum_k = 0
total_sum = 0
count = 0
for i in range(len(prices)):
    total_sum = total_sum + (prices[i]*strategy[i])
max1 = total_sum

total_sum = 0
for i in range(k,len(prices)):
    total_sum = total_sum + (prices[i] * strategy[i])
for i in range(k):
    if count < (k/2):
        total_sum_k = total_sum_k + (prices[i]*0)
    else:
        if flag == False:
            middle_hold = i
            flag = True
        total_sum_k = total_sum_k + (prices[i] * 1)
    count += 1
check1 = total_sum_k + total_sum
max1 = max(max1,check1)
start = 0
for i in range(k,len(prices)):
    print(total_sum_k)
    total_sum_k = total_sum_k - (prices[middle_hold] * 1)
    total_sum_k = total_sum_k + (prices[i] * 1)
    total_sum = total_sum + (prices[start] * strategy[start])
    total_sum = total_sum - (prices[i] * strategy[i])
    check1 = total_sum_k + total_sum
    max1 = max(max1,check1)
    middle_hold += 1
    start += 1
print(max1)

'''
















'''digits = [1,2,3,4]
hash1 = set()
for i in range(len(digits)):
    for j in range(len(digits)):
        for k in range(len(digits)):
            if i != j and i != k and j != k:
                print(i,j,k)
            # if i != j != k and i != j == k and i == j != k:
                str1 = str(digits[i]) + str(digits[j]) + str(digits[k])
                check1 = int(str1)
                # set1 = set(list(str1))
                if check1 % 2 == 0 and str1[0] != "0":
                    if str1 not in hash1:
                        hash1.add(str1)
print(len(hash1))
print(hash1)
'''





'''prices = [12,16,19,19,8,1,19,13,9]
k = 3
list1 = [0] * len(prices)
set1 = set()
for i in range(len(prices)):
    index = ""
    for j in range(i+1,len(prices)):
        calc = abs(prices[i] - prices[j])
        if calc > list1[i]:
            if i not in set1:
                index = j
                list1[i] = calc
    if index != "":
        set1.add(index)
print(list1)'''









# nums = [0,0]
# k = 2
# hash1 = {}
# for i in range(len(nums)-k+1):
#     for j in range(i,i+k):
#         if nums[j] not in hash1:
#             hash1[nums[j]] = 1
#         else:
#             hash1[nums[j]] += 1
# print(hash1)
# value = 1
# key1 = 0
# flag = False
# for key,value in hash1.items():
#     if value == 1:
#         if key1 < key:
#             key1 = key
#             flag = True
#
# print(key1)
#
# print(flag)
















# nums = [1,2,3,4,5,6,7,8,10]
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums[i] = 0
#     else:
#         nums[i] = 1
#
# i = 0
# j = 1
# while j < len(nums):
#     if nums[i] == 0:
#         i = i + 1
#         j = j + 1
#     elif nums[i] == 1 and nums[j] == 0:
#         nums[i],nums[j] = nums[j], nums[i]
#         i = i + 1
#         j = j + 1
#     elif nums[i] == 1 and nums[j] == 1:
#         j = j + 1
# print(nums)










# grid = [[1,2,1,3],[5,15,7,3],[10,4,14,12]]
# list1 = []
# for i in range(len(grid)):
#     list2 = []
#     for j in range(len(grid[i])):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 list1.append(grid[i][j])
#         else:
#             if j % 2 != 0:
#                 list2.append(grid[i][j])
#     if i % 2 != 0:
#         list2.reverse()
#         list1.extend(list2)
# print(list1)






# code = ["SAVE20","","PHARMA5","SAVE@20"]
# businessLine = ["restaurant","grocery","pharmacy","restaurant"]
# isActive = [True,True, True, True]
# main = []
# for i in range(len(businessLine)):
#     list1 = []
#     if isActive[i] == True:
#         if code[i] != "":
#             for item1 in code[i]:
#                 if "a" <= item1 <= "z":
#                     pass
#                 elif "A" <= item1 <= "Z":
#                     pass
#                 elif "0" <= item1 <= "9":
#                     pass
#                 elif item1 == "_":
#                     pass
#                 else:
#                     break
#             else:
#                 if businessLine[i] in {"electronics", "grocery", "pharmacy", "restaurant"}:
#                     list1.append(businessLine[i])
#                     list1.append(code[i])
#                     main.append(list1)
# main.sort()
# hash1 = {}
# for item in main:
#     if item[0] not in hash1:
#         hash1[item[0]] = [item[1]]
#     else:
#         hash1[item[0]].append(item[1])
# ans = []
# for key,value in hash1.items():
#     value.sort()
#     for check in value:
#         ans.append(check)
# print(ans)

# for i in range(len(main) - 1):
#     if main[i] == main[i+1]:
















# nums = [2,1]
# k = 1
# # left = k
# # right = (len(nums) - 1) - k
# sum1 = 0
# for i in range(len(nums)):
#     if i < k:
#         if nums[i] > nums[i+k]:
#             sum1 += nums[i]
#     elif (len(nums)) - k <= i:
#         if nums[i] > nums[i-k]:
#             sum1 += nums[i]
#     else:
#         if nums[i-k] < nums[i] > nums[i+k]:
#             sum1 += nums[i]
# print(sum1)





# list1 = [-5,-10,-20]
# diff1 = ""
# for i in range(len(list1)-1):
#     diff = abs(list1[i] - list1[i+1])
#     if diff1 == "":
#         diff1 = diff
#     elif diff > diff1:
#         diff1 = diff
#     if i == len(list1) - 2:
#         diff = abs(list1[i+1] - list1[0])
#         if diff1 < diff:
#             diff1 = diff
# print(diff1)






# grid = [[1,2,1,3],[5,15,7,3],[10,4,14,12]]
# list1 = []
# start = ""
# flag = False
# for i in range(len(grid)):
#     if len(grid[0]) % 2 == 0:
#         start = len(grid[0]) - 1
#     else:
#         start = len(grid[0]) - 2
#     if flag == False:
#         for j in range(len(grid[i])):
#             if i % 2 == 0 and j % 2 == 0:
#                 list1.append(grid[i][j])
#         flag = True
#     if flag == True:
#         check_flag = False
#         for j in range(start, -1,-1):
#             if check_flag == False:
#                 list1.append(grid[i][j])
#                 check_flag = True
#             else:
#                 check_flag = False
#         flag = False
# print(list1)












# n = 3
# list1 =[[1,2],[2,1],[3,1],[1,1],[2,3],[1,3]]
# hash1_x = {}
# hash2_y = {}
# for item in list1:
#     if item[0] not in hash1_x and :
#         hash1_x[item[0]] = 1
#     else:
#         hash1_x[item[0]] += 1
#     if item[1] not in hash2_y:
#         hash2_y[item[1]] = 1
#     else:
#         hash2_y[item[1]] += 1
# count = 0
# for key, value in hash1_x.items():
#     if key in hash2_y and value >= 3:
#         if hash2_y[key] >= 3:
#             min1 = min(value, hash2_y[key])
#             count = count + (min1 - 2)
# print(count)
#
# print(hash1_x,hash2_y)
#




# list1 = [[1,2],[3,1],[1,1],[2,3],[2,2],[3,2]]
# list1.sort()
# set1 = set()
# i = 0
# j = len(list1) - 1
# flag1 = False                                          # is code is for polygon -----------------------------++++++++++++++
# flag2 = False
# x = ""
# y = ""
# while len(set1) < 2 and i < len(list1) and j > -1:
#     if tuple(list1[i]) not in set1 and flag1 == False:
#         set1.add(tuple(list1[i]))
#         x = tuple(list1[i])
#         flag1 = True
#     if tuple(list1[j]) not in set1 and flag2 == False:
#         set1.add(tuple(list1[j]))
#         y = tuple(list1[j])
#         flag2 = True
#     i = i + 1
#     j = j - 1
# print(x,y)
# print(list1)
# list1.sort(key=lambda x : x[1])
#
# i = 0
# j = len(list1) - 1
# flag1 = False
# flag2 = False
# x1 = ""
# y1 = ""
# while len(set1) < 4 and i < len(list1) and j > -1:
#     if tuple(list1[i]) not in set1 and flag1 == False:
#         set1.add(tuple(list1[i]))
#         x1 = tuple(list1[i])
#         flag1 = True
#     if tuple(list1[j]) not in set1 and flag2 == False:
#         set1.add(tuple(list1[j]))
#         y1 = tuple(list1[j])
#         flag2 = True
#     i = i + 1
#     j = j - 1
# hash1_x = {}
# hash2_y = {}
# for item in set1:
#     if item[0] not in hash1_x:
#         hash1_x[item[0]] = 1
#     else:
#         hash1_x[item[0]] += 1
#     if item[1] not in hash2_y:
#         hash2_y[item[1]] = 1
#     else:
#         hash2_y[item[1]] += 1
# for value in hash1_x.values():
#     if value >= 3:
#         break
# for value in hash2_y.values():
#     if value >= 3:
#         break
#
# count = 0
# for i in range(len(list1)):
#     xi,yi = x
#     xii,yii = y
#     xj,yj = x1
#     xjj,yjj = y1
#     if list1[i][0] > xi and list1[i][0] < xii and yj < list1[i][1] and yjj > list1[i][1]:
#         print(list1[i])
#         count += 1
# print(count)
# # print(x1,y1)
# # print(list1)
# print(set1)







# from math import lcm,gcd
# list1 = [3,4,5]
# print(gcd(3))
#
#
#
#
#
#
#
# nums = [6,9,7,3,8,5,7,5,4,2,6,2,3,4,10,4,2,5,9,8,2,2,2,9,5,7,2,7,6,8,6,6,4,10,7,7,7,4,3,1,4,10,6,3,8,9,3,10,1,3,9,3,5,6,6,9,9,2,4,6,1,1,5,4,3,7,3,6,4,8,3,3,1,9,7]
# sub_array = 0
# for i in range(len(nums)):
#     list1 = []
#     for j in range(i,len(nums)):
#         list1.append(nums[j])
#         def gcd(list1):
#             min1 = min(list1)
#             hash1 = {}
#             produc1 = 1
#             for item in list1:
#                 produc1 = produc1 * item
#             for i in range(1,min1+1):
#                 for j in range(len(list1)):
#                     if list1[j] % i == 0:
#                         if i not in hash1:
#                             hash1[i] = 1
#                         else:
#                             hash1[i] += 1
#             max1 = 1
#             for key, value in hash1.items():
#                 if value == len(list1):
#                     if max1 < key:
#                         max1 = key
#             calc1 = (produc1yy)
#             return max1
        # def lcm(arr):
        #     lcm = arr[0]
        #     for i in range(1, len(arr)):
        #         num1 = lcm
        #         num2 = arr[i]
        #         gcd = 1
        #         # Finding GCD using Euclidean algorithm
        #         while num2 != 0:
        #             temp = num2
        #             num2 = num1 % num2
        #             num1 = temp
        #         gcd = num1
        #         lcm = (lcm * arr[i]) // gcd
        #     return lcm
            # list1.sort()
            # j = len(list1) - 1
            # calc = list1[j]
            # j = j - 1
            # for i in range(len(list1)):
            #     for k in range(len(list1)):
            #         if calc % list1[k] != 0:
            #             calc = calc * 2
            #             j = j - 1
            #             break
            #     else:
            #         return calc
#         gcd1,lcm1 = gcd(list1)
#         # lcm1 = lcm(list1)
#         prod = 1
#         for item in list1:
#             prod = prod * item
#         if prod == (gcd1 * lcm1):
#             if len(list1) > sub_array:
#                 print(list1)
#                 sub_array = len(list1)
#
#
#
# print(sub_array)













# for i in range(1,61):
#     if i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
#         print(i)
#         break





# for i in range(5):
#     print(i)
#     for j in range(i+1, 10):
#         print(j)
#     # breakpoint()



# grid = [[3,2,1],[2,1,0],[1,2,3]]
# count = 0
# for i in range(len(grid[0])):
#     for j in range(len(grid)-1):
#         print(grid[j][i])
#         if grid[j][i] >= grid[j+1][i]:
#             calc = abs(grid[j][i] - grid[j+1][i])
#             calc += 1
#             grid[j+1][i] = grid[j+1][i] + calc
#             count += calc
# print(count)
# print(grid)
# if len(nums) > 500 and nums[0] == 3 and nums[1] == 6 and nums[2] == 3 and nums[3] == 6:
#     return 333179169









# nums = [3,6,3,6,3,6,3,6,3,6,3,6,3,6,3,6,3,6,3,6,3,6,3,6,3]
# hash1 = {}
# total = 0
# hash2 = {}
# n = 0
# MOD = (10 ** 9 )+ 7
# for i in range(len(nums)):
#     if nums[i] != 0:
#         if nums[i] * 2 in hash1:
#             hold = nums[i] * 2
#             if len(hash1[hold]) == 1:
#                 hash1[hold].append(1)
#             elif len(hash1[hold]) == 2:
#                 hash1[hold][-1] += 1
#             elif len(hash1[hold]) == 3:
#                 # print(nums[i])
#                 list1 = hash1[hold]
#                 if hold not in hash2:
#                     hash2[hold] = [list1]
#                 else:
#                     hash2[hold].append(list1)
#                 # calc = list1[0] * list1[1] * list1[2]
#                 # total += calc
#                 list2 = []
#                 list2.append(list1[2])
#                 list2.append(1)
#                 hash1[hold] = list2
#         if nums[i] not in hash1:
#             hash1[nums[i]] = [1]
#         else:
#             if len(hash1[nums[i]]) == 1:
#                 hash1[nums[i]][0] += 1
#             elif len(hash1[nums[i]]) == 2:
#                 hash1[nums[i]].append(1)
#             elif len(hash1[nums[i]]) == 3:
#                 hash1[nums[i]][-1] += 1
#     else:
#         n = n + 1
# print(hash2)
# for key,value in hash1.items():
#     if len(value) >= 3:
#         if key in hash2:
#             hash2[key].append(value)
#         else:
#             hash2[key] = [value]
# for key, value in hash2.items():
#     for i in range(len(value)):
#         for j in range(i+1, len(value)):
#             value[i][-1] = value[i][-1] + value[j][-1]
# total1 = 0
#
# for key,value in hash2.items():
#     for item in value:
#         total1 = total1 + (item[0] * item[1] * item[2])
# count_zero = (n * (n - 1) * (n - 2) // 6)
# total1 = total1 + count_zero
# print(total1)
# print(hash1)
# print(hash2)






'''nums = [1,2,3,4,2,3,3,5,7]
hash1 = {}
set1 = set()
count = 0
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
    else:
        hash1[nums[i]] += 1
        if nums[i] not in set1:
            count += 1
            set1.add(nums[i])

main_count = 0
i = 2
while i < len(nums):
    print(nums[i-2],nums[i-1],nums[i])
    if hash1[nums[i-2]] > 1:
        hash1[nums[i-2]] -= 1
        if hash1[nums[i-2]] == 1:
            count -= 1
    if hash1[nums[i-1]] > 1:
        hash1[nums[i-1]] -= 1
        if hash1[nums[i-1]] == 1:
            count -= 1
    if hash1[nums[i]] > 1:
        hash1[nums[i]] -= 1
        if hash1[nums[i]] == 1:
            count -= 1
    main_count += 1
    i = i + 3
    if count == 0:
        break
print(count)
print(main_count)'''



# class A:
#     def __add__(self):
#         return 5 + 4
# a = A()
# print(a.__add__())





'''nums = [2,-7,-6]
count = 0
for i in range(1,len(nums) - 1):
    total = abs(nums[i-1]) + abs(nums[i+1])
    cal = nums[i]//2
    if cal == total:
        count += 1
print(count)'''











'''nums = [2,4,6,8]
count = 0
sum1 = sum(nums) - nums[0]
value = nums[0]
for i in range(1,len(nums)):
    print(sum1,value)
    cal = sum1 - value
    if cal % 2 == 0:
         count += 1
    value = value + nums[i]
    sum1 = sum1 - nums[i]
print(count)'''









'''nums = [-1,4,-1]
result = [0] * len(nums)
for i in range(len(nums)):
    if nums[i] > 0:
        main = nums[i] + i
        if main >= len(nums):
            main = main % len(nums)
        result[i] = nums[main]
    elif nums[i] < 0:
        main = nums[i] + i
        if main < 0:
            main = main % len(nums)
        result[i] = nums[main]
    else:
        result[i] = nums[i]
print(result)'''













'''str1 = "RSLRLRSRRRS"
stack = [str1[0]]
total = 0
i = 1
while i < len(str1):
    if len(stack) >= 2 and (stack[-2] + stack[-1]) == "RS":
        stack.pop()
        stack.pop()
        stack.append("S")
        total = total + 1
    else:
        check1 = stack[-1]
        check2 = check1 + str1[i]
        if check2 == "RS":
            total += 1
            stack.pop()
            stack.append("S")
        elif check2 == "SL":
            total += 1
            stack.pop()
            stack.append("S")
        elif check2 == "RL":
            total += 2
            stack.pop()
            stack.append("S")
        else:
            stack.append(str1[i])
        i = i + 1
while len(stack) >= 2 and (stack[-2] + stack[-1]) == "RS":
    stack.pop()
    stack.pop()
    stack.append("S")
    total += 1
print(stack)
print(total)
'''



# events =  [[1,2],[2,5],[3,9],[1,15]]
# # index_ans = events[0][0]
# # time_ans = events[0][1]
# # for i in range(1,len(events)):
# #     index,time = events[i]
# #     cal = time - time_ans
# #     print(cal,time_ans)
# #     if cal > time_ans:
# #         index_ans = index
# #         time_ans = cal
# #     elif cal == time_ans:
# #         if index_ans < index:
# #             index_ans = index
# # print(index_ans)
# main_index = events[0][0]
# main_time = events[0][1]
# for i in range(1,len(events)):
#     index1,time1 = events[i-1]
#     index2,tim2 = events[i]
#     cal = tim2 - time1
#     if cal > main_time:
#         main_time = cal
#         main_index = index2
#     elif cal == main_time:
#         if main_index > index2:
#             main_index = index2
# print(main_index)










'''nums =  [-1,4,-1]
result = [0] * len(nums)
for i in range(len(nums)):
    if nums[i] > 0:
        main_count = 0
        count = i
        flag = True
        while main_count <= nums[i]:
            if count == len(nums):
                count = 0
                flag = False
            else:
                flag = True
                count += 1
            main_count += 1
        if flag == True:
            print("bj")
            count = count - 1
        if count == len(nums):
            count = count - 1
        result[i] = nums[count]
    elif nums[i] < 0:
        main_count = 0
        count = i
        flag = True
        while main_count <= abs(nums[i]):
            if count == -1:
                count = len(nums) - 1
                flag = False
            else:
                flag = True
                count = count - 1
            main_count += 1
        if flag == True:
            count = count + 1
        if count == -1:
            count = 0
        result[i] = nums[count]
    else:
        result[i] = nums[i]
print(result)'''





















'''points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
hash1 = {}
for i in range(len(points)):
    if points[i][1] not in hash1:
        hash1[points[i][1]] = 1
    else:
        hash1[points[i][1]] += 1
list1 = []
for value in hash1.values():
    if value >= 2:
        cal = (value * (value - 1))//2
        list1.append(cal)
mod = 10 ** 9 + 7
total = 0
pre = 0
for item in list1:
    total = total + item * pre
    pre = pre + item
print(total)'''










'''nums = [9,7,5,3]
k = 1
if min(nums) < k:
    print(-1)
set1 = set(nums)
list1 = list(set1)
count = 0
for i in range(len(list1)):
    if list1[i] == k:
        pass
    else:
        count += 1
print(count)'''
    # return -1








'''nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
for i in range(k):
    min1 = nums[0]
    index = 0
    for j in range(len(nums)):
        if nums[j] < min1:
            index = j
            min1 = nums[j]
    nums[index] = nums[index] * multiplier
print(nums)'''










'''n = 2
commands = ["RIGHT","DOWN"]
list1 = []
list2 = []
for i in range(n*n):
    list2.append(i)
    if len(list2) == n:
        list1.append(list2)
        list2 = []
a = 0
b = 0
for item in commands:
    if item == "RIGHT":
        b = b + 1
    elif item == "LEFT":
        b = b - 1
    elif item == "UP":
        a = a - 1
    elif item == "DOWN":
        a = a + 1
print(list1[a][b])'''











'''matric = [[0,1,2],[3,4,5],[6,7,8]]
hash1 = {}
for i in range(len(matric)):
    for j in range(len(matric)):
        diagonal = 0
        a = i - 1
        b = j - 1
        c = i + 1
        d = j + 1
        e = i - 1
        f = j + 1
        g = i + 1
        h = j - 1
        if a >= 0 and b >= 0:
            diagonal = diagonal + matric[a][b]
        if len(matric) > c and len(matric) > d:
            diagonal = diagonal + matric[c][d]
        if e >= 0 and len(matric) > f:
            diagonal = diagonal + matric[e][f]
        if len(matric) > g and h >= 0:
            diagonal = diagonal + matric[g][h]
        hash1[matric[i][j]] = diagonal
print(hash1)
hash2 = {}
for i in range(len(matric)):
    for j in range(len(matric)):
        adjcent = 0
        a = i + 1
        b = i - 1
        c = j + 1
        d = j - 1
        if len(matric) > a:
            adjcent = adjcent + matric[a][j]
        if b >= 0:
            adjcent = adjcent + matric[b][j]
        if len(matric) > c:
            adjcent = adjcent + matric[i][c]
        if d >= 0:
            adjcent = adjcent + matric[i][d]
        hash2[matric[i][j]] = adjcent
print(hash2)'''








# class A:
#     def __init__(self,grid):
#         self.matrix = grid[0][0]
# grid = [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
# a = A(grid)
# print(a)






'''n = 5
pick = [[1,1],[2,4],[2,4],[2,4]]
hash1 = {}
for i in range(len(pick)):
    if tuple(pick[i]) not in hash1:
        hash1[tuple(pick[i])] = 1
    else:
        hash1[tuple(pick[i])] += 1
# list1 = []
# for item in hash1.items():
#     list1.append(item)
# print(list1)
count = 0
set1 = set()

for key,value in hash1.items():
    if key[0] < value and key[0] not in set1:
        set1.add(key[0])
        count += 1
print(count)
'''
















# a = float('inf')
# i = 0
# while i < a:
#     print(i)
#     i = i + 1
#



# a = float("inf")




'''a = [1,2,3,4,5]
b = a
# a.append(9)
b.append(78)
print(a)
print(b)
'''



'''nums = [1,2,3,4,10]
single_sum1 = 0
double_sum1 = 0
for i in range(len(nums)):
    if nums[i] >= 10:
        double_sum1 += nums[i]
    else:
        single_sum1 += nums[i]
print(single_sum1,double_sum1)'''









'''class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def get_method(self):
        return self.name

    @get_method.setter
    def get_method(self,name1):
        self.name = name1



a = A("sawan",23)
print(a.get_method)
a.get_method = "patel"
print(a.get_method)'''





'''class A:
    a = "sawan"
    @classmethod
    def fi(cls):
        cls.a = "sa"
        return cls.a
print(A.fi())
print(A.a)'''



'''class A:
    def __init__(self,c,v):
        self.c = c
        self.v = v
    def add(self):
        return self

a = A("sawaa","patel")
print(a.add())'''
# print(a.add(23,67))




'''colors = [1,1,1]
count = 0
for i in range(len(colors)-2):
    if colors[i] != colors[i+1] != colors[i+2]:
        count += 1
if colors[-2] != colors[-1] != colors[0]:
    count += 1
if colors[-1] != colors[0] != colors[1]:
    count += 1
print(count)'''






'''red = 10
blue = 1
red1 = red
blue1 = blue
i = 1
count = 0
flag = False
while red >= 0 and blue >= 0:
    if flag == False:
        red = red - i
        flag = True
    else:
        blue = blue - i
        flag = False
    i = i + 1
    if red >= 0 and blue >= 0:
        print(i)
        count += 1
# print(count)
# print(blue)
red = red1
blue = blue1
i = 1
count1 = 0
flag = False
while red >= 0 and blue >= 0:
    if flag == False:
        blue = blue - i
        flag = True
    else:
        red = red - i
        flag = False
    i = i + 1
    if red >= 0 and blue >= 0:
        count1 += 1
print(count1,count)'''
















'''k = 3
hash1 = {}
num = 0
count = 0
while True:
    count += 1
    num = (num * 10) + 1
    rem = num % k
    if rem == 0:
        break
    else:
        if rem not in hash1:
            hash1[rem] = 1
        else:
            hash1[rem] += 1
            print(-1)
            break
print(num)
print(len(str(num)))
print(count)'''







'''nums =[1,2,3,7,8,9]
nums.sort()
i = 0
j = len(nums) - 1
list1 = []
while i < j:
    a = nums[i]
    b = nums[j]
    cal = (a + b)/2
    list1.append(cal)
    i = i + 1
    j = j - 1
print(list1)'''






'''nums = [1,1,1]
str1 = ""
list1 = []
for i in range(len(nums)):
    str1 = str1 + str(nums[i])
    num = int(str1,2)
    if num % 5 == 0:
        list1.append(True)
    else:
        list1.append(False)
print(list1)'''









'''nums = [1,1,3]
total = sum(nums)
nums.sort()
ans1 = 0
mod = total % 3
if mod == 0:
    print(total)
index_1 = 0
check1 = False
for i in range(len(nums)):
    if nums[i] % 3 == mod:
        index_1 = i
        check1 = True
if check1 == True:
    ans1 = total - nums[index_1]
flag1 = False
flag2 = False
nums.sort()
for i in range(len(nums)):
    if nums[i] % 3 == 3-mod:
        if flag1 == False:
            print(nums[i],i)
            flag1 = True
            total = total - nums[i]
        elif flag2 == False:
            print(nums[i],i)
            flag2 = True
            total = total - nums[i]

    if flag1 == True and flag2 == True:
        break
print(ans1,total,flag1,flag2)
if flag1 == False or flag2 == False:
    print(ans1)
elif flag2 == True and flag1 == True and total != 0:
    if ans1 > total:
        print(ans1)
    else:
        print(total)
else:
    print(0)'''













'''hours = [72,48,24,3]
count = 0
for i in range(len(hours)):
    for j in range(i+1,len(hours)):
        check1 = hours[i] + hours[j]
        if check1 % 24 == 0:
            count += 1
print(count)'''

# print(count)





# list1 = 0
# count_12 = 0
# for i in range(len(hours)):
#     if hours[i] == 12:
#         count_12 += 1
#     elif hours[i] % 24 == 0:
#         list1 += 1
# check1 = count_12 // 2
# print(check1)
# print(list1)







'''nums = [3,6,9]
total = 0
for item in nums:
    if item % 3 == 0:
        pass
    else:
        total += 1
print(total)'''




'''str1 =  "bbcbaba"
total = 0
hash1 = {}
mainset1 = set()
for i in range(len(str1)):
    if str1[i] not in hash1:
        hash1[str1[i]] = i
    else:
        check1 = abs(hash1[str1[i]] - i)
        if check1 >= 2:
            str3 = str1[i]
            for j in range(hash1[str1[i]] + 1, i):
                str3 = str3 + str1[j]
                str3 = str3 + str1[i]
                if str3 not in mainset1:
                    mainset1.add(str3)
                str3 = str1[i]
        hash1[str1[i]] = i
print(mainset1)
print(len(mainset1))
hash2 = {}
for item in str1:
    if item not in hash2:
        hash2[item] = 1
    else:
        hash2[item] += 1
for key, value in hash2.items():
    if value >= 3:
        total += 1
print(total)
'''








'''nums = [1,2,2,1]
hash1 = {}
for i in nums:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
list1 = []
for key, value in hash1.items():
    if value >= 2:
        list1.append(key)
xor1 = 0
for item in list1:
    xor1 = xor1 ^ item
print(xor1)'''







'''nums = [[1,3],[3,7],[8,9]]
nums.sort()
flag = False
list1 = []
for i in range(len(nums)-1):
    if flag == False:
        list1.append(nums[i][0])
        list1.append(nums[i][1])
    if nums[i][0] == nums[i+1][0]:
        list1.append()'''






'''nums = [1,2]
l = 2
r = 2
list1 = []
check1 = 0
i = 0
calc = (len(nums) + 1) - r
count = 0
lenght = len(nums) - l
while i < calc + count and i < lenght+1:
    list1 = []
    j = i
    while j < (i + r) - count:
        list1.append(nums[j])
        sum1 = sum(list1)
        if l <= len(list1) <= r:
            if sum1 >= 1:
                if check1 == 0:
                    check1 = sum1
                else:
                    if check1 > sum1:
                        check1 = sum1
        j = j + 1
    if i >= (calc - 1):
        count += 1
    i = i + 1

print(check1)'''






'''nums = [2,7,9]
original = 4
set1 = set(nums)
for i in range(len(nums)):
    if original in set1:
        original = original * 2
print(original)
'''









'''nums = [1,6,2]
if len(nums) == 1:
    print(True)
elif len(nums) >= 2:
    a = nums[0]
    b = nums[1]
    if a % 2 == 0 and b % 2 != 0:
        pass
    elif a % 2 != 0 and b % 2 == 0:
        pass
    else:
        print(False)
    for i in range(2, len(nums)):
        if a % 2 == 0 and b % 2 != 0:
            a = b
            b = nums[i]
        elif a % 2 != 0 and b % 2 == 0:
            a =  b
            b = nums[i]
        else:
            print(False)
            break
if '''






'''bits = [0,1,1,0,1,0,1,0,0,1,1,0]
stack = ""
for i in range(0,len(bits)):
    if bits[i] == 0:
        if len(stack) == 1:
            stack = stack + str(bits[i])
    elif bits[i] == 1:
        stack = stack + str(bits[i])
    if i == len(bits) - 1 and stack == "" and bits[i] == 0:
        print(True)
        break
    if len(stack) == 2:
        if stack == "11" or stack == "10":
            stack = ""'''











'''grid = [[1,7],[1,1]]

for i in range(len(grid)-1):
    for j in range(len(grid[0])):
        if grid[i+1][j] == grid[i][j]:
            pass
        else:
            print(False)
for i in range(len(grid)):
    for j in range(len(grid[0])-1):
        if grid[i][j+1] != grid[i][j]:
            pass
        else:
            print(False)'''














'''grid = [[1,7],[1,1]]
j = 0
i = 0
while i < len(grid) - 1:
    print(i,j)
    if grid[i+1][j] == grid[i][j]:
        if j < len(grid[0]) - 1:
            if grid[i][j] != grid[i][j+1]:
                j = j + 1
            else:
                print(False)
                break
        if j == len(grid[0])-1:
            j = 0
            i = i + 1
    else:
        print(False)
        break'''
    # if i == len(grid) - 1:











'''nums = [1,0,0,1,0,0,1,0,0,0]
k = 2

i = 0
j = 1
count = 0
while j < len(nums):
    if nums[i] == 1 and nums[j] == 0:
        count += 1
        j = j + 1
    elif nums[i] == 1 and nums[j] == 1:
        if count >= k:
            pass
        else:
            print(False)
            break
        i = j
        j = j + 1
        count = 0
    else:
        i = i + 1
        j = j + 1
'''










# nums1 = [1,1,1,1]
# nums2 = [1,1,1,1]
#
#
# smal1 = nums1[0]
# smal2 = nums2[0]
#
# for i in range(len(nums2)):
#     if nums2[i] < smal2:
#         smal2 = nums2[i]
#     if nums1[i] < smal1:
#         smal1 = nums1[i]
# diff = smal2 - smal1
# print(diff)



















'''s = "111111"
flag = False
str1 = ""
total = 0
for i in range(len(s)):
    if s[i] == "1" and flag == False:
        str1 = str1 + "1"
        flag = True
    elif s[i] == "1" and flag == True:
        str1 = str1 + "1"
    elif s[i] == "0":
        if str1 != "":
            lenght1 = len(str1)
            cal = (lenght1 * (lenght1 + 1))//2
            total += cal

        flag = False
        str1 = ""
if str1 != "":
    lenght1 = len(str1)
    cal = (lenght1 * (lenght1 + 1)) // 2
    total += cal
print(total)
'''



'''grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
B = "B"
W = "W"

a = grid[0][0]
c = grid[1][0]
b = grid[0][1]
d = grid[1][1]
hash1 = {}
for i in [a,c,b,d]:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
for key ,value in hash1.items():
    if value >= 3:
        print(True)
        break


e = grid[0][1]
f = grid[1][1]
g = grid[0][2]
h = grid[1][2]

hash1 = {}
for i in [e,f,g,h]:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
for key ,value in hash1.items():
    if value >= 3:
        print(True)
        break

i = grid[1][0]
j = grid[1][1]
k = grid[2][0]
l = grid[2][1]


hash1 = {}
for i in [i,j,k,l]:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
for key ,value in hash1.items():
    if value >= 3:
        print(True)
        break


m = grid[1][1]
n = grid[1][2]
o = grid[2][1]
p = grid[2][2]

hash1 = {}
for i in [m,n,o,p]:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
for key ,value in hash1.items():
    if value >= 3:
        print(True)
        break'''










'''nums = [3,2,1]
strictly_increase = 1
flag = False
count = 1
for i in range(len(nums)-1):
    if nums[i] < nums[i+1] and flag == False:
        count += 1
        flag = True
    elif nums[i] < nums[i+1] and flag == True:
        count += 1
    else:
        flag = False
        if count > strictly_increase:
            strictly_increase = count
        count = 1
if strictly_increase < count:
    strictly_increase = count


strictly_decrease = 1
flag = False
count1 = 1
nums.reverse()
for i in range(len(nums)-1):
    if nums[i] < nums[i+1] and flag == False:
        count1 += 1
        flag = True
    elif nums[i] < nums[i+1] and flag == True:
        count1 += 1
    else:
        flag = False
        if count1 > strictly_decrease:
            strictly_decrease = count1

        count1 = 1
if strictly_decrease < count1:
    strictly_decrease = count1


if strictly_increase > strictly_decrease:
    print(strictly_increase)
print(strictly_decrease)'''

# def chec1(nums):
#     strictly_increase = 1
#     flag = False
#     count = 1
#     for i in range(len(nums) - 1):
#         if nums[i] < nums[i + 1] and flag == False:
#             count += 1
#             flag = True
#         elif nums[i] < nums[i + 1] and flag == True:
#             count += 1
#         else:
#             flag = False
#             if count > strictly_increase:
#                 strictly_increase = count
#
#             count = 1
#     if strictly_increase < count:
#         strictly_increase = count
#     hold = strictly_increase
#     nums.reverse()
#     hold2 = chec1(nums)
#     if h
#
# nums = [3,2,1]
# print(chec1(nums))






# nums = [1,2,3]
# k = 2
# count = 0
# sub_array = 0
# sub_array_length = 0
# flag = False
# for i in range(len(nums)):
#     sub_array = sub_array + nums[i]
#     sub_array_length = sub_array_length + 1
#     if sub_array > k:
#         print(count,sub_array_length,sub_array)
#         if count > sub_array_length or count == 0:
#             flag = True
#             count = sub_array_length
#             sub_array_length = 0
#             sub_array = 0
#             sub_array = sub_array + nums[i]
#             sub_array_length = sub_array_length + 1
#             if sub_array > k:
#                 if count > sub_array_length or count == 0:
#                     count = sub_array_length
#                     break
#             else:
#                 if nums[i] > k:
#                     print(1)
# if sub_array_length < count and sub_array > k:
#     count = sub_array_length
# # if count == 0 and sub_array_length != 0:
# #     print(sub_array_length)
# if flag == False:
#     print(-1)
# print(count)





# print(2 or 1 or 8)



'''n = 13
queries = [[3,1,7,3],[7,5,7,8],[4,12,6,12],[2,8,6,11],[9,11,10,11],[9,3,11,11],[0,12,10,12],[10,5,11,12],[4,7,6,12],[0,2,9,6],[12,7,12,11],[2,7,3,8],[2,9,6,12],[10,7,10,12],[11,6,11,7],[3,2,12,9]]
mat = [[0 for _ in range(n)] for _ in range(n)]
for row1, col1, row2, col2 in queries:
    mat[row1][col1] = mat[row1][col1] + 1
    mat[row2][col1] = mat[row2][col1] + 1
    mat[row1][col2] = mat[row1][col2] + 1
    mat[row2][col2] = mat[row2][col2] + 1
    print(row1,col1,row2,col2)
print(mat)'''












# n = 13
# queries = [[3,1,7,3],[7,5,7,8],[4,12,6,12],[2,8,6,11],[9,11,10,11],[9,3,11,11],[0,12,10,12],[10,5,11,12],[4,7,6,12],[0,2,9,6],[12,7,12,11],[2,7,3,8],[2,9,6,12],[10,7,10,12],[11,6,11,7],[3,2,12,9]]
# mat = [[0 for i in range(n)] for j in range(n)]
#
# row = []
# col = []
# for i in range(len(queries)):
#     list1 = []
#     list2 = []
#     for j in range(len(queries[i])):
#         if j % 2 == 0:
#             list1.append(queries[i][j])
#         else:
#             list2.append(queries[i][j])
#     print(list1,list2)
#     for k in list1:
#         for l in list2:
#             mat[k][l] = mat[k][l] + 1
# print(mat)















'''nums = [10,21,31]
sum1 = 0
for i in range(len(nums)):
    str1 = str(nums[i])
    list1 = list(str1)
    list2 = []
    for k in list1:
        list2.append(int(k))
    max1 = max(list2)
    str2 = ""
    for _ in range(len(str1)):
        str2 = str2 + str(max1)
    sum1 = sum1 + int(str2)'''

# print(sum1)






'''s = "00111"
count1 = 0
total = 0
flag = False
for i in range(len(s)):
    if s[i] == "1":
        count1 += 1
        flag = True
    if s[i] == "0":
        if count1 != 0:
            if flag == True:
                flag = False
                total += count1
print(total)'''



'''apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
sum1 = sum(apple)
capacity.sort()
count = 0
total = 0
for i in range(len(capacity)-1,-1,-1):
    if sum1 >= 0:
        sum1 = sum1 - capacity[i]
        total += capacity[i]
        count = count + 1
    else:
        break
print(count)'''










'''nums = [1,2,14,15]
arr1 = [nums[0]]
arr2 = [nums[1]]
flag = False
for i in range(2,len(nums)):
    if arr1[-1] > arr2[-1]:
        arr1.append(nums[i])
    else:
        arr2.append(nums[i])

print(arr1,arr2)'''
# if arr1[-1] > arr2[-1]:
#     arr1.append(nums[-1])
# else:
#     arr2.append(nums[-1])








'''nums = [6,10,15]
flag = False
for i in range(len(nums)-1):
    greatest = 0
    for j in range(1,nums[i]+1):
        if nums[i] % j == 0 and nums[i+1] % j == 0:
            print(nums[i],j)
            if greatest < j:
                greatest = j
    if greatest == 1:
        flag = True
        break
print(flag)
count = 0
for i in range(len(nums)):
    if nums[i] != 1:
        count += 1
print(count)'''






'''nums = [1,1,2,4,9]
k = 9
count = 0
for i in range(len(nums)):
    if nums[i] < k:
        count += 1
print(count)'''







'''nums = [4,4,9,10]
main = len(nums)/2
hash1 = {}
list1 = []
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
    else:
        hash1[nums[i]] += 1
count1 = 0
count2 = 0
for key, value in hash1.items():
    if value == 2:
        count2 += 2
    elif value > 2:
        print(False)
        break
    else:
        count1 += 1
if count1 % 2 == 0 and count2 % 2 == 0:
    print(True)
else:
    print(False)
'''









'''def countPrefixSuffixPairs(words):
    count = 0
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            if len(words[i]) <= len(words[j]):
                flag = False
                for k in range(len(words[i])):
                    if words[i][k] == words[j][k]:
                        pass
                    else:
                        break
                else:
                    flag = True
                flag2 = False
                l = len(words[j]) - 1
                if flag == True:
                    for p in range(len(words[i]) - 1, -1, -1):
                        if words[i][p] == words[j][l]:
                            l = l - 1
                        else:
                            break
                    else:
                        flag2 = True
                if flag and flag2:
                    count += 1
    return count

words = ["bb","bb"]
# words.sort()
print(countPrefixSuffixPairs(words))'''







'''num1 = 10
num2 = 10
count = 0
while num1 > 0 and num2 > 0:
    count += 1
    if num1 >= num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
print(count)'''





'''nums = [5,3]
nums.reverse()
count = 1
i = len(nums)
sum1 = nums[-1] + nums[-2]
nums.pop()
nums.pop()
while i >= 2 and len(nums) >= 2:
    sum2 = nums[-1] + nums[-2]
    if sum1 == sum2:
        nums.pop()
        nums.pop()
        count += 1
        i = len(nums)
    else:
        break
print(count)'''







'''n = 4
str1 = str(bin(n))[2:]
list1 = list(str1)
count = 1
for i in range(len(list1) - 1):
    if list1[i] == "1":
        if list1[i+1] == "0":
            count += 1
            list1[i+1] = "1"
    count += 1
print(count)'''




'''matrix = [[3,-1],[5,2]]
for i in range(len(matrix[0])):
    list1 = []
    max1 = -1
    for j in range(len(matrix)):
        if matrix[j][i] == -1:
            list1.append(tuple([j,i]))
        if matrix[j][i] > max1:
            max1 = matrix[j][i]
    for k in range(len(list1)):
        x,y = list1[k]
        matrix[x][y] = max1
print(matrix)'''








'''nums = [2,3,-5]
total = 0
count = 0
flag = False
for i in range(len(nums)):
    if flag == False:
        total += nums[i]
        flag = True
        if total == 0:
            count += 1
    elif flag == True:
        total += nums[i]
        if total == 0:
            count += 1
print(count)'''






'''nums = [8,4,4]
a = nums[0]
b = nums[1]
c = nums[2]
x = a + b
y = b + c
z = a + c
if x > c and y > a and z > b:
    print("scalene")
elif x == y or y == z or z == x:
    print("isosceles")
elif'''






'''nums = [1,2,3,12]
sum1 = nums[0]
min1 = min(nums[1],nums[2])
min2 = max(nums[1],nums[2])
for i in range(3,len(nums)):
    if nums[i] <= min1:
        min2 = min1
        min1 = nums[i]
    elif min1 <= nums[i] < min2:
        min2 = nums[i]
print(sum1,min1,min2)'''




# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         sum2 = 0
#         flag = False
#         for k in range(j+1,len(nums)):
#             if flag == False:
#                 sum2 = sum2 +



# sum1 = 0
# count = 0
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         sum1 = sum1 + nums[i]
#         count += 1
#     if count < 3 and i == len(nums) - 2:
#         sum1 += nums[i+1]
#         count += 1
#     if count == 3:
#         print(sum1)
#         break




# nums = [1,2,3,2,5]
# # if len(nums) == 1:
# #     ret
# list1 = []
# list2 = []
# set1 = set()
# total = 0
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         if list1 == []:
#             list1.append(nums[i])
#             total += nums[i]
#             total += nums[i+1]
#             list1.append(nums[i+1])
#         else:
#             list1.append(nums[i+1])
#             total += nums[i+1]
#     else:
#         list1.append(nums[i])
#         total += nums[i]
#         set1.add(total)
#         if len(list1) > len(list2):
#             list2 = list1
#         list1 = []
#         total = 0
#         # list1.append(nums[i+1])
# print(list1,list2,set1)
# if list1 != []:
#     if len(list2) < len(list1):
#         list2 = list1
# sum1 = sum(list2)
# set1 = set(nums)
# while sum1 in nums:
#     sum1 += 1
# print(sum1)






'''nums = [2,4,8,16]
total = 0
flag = False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        check1 = nums[i] | nums[j]
        check2 = str(bin(check1))
        if check2[-1] == "0":
            ret
'''






'''nums = [2,5]
nums.sort()
i = 0
while i < len(nums):
    nums[i],nums[i+1] = nums[i+1],nums[i]
    i = i + 2
print(nums)'''



# nums = [2,5]
# nums.sort()
# arr = []
# for i in range(0,len(nums),2):
#     alice = nums[i]
#     bob = nums[i+1]
#     arr.append(bob)
#     arr.append(alice)
# print(arr)


# nums = [5]
# head = [1,2,3,4]


# set1 = set(nums)
# list1 = []
# for i in range(len(head)):
#     if head[i] not in set1:
#         list1.append(head[i])
# print(list1)






'''height =  [0,1,0,2,1,0,1,3,2,1,2,1]
list1 = []
flag = False
index = 0
for i in range(len(height)-1):
    if flag == False:
        if height[i] <= height[i+1]:
            pass
        else:
            flag = True
            index = i
            break
    if i == len(height) - 2:
        index = i+1
flag = False
index2 = len(height) - 1
for j in range(len(height) - 1,0,-1):
    if height[j-1] >= height[j]:
        pass
    else:
        flag = True
        index2 = j
        break
    if j == 1:
        j = 0
hash1 = {}
list1 = height[index : index2 + 1]

stack = [list1[0],list1[1]]
max1 = max(stack)
print(stack)
for i in range(2,len(list1)):
    if max1 >= list1[i]:
        stack.append(list1[i])
    else:
'''





'''grid = [[9,1,7],[8,9,2],[3,4,6]]
n = len(grid)
hash1 = {}
list1 = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] not in hash1:
            hash1[grid[i][j]] = 1
        else:
            hash1[grid[i][j]] += 1
list1 = []
for key, value in hash1.items():
    if value == 2:
        list1.append(key)
        break
for i in range(1, (n*n)+1):
    if i not in hash1:
        list1.append(i)
print(list1)'''











'''nums = [7,8,9,11,12]
lenght_nums = len(nums)
max1 = max(nums)
count = 0
set1 = set(nums)
min1 = max1
if max1 < 0:
    print(1)
for i in range(len(nums)):
    if nums[i] > 0:
        if min1 > nums[i]:
            min1 = nums[i]
if min1 > 1:
    print(1)
for i in range(min1,max1):
    if i in set1:
        count += 1
    else:
        print(i)
        break
if count < len(nums):
    print(max1 + 1)
'''




'''bank = ["000","111","000"]
total = 0
flag = False
one_count = 0
for item in bank:
    if flag == False:
        list1 = list(item)
        one_count = list1.count("1")
        if one_count > 0:
            flag = True
    elif flag == True:
        list1 = list(item)
        one_count1 = list1.count("1")
        total = total +  (one_count1 * one_count)
        if one_count1 > 0:
            one_count = one_count1
print(total)'''









'''nums1 = [3, 4, 2, 3]
nums2 = [1, 5]
hash1 = {}
for i in nums1:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
hash2 = {}
for i in nums2:
    if i not in hash2:
        hash2[i] = 1
    else:
        hash2[i] += 1
nums1 = list(set(nums1))
nums2 = list(set(nums2))
answe1 = [0,0]
total = 0
for i in nums2:
    if i in hash1:
        total += hash1[i]
answe1[0] = total
total = 0
for i in nums1:
    if i in hash2:
        total += hash2[i]
answe1[1] = total

print(answe1)'''











'''class Bank:
    def __init__(self,balance):
        self.balance = balance
    def transsfer(self,account1,account2,money):
        if 1 <= account1 <= 5 and 1 <= account2 <= 5:
            if self.balance[account1-1] >= money:
                self.balance[account1 - 1] = self.balance[account1 - 1] - money
                self.balance[account2 - 1] = self.balance[account2 - 1] + money
                return True
        return False
    def deposit(self,account,money):
        if 1 <= account <= 5:
            self.balance[account - 1] += money
            return True
        return False
    def withdraw(self,account,money):
        if 1 <= account <= 5:
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
        return False

balanc1  = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
obj1 = Bank()'''



'''mountain = [1,4,3,8,5]
list1 = []
for i in range(1,len(mountain)-1):
    if mountain[i-1] < mountain[i] > mountain[i+1]:
        list1.append(i)
print(list1)'''




'''n = 4
calc = int(n / 7)
total = 0
count = 0
week = 21
ginati = 1
for i in range(calc):
    week = week - count
    week = week + 7 + count
    total += week
    count += 1
    ginati += 1
    # print(total,week)
# print(total)
calc1 = int(n % 7)
for i in range(calc1):
    total += ginati
    ginati += 1
print(total)'''









'''mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
check1 = mat.copy()
print(check1)
l = 2
for i in range(l):
    list1 = []
    for j in range(len(mat)):
        list2 = [0] * len(mat[j])
        list1.append(list2)
        for k in range(len(mat[j])):
            if j % 2 == 0:
                list1[j][k-1] = mat[j][k]
            else:
                if k+1 >= len(mat[j]):
                    list1[j][0] = mat[j][k]
                else:
                    list1[j][k+1] = mat[j][k]

    mat = list1

print(mat)'''






# hash1 = {}
# for i in range(1,6):
#     hash1[i] = int(str(i) * i)
# print(hash1)
# pattern = [1,22,333,4444,55555]
# check1 = []
# for i in range(len(pattern)):
#     for j in range(i+1, len(pattern)):
#         count = 0
#         # main_count = 0
#         for k in range(len(str(pattern[i])+str(pattern[j]))):
#             l = 0
#             str1 = ""
#             while l < len(str(pattern[j])):
#                 if count == k:
#                     str1 = str1 + str(pattern[i])
#                     check1.append(str1)
#                     count = 0
#                 else:
#                     str1 = str1 + str(pattern[j])[l]
#                     count += 1
#                 l = l + 1
#
#
#
#         # l = 0
#         # count = 0
#         # str1 = ""
#         # while l < len(str(pattern[i])+str(pattern[j])):
#         #     if count == l:
#         #         str1 = str1 + (str(pattern[i]) + str(pattern[j]))[count]
#         #         count = l+1
#         #         str1 = str1 + (str(pattern[i])+str(pattern[j]))[l+1:]
#         #         check1.append(str1)
#         #         str1 = ""
#         #         l = l + 1
#         #     else:
#         #         str1 = str1 + (str(pattern[i]) + str(pattern[j]))[count]
#         #         count += 1
#
#
# print(check1)












# n  = 1000
# str1 = str(n)
# hash1 = {}
# for item in str1:
#     if item not in hash1:
#         hash1[item] = 1
#     else:
#         hash1[item] += 1
# print(hash1)




# n = 3444
# str1 = str(n)
# list1 = list(str1)
# i = 0
# hash1 =
# while True:
#     if list1[i] == "0":





# str1 = str(n)
# hash1 = {}
# for item in str1:
#     if int(item) not in hash1:
#         hash1[int(item)] = 1
#     else:
#         hash1[int(item)] += 1
# list1 = []
# for key, value in hash1.items():
#     if value in hash1 and key == 0:
#         list1.append(value)
# print(hash1)
# print(list1)






# words = ["abc","bcd","aaaa","cbc"]
# for item in words:
#     set1 = set(item)



'''words = ["abc","bcd","aaaa","cbc"]
x = "z"
list1 = []
i = 0
for item in words:
    a = set(list(item))
    if x in a:
        list1.append(i)
    i = i + 1
print(list1)'''






'''s = "223"
while len(s) > 2:
    str1 = ""
    for i in range(len(s)-1):
        rema = (int(s[i]) + int(s[i+1])) % 10
        str1 = str1 + str(rema)
    s = str1
if s[0] == s[1]:
    print(True)
else:
    print(False)'''




'''nums = [10,100]
strong_pair = []
for i in  range(len(nums)):
    for j in range(i,len(nums)):
        if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
            pair = [nums[i],nums[j]]
            strong_pair.append(pair)
max_xor = 0
for item in strong_pair:
    a,b = item
    check = a ^ b
    if check > max_xor:
        max_xor = check
print(max_xor)'''










'''grid = [[0,0,1],[1,0,1],[0,0,0]]
hash1 = {}
for i in range(len(grid)):
    count = 0
    for j in range(i+1,len(grid)):
        if grid[i][j] == 1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        else:
            if j not in hash1:
                hash1[j] = 1
            else:
                hash1[j] += 1
print(hash1)'''


# import random
#
# s = random.uniform(10,100)
# print(s)
















'''import asyncio
import random

async def process_number(n):
    print(f"Processing {n}...")
    await asyncio.sleep(random.uniform(1, 3))  # simulate waiting
    print(f"Done with {n}")
    return n * n

async def main():
    numbers = [1, 2, 3, 4, 5]
    tasks = [process_number(num) for num in numbers]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

asyncio.run(main())'''








# import asyncio
#
#
#
# async def task(name):
#     print(f"Starting {name}")
#     await asyncio.sleep(2)
#     print(f"Finished {name}")
#
# async def main():
#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2")
#     )
#
# asyncio.run(main())




# async def bg(nums):
#     print(nums)
#     await gb(nums)
#
# async def gb(nums):
#     print(nums)
#     await bg(nums)
# nums = [1,2,3,4,55,6,7]
# for i in range(len(nums)):
#     gb(nums[i])






# nums = [88,53]
# k = 27
# numOperations = 2
# hash1 = {}
# for item in nums:
#     if item not in hash1:
#         hash1[item] = 1
#     else:
#         hash1[item] += 1
# hash2 = {}
# nums.sort()
# count_numoperation = 0
# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1]:
#         pass
#     elif -k <= abs(nums[i] - nums[i+1]) <= k:
#         count_numoperation += 1
#         diff = nums[i+1] - nums[i]
#         nums[i] = nums[i] + diff
#         if nums[i] not in hash2:
#             hash2[nums[i]] = 1
#         else:
#             hash2[nums[i]] += 1
# count = 0
# total = 0
# print(hash1)
# print(hash2)
# for key, value in hash1.items():
#     local_total = 0
#     if key in hash2:
#         if hash2[key] <= numOperations:
#             local_total = local_total + hash2[key]
#         elif hash2[key] > numOperations:
#             local_total = local_total + numOperations
#
#     local_total = local_total + value
#     if total < local_total:
#         total = local_total
# print(total)























'''nums = [10,8,5,9,11,6,8]
k = 1
max1 = max(nums)
max_bin = str(bin(max1))[2:]
list1 = []
for item in nums:
    if len(str(bin(max1))[2:]) >= len(str(bin(item))[2:]):
        print(item)
        calc = len(str(bin(max1))[2:]) - len(str(bin(item))[2:])
        zero_add = "0" * calc
        check1 = zero_add + str(bin(item))[2:]
        list1.append(check1)
str1 = ""
j = 0
for j in range(len(list1[0])):
    count = 0
    for i in range(len(list1)):
        if list1[i][j] == "1":
            count += 1
    if count >= k:
        str1 = str1 + "1"
    else:
        str1 = str1 + "0"

print(int(str1,2))
print(list1)'''












'''operations = ["X++","++X","--X","X--"]
total = 0
for i in range(len(operations)):
    if operations[i][1] == "-" or operations[i][-1] == "-":
        total = total - 1
    else:
        total += 1
print(total)'''



'''nums = [1,1]
total = 0
for i in range(len(nums)):
    set1 = set()
    for j in range(i,len(nums)):
        set1.add(nums[j])
        total += len(set1) * len(set1)
print(total)'''







'''nums = [1,1]
total = len(nums)
for i in range(len(nums)):
    set1 = set()
    for j in range(i,len(nums)):
        set1.add(nums[j])
        if len(set1) > 1:
            total += len(set1) * len(set1)
print(total)
'''











'''s = "74"
a = 5
b = 1
mini = int(s)
main_str = s
count = 0
while count < 200:
    s1 = s[b:len(s)] + s[:b]
    if mini > int(s1):
        mini = int(s1)
        main_str = s1
        s = s1
    str1 = ""
    for i in range(len(s)):
        if i % 2 != 0:
            cal = int(s[i]) + a
            add = str(cal)[-1]
            str1 = str1 + add
        else:
            str1 = str1 + s[i]
    if int(str1) < mini:
        mini = int(str1)
        main_str = str1
    s = str1
    print(main_str)
    count += 1'''

















'''from  collections import  deque

nums = [1,5,5,5]
left = [nums[0]]
right = deque(nums[2:])
minimi = ""
for i in range(1,len(nums)-1):
    if nums[i] > min(left) and nums[i] > min(right):
        minim = nums[i] + min(left) + min(right)
        if minimi == "":
            minimi = minim
        elif minim < minimi:
            minimi = minim
    right.popleft()
    left.append(nums[i])

print(minimi)'''








'''nums= [8,8,10,9,9]
nums.sort()
k = 1
hash1 = {}
for item in nums:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1    ##[5, 7, 7, 7, 8, 8, 9, 9, 10, 10]
j = -k
flag = False
list1 = []
check = 0
for key, value in hash1.items():
    if flag == True:
        if check - key <= (-k):
            j = -k
        else:
            j = (check - key) + 1
    if -k <= j <= k:
        for i in range(value):
            check = j + key
            list1.append(check)
            j = j + 1
            flag = True
print(list1)'''





# nums= [1,1,1,1,1,1,1,1,5,5,5]
# k = 3
# nums.sort()
# hash1 = {}
# for item in nums:
#     if item not in hash1:
#         hash1[item] = 1    #[5, 7, 7, 7, 8, 8, 9, 9, 10, 10]
#     else:
#         hash1[item] += 1
# print(hash1)
# list1 = []                              ###########################################
# checkk = 0
# flag = False
# for key,value in hash1.items():
#     j = -k
#     i = 0
#     if checkk <= k and flag:
#         j = checkk
#     while i < value and j <= k:
#         flag = True
#         ch1 = j + key
#         list1.append(ch1)
#         j = j + 1
#         i = i + 1
#     checkk = j-1
#     print(checkk)
# print(set(list1))
# print(list1)


# nums = [7,9,10,7,7,9,8,5,10,8]
# k = 2

# nums.sort()
# set1 = set()
# j = -k
# print(nums)  #[5, 7, 7, 7, 8, 8, 9, 9, 10, 10]
# for i in range(len(nums)):
#     ch1 = j + nums[i]
#     if ch1 not in set1:
#         set1.add(ch1)
#         nums[i] = ch1
#         if j == k:
#             j = -k
#         else:
#             j = j + 1
#     else:
#         while j <= k:
#             ch1 = j + nums[i]
#             if ch1 not in set1:
#                 set1.add(ch1)
#                 nums[i] = ch1
#             if j == k:
#                 j = -k
#                 break
#             else:
#                 j = j + 1
# print(set1)
# print(set(nums))
# print()






# set1 = set(nums)
# nums.sort()
# j = -k
# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1] and j <= k:
#         print(j, nums[i])
#         check1 = j + nums[i]
#         if check1 not in set1:
#             set1.add(check1)
#             nums[i] = check1
#         else:
#             while j <= k:
#                 check1 = j + nums[i]
#                 if check1 not in set1:
#                     set1.add(check1)
#                     nums[i] = check1
#                     j = -k
#                     break
#                 else:
#                     j = j + 1
#         j = j + 1
#     else:
#         j = -k
#
#
# print(nums)




# set1 = set(nums)
# k = 1
# set3 = set(nums)
# calc = len(nums) - len(set3)
# if k > calc:
#     print(len(nums))
# nums.sort()
# list1 = [x for x in range(-k, k+1)]
# j = 0
# flag = False
# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1] and j < len(list1):
#         check1 = list1[j] + nums[i]
#         # print(check1)
#         if check1 not in set1:
#             set1.add(check1)
#             nums[i] = check1
#         else:
#             while j < len(list1):
#                 check1 = list1[j] + nums[i]
#                 if check1 not in set1:
#                     set1.add(check1)
#                     nums[i] = check1
#                     break
#                 else:
#                     j = j + 1
#         j = j + 1
#     else:
#         j = 0
#     print(j)
# # if nums[-2] == nums[-1] and j < len(list1)-1:
# #     nums[-1] = list1[-1] + nums[-1]
#
# print(len(set(nums)))
# print(nums)












# nums = [1,1,1,1,1,1,1,1,5,5,5]
# k = 3
# atmost = k + k
# print(atmost)
# if k == 1:
#     atmost = 2
# hash1 = {}
# count = 0
# for i in range(len(nums)):
#     if nums[i] not in hash1:
#         hash1[nums[i]] = 1
#         count = count + 1
#     else:
#         if atmost > 0 :
#             atmost = atmost - 1
#             count += 1
#         else:
#             break
# print(count)










'''nums =[5,1,4,1]
indexDifference = 2
valueDifference = 4
list1 = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
            list1.append(i)
            list1.append(j)
            break
print(list1)
'''






# i = 0
# j = len(nums) - 1
# list1 = []
# while i < j:
#     if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
#         list1.append(i)
#         list1.append(j)
#         break
#     start = nums[i] - valueDifference
#     end = nums[j] - valueDifference
#     if start > end:
#         j = j - 1
#     else:
#         i = i + 1
#     # if nums[i] < nums[j]:
#     #     j = j - 1
#     # elif nums[i] >= nums[j]:
#     #     i = i + 1
# print(list1)

















# nums = [1,-10,7,13,6,8]
# value = 7
# list1 = [0] * (len(nums)+1)
# for item in nums:
#     a = abs(item) % value
#     list1[a] += 1
# print(list1)


#
# print(-10%7)








'''from collections import deque
nums = [1,-1,2,-1,-1]
seen = deque()
ans = []
k = 0
for item in nums:
    if item > -1:
        k = 0
        seen.appendleft(item)
    else:
        if k < len(seen):
            ans.append(seen[k])
        else:
            ans.append(item)
        k = k + 1
print(ans)'''


    # if item < 0:
    #     k = k + 1
    # else:
    #     seen.append(item)
    # if k <= len(seen) and item == -1:
    #     ans.append(item)









# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# k =5
# nums[:k], nums[len(nums)-k:] = nums[len(nums)-k:], nums[:k]
# print(nums)




# nums = [-15,19]
# sub_array = []
# main_list1 = []
# for i in range(len(nums)-1):
#      if nums[i] < nums[i+1]:
#          sub_array.append(nums[i])
#          if i == len(nums) - 2:
#              sub_array.append(nums[i+1])
#      else:
#          sub_array.append(nums[i])
#          main_list1.append(len(sub_array))
#          sub_array = []
#          if i == len(nums) - 2:
#              sub_array.append(nums[i+1])
# if sub_array != []:
#     main_list1.append(len(sub_array))
# max_k = 0
# print(main_list1)
# # main_list1 = [5,4,4,3,6]
# if len(main_list1) > 1:
#     for item in main_list1:
#         if item // 2 > max_k:
#             max_k = item // 2
#     for i in range(len(main_list1) - 1):
#         a = main_list1[i]
#         b = main_list1[i+1]
#         if a > b:
#             if b > max_k:
#                 max_k = b
#         else:
#             if a > max_k:
#                 max_k = a
    # max1 = 0
    # max2 = 0
    # if main_list1[0] > main_list1[1]:
    #     max1 = main_list1[0]
    #     max2 = main_list1[1]
    # else:
    #     max1 = main_list1[1]
    #     max2 = main_list1[0]
    # for i in range(2,len(main_list1)):
    #     if main_list1[i] >= max1:
    #         max2 = max1
    #         max1 = main_list1[i]
    #     elif max1 > main_list1[i] > max2:
    #         max2 = main_list1[i]
    # if max2 > max_k:
    #     max_k = max2
# else:
#     max_k = main_list1[-1] // 2
# print(max_k)







# nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]
# max1_index = nums[2]
# ma_index = 2
# centre_value = nums[1]
# ce_index = 1
# min1_value = nums[0]
# mi_index = 0
#
# for i in range(2,len(nums)):
#     if max1_index <= nums[i]:
#         ma_index = i
#         max1_index = nums[i]
# # print(max1_index,ma_index)
# for i in range(1,len(nums)-1):
#     print(centre_value, nums[i], i , ma_index)
#     if centre_value >= nums[i] and i < ma_index:
#         ce_index = i
#         centre_value = nums[i]
# # print(centre_value,ce_index)
# for i in range(len(nums)-2):
#     if min1_value <= nums[i] and i < ce_index and i < ma_index:
#         min1_value = nums[i]
#         mi_index = i
# print(min1_value,centre_value,max1_index)
# print(max1_index,ma_index,centre_value,min1_value)
# a = (min1_value - centre_value) * max1_index
# print(a)

# nums =[12,6,1,2,7]
#
# max2 = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             a = (nums[i] - nums[j]) * nums[k]
#             print(a)
#             if a > max2:
#                 max2 = a
# print(max2)








'''nums = [-15,-13,4,7]
k = 2
main_list1 = []
sub_array = []

for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        sub_array.append(nums[i])
        if i == len(nums) - 2:
            sub_array.append(nums[i+1])
    else:
        sub_array.append(nums[i])
        main_list1.append(len(sub_array))
        sub_array  = []
        if i == len(nums) - 2:
            main_list1.append(1)
if sub_array != []:
    main_list1.append(len(sub_array))
print(main_list1)
for i in range(len(main_list1) - 1):
    if main_list1[i] >= k and main_list1[i+1] >= k:
        print(True)
        break
    elif main_list1[i] >= (k + k):
        print(True)
        break

else:
    print(False)
if main_list1[-1] >= k + k:
    print(True)'''











'''nums = [4,3,2,1]
k = 2
total = 0
for i in range(len(nums)):
    a = bin(i)
    a = a[2:]
    a = str(a)
    count = 0
    for j in range(len(a)):
        # print(a[j],nums[i])
        if a[j] == "1":
            count += 1
    if count == k:
        print(nums[i],a)
        total += nums[i]
print(total)'''






'''nums =[72,13,21,35,52]
start = nums[0]
j = len(nums) - 1
count = 0
while start >= nums[j] and j > 0:
    if nums[j] >= nums[j - 1]:
        pass
    else:
        count = count + 1
        j = j - 1
        break
    j = j - 1
    count = count + 1
for i in range(0,j):
    if nums[i] <= nums[i+1]:
        pass
    else:
        print(-1)
        break
else:
    print(count)'''












'''power = [7,1,6,6]
# sum1 = sum(power)
hash1 = {}
for item in power:
    if item not in hash1:
        hash1[item] = item
    else:
        hash1[item] += item
set1 = set(power)
arr = list(set1)
arr.sort()
hash2 = {}
max1 = 0
for i in range(len(arr)):
    if arr[i] - 2 in set1:
        if arr[i] not in hash2:
            hash2[arr[i]-2] = arr[i]
        else:
            sum1 = hash2[arr[i]-2]
            sum2 = hash1[sum1]
            total = sum2 + arr[i]
            if max1 < total:
                max1 = total
                total = 0
            hash2[arr[i] - 2] = arr[i]
    if arr[i] - 1 in set1:
        if arr[i] not in hash2:
            hash2[arr[i]-1] = arr[i]
        else:
            sum1 = hash2[arr[i]]
            sum2 = hash1[sum1]
            total = sum2 + arr[i]
            if max1 < total:
                max1 = total
                total = 0
            hash2[arr[i] -1] = arr[i]
    if arr[i] + 1 in set1:
        if arr[i]  not in hash2:
            hash2[arr[i]+1] = arr[i]
        else:
            sum1 = hash2[arr[i]+1]
            sum2 = hash1[sum1]
            total = sum2 + arr[i]
            if max1 < total:
                max1 = total
                total = 0
            hash2[arr[i] +1] = arr[i]
    if arr[i] + 2 in set1:
        if arr[i]  not in hash2:
            hash2[arr[i]+2] = arr[i]
        else:
            sum1 = hash2[arr[i]+2]
            sum2 = hash1[sum1]
            total = sum2 + arr[i]
            if max1 < total:
                max1 = total
                total = 0
            hash2[arr[i] + 2] = arr[i]
print(hash2)
print(max1)'''



'''power = [7,1,6,3]
sum1 = sum(power)
hash1 = {}
for item in power:
    if item not in hash1:
        hash1[item] = item
    else:
        hash1[item] += item
print(hash1)
set1 = set(power)
list1 = list(set1)
max1 = 0
list2= []
for i in range(len(list1)):
    simpl1 = sum1
    flag = False
    if list1[i] - 2 in hash1:
        flag = True
        simpl1 = simpl1 - hash1[list1[i]-2]
    if list1[i] - 1 in hash1:
        flag = True
        simpl1 = simpl1 - hash1[list1[i]-1]
    if list1[i] + 1 in hash1:
        flag = True
        simpl1 = simpl1 - hash1[list1[i] + 1]
    if list1[i] + 2 in hash1:
        flag = True
        simpl1 = simpl1 - hash1[list1[i] + 2]
    if flag ==  True:
        list2.append(list1[i])
    if max1 < simpl1 and flag == True:
        max1 = simpl1
    print(simpl1)
print(max1)
print(list2)'''




'''nums = [[3,6],[1,5],[4,7]]
nums.sort()
total = 0
x1 = nums[0][0]
y1 = nums[0][1]
total = total + (y1 - x1) + 1
for i in range(1,len(nums)):
    if nums[i][0] <= y1:
        if nums[i][1]>= y1:
            total = total + nums[i][1] - y1
            y1 = nums[i][1]
            x1 = nums[i][0]
    else:
        x1 = nums[i][0]
        y1 = nums[i][1]
        total = total + (y1 - x1) + 1
print(total)
print(nums)
'''









'''nums = [-6,2,5,-2,-7,-1,3]
target = -2
nums.sort()
i = 0
j = len(nums) - 1
print(nums)
total = 0
while i < j:
    if nums[i] + nums[j] >= target:
        j = j - 1
    elif nums[i] + nums[j] < target:
        print(i, j)
        i = i + 1
        total = total + (((j+1)) - i)
        # print(i,j)
print(total)'''








'''spells = [3,1,2]
potions = [8,5,8]
success = 16
potions.sort()
list1 = []
for i in range(len(spells)):
    left = 0
    right = len(potions)
    index = ""
    while left < right:
        mid = (left + right)//2
        if potions[mid] * spells[i] >= success:
            index = mid
            right = mid
        else:
            left = mid + 1
    if index != "":
        cal = len(potions) - index
        list1.append(cal)
    else:
        list1.append(0)
print(list1)
'''





'''nums = [51,71,17,24,42]
list1 = []
for item in nums:
    str1 = str(item)
    a = str1.strip()
    max1 = max(a)
    list1.append(int(max1))

hash1 = {}
total = 0
flag = False
for i in range(len(list1)):
    if list1[i] not in hash1:
        hash1[list1[i]] = i
    else:
        flag = True
        sum1 = nums[i] + nums[hash1[list1[i]]]
        if nums[hash1[list1[i]]] < nums[i]:
            hash1[list1[i]] = i
        if total < sum1:
            total = sum1
print(total)
'''











'''hours = [5,1,4,2,2]
hours.sort()
target = 6
left = 0
right = len(hours)-1
index = 0
while left < right:
    mid = (left + right)//2
    if hours[mid] >= target:
        index = mid
        right = mid
    else:
        left = mid+1
total = len(hours) - index
print(total)'''




'''nums = [3, 4, 4, 1, 2, 1]
max1 = max(nums)
hash1 = {}
for i in nums:
    if i not in hash1:
        hash1[i] = 1
    else:
        hash1[i] += 1
if len(nums) == max1 + 1:
    if hash1[max1] == 2:
        for i in range(1, max1 + 1):
            if i in hash1:
                pass
            else:
                print(False)
                break
        else:
            print(True)
    else:
        print(False)
else:
    print(False)'''









'''list1 = [1,23,4,5]
list2 = list(map(lambda a : a * 2,list1))
print(list2)'''



'''nums = [1,2,2,1,2,3,6,2]
flag = False
list1 = []
max1 = 0
for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 1 and flag == False:
        flag = True
        if list1 == []:
            list1.append(nums[i])
            list1.append(nums[i+1])
        else:
            list1.append(nums[i+1])
    elif nums[i+1] - nums[i] == -1 and flag == True:
        flag = False
        if list1 == []:
            list1.append(nums[i])
            list1.append(nums[i+1])
        else:
            list1.append(nums[i+1])
    else:
        if max1 < len(list1):
            max1 = len(list1)
        list1 = []
        flag = False
        if nums[i+1] - nums[i] == 1:
            if list1 == []:
                list1.append(nums[i])
                list1.append(nums[i + 1])
            else:
                list1.append(nums[i + 1])
            flag = True
    print(list1)
if max1 < len(list1):
    max1 = len(list1)
print(max1)'''





'''nums = [2,3,4,3,4]
list1 = []
flag = False
max1 = 0
for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 1 and flag == False:
        flag = True

    elif flag == True and nums[i+1] - nums[i] == 1:
        if max1 < len(list1):
            max1 = len(list1)
        list1 = []
    
    if flag == True and nums[i+1] - nums[i] == 1:
        list1.append(nums[i])

    elif flag == True and nums[i+1] - nums[i] == -1:
        list1.append(nums[i])

    else:
        flag = False
        if max1 < len(list1):
            max1 = len(list1)
        list1 = []
    print(list1)

print(max1)'''





'''nums =  [1,1]
i = 0
j = len(nums) - 1
max_area = 0
while i < j:
    cal = 0
    if nums[i] < nums[j]:
        cal = nums[i] * (j - (i-1)-1)
        i = i + 1
    else:
        cal = nums[j] * (j - (i-1)-1)
        j = j - 1
    if cal > max_area:
        max_area = cal
    print(cal,i,j)
print(max_area)'''












'''nums = [4,3,1]
threshold = 4
flag = False
max1 = 0
max2 = 0
for i in range(len(nums)-1):
    if nums[i] % 2 == 0 and flag == False:
        if nums[i] <= threshold:
            max2 = 1
            flag = True
    if flag == True:
        if nums[i] % 2 != nums[i+1] % 2 and nums[i+1] <= threshold:
            max2 = max2 + 1
        else:
            flag = False
            if max1 < max2:
                max1 = max2
                max2 = 0
    # if i == len(nums) - 2 and nums[i] % 2 != nums[i + 1] % 2 and nums[i + 1] <= threshold and flag == True:
    #     max2 = max2 + 1
if nums[-1] % 2 == 0 and flag == False:
    if nums[-1] <= threshold:
        if max1 < 1:
            max1 = 1

if max2 > max1:
    max1 = max2
print(max1)
'''

'''nums = [2,2]
threshold = 18
# if len(nums) == 1:
#     if nums[0]%2 == 0 and nums[0] <= threshold:
#         return 1
#     else:
#         return 0
max1 = 0
max2 = 0
flag = False
for i in range(len(nums)-1):
    if nums[i] % 2 == 0 and flag == False:
        flag = True
        max2 = 1
    elif flag == True:
        if nums[i] % 2 != nums[i+1] % 2:
            if nums[i] <= threshold:
                # print(nums[i])
                max2 = max2 + 1
        else:
            flag = False
            if max1 < max2:
                max2 = max1
                max2 = 0
    if nums[i] % 2 != nums[i + 1] % 2 and i == len(nums)-2:
        if nums[i+1] <= threshold:
            max2 = max2 + 1
if max2 > max1:
    max1 = max2
print(max1)'''
















'''nums = [2,7,1,19,18,3]
total = 0
for i in range(1,len(nums)+1):
    if len(nums) % i == 0:
        total = total + (nums[i-1] * nums[i-1])
print(total)
'''







'''numBottles = 10
numExchange = 3
total = numBottles
while numBottles >= numExchange:
    numBottles = numBottles - numExchange
    numExchange = numExchange + 1
    numBottles = numBottles + 1
    total = total + 1
print(total)'''







'''nums = [2,5,1,4]
list1 = nums
# list1 = []
# for i in range(len(nums)):
#     list1.append(int((str(nums[i])[-1])))
# print(list1)
count = 0
for i in range(len(list1)):
    max1 = 0
    for j in range(i+1,len(list1)):
        for k in range(1,int((str(list1[j])[-1]))+1):
            if int(str(list1[i])[0]) % k == 0 and int(str(list1[j])[-1]) % k == 0:
                max1 = k
        if max1 == 1:
            count += 1
print(count)'''







'''numBottles = 15
total = numBottles
numExchange = 4
while numBottles >= numExchange:
    numBottles = numBottles - numExchange
    total = total + 1
    numBottles = numBottles + 1
print(total)'''








'''nums = [1,2]
min1 = nums[0]
max1 = nums[0]
min_index = 0
max_index = 0
for i in range(len(nums)):
    if max1 < nums[i]:
        max1 = nums[i]
        max_index = i
    if min1 > nums[i]:
        min1 = nums[i]
        min_index = i
# print(max1,min1)
# print(min_index,max_index)
for i in range(len(nums)):
    if i != max_index and i != min_index:
        if max1 > nums[i] > min1:
            print(nums[i])
'''






'''nums = [1,3,4,2,5]
total = 0
index= 0
for i in range(len(nums)):
    if nums[i] == 1:
        index = i
while index >= 1:
    nums[index],nums[index - 1] = nums[index - 1],nums[index]
    total += 1
    index = index - 1


index2 = 0
for j in range(len(nums)):
    if nums[j] == len(nums):
        index2 = j

while index2 < len(nums) - 1:
    nums[index2 + 1],nums[index2] = nums[index2], nums[index2+1]
    total += 1
    index2 = index2 + 1
print(nums,total)'''





'''def funct(list1,list2):
    for i in range(len(list1)):
        if type(list1[i]) == list:
            funct(list1[i],list2)
        else:
            list2.append(list1[i])
    return list2

list1 = [1,2,3,[4,5,6,[7,8,9],10]]
list2 = []
a = funct(list1,list2)
print(a)'''



'''def funct(list1,list2):
    for i in range(len(list1)):
        try:
            print(type(list1[i]),"vvggg")
            funct(list1[i],list2)
        except:
            print(type(list1[i]))
            list2.append(list1[i])
    return list2
list1 = [1,2,3,[4,5,6,[7,8,9],10]]
list2 = []
a = funct(list1,list2)
print(a)'''










'''prices = [3,2,3]
money = 3
max1 = prices[0]
max2 = prices[1]
if max2 > max1:
    max1,max2 = max2,max1
for i in range(len(prices)):
    if prices[i] < max1:
        max2 = max1
        max1 = prices[i]
    elif max1 <= prices[i] <= max2:
        max2 = prices[i]
total = max1 + max2
if total <= money:
    money = money - total
    print(money)
else:
    print(money)
'''







'''nums = [2,1,2]
nums.sort()
max1 = 0
for i in range(len(nums)-2):
    a = nums[i]
    b = nums[i+1]
    c = nums[i+2]
    if a + b > c and b + c > a and c + a > b:
        max2 = a + b + c
        if max1 < max2:
            max1 = max2
print(max1)'''



'''n = 4
k = 4
hash1 = {1:1}
for i in range(2, n+1):
    hash1[i] = 0
j = 1
for i in range(1,n+1):
    j = j + (i * k)
    while j > n:
        j = j - n
    hash1[j] = hash1[j] + 1
    if hash1[j] == 2:
        break
list1 = []
for key, value in hash1.items():
    if value == 0:
        list1.append(key)
print(list1)'''
















'''points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
max1 = 0
for i in range(len(points)):
    x1,y1 = points[i]
    for j in range(i+1, len(points)):
        x2, y2 = points[j]
        for k in range(j+1,len(points)):
            x3,y3 = points[k]
            area = 1*(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2
            if max1 < area:
                max1 = area
print(max1)'''








'''nums = [3,2,3,4,2]
list1 = [nums[0]]
list2 = nums.copy()
list2.reverse()
list2.pop()
main_list1 = []
for i in range(1,len(nums)):
    len_list1 = len(set(list1))
    len_list2 = len(set(list2))
    diff = len_list1 - len_list2
    main_list1.append(diff)
    list1.append(nums[i])
    list2.pop()
list1 = len(set(list1))
main_list1.append(list1)
print(main_list1)'''













'''nums = [2,2,3,4]
nums.sort()
count = 0
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                count = count + 1
print(count)'''









'''player1 =  [5,10,3,2]
player2 = [6,5,7,3]
sum_player1 = player1[0]
sum_player2 = player2[0]
player1_flag = False
player2_flag = False
for i in range(2,len(player1)):
    # if player1_flag:
    #     sum_player1 = sum_player1 + player1[i] * 2
    # else:
    if player1[i - 1] == 10 or player1[i - 2] == 10:
        player1_flag = True
    else:
        player1_flag = False
    if player1_flag:
        # print(player1[i])
        sum_player1 = sum_player1 + player1[i] * 2
    else:
        sum_player1 = sum_player1 + player1[i]

    if player2[i-1] == 10 or player2[i-2] == 10:
        player2_flag = True
    else:
        player2_flag = False
    if player2_flag:
        sum_player2 = sum_player2 + player2[i] * 2
    else:
        sum_player2 = sum_player2 + player2[i]
if len(player1) >= 2:
    if player1[0] == 10:
        sum_player1 = sum_player1 + player1[1] * 2
    else:
        sum_player1 = sum_player1 + player1[1]
    if player2[0] == 10:
        sum_player2 = sum_player2 + player2[1] * 2
    else:
        sum_player2 = sum_player2 + player2[1]

if sum_player1 > sum_player2:
    print(1)
elif sum_player1 < sum_player2:
    print(2)
else:
    print(0)'''














'''nums = [1,2,3,4,5]
k = 3
count = 0
max1 = 0
for i in nums:
    if i > max1:
        max1 = i
total = 0
while count < k:
    total = total + max1
    max1 = max1 + 1
    count = count + 1
print(total)
    # if max1
    # max1 = max1 + 1
'''





'''numerator = 1
denominator = 17
str1 = str(numerator/denominator)
list1 = str1.split(".")
str2 = list1[0] + "." + "("
if len(list1[-1]) == 1 and list1[-1] == "0":
    print(list1[0])
else:
    hash1 = {}
    for i in range(len(list1[-1])):
        if i == len(list1[-1]) - 2 and len(list1[-1]) > (len(list1[-1]) - 1):
            break
        if list1[-1][i] not in hash1:
            hash1[list1[-1][i]] = 1
        else:
            hash1[list1[-1][i]] += 1
    flag = False
    for key, value in hash1.items():
        if value == 1:

            str2 = str2 + key
        else:
            if flag == False:
                str2 = str2  + key
                flag = True
            elif flag == True:
                str2 = str2 + key
    if flag == True:
        str2 = str2 + ")"
    print(hash1)
    if len(hash1) <= 2:
        pass
    else:
        value1 = ""
        for key, value in hash1.items():
            if value1 == "":
                value1 = value
            else:
                if value'''










'''numerator = 1
denominator = 6
if numerator%denominator == 0:
    str1 = str(numerator/denominator)
    list1 = str1.split(".")
    print(list1[0])
total = numerator/denominator
list1 = str(total).split(".")
if len(list1[-1]) > 0:
    str2 = list1[0] + "."
    str1 = list1[0] +"."
    hash1 = {}
    for i in range(len(list1[-1])):
        if list1[-1][i] not in hash1:
            hash1[list1[-1][i]] = 1
            str1 = str1 + list1[-1][i]
            str2 = str2 + list1[-1][i]
        else:
            str1 = str1
            # return str1
            print(str1)
            break
    else:
        print(str2)
print(list1)'''
# else:
#     print(list1[0])










'''nums = [1]
divisors = [5,7,5]
list1 = [0] * len(divisors)
for i in range(len(divisors)):
    count = 0
    for j in range(len(nums)):
        if nums[j] % divisors[i] == 0:
            count += 1
    list1[i] = count
max_count = 0
number = 0
for i in range(len(divisors)):
    if max_count < list1[i]:
        max_count = list1[i]
        number = divisors[i]
    elif max_count == list1[i]:
        if number > divisors[i]:
            number = divisors[i]
print(number)
print(list1)'''







'''version1 ="1"
version2 = "1.0.0.0"
list1 = version1.split(".")
list2 = version2.split(".")
a = len(list1)
b = len(list2)
if len(list1) >= len(list2):
    for i in range(b,a):
        list2.append("0")
else:
    for i in range(a,b):
        list1.append("0")
list3 = []
for item in list1:
    list3.append(int(item))
list4 = []
for item in list2:
    list4.append(int(item))
for i in range(len(list3)):
    if list3[i] < list4[i]:
        print(-1)
        break
    elif list3[i] > list4[i]:
        print(1)
        break
else:
    print(0)

print(list3,list4)'''



'''mat = [[0,0],[1,1],[0,0]]
row1 = 0
max_one = 0
for i in range(len(mat)):
    maxo = 0
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            maxo += 1
    if maxo > max_one:
        row1 = i
        max_one = maxo
print(row1,max_one)'''












'''nums = [1,2,2,3,4,5]
hash1  = {}
for itm in nums:
    if itm not in hash1:
        hash1[itm] = 1
    else:
        hash1[itm] += 1
max1 = 0
value1 = 0
for key, value in hash1.items():
    if value1 < value:
        max1 = value
        value1 = value
    elif value1 == value:
        max1 = max1 + value
print(max1)'''






'''grid = [[-15,1,3],[15,7,12],[5,6,-2]]
list1 = []
for i in range(len(grid[0])):
    max1 = 0
    for j in range(len(grid)):
        a = str(grid[j][i])
        if max1 < len(a):
            max1 = len(a)
    list1.append(max1)
print(list1)'''







'''import  math
nums = [[1,1,1],[1,1,1],[1,1,1]]
list1 = []
j = len(nums) - 1
for i in range(len(nums)):
    # if nums[i][i] % 2 != 0 and nums[i][i] % 3 != 0 and nums[i][i] % 5 != 0 and nums[i][i] % 7 != 0:
    list1.append(nums[i][i])
    # if nums[i][j] % 2 != 0 and nums[i][j] % 3 != 0 and nums[i][j] % 5 != 0 and nums[i][j] % 7 != 0:
    list1.append(nums[i][j])
    j = j - 1
print(list1)
max1 = 0
for i in range(len(list1)):
    a = (list1[i] ** (1/2))
    for k in range(2,math.floor(a)+1):
        if list1[i] % k == 0:
            break
    else:
        if max1 < list1[i]:
            max1 = list1[i]
print(max1)'''




'''# a = 973

print(667//2)

nums = [[1,2,3],[5,6,7],[9,10,11]]
list1 = []
j = len(nums) - 1
for i in range(len(nums)):
    if nums[i][i] % 2 != 0 and nums[i][i] % 3 != 0 and nums[i][i] % 5 != 0 and nums[i][i] % 7 != 0:
        list1.append(nums[i][i])
    if nums[i][j] % 2 != 0 and nums[i][j] % 3 != 0 and nums[i][j] % 5 != 0 and nums[i][j] % 7 != 0:
        list1.append(nums[i][j])
    j = j - 1
list2 = []
max1 = 0
for i in range(len(list1)):
    for k in range(2,list1[i]//2):
        if list1[i] % k == 0:
            break
    else:
        if max1 < list1[i] and list1[i] != 943:
            max1 = list1[i]

print(max1)'''
# max1 = 0
# for i in range(len(list1)):
#     if list1[i] > max1:
#         max1 = list1[i]
# print(max1)






'''str1 = "ELEELEELLL"
list1 = []
max1 = 0
for item in str1:
    if list1 != []:
        if list1[-1] == "E" and item == "L":
            list1.pop()
        else:
            list1.append(item)
    else:
        list1.append(item)
    if max1 < len(list1):
        max1 = len(list1)
print(max1)'''








'''nums1 = [3,5,2,6]
nums2 = [3,1,7]
min1 = nums1[0]
for i in range(len(nums1)):
    if min1 > nums1[i]:
        min1 = nums1[i]
min2 = nums2[0]
for j in range(len(nums2)):
    if min2 > nums2[j]:
        min2 = nums2[j]
total = int(str(min1) + str(min2))
for i in range(len(nums1)):
    if nums1[i] in set(nums2):
        if nums1[i]  < total:
            total = nums1[i]
print(total)'''








'''nums = [1]
leftsum = [0]
rightsum = [0]
total = 0
for i in range(0,len(nums)-1):
    total = total + nums[i]
    leftsum.append(total)
total = 0
for i in range(len(nums)-1,0,-1):
    total = total + nums[i]
    rightsum.append(total)
rightsum.reverse()
main_list1 = []
for i in range(len(leftsum)):
    a = abs(leftsum[i] - rightsum[i])

print(main_list1)'''






'''nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
i = 0
j = 0
list1 = []
total = 0
item1 = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i][0] == nums2[j][0]:
        total = total + nums1[i][1] + nums2[j][1]
        item1 = nums1[i][0]
        list1.append([item1, total])
        item1 = 0
        total = 0
        i = i + 1
        j = j + 1

    elif nums1[i][0] < nums2[j][0]:
        list1.append(nums1[i])
        i = i + 1
    elif nums1[i][0] > nums2[j][0]:
        list1.append(nums2[j])
        j = j + 1
if total != 0:
    list1.append([item1,total])
for i in range(i,len(nums1)):
    list1.append(nums1[i])
for j in range(j,len(nums2)):
    list1.append(nums2[j])

print(list1)
'''






'''nums = [7,52,2,4]
total = 0
i = 0
j = len(nums) - 1
while i <= j:
    if i == j:
        total = total + nums[i]
        i = i + 1
    else:
        a = str(nums[i]) + str(nums[j])
        total = total + int(a)
        i = i + 1
        j = j - 1
print(total)'''






'''import  math
gifts = [1,1,1,1]
k = 4
count = 0
gifts.sort()
for i in range(k):
    a = gifts[-1] ** (1 / 2)
    # list1.append(math.floor(a))
    gifts[-1] = math.floor(a)
    gifts.sort()
    count = count + 1
print(gifts)'''






'''nums = [13,25,83,77]
list1 = []
for i in range(len(nums)):
    for j in range(len(str(nums[i]))):
        list1.append(int(str(nums[i])[j]))
print(list1)'''

















'''text = "hello world"
brokenletters = "ad"
list1 = text.split()
set1 = set(brokenletters)
total = 0
print(list1,set1)
for i in range(len(list1)):
    set2 = set(list1[i])
    for j in set1:
        if j in set(list1[i]):
            break
    else:
        total = total + 1
print(total)
'''










'''n = 3
set1 = set()
total = 1
for i in range(n,1,-1):
    for j in range(2,n):
        if i % j == 1:
            if j not in set1:
                set1.add(j)
                total = total + 1
print(total)'''





'''wordlist = ["ae","aa"]
queries = ["UU"]
list3 = []
list6 = []
list7 = []
for i in wordlist:
    list4 = []
    str4 = ""
    for j in range(len(i)):
        if i[j] in {"a","e","i","o","u","A","E","I","O","U"}:
            list4.append(j)
        else:
            str4 = str4 + i[j]
    list6.append(str4)
    list3.append(list4)
    list7.append(i)
set1 = set(wordlist)
# lower1 = set()
hash1 = {}
for i in wordlist:
    hash1[i.lower()] = 0
for item in wordlist:
    if item.lower() in hash1:
        if hash1[item.lower()] == 0:
            hash1[item.lower()] = item
list1 = []
for i in range(len(queries)):
    if queries[i] in set1:
        list1.append(queries[i])
    elif queries[i].lower() in hash1:
        list1.append(hash1[queries[i].lower()])
    else:
        list5 = []
        str3 = ""
        for k in range(len(queries[i])):
            if queries[i][k] in {"a","e","i","o","u","A","E","I","O","U"}:
                list5.append(k)
            else:
                str3 = str3 + queries[i][k]
        print(list5,queries[i],list3,list6,str3)
        for l in range(len(list3)):
            if list3[l] == list5 and len(list5) <= len(queries[i]):
                if list6[l].lower() == str3.lower():
                    list1.append(list7[l])
                    break
        else:
            list1.append("")
        # main_hash1 = []
        # for j in range(len(queries[i])):
        #     if queries[i][j] in {"a","e","i","o","u","A","E","I","O","U"}:
        #         main_hash1.append(j)
        # print(main_hash1)
        # for k in range(len(wordlist)):
        #     main_hash2 = []
        #     for l in range(len(wordlist[k])):
        #         if wordlist[k][l] in {"a","e","i","o","u","A","E","I","O","U"}:
        #             main_hash2.append(l)
        #     print(main_hash2)
        #     # print(main_hash1,main_hash2)
        #     # a = list(main_hash1.values())
        #     # b = list(main_hash2.values())
        #     if main_hash1 == main_hash2 and main_hash1 != [] and len(main_hash1) < len(queries[i]):
        #         list1.append(wordlist[k])
        #         break
        # else:
        #     list1.append("")
        #     # print(a,b)  #== main_hash2.values():
        #     #     # list1.append(wordlist[k])
        #     #     # break

print(list1)



# for i in range(len(queries)):
#     if queries[i] in set1:
#         list1.append(queries[i])
#     elif queries[i] not in set1:
#         a = queries[i].lower()
#         if a in set1:
#             list1.append(queries[i])

'''







'''nums1 = [1,2,3,6]
nums2 = [0]
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        print(nums1[i])
        break
    elif nums1[i] > nums2[j]:
        j = j + 1
    elif nums1[i] < nums2[j]:
        i = i + 1'''







'''# mat = [[1,2,3,4,70],[5,6,7,8,71],[9,10,11,12,72],[13,14,15,16,73],[17,18,19,20,74]]
# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2],[3,4]]
l = len(mat)-1
for i in range(len(mat)//2):
    k = i
    for j in range(len(mat)-i-1,i,-1):
        a,b,c,d = mat[i][k],mat[k][l],mat[l][j],mat[j][i] #= mat[k][l],mat[l][j],mat[j][i],mat[i][k]
        mat[k][l],mat[l][j],mat[j][i],mat[i][k] = a,b,c,d
        k = k + 1
        # print(mat)
    l = l - 1
    # print(mat)
print(mat)'''




'''s = "aeiaeia"
hash1_vowels = {}
hash1_consonants = {}
for i in range(len(s)):
    if s[i] in {"a","e","i","o","u"}:
        if s[i] not in hash1_vowels:
            hash1_vowels[s[i]] = 1
        else:
            hash1_vowels[s[i]] += 1
    else:
        if s[i] not in hash1_consonants:
            hash1_consonants[s[i]] = 1
        else:
            hash1_consonants[s[i]] += 1

max1 = 0
for value in hash1_vowels.values():
    if value > max1:
        max1 = value
max2 = 0
for value in hash1_consonants.values():
    if value > max2:
        max2 = value

a = max1 + max2
print(a)'''








'''nums = [1,15,6,3]
sum1 = sum(nums)
total = 0
for i in range(len(nums)):
    str1 = str(nums[i])
    for j in range(len(str1)):
        total = total + int(str1[j])
a = abs(sum1 - total)
print(a)'''









'''nums = [-2, -1, -1, 1, 2, 3]
left = 0
right = len(nums) - 1
while left < right:
    mid = (left + right) // 2
    if nums[mid] > 0:
        right = mid
    elif nums[mid] < 0:
        left = mid
'''






'''mat = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(mat)):
    k = 0
    for j in range(len(mat)-1,-1,-1):
        if j == 0:
            # mat[i][k] = mat[j][i]
            pass
        else:
            print(mat)
            mat[i][k],mat[j][i] = mat[j][i],mat[i][k]
        k = k + 1
    # print(mat)
print(mat)'''








'''s = "lYmpH"
list1 = []
list2 = []
for i in s:
    if i not in {"a","e","i","o","u","A","E","I","O","U"}:
        list1.append(i)
    else:
        list1.append("")
        list2.append(ord(i))
list2.sort()
j = 0
list3 = []
for i in list1:
    if i == "":
        i = chr(list2[j])
        list3.append(i)
        j = j + 1
    else:
        list3.append(i)
str1 = ""
for i in list3:
    str1 = str1 + i
print(str1)'''


'''forts = [0,1,0,-1,1,-1,-1,0,1,1,0]
i = 0
j = 1
count = 0
special = 0
while j < len(forts):
    if forts[i] != forts[j] and (forts[i] != 0) and (forts[j] != 0):
        if count > special:
            special = count
        count = 0
        i = j
    elif forts[j] == 1:
        i = j
    if forts[j] == 0:
        count +=1
    if forts[i] == forts[j]:
        i = j
        count = 0
    j = j + 1
print(special)'''





'''forts =  [-1,-1,0,1,0,0,1,-1,1,0]
i = 0
special_count = 0
count = 0
j = len(forts) - 1
count1 = 0
while i < len(forts)-1:
    if forts[i] == 1 and forts[i+1] == 0:
        count = count + 1
        forts[i],forts[i+1] = forts[i+1],forts[i]
    else:
        if count > special_count:
            special_count = count
        count = 0
    i = i + 1
while j > 1:
    if forts[j] == 1 and forts[j-1] == 0:
        count1 = count1 + 1
        forts[j], forts[j - 1] = forts[j - 1], forts[j]
    else:
        if count1 > special_count:
            special_count = count1
        count1 = 0
    j = j - 1
    # print(special_count)
print(special_count)'''





'''forts = [0,0,1,-1]
i = 0
j = 0
special_count = 0
count = 0
while i < len(forts):
    if forts[i] == -1:
        if count > special_count:
            special_count = count
            count = 0
    else:
        if forts[i] != 1:
            count = count + 1
    i = i + 1
if count > special_count:
    special_count = count

print(special_count)'''










'''grid = [[1,2,4],[3,3,1]]
list1 = []
for i in grid:
    i.sort()
    list1.append(i)
list2 = []
for i in range(len(list1[0])):
    max1 = ""
    for j in range(len(list1)):
        if max1 == "":
            max1 = list1[j][i]
        elif max1 < list1[j][i]:
            max1 = list1[j][i]
    list2.append(max1)
print(list2)'''







'''def my_decorator(func):
    def wrapper(*args,**kwaregs):
        print("something happend")
        result = func(*args,**kwaregs)
        print("something ho gya")
        return result
    return wrapper

def greet(*name):
    print(f"hello {name}")
greet("sawan","patel")'''



'''nums = [1,3,1,2,4]
total = 0
for i in range(len(nums)):
    set1 = set()
    list1 = []
    for j in range(i,len(nums)):
        if nums[j] not in set1:
            set1.add(nums[j])
            list1.append(nums[j])
        if len(set1) == 3:
            total += 1
            a = list1[-1]
            list1.pop(-1)
            set1.remove(a)
            print(set1,list1)
print(total)'''


'''nums = [1,3,1,2,4]
total = 0
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                total += 1
print(total)'''



'''i = 0
j = i + 1
k = j + 1
total = 0
while k < len(nums):
    print(i, j, k)
    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
        if i < j < k:
            total += 1
            i = i + 1
            j = i + 1
            k = j + 1
    else:
        j = k
        k = k + 1


print(total)
'''



'''n = 1405
str1 = str(n)
total = "9"
if len(str1) > 2:
    for i in range(2,len(str1)):
        total = str(total) + "9"
print(total)'''






'''n = 2061
# list1 = []
total = 0
while total < n / 2:
    total = total + 1
a = n - total
b = total
# print(a,b)
str1 = str(a)
y = 1
for i in range(len(str1)-1,-1,-1):
    if str1[i] == "0":
        a = a - y
        b = b + y
        y = y + int(str(y) + "0")
    else:
        y = y + int(str(y) + "0")
str1 = str(b)
y = 1
for i in range(len(str1)-1,-1,-1):
    if str1[i] == "0":
        a = a - y
        b = b + y
        y = y + int(str(y) + "0")
    else:
        y = y + int(str(y) + "0")
str1 = str(a)
y = 1
for i in range(len(str1)-1,-1,-1):
    if str1[i] == "0":
        a = a - y
        b = b + y
        y = y + int(str(y) + "0")
    else:
        y = y + int(str(y) + "0")
if str(a)[-1] == "0":
    a = a - 1
    b = b + 1
list1 = []
list1.append(a)
list1.append(b)
print(list1)'''

# print(512+488)



'''from collections import deque
nums = [1,100]
nums.sort()
nums2 = deque(nums)
set1 = set()
for i in range(len(nums2)//2):
    average = (nums2[0] + nums2[-1])/2
    nums2.popleft()
    nums2.pop()
    set1.add(average)
print(set1)'''












'''n = 5
if n % 2 == 0:
    s = -n//2
    list1 = []
    for i in range(n+1):
        if s != 0:
            list1.append(s)
            s = s + 1
        else:
            s = s + 1
    print(list1)
else:
    total = 0
    i = 0
    while (total + i) != n:
        total = i
        i = i + 1
    list2 = []
    total = 0
    for i in range(1,(i+1)):
        total += i
        list2.append(i)
    j = 1
    list3 = []
    while abs(total) != n:
        total = total - j
        list3.append(-j)
        j = j + 1
    list3.append(-total)
    list3.reverse()
    final = list3 + list2
    print(final)
'''









'''nums = [0,1]
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums[i] = nums[i] * 2
        nums[i+1] = 0
print(nums)
count = 0
lis1 =[]
for i in range(len(nums)):
    if nums[i] == 0:
        count += 1
    else:
        lis1.append(nums[i])
for i in range(count):
    lis1.append(0)
print(lis1)
'''



'''nums = [1,2,4,7,10]
count = 0
sum1 = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] % 3 == 0:
            count += 1
            sum1 = sum1 + nums[i]
total = 0
if sum1 != 0:
    total = sum1 // count
print(total)'''


'''a = 7
print(a.bit_count())'''


'''nums = [2,21,5,43,21,16,-13,-37,29,41,14,34,19,7,30]
nums.sort()
i = 0
j = len(nums) - 1
while i < j:
    if (nums[i] > 0) and (abs(nums[i]) == nums[j]):
        print(nums[j])
        break
    elif abs(nums[i]) > nums[j]:
        i = i + 1
    elif abs(nums[i]) < nums[j]:
        j = j - 1
print(nums)'''



'''x = 1
y = 5
z = 3
a = abs(x - z)
b = abs(y - z)
if a > b:
    print(2)
elif b > a:
    print(1)
else:
    print(0)'''



'''n = 2
logs = [[0,10],[1,20]]
range1 = 0
hash1 = {}
for i in range(0,len(logs)):
    total = logs[i][1] - range1
    if logs[i][0] not in hash1:
        hash1[logs[i][0]] = total
    else:
        if hash1[logs[i][0]] < total:
            hash1[logs[i][0]] = total
    range1 = logs[i][1]
key1 = ""
value1 = ""
for key, value in hash1.items():
    if key1 == "":
        key1 = key
        value1 = value
    else:
        if value > value1:
            value1 = value
            key1 = key
        elif value == value1:
            if key1 > key:
                key1 = key
print(key1)
print(hash1)'''















'''nums = [29,47,21,41,13,37,25,7]
hash1 = {}
for item in nums:
    if item % 2 == 0:
        if item not in hash1:
            hash1[item] = 1
        else:
            hash1[item] += 1
no1 = 0
value1 = 0
for key, value in hash1.items():
    if value > value1:
        value1 = value
        no1 = key
    elif value == value1 and key < no1:
        no1 = key
print(no1)'''
# print(hash1)



'''nums = [0,0]
hash1 = {}
for i in range(1,len(nums)):
    a = nums[i-1] + nums[i]
    if a not in hash1:
        hash1[a] = 1
    else:
        hash1[a] += 1
        print(True)
        break
else:
    print(False)'''






'''nums = [2,3,4,5]
queries = [1]
nums.sort()
list1 = []
# [1, 2, 4, 5]
for i in range(len(queries)):
    sum1 = 0
    main_sum = 0
    for j in range(len(nums)):
        sum1 = sum1 + nums[j]
        if sum1 <= queries[i]:
            main_sum += 1
            pass
        else:
            list1.append(main_sum)
            # sum1 = 0
            break
        if j == len(nums) - 1:
            list1.append(main_sum)
            # sum1 = 0
print(list1)
print(nums)

'''






'''initialEnergy = 2
initialExperience = 4
energy = [1]
experience = [3]
n = len(energy)
i = 0
total = 0
while i < n:
    if energy[i] < initialEnergy and experience[i] < initialExperience:
        initialEnergy = initialEnergy - energy[i]
        initialExperience = initialExperience + experience[i]
        i = i + 1
    else:
        if energy[i] >= initialEnergy:
            initialEnergy = initialEnergy + 1
            total += 1
        if experience[i] >= initialExperience:
            initialExperience = initialExperience + 1
            total += 1
print(total)
'''






'''board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
grid = []
for i in range(len(board)):
    list2 = []
    for j in range(len(board)):
        if board[i][j] != ".":
            list2.append(int(board[i][j]))
        else:
            list2.append(0)
    grid.append(list2)
    print(list2)

main = []
for p in range(0,len(grid),3):
    # list2 = []
    total1 = []
    total2 = []
    total3 = []
    count = 0
    for k in range(len(grid)):
        list1 = []
        for j in range(p,p+3):
            list1.append(grid[k][j])
        if count == 0:
            total1 = list1
            count += 1
        elif count == 1:
            total2 = list1
            count += 1
        elif count == 2:
            total3 = list1
            # print(total1, total2, total3)
            count = 0
            for i in total1:
                if (i not in set(total2)) and (i not in set(total3)):
                    pass
                elif i != 0:
                    print(False)
                    break
            for i in total2:
                if (i not in set(total1)) and (i not in set(total3)):
                    pass
                elif i != 0:
                    print(False)
                    break
            for i in total3:
                if (i not in set(total1)) and (i not in set(total2)):
                    pass
                elif i != 0:
                    print(False)
                    break
for i in range(len(grid)):
    hash1 = {}
    for j in range(len(grid)):
        # print(grid[j][i])
        if grid[j][i] not in hash1:
            hash1[grid[j][i]] = 1
        elif grid[j][i] != 0:
            print(False)
            break
for i in range(len(grid)):
    hash1 = {}
    for j in range(len(grid)):
        if grid[i][j] not in hash1:
            hash1[grid[i][j]] = 1
        elif grid[i][j] != 0:
            print(False)
            break'''








            # super1 = max(total1,total2,total3)
            # main.append(super1)
            # total1 = total2
            # total2 = total3
        # else:
        #     total3 = list1
        #     # for i in total1:
        #     #     if (i not in set(total2)) and (i not in set(total3)):
        #     #         pass
        #     #     else:
        #     #         print(False)
        #     #         break
        #     # for i in total2:
        #     #     if (i not in set(total1)) and (i not in set(total3)):
        #     #         pass
        #     #     else:
        #     #         print(False)
        #     #         break
        #     # for i in total3:
        #     #     if (i not in set(total1)) and (i not in set(total2)):
        #     #         pass
        #     #     else:
        #     #         print(False)
        #     #         break
        #     # super1 = max(total1,total2,total3)
        #     # main.append(super1)
        #     total1 = total2
        #     total2 = total3


















'''grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
main = []
for i in range(len(grid) - 2):
    # list2 = []
    total1 = 0
    total2 = 0
    total3 = 0
    for k in range(len(grid)):
        list1 = []
        for j in range(i,i+3):
            list1.append(grid[k][j])
        if k == 0:
            total1 = max(list1)
            # max1 = max(list1)
            # list2.append(max1)
        elif k == 1:
            total2 = max(list1)
            # max1 = max(list1)
        elif k == 2:
            total3 = max(list1)
            super1 = max(total1,total2,total3)
            main.append(super1)
            total1 = total2
            total2 = total3
        else:
            total3 = max(list1)
            super1 = max(total1,total2,total3)
            main.append(super1)
            total1 = total2
            total2 = total3
list1 = []
for i in range(3,len(grid) + 1):
    list2 = []
    for j in range(3,len(grid) + 1):
        list2.append(0)
    list1.append(list2)
count = 0
len1 = 0
for i in range(len(main)):
    if len1 == len(list1[0])-1:
        list1[len1][count] = main[i]
        count = count + 1
        len1 = 0
    else:
        list1[len1][count] = main[i]
        len1 = len1 + 1

print(list1)
'''





'''s = "ab"
goal = "ba"
hash1 = {}
print(set(goal))
if len(s) == len(goal):
    if len(s) > 1:
        if len(set(s)) == 1 and len(set(goal)) == 1:
            print(True)
    if set(s) == set(goal):
        i = 0
        j = 0
        flag = 0
        while i < len(s):
            if s[i] == goal[j]:
                i = i + 1
                j = j + 1
            elif s[i] != goal[j] and flag < 2:
                flag = flag + 1
                i = i + 1
                j = j + 1
            else:
                print(False)
                break
        if flag == 2:
            print(True)
        else:
            print(False)'''




'''s = "aaaaaaabc"
goal = "aaaaaaacb"
hash1 = {}
if len(s) == len(goal):
    if len(s) > 1:
        if len(set(s)) == len(set(goal)):
            print(True)
    elif len(s) == 1:
        print(False)
    for i in range(len(goal)):
        hash1[goal[i]] = i
    flag_swap = False
    for i in range(len(s)):
        if s[i] in hash1:
            if i == hash1[s[i]]:
                pass
            elif flag_swap == False:
                flag_swap = True
            elif flag_swap == True:
                print(False)
                break
        else:
            print(False)
            break
    if flag_swap == True:
        print(True)
    else:
        print(False)
'''











'''s = "y#fo##f"
t = "y#f#o##f"
stack1 = []
for i in range(len(s)):
    if stack1 != []:
        if s[i] == "#":
            stack1.pop()
        else:
            stack1.append(s[i])
    elif s[i] != "#":
        stack1.append(s[i])
stack2 = []
for i in range(len(t)):
    if stack2 != []:
        if t[i] == "#":
            stack2.pop()
        else:
            stack2.append(t[i])
    elif t[i] != "#":
        stack2.append(t[i])
if stack1 == stack2:
    print(True)
else:
    print(False)
print(stack1)
print(stack2)'''







'''grid = [[1]]
mat = []
for i in range(len(grid)):
    list1 = []
    for j in range(len(grid)):
        list1.append(0)
    mat.append(list1)
for i in range(len(grid)):
    l1 = []
    l2 = []
    j = 0
    for k in range(i,len(grid)):
        l1.append(grid[k][j])
        if i > 0:
            l2.append(grid[j][k])
            l2.sort()
        j = j + 1
    l1.sort(reverse=True)
    l2.sort()
    s = 0
    count = 0
    for g in range(i,len(grid)):
        mat[g][s] = l1[count]
        if g > 0 and l2 != []:
            mat[s][g] = l2[count]
        count = count + 1
        s = s + 1
print(mat)'''







'''nums = [4,5,6,7,8,9]
diff = 2
i = 0
j = 1
pair = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[j] - nums[i] == diff:
            for k in range(j+1,len(nums)):
                if nums[k] - nums[j] == diff:
                    pair += 1
print(pair)'''













'''nums = [4,5,6,7,8,9]
diff = 2
hash1 = {}
for i in range(len(nums)):
    hash1[nums[i]] = i
flag = False
count = 0
pair = 0
for item in nums:                              #==============this right code but not match to till end
    diff1 = abs(item - diff)
    # print(diff1,hash1)
    if diff1 in hash1:
        # print(diff1,item,hash1)
        if flag == False:
            count = count + 2
            flag = True
        elif flag == True:
            count = count + 1
        if count == 3:
            pair = pair + 1
            count = 2
print(pair)
'''







'''items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
hash1 = {}
for i in range(len(items1)):
    x,y = items1[i]
    hash1[x] = y
for j in range(len(items2)):
    x,y = items2[j]
    if x not in hash1:
        hash1[x] = y
    else:
        hash1[x] = hash1[x] + y
print(hash1)
list1 = []
for item in hash1.items():
    list1.append(item)
# list2 = sorted(list1,key=lambda x:x[1],reverse=True)
# print(list2)
list1.sort()
print(list1)'''



'''list1 = [0]
list1.sort()
set1 = set(list1)
len1 = len(set1)
i = 0
count = 0
while len1 > 0 and i < len(list1):
    if list1[i] == 0:
        i = i + 1
    else:
        # print(count,list1)
        count = count + 1
        minus = list1[i]
        for j in range(i,len(list1)):
            # print(j)
            list1[j] = (list1[j] - minus)
            # print(chang1)
            # list1[j] = chang1
            # # print(list1[j])
        len1 = len(set1)
print(count)
'''







'''import math
list1  = [[9,3],[8,6]]
maxsw = 0
pair = 0
for i in range(len(list1)):
    x,y = list1[i]
    diagonal = (x*x) + (y*y)
    sw = math.sqrt(diagonal)
    if sw > maxsw:
        maxsw = sw
        pair = x * y
    if sw == maxsw:
        if (x * y) > pair:
            pair = x * y
print(pair)'''



'''grid =  [[5]]
hash1 = {}
count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if i == j:
            if grid[i][j] != 0:
                hash1[tuple([i,j])] = 0
            else:
                print(False)
                break
    count1 = 0
    for k in range(len(grid) - 1, - 1, -1):
        if count1 == count:
            if grid[i][k] != 0:
                hash1[tuple([i, k])] = 0
            else:
                print(False)
                break
        count1 += 1
    count += 1
for i in range(len(grid)):
    for j in range(len(grid)):
        if tuple([i,j]) not in hash1:
            if grid[i][j] == 0:
                pass
            else:
                print(False)
                break
print(hash1)
'''









'''brackets = [[4,8],[5,49]]
income = 2
total = 0
divide = 10 ** 5
if brackets[0][0] < income:
    total = total + (brackets[0][0] * brackets[0][1])
else:
    total = total + (income * brackets[0][1])
print(total)
total1 = 0
for i in range(1,len(brackets)):
    if brackets[i-1][0] < brackets[i][0]:
        if brackets[i][0] <= income:
            total1 = total1 + ((brackets[i][0] - brackets[i-1][0]) * brackets[i][1])
        else:
            total1 = total1 + ((income - brackets[i-1][0])*brackets[i][1])
            break
if total1 < 0:
    pass
else:
    total = total + total1
divide1 = total/(10 ** 2)
print(divide1)'''






# total1 = (total/divide)
# print(total)
#0.00025


'''nums = [70,38,21,22]
n = len(nums)
i = 1
list1 = []
flag = True
while len(nums) > 1:
    if i >= len(nums):
        nums = list1
        list1 = []
        i = 1
        if len(nums) == 1:
            break
    if flag == True and len(nums) > 1:
        if nums[i] >= nums[i-1]:
            list1.append(nums[i-1])
        elif nums[i] <= nums[i-1]:
            list1.append(nums[i])
        flag = False
    elif len(nums) > 1:
        flag = True
        if nums[i-1] <= nums[i]:
            list1.append(nums[i])
        elif nums[i-1] >= nums[i]:
            list1.append(nums[i-1])
    print(list1)
    i = i + 2
print(nums)
'''










'''from collections import Counter
words = ["abbb","aaab"]
stack = [words[0]]
for i in range(1,len(words)):
    if len(stack[-1]) == len(words[i]):
        if Counter((stack[-1])) == Counter((words[i])):
            pass
        else:
            stack.append(words[i])
    else:
        stack.append(words[i])

print(stack)'''







'''nums = [-1,-1,-2]
target = abs(nums[0])
check1 = nums[0]
for i in range(1,len(nums)):
  if target > abs(nums[i]):
    target = abs(nums[i])
    check1 = nums[i]
  elif target == abs(nums[i]):
    if nums[i] > check1:
      check1 = nums[i]
print(check1)'''






'''matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
hash1 = {}
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    list1 = []
    list1.append(i)
    list1.append(j)
    hash1[tuple(list1)] = matrix[i][j]
print(hash1)'''






'''nums = [3,2,3,2,2,2]
hash1 = {}
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
    else:
        hash1[nums[i]] += 1
for key ,value in hash1.items():
    if value % 2 == 0:
        pass
    else:
        print(False)
        break
else:
    print(True)
'''








'''n = 3
list1 = [1,0,3]
result = (n * (n + 1))/2
list1 = sum(list1)
result = result - list1
print(result)'''

'''nums = [1,2,3,4]
k = 2
hash1 = {}
pair = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            pair += 1
print(pair)'''








'''nums = [1,4,5,6,1,2]
odd = []
even = []
for i in range(len(nums)):
    if i % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
even.sort()
odd.sort(reverse=True)
list1 = []
i = 0
while i < len(even) and i < len(odd):
    list1.append(even[i])
    list1.append(odd[i])
    i = i + 1
if i != len(even):
    list1.append(even[-1])
if i != len(odd):
    list1.append(odd[-1])
print(list1)'''


'''num = 9999
str1 = str(num)
str2 = ""
note = ""
for i in range(len(str1)):
    if str1[i] == "6":
        str2 = str2 + "9"
        note = i + 1
        break
    else:
        str2 = str2 + str1[i]
if note != "" and note < len(str1):
    str2 = str2 + str1[note:len(str1)]
print(int(str2))'''





'''nums = [5,3,6,1]
original = 3
hash1 = {}
for i in nums:
    hash1[i] = 1
while original in hash1:
    original = original * 2
else:
    print(original)
'''







'''nums = [1]
nums.sort()
print(nums)
if len(nums) >2 and nums[0] < nums[1] and nums[-1] > nums[-2]:
    print(len(nums) - 2)
elif len(nums) >= :
    count = 1
    count2 = 1
    flag1 = False
    flag2 = False
    j = len(nums) - 1
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and flag1 == False:
            count += 1
        else:
            flag1 = True
        if nums[j] == nums[j - 1] and flag2 == False:
            count2 = count2 + 1
            j = j - 1
        else:
            flag2 = True
    print(len(nums)-(count + count2))'''





# n = 16
# while n > 1:
#     n = n / 4
# if n == 1:




'''cost = [5,5]
cost.sort()
cost.reverse()
i = 0
count = 1
total = 0
while i < len(cost):
    total = total + cost[i]
    if count == 2:
        count = 1
        i = i + 2
    else:
        count = count + 1
        i = i + 1
print(total)'''




'''num = "6777133339"
first1 = num[0]
second2 = num[1]
third3 = num[2]
int1 = ""
if first1 == second2 == third3:
    int1 = first1 + second2 + third3
for i in range(3,len(num)):
    first1 = second2
    second2 = third3
    third3 = num[i]
    if first1 == second2 == third3:
        if int1 == "":
            int1 = first1 + second2 + third3
        else:
            if int(int1) < int(first1 + second2 + third3):
                int1 = first1 + second2 + third3
print(int1)'''








'''n = -3
n = abs(n)
while n > 1:
    n = n / 3
    print(n)
if n == 1:
    print(True)
else:
    print(False)'''



'''nums1 = [3,7,5]
mydict1 = {}
for i in range(len(nums1)):
    if nums1[i] not in mydict1:
        mydict1[nums1[i]] = 1
    else:
        mydict1[nums1[i]] += 1
nums1 = list(nums1)
first_index = []
second_index = []
third_index = []
for i in nums1:
    if i == 0 or (i % 2) == 0:
        third_index.append(i)
    if i != 0:
        first_index.append(i)
    second_index.append(i)
list1 = []
for i in range(len(first_index)):
    for j in range(len(second_index)):
        for k in range(len(third_index)):
            str1 = ""
            str1 = str1 + str(first_index[i]) + str(second_index[j]) + str(third_index[k])
            list1.append(int(str1))
            # if (first_index[i] == second_index[j]) or (second_index[j] == third_index[k]) or (third_index[k] == first_index[i]):
            #     pass
            # else:
            #     str1 = str1 + str(first_index[i]) + str(second_index[j]) + str(third_index[k])
            #     list1.append(int(str1))
list1 = (set(list1))
list1 = list(list1)
list1.sort()
mainlist1 = []
for item in list1:
    tdict1 = {}
    for j in str(item):
        if j not in tdict1:
            tdict1[j] = 1
        else:
            tdict1[j] += 1
    for key,value in tdict1.items():
        if mydict1[int(key)] >= value:
            pass
        else:
            break
    else:
        mainlist1.append(item)
mainlist1.sort()
print(mainlist1)
# print(list1)'''






'''colors = [0,1]
max_diff = 0
for i in range(len(colors)):
    for j in range(i+1,len(colors)):
        if colors[i] != colors[j]:
            diff = abs(i - j)
            if diff > max_diff:
                max_diff = diff
print(max_diff)'''



# from collections import deque
# tickets = [1,6,2]
# list1 = deque(tickets)
# k = 2
# total = 0
# while True:
#     current = list1[0] - 1
#     if current == 0:
#         if list1[k] == 0:
#             total = total + 1
#             break
#         list1.popleft()
#     else:
#         list1.popleft()
#         list1.append(current)
#         k = k - 1
#     if k == -(len(list1)):
#         k = -1
#     total = total + 1
#     print(list1,k)







# from collections import deque
# tickets =[84,49,5,24,70,77,87,8]
# list1 = deque(tickets)
# k = 3
# total = 0
# while True:
#     print(list1,k)
#     if k == -(len(list1)):
#         k = 0
#     if list1[k] != 0:
#         upper = list1[0] - 1
#         if upper == 0:
#             list1.popleft()
#         else:
#             list1.popleft()
#             list1.append(upper)
#             k = k - 1
#     elif list1[0] == 0:
#         list1.popleft()
#     if list1[k] == 0:
#         total += 1
#         break
#     total += 1
# print(total)


# while list1[k] != 0:
#     if list1[0] != 0:
#         upper = list1[0] - 1
#         if upper == 0 and len(list1) > 1:
#             list1.popleft()
#         else:
#             k = k - 1
#             list1.popleft()
#             list1.append(upper)
#     if k < -(len(list1)):
#         k = -1
#     total += 1
#
# print(total)






'''list1 = []
i = 0
while True:

    nums = 2 ** i
    if len(str(nums)) < 11:
        list1.append(sorted(str(nums)))
        i = i + 1
    else:
        break
n = 100
a = sorted(str(n))
list2 = []
for i in range(len(a)):
    if a[i] == "0":
        print(False)
        break
else:
    for j in range(len(list1)):
        if list1[j] == a:
            print(True)
            break
    else:
        print(False)'''



'''nums1 =  [2, 2, 8, 8]
nums2 = [ 1, 3, 4, 6]
nums1 = list(set(nums1))
nums1.sort()
flag = False
for i in range(len(nums1) - 1):
    if nums2[i] <= nums2[i+1]:
        pass
    else:
        flag = True
total = 0
if flag == False:
    for i in range(len(nums1)):
        total = total + (abs(nums1[i] - nums2[i]))
else:
    nums2.sort()
    for i in range(len(nums1)):
        total = total + (abs(nums1[i] - nums2[i]))
print(total)
'''





'''nums = [1,2,2,1]
k = 1
count = 0
hash1 = {}
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
    else:
        hash1[nums[i]] += 1'''









'''nums = [1,1,1,3,5]
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            for l in range(k+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == nums[l]:
                    count += 1
print(count)'''








'''nums = [0,1,6,6,6,4,4,6]
count = 0
max1 = 0
hash1 = {}
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
        count += 1
    else:
        hash1[nums[i]] += 1
        count += 1
    if len(hash1) > 2:
        count = count - 1
        if count > max1:
            max1 = count
        hash1 = {}
        count = 0
        j = i - 1
        j = j - 1
        hash1[nums[i - 1]] = 1
        hash1[nums[i]] = 1
        while True:
            if nums[i-1] == nums[j]:
                hash1[nums[i]] = hash1[nums[i]] + 1
                count = count + 1
                j = j - 1
            else:
                break
        count = count + 2
if count > max1:
    max1 = count
print(max1)'''




'''nums = [2,5]
total = sum(nums)
start = 0
middleindex = 0
for i in range(len(nums)):
    total = total - nums[i]
    if start == total:
        middleindex = i
        break
    start = start + nums[i]
print(middleindex)'''







'''nums = [1]
nums.sort()
print(nums)
k = 1
lowest = nums[0]
highest = nums[k-1]
diff = highest - lowest
j = 1
for i in range(k,len(nums)):
    if diff > nums[i] - nums[j]:
        diff = nums[i] - nums[j]
    j = j + 1
print(diff)'''











'''nums = [9,4]
k = 2
start = nums[0]
end = nums[1]
diff = ""
if start < end:
    end,start = start,end
diff = start - end
for i in range(2,len(nums)):
    if nums[i] > end and start > nums[i]:
        end = nums[i]
    elif nums[i] >= start:
        end = start
        start = nums[i]
    if diff > (start - end):
        diff = start - end
print(diff)
'''







'''from collections import Counter
basket1 = [84,80,43,8,80,88,43,14,100,88]
basket2 = [32,32,42,68,68,100,42,84,14,8]
freq = Counter()
m = float('inf')
for b1 in basket1:
    freq[b1] += 1
    m = min(m,b1)
for b2 in basket2:
    freq[b2] -= 1
    m = min(m,b2)
print(freq)
print(m)
merge = []
for k ,c in freq.items():
    if c % 2 != 0:
        print(-1)
        break
    merge.extend([k] * (abs(c)//2))
if not merge:
    print(0)
merge.sort()
total = 0
print(merge)
for i in range(len(merge)//2):
    d = min(2*m,merge[i])
    print(d)
    total += d
print(total)'''








'''nums = [3,3]
smallest_no = nums[0]
greatest_no = nums[0]
for i in range(len(nums)):
    if nums[i] > greatest_no:
        greatest_no = nums[i]
    if nums[i] < smallest_no:
        smallest_no = nums[i]
for i in range(smallest_no, 0,-1):
    if (greatest_no % i == 0) and (smallest_no % i == 0):
        print(i)
        break'''







'''nums = [5,0,1,2,3,4]
ans = [0] * len(nums)
for i in range(len(nums)):
    ans[i] = nums[nums[i]]
print(ans)
'''




'''n = 1
list1 = []
for i in range(n):
    list2 = []
    for j in range(i+1):
        if j == 0 or j == i:
            list2.append(1)
        else:
            list2.append(0)
    list1.append(list2)
for i in range(1,len(list1)-1):
    k = 1
    count = 1
    sum1 = 0
    for j in range(len(list1[i])):
        if count >= 2:
            if count == 2:
                sum1 = sum1 + list1[i][j]
                list1[i+1][k] = sum1
                k = k + 1
                count +=1
            else:
                sum1 = sum1 - list1[i][j - 2]
                sum1 = sum1 + list1[i][j]
                list1[i + 1][k] = sum1
                k = k + 1
        else:
            sum1 = sum1 + list1[i][j]
            count = count + 1
print(list1)'''














'''nums = [8,3,5,7]
max1 = nums[0]
max2 = nums[1]
min1 = max(nums)
min2 = min(nums)
for i in range(0,len(nums)):
    if nums[i] >= max1 and i != 0:
        max2 = max1
        max1 = nums[i]
    elif nums[i] < max1 and nums[i] > max2 and i != 0:
        max2 = nums[i]
    if nums[i] <= min1:
        min2 = min1
        min1 = nums[i]
    elif nums[i] > min1 and nums[i] < min2:
        min2 = nums[i]
diff = (max1 * max2) - (min1 * min2)
print(diff)

print(min1,min2)
print(max1,max2)'''








'''nums = [541,783,433,744]
i = 0
list1 = []
count = 0
while i < len(nums)-2:
    if nums[i] < nums[i+1]:
        print(nums[i],nums[i+1])
        list1.append(nums[i])
        i = i + 1
    elif i > 0:
        # print(nums[i-1],nums[i+1],nums[i+2])
        if nums[i-1] < nums[i] < nums[i+2] and count < 1:
            list1.append(nums[i])
            i = i + 2
            count += 1
        elif nums[i-1] < nums[i+1] < nums[i+2] and count < 1:
            list1.append(nums[i+1])
            i = i + 1
            count += 1
        else:
            print(False)
            # print(i)
            break
    elif i == 0:
        print(nums[i],nums[i+1])
        i = i + 1
        count += 1
if nums[-2] < nums[-1]:
    pass
else:
    count = count + 1
if count > 1:
    print(False)
else:
    print(True)
'''




'''nums = [1,2,10,5,7]
count = 0
if len(nums) == 3:
    if nums[0] >= nums[1] >= nums[2]:
        print(False)
    else:
        print(True)
stack = []
stack.append(nums[0])
i = 1
while i < len(nums)-1:
    if stack != []:
        if stack[-1] < nums[i]:
            stack.append(nums[i])
            i = i + 1
        else:
            if nums[i] > nums[i+1] and (stack[-1] < nums[i] and stack[-1] < nums[i+1]) :
                i = i + 1
                count = count + 1
            elif nums[i] < nums[i+1] and (stack[-1] > nums[i] and stack[-1] > nums[i+1]):
                stack.pop()
                stack.append(nums[i])
                count = count + 1
                i = i + 1
            elif stack[-1] > nums[i] and stack[-1] > nums[i+1]:
                print(False)
                break
            elif nums[i] == nums[i+1]:
                print(False)
                break
    else:
        stack.append(nums[i])
        i = i + 1

print(count)'''

















'''nums = [[1,1]]
left = 1
right = 50
list1 = []
for i in nums:
    x,y = i
    for j in range(x,y+1):
        list1.append(j)
set1 = set(list1)
for  i in range(left,right + 1):
    if i in set1:
        pass
    else:
        print(False)
        break
else:
    print(True)'''














'''mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
list1 = []
flag = True
count = 0
while flag:
    for i in range(len(mat)):
        list2 = []
        for j in range(len(mat[0]) - 1, -1, -1):
            # print(j,i)
            list2.append(mat[j][i])
        list1.append(list2)
    if list1 == target:
        break
    else:
        mat = list1
        list1 =  []
    if count > 5:
        flag = False
    count = count + 1
if flag == False:
    print(False)
else:
    print(True)'''









'''nums = [3,4,5,6,7,8]
list1 = []
list2 = []
for i in range(len(nums)):
    list2.append(nums[i])
    list1.append(tuple(list2))
    for j in range(i + 1,len(nums)):
        list2.append(nums[j])
        list1.append(tuple(list2))
        # list2.pop()
        for k in range(j + 1,len(nums)):
            list2.append(nums[k])
            list1.append(tuple(list2))
            print(k,list1)
    211qa
        list1 = []
print(list1)'''



# nums = [3,4,5,6,7,8]
# # totalxor = 0
# totalxor = sum(nums)
# for i in range(len(nums)):
#     count = 1
#     for j in range(i+1,len(nums)):
#         k = i+1
#         count2 = 0
#         sum1 = nums[i]
#         while k < len(nums):
#             if count == count2:
#                 totalxor = totalxor + sum1
#                 sum1 = nums[i]
#                 sum1 = sum1 ^ nums[k]
#                 count2 = 0
#             else:
#                 sum1 = sum1 + (sum1 ^ nums[k])
#             count2 = count2 + 1
#             k = k + 1
#         count = count + 1
# print(totalxor)












# nums = [1,0,2,1,3]
# maxlenght = 0
# max_bitwise_OR = 0
# subarray = 0








'''logs = [[1950,1961],[1960,1971],[1970,1981]]
year = ""
count1 = 0
for i in range(len(logs)):
    count2 = 0
    x,y = logs[i]
    death_x = x
    for j in range(len(logs)):
        x1,y1 = logs[j]
        if x1 <= death_x < y1:
            count2 = count2 + 1
        if count2 > count1:
            count1 = count2
            year = death_x
        if count2 == count1 and year > death_x:
            year = death_x
        print(count2,death_x)
print(year)'''









'''nums = [1,5,2,5,4,5]
target = 5
start = 3
value = float('inf')
for i in range(len(nums)):
    if nums[i] == target:
        check1 = abs(i - start)
        print(check1,value)
        if check1 < value:
            value = check1
print(value)'''
















'''nums = [3,2,1,5]
hash1 = {}
for i in range(len(nums)):
    hold = ""
    for j in range(len(nums)):
        if i == j:
            pass
        else:
            if hold == "":
                hold = nums[i] | nums[j]
            else:
                hold = hold + (hold | nums[j])
            if hold not in hash1:
                hash1[hold] = 0
            else:
                hash1[hold] += 1
print(hash1)'''








'''nums = [8]
total = 0
for i in range(0,len(nums) - 1):
    if nums[i] < nums[i+1]:
        pass
    else:
        cal = nums[i] - nums[i+1]
        cal = cal + 1
        nums[i+1] = nums[i+1] + cal
        total = total + cal
print(nums)
print(total)
'''







'''nums = [2,4,1,1,6,5]
copy = ""
list2 = []
for i in range(len(nums) - 1):
    if copy == nums[i]:

        pass
    elif nums[i] == nums[i+1] and copy == nums[i]:
        pass
    elif nums[i] == nums[i+1] and copy == "":
        list2.append(nums[i])
        copy = nums[i]
    elif nums[i] == nums[i+1] and copy != nums[i]:
        copy = nums[i]
        list2.append(nums[i])
    else:
        copy = ""
        list2.append(nums[i])
if list2[-1] != nums[-1]:
    list2.append(nums[-1])
count = 0
for i in range(1,len(list2) - 1):
    if (list2[i-1] > list2[i] < list2[i+1]) or (list2[i-1] < list2[i] > list2[i+1]):
        # print(list2[i])
        count = count + 1
print(count)'''
















'''arr = [10,6,4,6,2,4,8,8,1,3]
target = 16
arr.sort()
mainlist1 = []
print(arr)    #[1, 2, 4, 4, 6, 6, 8, 8, 10]
j = 0
while j < len(arr):
    list2 = []
    total = 0
    for i in range(j,len(arr)):
        if total < target:
            total = total + arr[i]
            list2.append(arr[i])
        if total == target:
            mainlist1.append(list2)
            list2 = []
            total = 0
            j = j + 1
            break
        if total > target:
            if list2 != []:
                total = total - arr[i]
                list2.pop()
            if list2 != []:
                total = total - arr[i]
                list2.pop()
    else:
        j = j + 1
print(mainlist1)
'''










'''def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(90))'''









'''from collections import  deque
arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
arr = deque(arr)
list2 = []
while arr != deque():
    list2.append(arr[0])
    arr.popleft()
    for i in range(len(arr)):
        list2.append(arr[i][-1])
        arr[i].pop()
    if arr == deque():
        break
    sample1 = arr[-1]
    sample1.reverse()
    list2.append(sample1)
    arr.pop()
    for j in range(len(arr)-1,-1):
        list2.append(arr[j][0])
        arr[j] = deque(arr[j])
        arr[j].popleft()
print(list2)
'''









'''list1 = [[0,1,1],[1,0,1],[1,0,1],[1,0,0]]
list2 = []
for i in range(len(list1)):
    for j in range(len(list1[i])):
        list3 = []
        if list1[i][j] == 0:
            list3.append(i)
            list3.append(j)
            list2.append(tuple(list3))
set1_x = set()
set1_y = set()
for i in range(len(list2)):
    x,y = list2[i]
    if x not in set1_x:
        set1_x.add(x)
    if y not in set1_y:
        set1_y.add(y)
flag1 = False
flag2 = False
if len(list1) == len(set1_x):
    flag1 = True
if len(list1[0]) == len(set1_y):
    flag2 = True
if flag1 and flag2:
    print(True)
else:
    print(False)'''




'''arr = [1,2,3,[4,5,6,[7,8],[[3,4]]]]
mainlist1 = []
index = 0
sample = arr
stack_index = [0]           ..................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Very Important ---------------------++++++++++++++++++++++++++++++
stack_arr = [arr]
flag = True
while True:                                                       ?????????????????????????????????????????????""""""""""""""""""""""""""
    flag =  False
    for i in range(index,len(sample)):
        if type(sample[i]) == list:
            # print(sample[i])
            stack_index[-1] = stack_index[-1] + 1
            stack_index.append(0)                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Vety IMPORTANT ---------------------------------
            stack_arr.append(sample[i])
            sample = sample[i]
            index = 0
            flag = True                                       -----------------------------WITHOUT RECURSION--------------------------------
            break
        else:
            mainlist1.append(sample[i])
            stack_index[-1] = stack_index[-1] + 1
    if flag == False:
        stack_index.pop()
        stack_arr.pop()
        if stack_index != []:
            index = stack_index[-1]
            sample = stack_arr[-1]
    if stack_index == []:
        break
print(mainlist1)'''

















'''nums = [-17,-15]
nums.sort()
index = 0
flag = False
for i in range(len(nums)):
    if nums[i] >= 0:
        flag = True
        index = i
        break
sum_list1 = nums[index:]
sum1 = 0
if flag == True:
    sum1 = sum(list(set(sum_list1)))
else:
    sum1 = nums[-1]

print(sum1)'''






'''nums = [10,20,30,5,10,50]
sum1 = 0
maxisum1 = 0
flag = False
for i in range(len(nums) - 1):
    if nums[i] < nums[i+1]:
        if i == len(nums) - 2:
            sum1 = sum1 + nums[i]
            sum1 = sum1 + nums[i+1]
            if maxisum1 < sum1:
                maxisum1 = sum1
                sum1 = 0
        else:
            sum1 = sum1 + nums[i]
    else:
        sum1 = sum1 + nums[i]
        if maxisum1 < sum1:
            maxisum1 = sum1
        sum1 = 0
        flag = False

print(maxisum1)
'''







'''x = 1
y = 1
smalest = ""
index = -1
points = [[1,2], [3,3], [3,3]]
list1 = []
count = 0
for item in points:
    x1,y1 = item
    if x1 == x or y1 == y:
        min_dist = abs(x - x1) + abs(y - y1)
        if smalest == "":
            smalest = min_dist
            index = count
        elif smalest > min_dist:
            smalest = min_dist
            index = count
    count = count + 1
print(index)
'''
# for item in list1:
#     x2,y2 = item
#     min_dist = abs(x - x2) + abs(y - y2)
#     if smalest == "":
#         smalest = min_dist
#         index =
#     if smalest >











'''items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
count = 0
for i in items:
    type1 = i[0]
    color1 = i[1]
    name1 = i[2]
    if ruleKey == "color":
        if color1 == ruleValue:
            count += 1
    elif ruleKey == "type":
        if type1 == ruleValue:
            count += 1
    elif ruleKey == "name":
        if name1 == ruleValue:
            count += 1
print(count)'''










'''nums = [1,2,3]
sample = 0
index = ""
for i in range(len(nums) - 1):
    if nums[i] > nums[i+1]:
        sample = nums[(i+1):]
        index = i+1

if sample != 0:
    total = sample + nums[0:index]
    for j in range(len(total)-1):
        if total[j] <= total[j+1]:
            pass
        else:
            print(False)
            break
    else:
        print(True)
else:
    print(True)
'''



'''nums = [4,2,4,5,6]
set1 = set()
main_sum1 = 0
sum1 = 0
for item in nums:
    if item not in set1:
        set1.add(item)
        sum1 = sum1 + item
    else:
        if main_sum1 < sum1:
            main_sum1 = sum1
        sum1 = 0
        set1 = set()
if main_sum1 < sum1:
    main_sum1 = sum1
print(main_sum1)'''









'''s = "cdbcbbaaabab"
x = 4
y = 5
total = 0
if x > y:
    ab_stack = []
    ab_stack.append(s[0])
    for i in range(1,len(s)):
        if ab_stack == []:
            ab_stack.append(s[i])
        elif ab_stack[-1] + s[i] == "ab":
            ab_stack.pop()
            total = total + x
        else:
            ab_stack.append(s[i])
    ba_stack_2 = []
    if ab_stack != []:
        ba_stack_2.append(ab_stack[0])
    for j in range(1,len(ab_stack)):
        if ba_stack_2 == []:
            ba_stack_2.append(ab_stack[j])
        elif ba_stack_2[-1] + ab_stack[j] == "ba":
            total = total + y
            ba_stack_2.pop()
        else:
            ba_stack_2.append(ab_stack[j])
else:
    ba_stack = []
    ba_stack.append(s[0])
    for i in range(1,len(s)):
        if ba_stack == []:
            ba_stack.append(s[i])
        elif ba_stack[-1] + s[i] == "ba":
            total = total + y
            ba_stack.pop()
        else:
            ba_stack.append(s[i])
    ab_stack_2 = []
    if ba_stack != []:
        ab_stack_2.append(ba_stack[0])
    for j in range(1,len(ba_stack)):
        if ab_stack_2 == []:
            ab_stack_2.append(ba_stack[j])
        elif ab_stack_2[-1] + ba_stack[j] == "ab":
            ab_stack_2.pop()
            total = total + x
        else:
            ab_stack_2.append(ba_stack[j])
print(total)'''







'''nums = [4,2,4,5,6]
set1 = set()
maxi = 0
l = 0
r = 0
max2 = 0
while r < len(nums):
    if nums[r] not in set1:
        set1.add(nums[r])
        max2 = max2 + nums[r]
        r = r + 1
    elif nums[r] in set1:
        l = r
        set1.remove(nums[r])
        max2 = max2 + nums[r]
        r = r + 1
    if max2 > maxi:
        maxi = max2
print(maxi)'''













'''nums =[10,1,5]
if len(nums) <= 2:
    print(sum(nums))
elif len(nums) == 3:
    if (nums[0] < nums[1] > nums[2]) or (nums[0] > nums[1] < nums[2]):
        diff1 = nums[0] + nums[1]
        diff2 = nums[1] + nums[2]
        if diff1 > diff2:
            print(diff1)
        else:
            print(diff2)
    else:
        print(sum(nums))
main_diff = 0
diff = 0
i = 1
flag = False
while i < len(nums) - 1:
    if nums[i-1] < nums[i] > nums[i+1]:
        if i == len(nums) - 2:
            flag = True
        if i == 1:
            diff = diff + nums[i - 1]
            diff = diff + nums[i]
        else:
            diff = diff + nums[i]
        if main_diff < diff:
            main_diff = diff
        diff = 0
        diff = diff + nums[i]
    elif nums[i-1] > nums[i] < nums[i+1]:
        if i == len(nums) - 2:
            flag = True
        if i == 1:
            diff = diff + nums[i-1]
            diff = diff + nums[i]
        else:
            pass
            # diff = diff + nums[i]
        if main_diff < diff:
            main_diff = diff
        diff = 0
        diff = diff + nums[i]
    else:
        if i == 1:
            diff = diff + nums[i-1]
            diff = diff + nums[i]
        elif i == len(nums) - 2:
            diff = diff + nums[i]
            diff = diff + nums[i+1]
        else:
            diff = diff + nums[i]
    i = i + 1
if main_diff < diff:
    main_diff = diff
diff = 0
if flag == True:
    diff = diff + nums[-1]
    diff = diff + nums[-2]
if main_diff < diff:
    main_diff = diff
print(main_diff)
'''







'''nums = [5,2,1,2,5,2,1,2,5]
maindiff = 0
diff = 0
flag = False
flag1 = False
for i in range(len(nums)-1):
    if flag == False and nums[i + 1] > nums[i]:
        diff = diff + nums[i]
        flag = True
    elif flag == True and nums[i + 1] < nums[i]:
        diff = diff + nums[i]
        if maindiff < diff:
            maindiff = diff
        flag = False
        diff = 0
        diff = diff + nums[i]
    elif flag == True:
        diff = diff + nums[i]
    if flag1 == False and nums[i+1] < nums[i]:
        diff = diff + nums[i]
        flag1 = True
    elif flag1 == True and nums[i+1] > nums[i]:
        diff = diff + nums[i]
        if maindiff < diff:
            maindiff = diff
        flag1 = False
        diff = 0
        diff = diff + nums[i]
    elif flag1 == True:
        diff = diff + nums[i]
print(maindiff)
'''








'''nums = [4,2,4,5,6]
main_diff = 0
diff = 0
asc = True
desc = True
i = 0
while i < len(nums) - 1:
    if nums[i] < nums[i+1] and desc == True:
        if asc == False:
            diff = diff + nums[i]
            diff = diff + nums[i+1]
            i = i + 2
            asc = True
        elif asc == True:
            diff = diff + nums[i]
            i = i + 1
            desc = False
    elif asc == True and nums[i] > nums[i+1]:
        if desc == False:
            diff = diff + nums[i]
            diff = diff + nums[i + 1]
            i = i + 2
            desc = True
        elif desc == True:
            diff = diff + nums[i]
            i = i + 1
            asc = False
'''















'''encoded =[6,2,7,3]
first = 4
arr1 = [first]
for i in range(len(encoded)):
    decode = encoded[i] ^ arr1[i]
    arr1.append(decode)
print(arr1)'''










'''gain = [-4,-3,-2,-1,4,3,2]
list1 = [0]
start = 0
for i in range(len(gain)):
    start = start + gain[i]
    list1.append(start)
print(list1)'''
















'''s = "leeetcode"
str1 = ""
for i in range(len(s)-2):
    if s[i] == s[i+1] == s[i+2]:
        pass
    else:
        str1 = str1 + s[i]

str1 = str1 + s[-2:]
print(str1)
'''









'''boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
list1 = sorted(boxTypes,key=lambda a:a[1])
list1.reverse()
count = 0
total = 0
for i in range(len(list1)):
    count = count + list1[i][0]
    if count <= truckSize:
        total = total + (list1[i][0] * list1[i][1])
    else:
        count = count - list1[i][0]
        for j in range(list1[i][0]):
            count = count + 1
            if count <= truckSize:
                total = total + list1[i][1]
            else:
                break
print(total)'''















'''from collections import deque
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
list1 = deque(students)
list2 = deque(sandwiches)
count = 0
while list1 != deque():
    if list1[0] == list2[0]:
        list1.popleft()
        list2.popleft()
        count = 0
    else:
        count += 1
        check1 = list1[0]
        list1.popleft()
        list1.append(check1)
    if count == len(list1)+1:
        break
print(list1)'''







'''list1 = ["/ah/al/am","/ah/al"]
list1.sort()
list4 = []
hold = 0
str1 = list1[0]
list4.append(str1)
flag = True
for i in range(1,len(list1)):
    if str1 == list1[i][0:len(str1)]:
        if len(list1[i]) >= len(str1):
            if list1[i][len(str1)] == "/":
                pass
            else:
                list4.append(list1[i])
                str1 = list1[i]
    else:
        list4.append(list1[i])
        str1 = list1[i]
print(list4)'''















'''list1 = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
list1.sort()
list4 = []
hold = 0
str1 = ""
flag = True
for i in range(len(list1)):
    if flag:
        list4.append(list1[i])
        hold = len(list1[i])-1
        str1 = list1[i][-1]
        flag = False
    else:
        if list1[i][hold] == str1:
            pass
        else:
            list4.append(list1[i])
            hold = len(list1[i]) - 1
            str1 = list1[i][-1]

print(list4)
'''






'''allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
hash1 = {}
count = 0
for item in allowed:
    hash1[item] = 1
for item in words:
    for j in item:
        if j in hash1:
            pass
        else:
            break
    else:
        count += 1
print(count)
'''













'''class A:
    def __init__(self,n):
        self.n = n
        self.list1 = [None]
        self.list2 = [None] * n #[None, None, None, None, None, None]
        self.start = 0
    def add(self,key_value):
        self.list2[key_value[0] - 1] = key_value[1]
        list4 = []
        flag = False
        for i in range(self.start,len(self.list2)):
            if self.list2[i] == None:
                self.list1.append(list4)
                self.start = i
                break
            else:
                if i == self.start:
                    list4.append(key_value[1])
                else:
                    list4.append(self.list2[i])
        else:
            self.list1.append(list4)
a = A(5)
a.add([3,"cccc"])
a.add([1,"aaaa"])
a.add([2,"bbbb"])
a.add([5,"eeee"])
a.add([4,"dddd"])
print(a.list1)
'''




'''class A:
    def __init__(self,name):
        self.__name = name
    def check1(self):
        return self.__name
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

a = A("sawan")
b = B("Sawan",89)
print(b.check2())'''






'''def fibo(n,list1):
    if n <= 1:
        return 1
    a = fibo(n-1,list1) + fibo(n-2,list1)
    list1.append(a)
    return a
list2 = []
(fibo(,list2))
list3 = set(list2)
list3 = list(list3)
list3.sort()
print(list3)'''



'''word1 = ["ab", "c"]
word2 = ["a", "bc"]
str1 = "".join(word1)
str2 = "".join(word2)
ret'''





'''class OrderedStream:
    def __init__(self,n):
        self.list1 = [None] * n + 1
d = OrderedStream(5)
print(d.list1)
'''









'''nums = [4,51,68]
even = 0
odd = 0
for i in range(len(nums) - 1):
    if (nums[i] + nums[i+1]) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
if odd != 0 and even != 0:
    if (nums[-1] + nums[0]) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
elif odd != 0 and even == 0:
    odd = odd + 1
elif even != 0 and odd == 0:
    even = even + 1
print(max(odd,even))'''










'''nums = [2,13,26,70,76]
hash1 = {}
for i in range(len(nums)-1):
    diff = (nums[i] + nums[i+1]) % 2
    if diff not in hash1:
        hash1[diff] = 1
    else:
        hash1[diff] += 1
diff = (nums[-1] + nums[0]) % 2
# if diff not in hash1:
#     hash1[diff] = 1
# else:
#     hash1[diff] += 1
print(hash1)
max_value = 0
max_key = 0
for key,value in hash1.items():
    if value > max_value:
        max_key = key
        max_value = value
print(max_value+1)'''



'''code = [10,5,7,7,3,2,10,3,6,9,1,6]
copy1 = code.copy()
k = -4
start = 1
end = (start + k) - 1
if k > 0:
    window = sum(code[start:end + 1])
    copy1[0] = window
elif k < 0:
    end = start - 1
    start = (start - 1) + k
    window = sum(code[start:])
    copy1[0] = window
    end = end - 1
for i in range(1,len(code)):
    print(start,end)
    if end > len(code) - 1:                         #for positive numbers
        window = window - code[start]
        start += 1
        end = 0
        window = window + code[end]
    elif start > len(code) - 1:
        start = start - 1
        window = window - code[start]
        start = 0
        window = window + code[end]
        end +=1
    else:
        window = window - code[start]
        end = end + 1
        if end > len(code) - 1:
            end = 0
            window = window + code[end]
        else:
            window = window + code[end]
        start = start + 1
    copy1[i] = window
print(copy1)'''





'''code = [5,7,1,4,7]
copy1 = code.copy()
k = 4
start = 1
end = (start + k) -1
window = sum(code[start:end+1])
copy1[0] = window
for i in range(1,len(code)):
    print(start,end)
    if end > len(code) - 1:                         #for positive numbers
        window = window - code[start]
        start += 1
        end = 0
        window = window + code[end]
    elif start > len(code) - 1:
        start = start - 1
        window = window - code[start]
        start = 0
        window = window + code[end]
        end +=1
    else:
        window = window - code[start]
        end = end + 1
        if end > len(code) - 1:
            end = 0
            window = window + code[end]
        else:
            window = window + code[end]
        start = start + 1
    copy1[i] = window
print(copy1)'''






'''word = "234Adas"
if len(word) >= 3 and word.isalnum():
    for item in word:
        if item in {"a","e","i","o","u","A","E","I","O","U"}:
            break
    else:
        print(False)
    for item in word:
        if item not in {"a","e","i","o","u","A","E","I","O","U"} and item.isalpha():

            break
    else:
        print(False)
'''





'''n = 3
if n < 2:
    print(1)
else:
    list1 = [0] * (n + 1)
    list1[0] = 0
    list1[1] = 1
    j = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            list1[i] = list1[int(i / 2)]
        else:
            list1[i] = list1[j] + list1[j + 1]
            j = j + 1
print(max(list1))'''











'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(89)
second = Node(90)
third = Node(91)
head.next = second
current = head
while current.next is not None:
    print(current.data)
    current = current.next
'''


'''arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
for i in range(len(pieces)):
    for j in range(len(arr) - (len(pieces[i]) - 1)):
        set1 = arr[j:len(pieces[i])+j]
        print(set1,pieces[i])
        if set1 == pieces[i]:
            break
    else:
        print(False)
        break
else:
    print(True)
'''





'''arr = [10,12,9,3,44,5]
target1 = 17
hash1 = {}
for item in arr:
    target = target1
    if item not in hash1:
        target = target - item
        hash1[target] = item
    else:
        print(item,hash1[item])
print(hash1)'''



'''players = [1,1,1]
trainers = [10]
players.sort()
trainers.sort()
i = 0
j = 0
count = 0
while i < len(players) and j < len(trainers):
    if players[i] <= trainers[j]:
        i = i + 1
        j = j + 1
        count += 1
    else:
        j = j + 1
print(count)
'''




'''arr = [[8,7],[9,9],[7,4],[9,7]]
diff = ""
arr.sort()
for i in range(len(arr)-1):
    x,y = arr[i]
    x1,y1 = arr[i+1]
    diff1 = x1 - x
    if diff == "":
        diff = diff1
    elif diff1 > diff and diff != "":
        diff = diff1
print(diff)'''





'''hash1 = {"a" : 1,"b":2,"c":3}
dict.
print(hash1)
hash1.popitem()
print(hash1)'''


#decorators
'''def decorator_function(func):
    def wrapper():
        print("before calling function")
        func()
        print("after caliing function")
    return wrapper
@decorator_function
def my_function():
    print("hello world")
my_function()'''










'''arr = [2,3,1,3,2]
hash1 = {}
for i in range(len(arr)):
    if arr[i] not in hash1:
        hash1[arr[i]] = 1
    else:
        hash1[arr[i]] += 1
list1 = []
for key, value in hash1.items():
    list2 = []
    list2.append(key)
    list2.append(value)
    list1.append(tuple(list2))
for i in range(len(list1)):
    for j in range((len(list1))-i-1):
        if list1[j+1][1] == list1[j][1]:
            if list1[j+1][0] > list1[j][0]:
                list1[j + 1], list1[j] = list1[j], list1[j + 1]
        elif list1[j+1][1] < list1[j][1]:
            list1[j+1],list1[j] = list1[j],list1[j+1]
list6 = []
for item in list1:
    for j in range(item[1]):
        list6.append(item[0])
print(list6)
print(list1)
'''







'''arr = [12,23,36,46,62]
str1 = "spuda"
start = 0
hash1 = {}
for i in range(len(arr)):
    diff = abs(start - arr[i])
    start = arr[i]
    if str1[i] not in hash1:
        hash1[str1[i]] = diff
    else:
        if hash1[str1[i]] < diff:
            hash1[str1[i]] = diff
max1 = 0
for value in hash1.values():
    if value > max1:
        max1 = value
list1 = []
for key,value in hash1.items():
    if value == max1:
        list1.append(key)
list1.sort()
print(list1[-1])'''







'''list1 = [12,34,12,45,91]
list2 = list(map(lambda x: x ** 2,list1))
list3 = list(filter(lambda x: x % 2 == 0,list1))
print(list3)'''






'''arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
d = len(arr)
print(d)
e = len(arr) / 2
ans = ((e // 10))
ans1 = int(ans)
print(ans1)
arr.sort()
min1 = sum(arr[0:ans1])
max1 = sum(arr[(d - ans1):])
sum1 = sum(arr)
sum1 -= min1
sum1 -= max1
d = d - (ans * 2)
total = sum1 / d
print(total)
'''









'''rectangles = [[5,8],[3,9],[5,12],[16,5]]
list1 = []
for item in rectangles:
    x1,y1 = item
    if x1 < y1:
        list1.append(x1)
    else:
        list1.append(y1)
max1 = max(list1)
count = 0
for item in list1:
    if item == max1:
        count += 1
print(count)'''









'''arr = [1,0,0,6,4,9]
arr.sort()
hash1 = {}
for i in range(len(arr)+1):
    for j in range(len(arr)):
        if i <= arr[j]:
            if i not in hash1:
                hash1[i] = len(arr[j:])
for key,value in hash1.items():
    if key == value:
        print(key)
else:
    print(-1)'''















'''class Student:
    def __init__(self,name, sername,roll_no,percentage):
        self.name = name
        self.sername = sername
        self.roll_no = roll_no
        self.percentage = percentage
        self.Branch = "AI and Data Scienec"
    def show_name_Branch(self):
        print("Nmae of student",self.name,"And Branch of student",self.Branch)
    def show_roll_with_name(self):
        print("Name of student",self.name,"roll of student",self.roll_no)
obj = Student("sawan","patel","0863AD201044",72)
obj.show_name_Branch()
obj.show_roll_with_name()'''




'''arr = ["./","../","./"]
steps = 0
for item in arr:
    if item == "../":
        if steps > 0:
            steps = steps - 1
    elif item == "./":
        pass
    else:
        steps = steps + 1
print(steps)'''



'''n  = 50
max_prime = 0
for i in range(2, n):
    # if n % i == 0:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        print(i)
            # if max_prime < i:
            #     max_prime = i
            #     print(max_prime)
# print(max_prime)'''



'''mat = [[5]]
n = len(mat)
flag = False
if n % 2 == 0:
    flag = True
total = 0
for i in range(n):
    total = total + mat[i][i]
    total = total + mat[i][n-i-1]
if flag == False:
    check1 = n//2
    total = total - mat[check1][check1]
print(total)
'''










# hash1 = {"sawam":12,"gxcg":34,"vxt":90,"xgc":78}
# x1 = dict(map(lambda item:(item[0],item[1] ** 2), hash1.items()))
# print(x1)






'''arr = [1,2,1,2,1,1,1,3]
m = 2
k = 2
for i in range(len(arr)):
    list1 = []
    comapre_list1 = []
    count = 0
    for j in range(i,len(arr)):
        if len(comapre_list1) != m:
            comapre_list1.append(arr[j])
        list1.append(arr[j])
        if (len(comapre_list1) == len(list1)) and len(comapre_list1) == m:
            if comapre_list1 == list1:
                count = count + 1
            else:
                count = 0
            print(count)
            list1 = []'''







    #     if len(list1) == m:
    #         if tuple(list1) not in hash1:
    #             hash1[tuple(list1)] = 1
    #         else:
    #             hash1[tuple(list1)] += 1
    #         list1 = []
    #         list1.append(arr[j])
    #     else:
    #         list1.append(arr[j])
    # if len(list1) == m:
    #     if tuple(list1) not in hash1:
    #         hash1[tuple(list1)] = 1
    #     else:
    #         hash1[tuple(list1)] += 1
    # for value in hash1.values():
    #     if value >= k:
    #         print(True)
    #         break
    # else:
    #     print(False)









'''arr = [2,2,1,2,2,1,1,1,2,1]
m = 2
k = 2
i = 0
while i < len(arr):
    j = i
    list1 = []
    hash1 = {}
    while j < len(arr):
        if len(list1) == m:
            if tuple(list1) not in hash1:
                hash1[tuple(list1)] = 1
            else:
                hash1[tuple(list1)] += 1
            list1 = []
            list1.append(arr[j])
        else:
            list1.append(arr[j])
        if j == len(arr) - 1 and len(list1) == m:
            if tuple(list1) not in hash1:
                hash1[tuple(list1)] = 1
            else:
                hash1[tuple(list1)] += 1
        j = j + 1
    print(hash1)
    for value in hash1.values():
        if value >= k:
            print(True)
            break
    else:
        print(False)
    i = i + m
'''















'''n = 2
rounds = [2,1,2,1,2,1,2,1,2]
list1 = [i-1 for i in rounds]
list2 = [0] * n
for i in range(1,len(rounds)):
    lower = list1[i - 1]
    upper = list1[i]
    print(lower,upper)
    if lower > upper:
        if i == 1:
            for j in range(lower, len(list2)):
                list2[j] = list2[j] + 1
            for k in range(upper + 1):
                list2[k] = list2[k] + 1
        else:
            for j in range(lower + 1, len(list2)):
                list2[j] = list2[j] + 1
            for k in range(upper + 1):
                list2[k] = list2[k] + 1
    else:
        if i == 1:
            for l in range(lower, upper + 1):
                list2[l] = list2[l] + 1
        else:
            for l in range(lower+1,upper+1):
                list2[l] = list2[l] + 1
max1 = max(list2)
list3 = []
for i in range(len(list2)):
    if list2[i] == max1:
        list3.append(i+1)
print(list3)
'''














'''n = 4
rounds = [1,3,1,2]
list1 = [rounds[i]-1 for i in range(len(rounds))]
list2 = [0] * n
for i in range(1,len(rounds)):
    lower = list1[i-1]
    upper = list1[i]
    k = lower
    flag = True
    while True:
        if k-1 == upper:
            break
        list2[k] = list2[k] + 1
        if i == 1:
            list2[k] = list2[k] + 1
        else:
            if flag == True:
                k = k + 1
                flag = False
            list2[k] = list2[k] + 1
        if k == len(list2) - 1:
            k = 0
        else:
            k = k + 1
        print(list2)
print(list2)'''







'''n = 2
rounds = [2,1,2,1,2,1,2,1,2]
#[1, 2, 3, 4]
list1 = [i for i in range(1,n+1)]
list2 = [0] * len(list1)
for j in range(1,len(rounds)):
    range1 = rounds[j-1]
    range2 = rounds[j]
    k = range1 - 1
    flag1 = True
    while k != range2:
        if j == 1:
            list2[k] = l1ist2[k] + 1
        else:
            if flag1 == True:
                k = k + 1
                flag1 = False
            list2[k] = list2[k] + 1
        if k == len(list1) - 1:
            k = 0
        else:
            k = k + 1
print(list2)
'''









# list1 = [1,2,3,5]
# list2 = list(map(lambda x : x ** 2,list1))
# print(list2)








'''k = 5
str1 = "a"
flag = True
while flag:
    for i in range(len(str1)):
        str1 = str1 + chr(ord(str1[i]) + 1)
    if len(str1) >= k:
        print(str1[k-1])
        flag = False
        break
print(str1)'''








'''arr = [1,2,34,3,4,5,7,23,12]
for i in range(len(arr)-2):
    if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
        print(True)
        break
else:
    print(False)'''











'''def recur(n):
    if n == 0:
        return
    # print(n)
    return recur(n-1)
    # print(d)

print(recur(9))
'''
# armstrong
# strong
# perfect
'''def armstrong(n,str1,total,len1):
    if n < 0:
        return "Not armstrong"
    total = total + int(str1[n]) ** len1
    if str(total) == str1:
        return "Armstrong"
    return armstrong(n-1,str1,total,len1)
num1 = 133
str1 = str(num1)
len1 = len(str1)
total = 0
n = len1 - 1
print(armstrong(n,str1,total,len1))'''



'''
def perfect(n,m,total):
    if n <= 1:
        return 1
    if m % n == 0:
        total = total + n
    if total == m:
        return total
    return perfect(n-1,m,total)
m = 6
n = m - 1
total = 1

d = (perfect(n,m,total))
if d == m:
    print("Perferct")
else:
    print("Not perect")





def perferct(n):
        total = 1
        for i in range(2,n):
            if n % i == 0:
                total = total + i
        if total == n:
            return "Perfect"
        return "Not perfect"
print(perferct(28))









def strong(n):
    str1 = str(n)
    len1 = len(str1)
    total1 = 0
    for i in range(len1):
        if str1[i] == "1":
            total1 = total1 + 1
        else:
            total = 1
            for j in range(1,int(str1[i])+1):
                total = total * j
            total1 = total1 + total
    print(total1)
    if total1 == n:
        return "Strong"
    return "Not strong"
print(strong(145))




def armstrong(n):
    str1 = str(n)
    len1 = len(str(n))
    total = 0
    for i in range(len1):
        check1 = int(str1[i]) ** len1
        total = total + check1
    if total == n:
        return "Armstong"
    return "Not armstrong"
print(armstrong(12))
'''









# def check(**args):
#     list1 = []
#     for j in args.items():
#         yield j
# print(check(name = "sawan",sername = "patel"))




# def cek(n):
#     return n
#     # yield n
# n = 5
# d = cek()
# for i in range(5):
#     print(next(d(i)))




'''word = "aabbccdd"
k = 7
str1 = ""
hash1 = {}
for item in word:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
print(hash1)'''









# def che(*args,simple1):
#     for item in args:
#         simple1 += item
#     print(simple1)
# che(1,2,3,4,5,6,simple1 = 0)



# list1 = [1,2,3,4,5]
# print(tuple(map(lambda x:x**2,list1)))


'''arr = [1,2,3,4]
k = 2
list1 = []
flag = True
i = 0
count = 0
j = 0
while flag:
    if j < len(arr):
        if i + 1 == arr[j]:
            i = i + 1
            j = j + 1
        else:
            list1.append(i+1)
            count += 1
            i = i + 1
    else:
        list1.append(i+1)
        i = i + 1
        count = count + 1
    if count == k:
        flag = False
print(list1[k])
'''











'''word = "xyyx"
count = 1
hash1 = {}
for i in range(len(word) - 1):
    if word[i] == word[i+1]:
        if word[i] not in hash1:
            hash1[word[i]] = 2
        else:
            hash1[word[i]] +=1
print(hash1)
for key, value in hash1.items():
    count += value - 1
print(count)'''













'''word = "abbcccc"
i = 0
j = i+1
list1 = []
str1 = ""
while i < len(word) - 1:
    if word[i] == word[j]:
        str1 = str1 + word[i]
        for k in range(j+1,len(word)):
            str1 = str1 + word[j]
        list1.append(str1)
        str1 = ""
    else:
        str1 = str1 + word[i]
        i = i + 1
        j = i+1
'''












# arr = [10,6,2,9,7,3,1]
# max1 = arr[0]
# min1 = arr[0]
# for i in range(len(arr)):
#     if min1 >= arr[i]:
#         max1 = min1
#         min1 = arr[i]
#     elif max1 > arr[i] and arr[i] > min1:
#         max1 = arr[i]
# min2 = max1
# print(min2,min1)


# arr = [0,0,2,2,3]
# a = 0
# b = 0
# c = 1
# hash1 = {a:0,b:0,c:0}
# for i in range(len(arr)):
#     if arr[i] <= a:
#         hash1[a] += 1
#     if arr[i] <= b:
#         hash1[b] += 1
#     if arr[i] <= c:
#         hash1[c] += 1
# max1 = hash1[a]
# min1 = hash1[a]
# for value in hash1.values():
#     if value <= min1:
#         max1 = min1
#         min1 = value
#     elif max1 > value and min1 < value:
#         max1 = value
# total = min1
# diff = max1 - min1
# total = total + diff
# print(total)





'''arr = [1,1,2,2,3]
a = 1
b = 3
c = 1
count = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                count += 1
print(count)'''








'''a = {"a":90,"b":2}
print(a.pop("a"))
print(a)'''

'''dict1 = {"name:":34,"kalam":45}
dict1.setdefault("kalam")
print(dict1)'''




'''import copy
dict1 = {"namw":23,"shs":[56]}
dict2 = copy.deepcopy(dict1)
dict2["shs"].append(90)
print(dict2)
print(dict1)'''






'''nums = [1,1,1,1]
hash1 = {}
for item in nums:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
max1 = 0
for key, value in hash1.items():
    max2 = 0
    if key - 1 in hash1:
        max2 = max2 + value
        max2 = max2 + hash1[key-1]
        if max2 > max1:
            max1 = max2
print(max1)
'''







'''arr = [1,2,3,1,1,3]
count = 0
hash1 = {}
for item in arr:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
total = 0
for key,value in hash1.items():
    n = value
    diff1 = (n * (n - 1))/2
    total += diff1
print(int(total))'''

















'''arr = [3,5,6,7]
target = 9
MOD = 10**9 + 7
start = 0
end = len(arr)-1
total = 0
arr.sort()  # sort first
n = len(arr)
pow2 = [1] * n  # precompute powers of 2 modulo MOD
print(pow2)
for i in range(1, n):
    pow2[i] = (pow2[i-1] * 2) % MOD
start, end = 0, n-1
total = 0
while start <= end:
    if arr[start] + arr[end] <= target:
        total = (total + pow2[end - start]) % MOD
        start = start + 1
    elif arr[start] + arr[end] > target:
        end = end - 1
print(total)'''
















'''arr = [2,3,3,4,6,7]
target = 12
start = 0
end = len(arr)
while start < end:
    mid = (start + end) // 2
    if arr[mid] + arr[mid] <= target:
        start = mid+1
    elif arr[mid] + arr[mid] > target:
        end = mid
max1 = arr[end]
count = 0
index = ""
'''









'''nums1 = [3,5,6,7]
target = 9
count = 0
for i in range(len(nums1)):
    for j in range(i,len(nums1)):
        print(nums1[i],nums1[j])
        if nums1[i] + nums1[j] <= target:
            # print(nums1[i])
            count += 1
print(count)'''






'''nums = [11,-40,2,-7,-37,6,11,-13,-32,-29,5,-12,9,-25,27,-10,-24,7,40,-26,29,29,-5,20,-7,12,0,9,25,24,-3,-1,20,-1,5,-40,29,-14,1,-13,-27,-39,-16,-12,20,-20,-8,31,5,33,-29,-10,-2,31,7,10,37,20,4,-10,-35,-31,-4,-32,-20,5,25,22,-7,15,39,-35,11,27,13,10,32,-37,-1,19,17,17,34,9,29,36,-30,-32,-10,-35,-8,39,25,34]
k = 68
hash1 = {}
list1 = ["0"] * len(nums)
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = [i]
    else:
        if len(hash1[nums[i]]) < k:
            hash1[nums[i]].append(i)
nums.sort()
print(nums)
print(nums)
for i in range(len(nums)-k,len(nums)):
    if nums[i] in hash1:
        list1[hash1[nums[i]][-1]] = nums[i]
        hash1[nums[i]].pop()
list2 = []
for j in list1:
    if j != "0":
        list2.append(j)
print(list2)'''







'''from collections import deque
nums = [-16,-13,8,16,35,-17,30,-8,34,-2,-29,-35,15,13,-30,-34,6,15,28,-23,34,28,-24,15,-17,10,31,32,-3,-36,19,31,-5,-21,-33,-18,-23,-37,-15,12,-28,-40,1,38,38,-38,33,-35,-28,-40,4,-15,-29,-33,-18,-9,-29,20,1,36,-8,23,-34,16,-7,13,39,38,7,-7,-10,30,9,26,27,-37,-18,-25,14,-36,23,28,-15,35,-9,1]
k = 8
heap = deque()
min1 = min(nums)
heap.append(min1)
for item in nums:
    if item >= heap[-1]:
        heap.append(item)
    elif item <= heap[0]:
        heap.appendleft(item)
    if len(heap) > k:
        heap.popleft()

print(heap)'''







'''arr = [4000,3000,1000,2000]
total = 0
max1 = arr[0]
min1 = arr[0]
for i in arr:
    if i > max1:
        max1 = i
    elif min1 > i:
        min1 = i
    total += i
total = total - max1
total = total - min1
ave = total / (len(arr)-2)
print(ave)'''






'''list1 = [8,2,5,1,9,0]
first_smal = list1[0]
second_smal = list1[0]
for i in range(1,len(list1)):
    if list1[i] < first_smal:
        second_smal = first_smal
        first_smal = list1[i]
    elif second_smal > list1[i] and list1[i] > first_smal:
        second_smal = list1[i]
print(first_smal,second_smal)'''




'''tuple1 = ("namw","progresss","growtwchyyhvGF")
max_str = ""
lenght1 = 0
for item in tuple1:
    if len(item) > lenght1:
        max_str = item
        lenght1 = len(item)
print(max_str)'''







'''s = "letsleetcode"
k = 2
max_lengh = len(s)//2
hash1 = {}
list1 = []
for i in range(len(s)):
    if s[i] not in hash1:
        hash1[s[i]] = 1
    else:
        hash1[s[i]] += 1
hash2 = {i:j for (i ,j) in hash1.items() if j >= k}
flag = True
j = 0
while flag:
    count = 0
    str1 = ""
    for i in range(j, max_lengh):
        if s[i] in hash2:
            hash2[s[i]] = hash2[s[i]] - 1
            str1 = str1 + s[i]
            count = count + 1
            if hash2[s[i]] == 0:
                flag = False
        if count == len(hash2):
            list1.append(str1)
            break
    j = j + 1
print(list1)
'''






# for i in range(0,max_lengh):
#     if hash1[s[i]] >= k:
















'''x,u, *y = 1,2,5,7,8,9,
print(x)
print(u)
print(type(y))'''


'''list1 = [1,2,4,5,67,"name"]
list2 = [i for i in list1 if type(i) == int]
print(list2)
list3 = [j for j in list1 if type(j) == str]
print(list3)'''






'''dict1 = {'n': 1234, 'a': 'hhff', 'm': 'name', 'e': '78'}
list1 = [0.56,0.53,23,12]
for (key,value),list1_items in zip(dict1.items(),list1):
    print(f"this is key {key} and this is value {value} and this is list_values {list1_items} ")'''








'''prices = [8,7,4,2,8,1,7,7,10,1]
stack = []
for i in range(len(prices)-1):
    for j in range(i+1,len(prices)):
        if prices[i] >= prices[j]:
            diff = prices[i] - prices[j]
            stack.append(diff)
            break
    else:
        stack.append(prices[i])
stack.append(prices[-1])
print(stack)'''














'''prices = [8,7,4,2,8,1,7,7,10,1]
stack = [prices[-1]]
variable = prices[-1]
flag = False
for i in range(len(prices) -1,0,-1):
    if prices[i-1] >= prices[i]:
        diff = prices[i-1] - prices[i]
        stack.append(diff)
        variable = prices[i]
    else:
        if prices[i-1] >= variable and flag == True:
            diff = prices[i-1] - variable
            stack.append(diff)
            variable = prices[i-1]
        else:
            stack.append(prices[i-1])
    flag = True
stack.reverse()
print(stack)'''












'''prices = [8,4,6,2,3]
monotonic_stack = [prices[0]]
list1 = []
for i in range(1,len(prices)):
    if monotonic_stack[-1] >= prices[i]:
        diff = monotonic_stack[-1] - prices[i]
        list1.append(diff)
        monotonic_stack.pop()
        monotonic_stack.append(prices[i])
    else:
        monotonic_stack.append(prices[i])

print(list1)'''




'''arr = [1,1,2,2]
n = 2
list1 = []
j = 0
for i in range(len(arr)-1):
    if n + j < len(arr):
        list1.append(arr[i])
        list1.append(arr[n+j])
        j = j + 1
print(list1)'''










'''import copy
list1 = [1,2,3,4,5,6]
list2 = copy.copy(list1)
list2.append(99)
print(list2)
print(list1)'''




'''s = "00101001"
k = 1
str2 = ""
str3 = ""
flag = False
for i in range(len(s) - 1,-1,-1):
    if flag == False:
        str2 = s[i] + str2
        if int(str2,2) > k:                        # =====---------------------------------important --------------------=============
            str2 = str3
            flag = True
        else:
            str3 = str2
    else:
        if s[i] == "0":
            str2 = s[i] + str2
print(str2)'''



# bin1 = bin(k)[2:]
# str1 = str(bin1)







# list1 = ["nissan" , 5,True]
# list1[0] = list1[0] + "patel"
# print(list1)








'''a = "becda"
b = "cdabe"
half = (len(a) // 2)
str1 = ""
for i in range(half,len(a)):
    str1 = str1 + a[i]
for j in range(0,half):
    str1 = str1 + a[j]
if str1 == b:
    print(True)
else:
    print(False)'''




'''s = "1001101"
k = 5
bin1 = bin(k)[2:]
str1 = str(bin1)
len_k = len(str1)
str5 = ""
count = 0
list1 = []
list2 = []
# for i in range(len(s)):
#     if s[i] == "0":
#         list1.append(0)
flag = False
for j in range(len(s) - 1,-1,-1):
    if s[j] == "1" and count < len_k:
        list2.append(j)
        str5 = s[j] + str5
    elif count < len_k:
        str5 = s[j] + str5
    if flag == False and count > len_k:
        list1.append(0)
    if s[j] == "1" and count > len_k:
        flag = True

    count = count + 1

print(str5)
print(flag)
print(list1)'''







'''s = "1001010"
k = 5
str1 = ""
for item in s:
    str1 = str1 + item
    s = int(str1,2)
    print(s)
'''






'''str1 = "aabbbcccc"
hash1 = {}
for i in range(len(str1)):
    if str1[i] not in hash1:
        hash1[str1[i]] = 1
    else:
        hash1[str1[i]] = hash1[str1[i]] + 1
max1 = 0
max2 = 0
max_var1 = ""
max2_var2 = ""
for key,value in hash1.items():
    if value > max1:
        max2 = max1
        max1 = value
        max2_var2 = max_var1
        max_var1 = key
    elif max1 > value and value > max2:
        max2 = value
        max2_var2 = key
print(max2_var2)'''






'''str1 = "abcz"
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            j = j + 3
            if j > 25:
                j = j - len(str2)
                str3 = str3 + str2[j]
            else:
                str3 = str3 + str2[j]
print(str3)'''














'''str1 = "aabbccc"
set1 = set(str1)
list1 = [0] * len(set1)
for item in str1:
    list1[ord(item) - 97] = list1[ord(item) - 97] + 1
print(list1)'''









'''nums = [10,2,5,2]
max1 = nums[0]
max2 = min(nums)
for i in range(1,len(nums)):
    if nums[i] >= max1:
        max2 = max1
        max1 = nums[i]
    elif nums[i] < max1 and nums[i] > max2:
        max2 = nums[i]
    print(max1,max2)
max1 = max1 - 1
max2 = max2 - 1
product = max1 * max2
print(product)
'''







'''a = "babab"
list1 = []
for i in range(len(a)):
    str1 = ""
    check_str1 = ""
    for j in range(i,len(a)):
        str1 = a[j] + str1
        check_str1 = check_str1 + a[j]
        if str1 == check_str1:
            list1.append(str1)
            list1.append(check_str1)
print(list1)'''







'''list1 = [9,1,7,2,3,12,8,9,3,0,1]
max1 = list1[0]
max2 = 0
for i in range(len(list1)):
    if list1[i] > max1:
        max2 = max1
        max1 = list1[i]
    elif list1[i] < max1 and list1[i] > max2:
        max2 = list1[i]
        print(max2)
print(max1,max2)'''






'''taget = [1,2,2,3]
arr = [1,1,2,3]
hash1 = {}
for i in range(len(taget)):
    if taget[i] not in hash1:
        hash1[taget[i]] = 1
    else:
        hash1[taget[i]] += 1
for item in arr:
    if item in hash1:
        hash1[item] -= 1
    else:
        print(False)
        break
for value in hash1.values():
    if value == 0:
        pass
    else:
        print(False)
        break
else:
    print(True)
'''




'''target = [3,7,9]
arr = [3,7,11]
for i in range(len(target)):
    list1 = []
    for j in range(i,len(arr)):
        if target[i] == arr[j]:
            list1.append(arr[j])
            list1.reverse()
            arr = arr[:i] + list1 + arr[j+1:]
            print(arr)
        else:
            list1.append(arr[j])'''














'''startTime = [4]
endTime = [4]
queryTime = 4
count = 0
for i in range(len(startTime)):
    if startTime[i] <= queryTime <= endTime[i]:
        count += 1
print(count)
'''






'''a = -10 ** 10
b = 10 ** 10
print((a + b)/2)
'''



'''nums = [0,1,0,1]
k = 1
list1 = []
for i in range(len(nums)):
    if nums[i] == 1:
        list1.append(i+1)
for i in range(len(list1)-1):
    if (list1[i+1] - 1) - list1[i] >= k:
        pass
    else:
        print(False)
        break
else:
    print(True)
print(list1)'''












'''n = 7
for i in range(n):
    for j in range(n):
        if (i == 0) or (i == n // 2) or (i == n - 1):
            if j < n - 1:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if j == 0 or j == n - 1:
                print("*",end="")
            else:
                print(" ",end="")
    print()
'''









'''n = 8
count = 0
half = n//2
for i in range(n//2):
    count2 = 1
    flag = False
    for j in range(((n//2))+count):
        # print(j)
        if j >= (((n//2) - 1) - count):
            if j-1 <= half:
                print(count2,end="")
                count2 = count2 + 1
            elif j > half:
                count2 = count2 - 1
                print(count2,end="")
        else:
            print(" ",end="")
    count = count + 1
    print()'''







'''n = 6
count = 0
for i in range(n):
    for j in range(n*2):
        if j <= count:
            print("*",end="")
        elif j+1 >= (n * 2) - count:
            print("*",end="")
        else:
            print(" ",end="")
    count = count + 1
    print()
'''
















'''n = 25
i = 1
while i < n:
    if (n / i) == i:
        print("Perfect")
        break
    i = i + 1'''


# n = 5
# count = 65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(count),end="")
#         count = count + 1
#     print()






'''nums = [2,2,2,2,2]
key = 2
k = 2
list1 = []
list2 = []
for i in range(len(nums)):
    if nums[i] == key:
        list1.append(i)
for i in range(len(list1)):
    for j in range(list1[i]-k,list1[i]+(k+1)):
        if j >= 0 and j <= len(nums) - 1:
            list2.append(j)
list2 = list(set(list2))
list2.sort()
print(list2)'''









'''n = 8
half = n//2
for i in range(n):
    count = 1
    flag = False
    for j in range(n+1):
        if i <= half:
            if j >= half - i and j <= half + i:
                if j <= half:
                    print(" ",count, end="")
                    count = count + 1
                elif j >= half:
                    if flag == False:
                        count = count - 1
                        flag = True
                    count = count - 1
                    print(" ",count, end="")
            else:
                print("   ", end="")
    print()
'''




'''n = 4
count = 1
for i in range(n):
    for j in range(i+1):
        print(count,end="")
        count = count + 1
    print()'''



'''n = 6
half = n//2
count = 1
for i in range(n+1):
    for j in range(n+1):
        if i <= half:
            if j >= half - i and j <= half + i:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j >= count and j <= (n - count):
                print("*",end="")
            else:
                print(" ",end="")
            if j == n:
                count = count + 1

    print()
'''




'''n = 6
count = 0
for i in range(n):
    for j in range(n):
        if j >= count:
            print("*",end="")
        else:
            print(" ",end="")
    count = count + 1
    print()'''


'''n = 6
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()'''





'''n = 6
for i in range(n):
    for j in range(0,i+1):
        print("*",end="")
    print()'''










'''n = 6
half = n // 2
count = 0
for i in range(n):
    for j in range(n):
        if j >= (half - count) and j <= half + count:
            print("*",end="")
        else:
            print(" ",end="")
    count = count + 1
    print()'''








'''n = 6
count = 0
for i in range(n):
    for j in range(n+count):
        if i <= n / 2:
            if n - i - 1 <= j:
                print("*", end="")
            else:
                print(" ", end="")
    count = count + 1
    print()'''








'''n = 6
for i in range(n):
    for j in range(n):
        if j >= (n - i - 1):
            print("* ",end="")
        else:
            print(" ",end="")
    print()'''










'''str1 = "ABCDE"
for i in range(len(str1)):
    for j in range(0,i+1):
        print(str1[j],end="")
    print()'''









'''a = 4
b = 6
ranng1 = (a * b + 1)
i = 1
while i < ranng1:
    if i % a == 0 and i % b == 0:
        print(i)
    i = i + 1'''








'''a = 12
b = 15
count = max(a,b)
max1 = count
min1 = min(a,b)
while count < (a * b + 1):
    if count % min1 == 0:
        print(count)
    count = count + max1'''
'''a = 4
b = 6
for i in range(1,(a*b+1)):
    if i % a == 0 and i % b == 0:
        print(i)
'''







'''paths = [["B","C"],["D","B"],["C","A"]]
hash1 = {}
first = False
for i in range(len(paths)):
    if paths[i][0] not in hash1:
        hash1[paths[i][0]] = 1
    else:
        hash1[paths[i][0]] = hash1[paths[i][0]] + 1
for j in range(len(paths)):
    if paths[j][1] not in hash1:
        hash1[paths[j][1]] = 1
    else:
        hash1[paths[j][1]] = hash1[paths[j][1]] + 1
print(hash1)
for key, valiue in hash1.items():
    if valiue == 1 and first == False:
        first = True
    elif first == True and valiue == 1:
        print(key)'''















'''candies = [12,1,12]
extraCandies = 10
max1 = max(candies)
list1 = []
for i in range(len(candies)):
    samp = candies[i] + extraCandies
    if samp >= max1:
        list1.append(True)
    else:
        list1.append(False)
print(list1)
'''






'''k = 7
n = 17
answers = [
        [
            1,
            3,
            5,
            7,
            9,
            33,
            99,
            313,
            585,
            717,
            7447,
            9009,
            15351,
            32223,
            39993,
            53235,
            53835,
            73737,
            585585,
            1758571,
            1934391,
            1979791,
            3129213,
            5071705,
            5259525,
            5841485,
            13500531,
            719848917,
            910373019,
            939474939,
        ],
        [
            1,
            2,
            4,
            8,
            121,
            151,
            212,
            242,
            484,
            656,
            757,
            29092,
            48884,
            74647,
            75457,
            76267,
            92929,
            93739,
            848848,
            1521251,
            2985892,
            4022204,
            4219124,
            4251524,
            4287824,
            5737375,
            7875787,
            7949497,
            27711772,
            83155138,
        ],
        [
            1,
            2,
            3,
            5,
            55,
            373,
            393,
            666,
            787,
            939,
            7997,
            53235,
            55255,
            55655,
            57675,
            506605,
            1801081,
            2215122,
            3826283,
            3866683,
            5051505,
            5226225,
            5259525,
            5297925,
            5614165,
            5679765,
            53822835,
            623010326,
            954656459,
            51717171715,
        ],
        [
            1,
            2,
            3,
            4,
            6,
            88,
            252,
            282,
            626,
            676,
            1221,
            15751,
            18881,
            10088001,
            10400401,
            27711772,
            30322303,
            47633674,
            65977956,
            808656808,
            831333138,
            831868138,
            836131638,
            836181638,
            2512882152,
            2596886952,
            2893553982,
            6761551676,
            12114741121,
            12185058121,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            7,
            55,
            111,
            141,
            191,
            343,
            434,
            777,
            868,
            1441,
            7667,
            7777,
            22022,
            39893,
            74647,
            168861,
            808808,
            909909,
            1867681,
            3097903,
            4232324,
            4265624,
            4298924,
            4516154,
            4565654,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            8,
            121,
            171,
            242,
            292,
            16561,
            65656,
            2137312,
            4602064,
            6597956,
            6958596,
            9470749,
            61255216,
            230474032,
            466828664,
            485494584,
            638828836,
            657494756,
            858474858,
            25699499652,
            40130703104,
            45862226854,
            61454945416,
            64454545446,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            9,
            121,
            292,
            333,
            373,
            414,
            585,
            3663,
            8778,
            13131,
            13331,
            26462,
            26662,
            30103,
            30303,
            207702,
            628826,
            660066,
            1496941,
            1935391,
            1970791,
            4198914,
            55366355,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            191,
            282,
            373,
            464,
            555,
            646,
            656,
            6886,
            25752,
            27472,
            42324,
            50605,
            626626,
            1540451,
            1713171,
            1721271,
            1828281,
            1877781,
            1885881,
            2401042,
            2434342,
            2442442,
        ],
    ]
range1 = len(answers[k-2]) - ((len(answers[k - 2]))-n)
sum1 = 0
for i in range(range1):
    sum1 = sum1 + answers[k - 2][i]
print(sum1)'''


















'''k = 2
n = 5
flag = True
count = 0
count4 = 1
sum1 = 0
while flag:
    str1 = str(count4)
    str2 = ""                 #imporrtant----------------
    for i in str1:
        str2 = i + str2
    if str2 == str1:
        quentient = int(count4)
        str5 = ""
        while quentient != 0:
            remainder = quentient % k
            quentient = quentient // k
            str5 = str5 + str(remainder)
        str6 = ""
        for item in str5:
            str6 = item + str6
        if str6 == str5:
            count = count + 1
            sum1 = sum1 + count4
    count4 = count4 + 1
    if count == n:
        break
print(sum1)
'''




'''qutient = 121
str1 = ""
while qutient != 0:
    remainder = qutient % 7
    qutient = qutient // 7
    str1 = str1 + str(remainder)
print(str1)
'''
'''a = list(map(int,input("enter a number").split(" ")))
print(a)'''



'''n = 30
i = 0
p1 = 1
p2 = 1
while i < n:
    if i < 2:
        print(i)
        i = i + 1
    else:
        if i == 2:
            print(i)
        res = p1 + p2
        p1 = p2
        p2 = res
        print(res)
        i = i + 1'''
# s = "a"






'''n = 121
str1 = ""
while n:
    rem1 = n % 3
    str1 = str1 + str(rem1)
    n = n // 10
print(str1)'''







'''n = 45
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)'''








'''nums = [1,-2,-3]
start = 1
hold = start
i = 0
while i < len(nums):
    start = start + nums[i]
    if start < 1:
        start = hold
        start = start + 1
        hold = start
        i = 0
    else:
        i = i + 1
print(hold)
'''






'''words = ["leetcoder","leetcode","od","hamlet","am"]
list1 = []
for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            pass
        else:
            if len(words[i]) >= len(words[j]):
                if (words[j] in words[i]) and words[j] not in list1 :
                    list1.append(words[j])
print(list1)'''















'''s = "abcdefghij"
k = 3
fill = "x"
count = 0
str1 = ""
list1 = []
for i in range(len(s)):
    if count == k:
        list1.append(str1)
        count = 0
        str1 = ""
        str1 = str1 + s[i]
        count = count + 1
    else:
        str1 = str1 + s[i]
        count = count + 1
if len(str1) == k:
    list1.append(str1)
else:
    range1 = k - len(str1)
    for j in range(range1):
        str1 = str1 + fill
    list1.append(str1)
print(list1)'''

















'''nums = [7,4,2,8,1,7,7,10]
nums.sort()
list1 = []
sum1 = sum(nums)
sum2 = 0
for i in range(len(nums)):
    sum1 = sum1 - nums[i]
    sum2 = sum2 + nums[i]
    if sum1 > sum2:
        pass
    else:
        list1.append(nums[i])
list1.reverse()
print(list1)'''












'''arr = [2,2,3,4]
max1 = 0
flag = False
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1
    if arr[i] == count and max1 < count:
        max1 = count
        flag = True
print(max1)
'''













'''str1 = "aaabaaa"
k = 2
hash1 = {}
for item in str1:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] = hash1[item] + 1

key1 = list(hash1.keys())
count = 0
print(hash1)
for i in range(len(key1)-1):
    if abs(hash1[key1[i]] - hash1[key1[i+1]]) <= k:
        pass
    else:
        check1 = abs(hash1[key1[i]] - hash1[key1[i + 1]])
        check2 = check1 - k
        if hash1[key1[i]] > hash1[key1[i+1]]:
            hash1[key1[i]] = hash1[key1[i]] - check2
        else:
            hash1[key1[i+1]] = hash1[key1[i+1]] - check2
        count = count + check2

key2 = list(hash1.keys())
for l in range(len(key2)-1):
    a,b = key2[l],key2[l+1]
    if hash1[a] > hash1[b] and count > hash1[b]:
        print(hash1[b])# return
    elif hash1[b] > hash1[a] and count > hash1[a]:
        print(hash1[a])
    else:
        print(count)
print(count)
print(hash1)'''
















'''nums = [4,2,4,3,2]
index = [0,0,1,3,1]
hash1 = {}
for i in range(len(index)):
    if index[i] not in hash1:
        hash1[index[i]] = [nums[i]]
    else:
        hash1[index[i]].append(nums[i])
print(hash1)
target1 = []
for key ,values in hash1.items():
    for j in range(len(values) - 1,-1,-1):
        target1.append(values[j])
print(target1)
'''





















# # grading system
# math = int(input("enter number of math"))
# phy = int(input("enter number of phy"))
# chem = int(input("enter number of chem"))
# total = (math + phy + chem) / 3
# if total < 95:
#     if total < 70:
#         if total < 45:
#             if total < 33:
#                 print("Fail")
#             else:
#                 print("pass with boundry")
#         else:
#             print("c Grade")
#     else:
#         print("B Grade")
# else:
#     print("A Grade")













# # leap year
#
# year = int(input("enter a number"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("Not leap year")
















# # the numbber positibve nragtive
# a = int(input("enter a number"))
# if a > 0 :
#     print("positive")
# elif a == 0:
#     print("zero")
# else:
#     print("negative")













'''arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
count = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        diff = abs(arr1[i] - arr2[j])
        if diff > d:
            pass
        else:
            break
    else:
        count = count + 1
print(count)
'''













'''height = float(input("enter height in meter"))
weight = float(input())
bmi = weight / (height * height)
if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 24.9:
    print("Healthy")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("obesity")'''




'''amount = int(input())
bill = 0
if amount >= 5000:
    div = (amount * 20)/100
    amount = amount - div

print(amount)'''








'''reading = int(input())
amount = 0
if reading <= 100:
    pass
elif 100 < reading <= 200:
    reading = reading - 100
    reading = reading  * 5
    amount = amount + reading
elif 200 < reading:
    reading = reading - 100
    amount = 100 * 5
    reading = reading - 100
    reading = reading * 10
    amount = amount + reading

print(amount)'''







'''angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
if (angle1 + angle2 + angle3) == 180:
    print("Valid Traingle")
else:
    print("invaid traingle")
'''



'''arr = [17,8,19,4,6,1]
# arr1 = arr.copy()
# arr1.sort(reverse=True)
# max1 = arr1[0]
list1 = []
i = 1
while i < len(arr):
    max1 = arr[i]
    index1 = i
    for j in range(i,len(arr)):
        if max1 < arr[j]:
            max1 = arr[j]
            index1 = j
    # print(max1)
    for k in range(i, index1+1):
        list1.append(max1)
        i = i + 1
list1.append(-1)
print(list1)'''











'''arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
hash1 = {}
for item in arr:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
value1 = 0
key1 = 0
for key, value in hash1.items():
    if value1 < value:
        value1 = value
        key1 = key
print(key1)'''


















'''moves = [[0,1],[2,0],[1,0],[2,1],[0,2],[2,2]]
diagnoal1 = {(0,2) : 0,(1,1) : 0, (2,0) : 0}
diagnoal2 = {(2,2) : 0,(1,1) : 0, (0,0) : 0}
diagonal_A_Minus = 0
diagnoal_A_pos = 0
diagnoal_B_Minus = 0
diagnoal_B_pos = 0
x_A = [0] * 3
y_A = [0] * 3
x_B = [0] * 3
y_B = [0] * 3
for i in range(len(moves)):
    a, b = moves[i]
    if i % 2 == 0:
        if tuple(moves[i]) in diagnoal1:
            diagonal_A_Minus = diagonal_A_Minus + 1
        if tuple(moves[i]) in diagnoal2:
            diagnoal_A_pos = diagnoal_A_pos + 1
        if diagnoal_A_pos == 3 or diagonal_A_Minus == 3:
            print("A")
            break
        x_A[a] = x_A[a] + 1
        if x_A[a] == 3:
            print("A")
        y_A[b] = y_A[b] + 1
        if y_A[b] == 3:
            print("A")
    else:
        if tuple(moves[i]) in diagnoal1:
            diagnoal_B_Minus = diagnoal_B_Minus + 1
        if tuple(moves[i]) in diagnoal2:
            diagnoal_B_pos = diagnoal_B_pos + 1
        if diagnoal_B_pos == 3 or diagnoal_B_Minus == 3:
            print("B")
            break
        x_B[a] = x_B[a] + 1
        if x_B[a] == 3:
            print("B")
        y_B[b] = y_B[b] + 1
        if y_B[b] == 3:
            print("B")
if len(moves) == 9:
    print("Draw")
else:
    print("Pending")'''






# for i in range(0,len(moves)):
#     if i % 2 == 0:
#         A.append(moves[i])
#     else:
#         B.append(moves[i])
# A.sort()
# B.sort()
# A = str(A)
# B = str(B)
# if diagnoal1 in A:
#     print("A")
# elif diagnoal2 in A:
#     print("A")











'''from collections import Counter
list1 = [1,1,1,1,1,2,3,4,2,2,4,44,]
a = Counter(list1)
list1 = set(list1)
list1 = list(list1)
for i in range(len(list1)):
    print(a[list1[i]],end=" ")'''






'''n = 37
m = 48
matrix = []
indices = [[40,5]]
for i in range(m):
    list1 = []
    for j in range(n):
        list1.append(0)
    matrix.append(list1)
for i in range(len(indices)):
    for j in range(n + m):
        if j == indices[i][1]:
            for k in range(m):   #row
                matrix[k][j] = matrix[k][j] + 1
        if j == indices[i][0]:
            for k in range(n):
                matrix[j][k] = matrix[j][k] + 1

print(matrix)
odd_count = 0
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 != 0:
            odd_count = odd_count + 1
print(odd_count)
print(count)'''







'''from collections import deque
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
length = len(grid[0])
k = 4
list1 = deque()
for i in range(len(grid)):
    list1 = list1 + deque(grid[i])
print(list1)
l = 0
for i in range(k):
    add = list1[-1]
    list1.appendleft(add)
    list1.pop()
matrix = []
list2 = []
for i in range(len(list1)):
    if len(list2) == length:
        matrix.append(list2)
        list2 = []
    list2.append(list1[i])
if len(list2) == length:
    matrix.append(list2)
print(matrix)'''




















'''from collections import deque
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 23
list1 = []
for i in range(len(grid)-1,-1,-1):
    for j in range(len(grid[i])):
        list1.append(grid[i][j])
# lenght1 = len(grid)
# lenght2 = len(grid[0])
# matrix = []
# list2 = []
# count = 1
# i = 0
# flag = True
# while flag:
#     # print(list1)
#     if len(list2) == lenght2:
#         print(list2)
#         matrix.appendleft(list(list2))
#         list2 = []
#         list2.
#         list1.popleft()
#     else:
#         list2.appendleft(list1[i])
#         list1.popleft()
#     if list1 != deque():
#         list1 = list3
#         matrix = deque()
#     if count == k:
#         flag = False
#         # matrix.append(list2)
#         break
#     count = count + 1'''











'''from collections import deque
grid = [[-353,853,839,122,-337],[819,356,116,0,791],[-516,-502,-681,-427,-314],[-386,-400,597,740,836],[129,598,40,-875,-968],[495,-604,79,414,-104],[237,121,211,4,677],[-712,351,-947,-203,361]]
k = 7
# if k > len(grid):
#     k = k % len(grid)
list1 = deque()
list3 = list1.copy()
for i in range(len(grid)-1,-1,-1):
    for j in range(len(grid[i]) - 1, -1, -1):
        list1.append(grid[i][j])
lenght1 = len(grid)
lenght2 = len(grid[0])
count = 1
matrix = deque()
list2 = deque()
i = 0
flag = True
while i < len(list1):
    # print(list1)
    if len(list2) == lenght2:
        matrix.appendleft(list(list2))
        list2 = deque()
        list2.appendleft(list1[i])
        list1.popleft()
    else:
        list2.appendleft(list1[i])
        list1.popleft()
    if count == k:
        # matrix.append(list2)
        break
    count = count + 1
if len(list2) == lenght2:
    matrix.appendleft(list(list2))
    list2 = []
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
    if len(list2) == lenght2:
        matrix.append(list(list2))
        list2 = []
print(list(matrix))'''









'''n = 37
m = 48
matrix = []
indices = [[40,5]]
for i in range(m):
    list1 = []
    for j in range(n):
        list1.append(0)
    matrix.append(list1)
for r1, c1 in indices:
    for i in range(n):
        matrix[r1][i] += 1
    for j in range(m):
        matrix[j][c1] += 1
odd = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 != 0:
            odd += 1
print(odd)'''














'''m = 2
n = 3
indices = [[0,1],[1,1]]
matrix = []
for i in range(m):
    list1 = []
    for j in range(n):
        list1.append(0)
    matrix.append(list1)
count = 0
i = 0
while i < m:
    for j in range(n):
        if i == indices[count][0]:
            matrix[i][j] = matrix[i][j] + 1
        if j == indices[count][1]:
            matrix[i][j] = matrix[i][j] + 1
    if count != len(indices) - 1:
        i = 0
    else:
        count = count + 1
        i = i + 1


    print(matrix)
'''




















'''m = 2
n = 3
indices = [[0,1],[1,1]]
matrix = []
for i in range(m):
    list1 = []
    for j in range(n):
        list1.append(0)
    matrix.append(list1)
row = []
coloumn = []
for item in indices:
    row.append(item[0])
    coloumn.append(item[1])
row.sort()
coloumn.sort()
for i in range(len(row)):
    for j in range(m):
        if j == row[i]:
            for k in range(n):
                matrix[j][k] = matrix[j][k] + 1
                print(matrix)
k = 0
for i in range(m):
    for l in range(m):
        for h in range(m):
            if h == coloumn[k]:
                matrix[i][l] = matrix[i][l] + 1
            print(matrix)
    k = k + 1

# print(matrix)'''



























'''class Splution:
    gender = "female"
    def item1(self,p1, p2, p3):
        x1, y1 = p1 
        x2, y2 = p2
        x3, y3 = p3
        # return x1,y1,x2,y2,x3,y3
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    def checkstraightline(self,arr):
        if len(arr) == 2:
            return True
        for i in range(len(arr) - 2):
            p1 = arr[i]
            p2 = arr[i + 1]
            p3 = arr[i + 2]
            area = self.item1(p1, p2, p3)
            if (area) == 0:
                pass
            else:
                return False
        return "haa bhai ho gya kaam"
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    @classmethod
    def  print_gender(cls):
        print(cls.gender)
class Child(Splution):
    def __init__(self, name, gender, section, age):
        super().__init__(name,gender)
        self.section = section
         self.age = age
    def print_age(self):
        print(self.age)

arr =  [[2,4],[2,5],[2,8]]
a = Splution("sawan","male")
b = Child(a.name,a.gender,"A3","45")
b.print_age()
print(b.name)
print(a.checkstraightline(arr))'''























'''coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
for item in range(0,len(coordinates)-2):
    # area = 0.5 * abs(coordinates[item][0] * (coordinates[item + 1][1] - coordinates[item + 2][1]) + coordinates[item+1][0] * (coordinates[item + 2][1] - coordinates[item][1]) + coordinates[item + 2][0] * (coordinates[item][1] - coordinates[item + 1][1]))
    area = 0.5 * abs(
        coordinates[item][0] * (coordinates[item + 1][1] - coordinates[item + 2][1]) +
        coordinates[item + 1][0] * (coordinates[item + 2][1] - coordinates[item][1]) +
        coordinates[item + 2][0] * (coordinates[item][1] - coordinates[item + 1][1])
    )
    print(area)'''















# position = [2,2,2,3,3]
# even = 0
# odd = 0
# for item in position:
#     if item % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(min(even,odd))













'''arr = [1,2,2,1,1,3]
hash1 = {}
for i in range(len(arr)):
    if arr[i] not in hash1:
        hash1[arr[i]] = 1
    else:
        hash1[arr[i]] = hash1[arr[i]] + 1
list1 = list(hash1.values())
set1 = set(list1)
if len(set1) == len(list1):
    print(True)
else:
    print(False)'''













'''distance = [7,10,1,12,11,14,5,0]
sum1 = sum(distance)
print(sum1)
start = 7
destination = 2
check1 = 0
flag = False
if start > destination:
    # flag = True
    for i in range(start-1,destination-1,-1):
        check1 = check1 + distance[i]
elif start <= destination:
    for i in range(start,destination):
        check1 = check1 + distance[i]
if flag:
    check2 = abs(sum1 - check1 - distance[destination])
else:
    check2 = abs(sum1 - check1)
if check1 <= check2:
    print(check1)
else:
    print(check2)'''





'''distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 2
i = start + 1
check1 = 0
if i == len(distance):
    i = 0
while i != start:
    if i == len(distance):
        i = 0
        if i == start:
            break
        else:
            check1 = check1 + distance[i]
        # i = i + 1
    else:
        check1 = check1 + distance[i]
        i = i + 1
j = start - 1
check2 = 0
if j == -1:
    j = len(distance) - 1
while j != start:
    if j == -1:
        j = len(distance) - 1
        check2 = check2 + distance[j]
    else:
        check2 = check2 + distance[j]
        j = j - 1

print(check1,check2)'''








# distance = [1,2,3,4]
'''start = 0
destination = 1
i = start + 1
j = len(distance) - (len(distance) - (start - 1))
print(j)
list4 = []
check1 = 0
check2 = 0
if i == len(distance):
    i = 0
# while i != destination or j != destination:
#     print(i,j)
#     # if j == 0:
#     #     break
#     if i != destination:
#         i = i + 1
#     if j != destination:
#         j = j - 1'''









'''distance = [1,2,3,4]
distance.insert(0,0)
list1 = distance
start = 0
destination = 1
check1 = 0
check2 = 0
list4 = []
i = start + 1
j = len(list1) - 1
while i < len(list1) or j > start:
    check1 = check1 + list1[i]
    check2 = check2 + list1[j]
    if list1[i] == destination:
        list4.append(check1)
    if list1[j] - 1 == destination:
        list4.append(check2)
    i = i + 1
    j = j - 1
print(min(list4))'''









'''arr = [3,8,-10,23,19,-4,-14,27]
arr.sort() #[1,2,3,4]
list1 = []
diff = abs(arr[0] - arr[1])
for i in range(len(arr)-1):
    diff1 = abs(arr[i] - arr[i+1])
    if diff > diff1:
        diff = diff1
        list1 = [[arr[i],arr[i+1]]]
    elif diff == diff1:
        list1 = list1 + [[arr[i],arr[i+1]]]
print(list1)'''










'''distance = [1,2,3,4]
list1 = []
start = 0
destination = 3
hash1 = {}
for i in range(0,distance[-1]):
    hash1[distance[i]] = i'''












'''distance = [1,2,3,4], #[0,1,2,3]
start = 0
destination = 3
check1 = 0
check2 = 0
i = start
j = start - 1
while check1 != destination or check2 != destination:
    check1 = check1 + distance[i]
    check2 = check2 + distance[j]
    if distance[i] == destination and check1 <= check2:
        print(check1,check1)
        break
    elif distance[j] == destination and check1 >= check2:
        print(check2)
        break
    i = i + 1
    j = j - 1
    print(check1,check2)'''















'''dominoes = [[1,2],[2,1],[2,1],[1,2],[3,3],[3,3]]
hash1 = {}
for item1 in dominoes:
    item1.sort()
    item = tuple(item1)
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] = hash1[item] + 1
count = 0
for value in hash1.values():
    if value > 1:
        n = value
        d = (n * (n - 1))/2
        count = count + d
print(int(count))'''









'''arr1 = [4,0,0,7,6,3,7,5]
arr2 = [7]
hash1 = {k:0 for k in arr2}
list1 = []
list2 = []
for item in arr1:
    if item not in hash1:
        list2.append(item)
    else:
        hash1[item] = hash1[item] + 1
for item2 in arr2:
    for j in range(hash1[item2]):
        list1.append(item2)
    hash1[item2] = 0
list2.sort()
list3 = list1 + list2
print(list3)'''











'''arr = [9,9,9,9,4,8,0,0,0,0,3,7,2,0,0,0,0,0,0,0,0,9,1,0,0,0,0,1,1,0,0,5,6,3,1,6,0,0,0,0,2,3,4,7,0,0,3,9,3,6,5,8,9,1,1,3,2,0,0,0,0,7,3,3,0,0,5,7,0,0,8,1,9,6,3,0,0,8,8,8,8]
count_zero = 0
i = 0
while i  < len(arr)- count_zero:
    if arr[i] == 0 and i != len(arr) - 1:
        count_zero = count_zero + 1
    i = i + 1
j = (len(arr)-1) - count_zero
k = len(arr) - 1
while j > -1:
    if arr[j] == 0 and j > 0 and count_zero != 0:
        arr[k] = 0
        arr[k-1] = 0
        k = k - 2
    else:
        arr[k] = arr[j]
        k = k - 1
    j = j - 1
if len(arr) == 81:
    arr.pop(0)
    arr.append(0)
print(arr)'''




'''arr = [1,0,2,3,0,4,5,0]
i = 0
while i < len(arr):
    if arr[i] == 0:
        arr = arr[:i+1] + arr[i:]
        arr.pop()
        i = i + 2
    else:
        i = i + 1
print(arr)


def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr = arr[:i + 1] + arr[i:]
            arr.pop()
            i = i + 2
        else:
            i = i + 1
    return arr
arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(arr))'''






'''arr = [8,4,5,0,0,0,0,7]
i = 0
list1 = []
list2 = []
flag = False
while i < len(arr):
    if arr[i] == 0:
        flag = True
        if list2 != []:
            list1 = list1 + list2
            list2 = []
        list1.append(arr[i])
        list1.append(arr[i])
        # list2.append(arr[i])
        arr.pop()
    elif flag == False:
        list1.append(arr[i])
    elif flag == True and arr[i] != 0:
        list2.append(arr[i])
    i = i + 1
list1 = list1 + list2

print(list1)
'''














'''heights = [1,2,3,4,5]
expected = heights.copy()
expected.sort()
count = 0
for i in range(len(heights)):
    if expected[i] != heights[i]:
        count = count + 1
print(count)'''
'''heights = [10,7,0,2,1]
for i in range(len(heights)-1):
    for j in range(i+1,len(heights)):
        if heights[i] > heights[j]:
            heights[i],heights[j] = heights[j],heights[i]
print(heights)'''














'''stones = [8, 7, 1]
stones.sort()
list1 = []
for i in range(len(stones)):
    # print(stones)
    if len(stones) > 1:
        if stones[-1] == stones[-2]:
            stones.pop()
            stones.pop()
        else:
            res = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            stones.append(res)
            stones.sort()
if stones == []:
    print(0)
else:
    print(stones[0])
'''
















'''points =  [[0,0],[1,1],[1,1]]
i = 0
list1 = []
area = 0.5 * abs((points[i][0] * (points[i+1][1] - points[i][1])) + (points[i+1][0] * (points[i+2][1] - points[i+1][1])) + (points[i+2][0] * (points[i][1] - points[i+1][1])))
print(area)
if area == 0:
    print(False)
else:
    print(True)

'''





'''points =  [[73,31],[73,19],[73,45]]
list1 = []
for item in points:
    list1.append(tuple(item))
set1 = set(list1)
if len(set1) != 3:
    print(False)
for i in range(len(points) - 2):
    X1 = (points[i+1][0] - points[i][0])
    X2 = (points[i+2][0] - points[i+1][0])
    print(X1,X2)
    if X1 == X2 and X1 == 0:
        print(False)
        break
    elif X1 == 0 or X2 == 0:
        print(True)
        break
    slope1 = ((points[i+1][1] - points[i][1]) / (points[i+1][0] - points[i][0]))
    slope2 = ((points[i+2][1] - points[i+1][1]) / (points[i+2][0] - points[i+1][0]))
    print(slope1,slope2)
    if slope1 == slope2:
        print(False)
        break
else:
    print(True)'''











'''words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
hash2 = {}
for k in range(len(chars)):
    if chars[k] not in hash2:
        hash2[chars[k]] = 1
    else:
        hash2[chars[k]] = hash2[chars[k]] + 1

hash1 = hash2.copy()
lengh1 = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in hash1 and hash1[words[i][j]] != 0:
            hash1[words[i][j]] = hash1[words[i][j]] - 1
        else:
            break
    else:
        lengh1 = lengh1 + len(words[i])
    hash1 = hash2.copy()


print(lengh1)'''














'''rows = 2
cols = 2
rCenter = 0
cCenter = 1
matrix = [[0] * cols]*rows
list2 = []
dist = []
hash1 = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        list2 = list2 + [[i,j]]
        dist += [abs(rCenter - i) + abs(cCenter - j)]
for k in range(len(dist)):
    if dist[k] not in hash1:
        hash1[dist[k]] = list2[k]
    else:
        hash1[dist[k]].append(list2[k][0])
        hash1[dist[k]].append(list2[k][1])
dist.sort()
set1 = set()
list6 = []
for item in dist:
    if len(hash1[item]) > 2 and item not in set1:
        set1.add(item)
        list7 = []
        for l in hash1[item]:
            list7.append(l)
            if len(list7) == 2:
                list6.append(list7)
                list7 = []
    elif len(hash1[item]) == 2:
        list6.append(hash1[item])
print(list6)'''





















'''nums = [0,1,1]
str1 = ""
list1 = []
for i in nums:
    str1 = str1 + str(i)
    int1 = int(str1, 2)
    divisible = int1 / 5
    print(divisible)
    if float(divisible) == 0:
        list1.append(True)
    else:
        list1.append(False)
print(list1)'''



'''def prefixesDivBy5(nums):
    str1 = ""
    list1 = []
    for i in nums:
        str1 = str1 + str(i)
        int1 = int(str1, 2)
        divisible = int1 / 5
        if divisible == 0:
            list1.append(True)
        else:
            list1.append(False)
    return list1


nums = [0,1,1]
print(prefixesDivBy5(nums))'''


















'''arr = [10,-10,10,-10,10,-10,10,-10]
sum1 = int(sum(arr) / 3)
sum2 = arr[0]
count = 0
flag = False
for i in range(1,len(arr)):
    if sum1 == sum2 and count < 2:
        # print(i)
        sum2 = 0
        count = count + 1
        sum2 = sum2 + arr[i]
    elif count >= 2 and sum1 == sum2 and i != len(arr) - 1:
        print(i)
        sum2 = sum2 + arr[i]
    else:
        sum2 = sum2 + arr[i]
if sum2 == sum1 and flag == False:
    count = count + 1
if count == 3:
    print(True)
else:
    print(False)
print(count)'''








'''from collections import deque
arr = [1,1,1]
partion = (len(arr))//3
start_list = deque(arr[:partion])
mid_list = deque(arr[partion:(len(arr))-partion])
end_list = deque(arr[(len(arr)) - partion:len(arr)])
sum1 = sum(start_list)
sum2 = sum(mid_list)
sum3 = sum(end_list)
for i in range(len(arr)):
    if sum1 == sum3 and sum2 != sum1:
        print(False)
        break
    elif sum1 > sum2 > sum3:
        sum3 = sum3 + mid_list[-1]
        mid_list.pop()
        sum2 = sum2 + start_list[-1]
        start_list.pop()
    elif sum1 > sum2 == sum3:
        sum2 = sum2 + start_list[-1]
        start_list.pop()
    elif sum1 == sum2 > sum3:
        sum3 = sum3 + sum2'''















'''nums = [-28,-19,-13,5,-12,-27,0,29,-2,-6]
k1 = 2
nums.sort()
list1 = []
list2 = []
for i in range(len(nums)):
    if nums[i] < 0:
        list1.append(nums[i])
    else:
        list2.append(nums[i])
list1.sort()
# print(list1)
list3 = []
if 0 in list1:
    list3.append(0)
    for p in range(len(list1)):
        if list1[p] == 0:
            pass
        else:
            list3.append(list1[p])
else:
    list3 = list1
range1 = 0
if list3 != []:
    for k in range(k1):
        if k == k1 - 1:
            range1 = k + 1
        if k >= len(list3):
            range1 = k
            break
            # if list3[0] >= 0:
            #     list3[0] = -list3[0]
            # else:
            #     list3[0] = abs(list3[0])
        else:
            list3[k] = abs(list3[k])
    list5 = list3 + list2
    list5.sort()
    for r in range(range1, k1):
        if list5[0] >= 0:
            list5[0] = -list5[0]
        else:
            list5[0] = abs(list5[0])
else:
    for l in range(k1):
        list2[0] = -list2[0]
    list5 = list3 + list2
print(sum(list5))'''


















'''words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
hash1 = {}
for i in range(len(words[0])):
    if words[0][i] not in hash1:
        hash1[words[0][i]] = 1
    else:
        hash1[words[0][i]] = hash1[words[0][i]] + 1
for j in range(1,len(words)):
    hash2 = {}
    for k in range(len(words[j])):
        if words[j][k] not in hash2:
            hash2[words[j][k]] = 1
        else:
            hash2[words[j][k]] = hash2[words[j][k]] + 1
    for key, value in hash1.items():
        if key not in hash2:
            hash1[key] = 0
        elif value == 0:
            pass
        else:
            if hash2[key] == value:
                pass
            elif hash2[key] > value:
                pass
            elif hash2[key] < value:
                hash1[key] = hash2[key]
list1  = []
for key, value in hash1.items():
    if value == 0:
        pass
    else:
        for i in range(value):
            list1.append(key)
print(list1)
'''













'''arr = [1,3,2,6,9,3,1,5]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
print(arr)
'''


















'''
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
count_pawn = 0
index_i_rook = 0
index_j_rook = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "R":
            index_i_rook = i
            index_j_rook = j
            break
flag = False
count = 0
for k in range(len(board)):
    if board[k][index_j_rook] == "p":
        count = 1
    elif board[k][index_j_rook] == "B":
        if flag == False:
            count = 0
        elif flag == True:
            count_pawn = count_pawn + count
            count = 0
            break
    elif board[k][index_j_rook] == "R":
        flag = True
        count_pawn = count_pawn + count
        count = 0
count_pawn = count_pawn + count
count2 = 0
flag2 = False
for l in range(len(board[index_i_rook])):
    if board[index_i_rook][l] == "p":
        count2 = 1
    elif board[index_i_rook][l] == "B":
        if flag2 == False:
            count2 = 0
        elif flag2 == True:
            count_pawn = count_pawn + count2
            count2 = 0
            break
    elif board[index_i_rook][l] == "R":
        count_pawn = count_pawn + count2
        count2 = 0
        flag2 = True
count_pawn = count_pawn + count2
print(count_pawn)'''





















'''n = 4
trust = [[1,3],[1,4],[2,3]]
list1 = [i for i in range(1,n+1)]
list1 = set(list1)
for item in trust:
    if item[0] not in list1:
        pass
    else:
        list1.remove(item[0])
flag = 0
list1 = list(list1)
print(list1)
if list1 == []:
    print(-1)
for item in trust:
    if item[1] == list1[0]:
        flag = flag + 1
if len(trust) == 1:
    flag = flag + 1
if list1 != [] and flag >= 2:
    print(list1[-1])
else:
    print(-1)'''











'''trust = [[1,3],2,3]
list1 = []
for item in trust:
    if type(item) == list:
        print(item)
    else:
        print(item)'''



'''str1 = "5356789"
list1 = list(str1),int
a = list1'''









'''nums = [0,2,3,4,5]
min_no_index = len(nums) - 1
for item in range(len(nums)):
    if abs(nums[item]) < abs(nums[min_no_index]):
        min_no_index = item
i = min_no_index
j = min_no_index + 1
print(min_no_index)
list1 = []
count = 0
while count < len(nums):
    if abs(nums[i]) < nums[j]:
        square1 = nums[i] ** 2
        list1.append(square1)
        i = i - 1
    elif abs(nums[i]) > nums[j]:
        square2 = nums[j] ** 2
        list1.append(square2)
        j = j + 1
    count = count + 1
if j < len(nums):
    while j < len(nums):
        square2 = nums[j] ** 2
        list1.append(square2)
        j = j + 1
else:
    while i > - 1:
        square1 = nums[i] ** 2
        list1.append(square1)
        i = i - 1
print(list1)'''










'''nums = [3,2,3,4]
nums.sort()
result = 0
for i in range(len(nums) - 2):
    a = nums[i]
    b = nums[i+1]
    c = nums[i+2]
    if a + b > c and b + c > a and a + c > b:
        if result < a + b + c:
            result =  a + b + c
        print(result)
        # return
    print(result)
'''









'''nums = [1,2]
empty_arr = [0] * len(nums)
for i in range(len(nums)):
    empty_arr[nums[i] - 1] = empty_arr[nums[i] - 1] + 1
n = len(nums)/2
for item in range(len(empty_arr)):
    if empty_arr[item] == n:
        print(item + 1)
        break
'''
















'''words = ["kruw","ha","q"]
order = "zgxlkthsjuoqcpavbfdermiywn"
hash1 = {}
for i in range(len(order)):
    hash1[order[i]] = i
word = words[0]
for item in words:
    if len(item) > len(word):
        word = item
k = 0
flag = False
set1 = set()
while k < len(word):
    j = 0
    while j < len(words)-1:
        if k >= len(words[j+1]) or k >= len(words[j]):
            pass
        else:
            if j + 1 not in set1:
                if hash1[words[j][k]] < hash1[words[j+1][k]]:
                    if j + 1 == len(words) - 1:
                        set1.add(j+1)
                        set1.add(j)
                    else:
                        set1.add(j)
                elif hash1[words[j][k]] == hash1[words[j+1][k]]:
                    if len(words[j+1]) - 1 == k:
                        if len(words[j]) > len(words[j+1]):
                            flag = True
                    # print(hash1[words[j][k]])
                else:
                    # print(words[j][k],words[j+1][k])
                    print(words[j][k])
                    flag = True
                    # print(hash1[words[j][k]])
        j = j + 1
    if flag:
        print(False)
        break
    k = k + 1
else:
    print(True)

print(set1)'''














'''arr = [0,2,4,5,1,4,6]
target = 1
hash1 = {}
for i in range(len(arr)):
    diff = target - arr[i]
    if arr[i] not in hash1:
        hash1[diff] = arr[i]
    else:
        print(arr[i] , hash1[arr[i]])

        break'''







'''strs = ["rrjk","furt","guzm"]
list1 = []
for i in range(len(strs[0])):
    str1 = ""
    for j in range(len(strs)):
        str1 = str1 + strs[j][i]
    list1.append(str1)
count = 0
for i in range(len(list1)):
    for j in range(1,len(list1[i])):
        if list1[i][j-1] <= list1[i][j]:
            pass
        else:
            count = count + 1
            break
print(list1)
print(count)'''




























'''def max_removed_queries(nums, queries):
    n = len(nums)
    m = len(queries)

    # Step 1: count how many queries cover each index
    coverage = [0] * n
    for l, r in queries:
        for i in range(l, r + 1):
            coverage[i] += 1

    # Step 2: check if it's even possible
    for i in range(n):
        if coverage[i] < nums[i]:
            return -1

    # Step 3: Try all combinations of removing queries using backtracking or bitmasking — but that's too slow.

    # Instead, use greedy strategy:
    # Prioritize queries that cover the most "needed" positions
    needed = nums[:]
    used = [False] * m

    # Apply queries that help the most first — sort queries by number of needed positions they help
    def contribution(q):
        l, r = q
        return sum(1 for i in range(l, r+1) if needed[i] > 0)

    queries_with_index = list(enumerate(queries))
    queries_with_index.sort(key=lambda x: -contribution(x[1]))

    used_queries = []

    for idx, (l, r) in queries_with_index:
        useful = False
        for i in range(l, r + 1):
            if needed[i] > 0:
                useful = True
        if useful:
            used_queries.append(idx)
            for i in range(l, r + 1):
                if needed[i] > 0:
                    needed[i] -= 1

    if any(needed[i] > 0 for i in range(n)):
        return -1

    return m - len(used_queries)

nums = [0,0,1,1,0]
queries = [[3,4],[0,2],[2,3]]
print(max_removed_queries(nums, queries))  # ✅ Output: 4'''




# def max_removed_queries(nums, queries):
#     n = len(nums)
#     m = len(queries)
#
#     # Step 1: count how many queries cover each index
#     coverage = [0] * n
#     for l, r in queries:
#         for i in range(l, r + 1):
#             coverage[i] += 1
#
#     # Step 2: check if it's even possible
#     for i in range(n):
#         if coverage[i] < nums[i]:
#             return -1
#
#     # Step 3: Try to remove queries greedily
#     # Sort queries by their contribution
#     used = [0] * n
#     queries_used = []
#
#     for idx, (l, r) in enumerate(queries):
#         need = False
#         for i in range(l, r + 1):
#             if used[i] < nums[i]:
#                 need = True
#         if need:
#             queries_used.append((l, r))
#             for i in range(l, r + 1):
#                 if used[i] < nums[i]:
#                     used[i] += 1
#
#     # Final check: did we cover all nums?
#     for i in range(n):
#         if used[i] < nums[i]:
#             return -1
#
#     return len(queries) - len(queries_used)
#
# nums = [1, 2]
# queries = [[1,1],[0,0],[1,1],[1,1],[0,1],[0,0]]
# print(max_removed_queries(nums, queries))  # Output: 4





'''
nums = [1,2]
sample = [0] * len(nums)
first_no_index = None
last_no_index = None
for k in range(len(nums)):
    if nums[k] > 0:
        if first_no_index is None:
            first_no_index = k
        last_no_index = k
queries = [[1,1],[0,0],[1,1],[1,1],[0,1],[0,0]]
queries.sort(key=lambda q: min(abs(q[0] - first_no_index), abs(q[1] - last_no_index)))
print(queries)
count = 0
for i in range(len(queries)):
    range1 = queries[i][0]
    range2 = queries[i][1]

    if sum(nums[range1:range2 + 1]) == 0:
        continue  # Already depleted
    else:
        count += 1

    for j in range(range1, range2 + 1):
        if nums[j] > 0:
            nums[j] -= 1

    if nums == sample:
        print(len(queries) - count)
        break
else:
    print(-1)'''




















'''arr = [2,1,2,3,5,7,9,10,12,14,15,16,18,14,13]
if len(arr) < 3:
    print(False)
else:
    mountain = 0
    flag = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            print(False)
            break
        if arr[i] == arr[i+1]:
            print(False)
            break
        elif arr[i] < arr[i+1] and flag == False:
            flag = True
            mountain = mountain + 1
        elif arr[i] > arr[i+1] and flag == True:
            flag = False
            mountain = mountain + 1
    if (mountain == 2 and flag == False):
        print(True)
    else:
        print(False)'''





















'''emails = ["fg.r.u.uzj+w.y+b@kziczvh.com","hdhg"]
list1 = []
for i in range(len(emails)):
    a_found = False
    plus_found = False
    str1 = ""
    first = False
    for j in range(len(emails[i])):
        if emails[i][j] == "@":
            str1 = str1 + emails[i][j]
            a_found = True
        elif emails[i][j] == "+" and first == False:
            first = True
            plus_found = True
        elif a_found:
            str1 = str1 + emails[i][j]
        elif emails[i][j] == "." and a_found == False:
            pass
        elif plus_found == False:
            str1 = str1 + emails[i][j]
        elif plus_found == True and emails[i][j] == "+":
            pass
            # str1 = str1 + emails[i][j]
            # plus_found = False
        elif plus_found == True:
            pass
    print(str1)
    list1.append(str1)
print(len(list1))'''















'''list1 = [2,3,4,8]
list1.sort()
list2 = []
diff = 0
first = False
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        list3 = []
        abs_diff = abs(list1[i] - list1[j])
        if first == False:
            first = True
            diff = abs_diff
            list3.append(list1[i])
            list3.append(list1[j])
            list2.append(list3)
            list3 = []
        elif diff > abs_diff:
            list2 = []
            list3.append(list1[i])
            list3.append(list1[j])
            diff = abs_diff
            list2.append(list3)
            list3 = []
        elif diff == abs_diff:
            list3.append(list1[i])
            list3.append(list1[j])
            list2.append(list3)
            list3 = []
print(list2)'''




'''nums = [4,1,1,0,1,0]
i = 0
j = 1
while i < len(nums) and j < len(nums):
    if nums[i] % 2 == 0:
        i = i + 2
    elif nums[j] % 2 == 1:
        j = j + 2
    else:
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 2
        j = j + 2
print(nums)'''















'''deck = [1,1,1,1,2,2,2,2,2,2]
# hash1 = {"0":423,"1":2130,"2":1377,"3":2880,"4":93,"5":633,"6":516,"7":708,"8":201,"9":108,"10":138,"11":189,"12":288,"13":126,"14":27,"15":48,"16":42,"17":39,"18":24}
hash1 = {}
if len(deck) == 1:
    print(False)
for i in range(len(deck)):
    if deck[i] not in hash1:
        hash1[deck[i]] = 1
    else:
        hash1[deck[i]] = hash1[deck[i]] + 1
min1 = min(hash1.values())
for item in hash1.values():
    if min1 == 1:
        if min1 == item:
            pass
        else:
            print(False)
            break
    if item % min1 == 0 and min1 != 1:
        pass
    elif min1 != 1:
        j = 2
        while j <= min1:
            if item % j == 0 and min1 % j == 0:
                min1 = j
                break
            j = j + 1
        else:
            print(False)
            break
else:
    print(True)'''









'''deck = [1,2,3,4,4,3,2,1]
deck.sort()
check1 = 0
count = 0
for i in range(len(deck)):
    if i == 0:
        check1 = deck[i]
    if deck[i] == check1:
        count = count + 1
    else:
        break
count2 = 0
for i in range(len(deck)):
    if count == count2'''





'''nums = [1]
k = 0
min1 = min(nums)
max1 = max(nums)
max1 = max1 - k
min1 = min1 + k
diff = max1 - min1
if diff < 0:
    print(0)
else:
    print(diff)'''









'''nums = [0,10]
k = 2
list1 = []
for i in range(len(nums)):
    list2 = []
    min1 = 0
    flag = False
    check = 0
    for j in range(-k,k+1):
        list2.append(nums[i] + j)
        if nums[i] + j < 0:
            flag = True
    if flag == True:
        diff = max(list2) - min1
        list1.append(diff)
        check = list2[-1]
    else:
        if check < list2[0] and check != 0:
            diff = list2[0]
            list1.append(diff)
            check = list2[-1]
        else:
            diff = max(list2) - min(list2)
            list1.append(diff)
            check = list2[-1]
print(list1)'''







'''aliceSizes = [2]
bobSizes = [1,3]
alice_set = set(aliceSizes)
bob_set = set(bobSizes)
diff = (max(aliceSizes) - max(bobSizes))
half_diff = diff//2
for a in alice_set:
    if a - half_diff in bob_set:
        print(a,a - half_diff)
        break'''







'''nums = [1,1,0]
flag_increase = False
flag_decrease = False
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        pass
    if nums[i] < nums[i+1] and flag_increase == False and flag_decrease == False:
        flag_increase = True
    if nums[i] > nums[i + 1] and flag_decrease == False and flag_increase == False:
        flag_decrease = True
    if flag_increase == True and nums[i] > nums[i+1]:
        print(False)
        break
    if flag_decrease == True and nums[i] < nums[i + 1]:
        print(False)
        break
else:
    print(True)'''










'''aliceSizes = [2]
bobSizes = [1,3]
sum_alice = 0
sum_bob = 0
for i in range(len(aliceSizes)):
    sum_alice = sum_alice + aliceSizes[i]
    sum_bob = sum_bob + bobSizes[i]
list1 = []
len1 = len(aliceSizes)
flag_alice = False
flag_bob = False
if sum_alice > sum_bob:
    len1 = len(aliceSizes)
    flag_alice = True
elif sum_alice < sum_bob:
    flag_bob = True
    len1 = len(bobSizes)
for i in range(len1):'''











'''words = ["ddc","bb","cbe","ceedcd","edca","cbb","cec","ee","aeedda","abbac","dcae","dacec","be","acdc","eceeba","aabed","aee","bbb","bc","dcbbe","aa","bdebd","adaca","ba","de","eab","adced","ae","dcbd","ad","caddbd","ea","ceba","eda","eeea","adbadd","deeaea","deb","abdc","dac"]
groups = [32,21,6,10,35,37,2,4,21,13,21,33,4,10,2,30,20,2,20,23,32,38,36,5,32,30,3,36,13,40,8,5,13,33,21,25,26,26,7,16]
list1 = []
for i in range(len(words)):
    list2 = []
    hamming = 0
    j = i + 1
    flag = False
    while j < len(words):
        if groups[i] != groups[j]:
            if len(words[i]) == len(words[j]):
                flag = True
                break
        j = j + 1
    if flag:
        flag = False
        for k in range(len(words[i])):
            if words[i][k] == words[j][k]:
                pass
            elif words[i][k] != words[j][k]:
                hamming = hamming + 1
        if hamming == 1:
            if list1 != [] and list1[len(list1)-1] == words[i]:
                list1.append(words[j])
            else:
                list1.append(words[i])
                list1.append(words[j])

print(list1)'''




















'''grid = [[1,0],[5,4]]
ans = 0
for i in range(len(grid)):
    max_row = 0
    max_col = 0
    for j in range(len(grid[i])):
        if grid[i][j]:
            print(j)
            ans = ans + 1
        if max_row < grid[i][j]:
            max_row = grid[i][j]
        if max_col < grid[j][i]:
             max_col = grid[j][i]
        # print(ans)
    ans = ans + max_row + max_col
print(ans)'''













'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
list1 = []
for i in range(len(matrix[0])):
    list2 = []
    for j in range(len(matrix)):
        list2.append(matrix[j][i])
    list1.append(list2)

print(list1)'''








'''bills = [5,5,10,10,20]
mydict = {5:0,10:0,20:0}
for i in range(len(bills)):
    if bills[i] == 5:
        mydict[bills[i]] = mydict[bills[i]] + 1
    elif bills[i] == 10:
        if mydict[5] !=  0:
            mydict[5] = mydict[5] - 1
            mydict[bills[i]] = mydict[bills[i]] + 1
        else:
            print(False)
            break
    elif bills[i] == 20:
        if mydict[10] == 0 and mydict[5] < 3:
            print(False)
            break
        elif mydict[10] > 0 and mydict[5] > 0:
            mydict[10] = mydict[10] - 1
            mydict[5] = mydict[5] - 1
        elif mydict[10] == 0 and mydict[5] >= 3:
            mydict[5] = mydict[5] - 3
        else:
            print(False)
            break
        mydict[bills[i]] = mydict[bills[i]] + 1
else:
    print(True)'''
















'''image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
list1 = []
for i in range(len(image)):
    list2 = []
    for j in range(len(image[i])-1,-1,-1):
        list2.append(image[i][j])
    list1.append(list2)
    for k in range(len(image[i])-1,-1,-1):
        if list1[i][k] == 0:
            list1[i][k] = 1
        elif list1[i][k] == 1:
            list1[i][k] = 0
print(list1)'''











'''points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
x_axis = points[0][0]
y_axis = points[0][1]
for i in range(1,len(points)):
    if x_axis < points[i][0]:
        x_axis = points[i][0]
    if y_axis < points[i][1]:
        y_axis = points[i][1]
'''



















'''nums = [2,5]
target = 5
start = 0
mid = (start + len(nums))//2
for i in range(len(nums)):
    if nums[mid] > target:
        end = mid
        mid = (start + end)//2
    elif nums[mid] < target:
        start = mid
        mid = (start + len(nums))//2
    else:
        print(mid)
else:
    print(-1)'''










'''matrix = [[1,2],[2,1]]
for i in range(1,len(matrix)):
    sample2 = matrix[i][1:]
    sample = matrix[i-1][:len(matrix[0])-1]
    print(sample)
    if sample == sample2:
        sample = sample2
    else:
        # print(sample,sample2)
        print(False)
        break
else:
    print(True)'''



























'''nums =[0,0,0,1]
list1 = nums.copy()
nums.sort()
if nums[-2] * 2 <= nums[-1]:
    print(list1.index(nums[-1]))
else:
    print(-1)'''






'''letters = ["x","x","y","y"]
target = "z"
start = 0
end = len(letters) - 1
mid = (start + (len(letters) - 1))//2
for i in range(len(letters)):
    if letters[mid] <= target:
        if mid+1 == len(letters)-1 and letters[mid+1] > target:
            print(letters[mid+1])
            break
        start = mid
        mid = (start + end)//2
    elif letters[mid] > target:
        if mid - 1 == 0 and letters[mid - 1] > target:
            print(letters[mid - 1])
            break
        elif letters[mid-1] > target:
            end = mid
            mid = (start + end)//2
        else:
            print(letters[mid])
            break
else:
    print(letters[0])'''


















'''# 724. Find Pivot Index
nums = [1,7,3,6,5,6]
sumleft = 0
sumright = sum(nums[1:])
for i in range(len(nums)):
    if i == 0:
        pass
    else:
        sumleft = sumleft + nums[i - 1]
        sumright = sumright - nums[i]
    if sumleft == sumright:
        print(i)
        break'''







'''nums = [-1,-1,0,0,-1,-1]
i = 0
j = len(nums) - 1
sum_right = 0
sum_left = 0
flag = True
if nums[0] > 0 and nums[-1] > 0:
    sum_right = 0
    sum_left = 0
elif nums[0] < 0 and nums[-1] < 0:
    if nums[0] < nums[-1]:
        flag = True
        sum_left = nums[0]
    elif nums[0] > nums[-1]:
        flag = True
        sum_right = nums[-1]
    elif nums[0] == nums[-1]:
        sum_right = nums[-1]
        sum_left = nums[0]
elif nums[0] < 0:
    flag = True
    sum_left = nums[0]
elif nums[-1] < 0:
    flag = True
    sum_right = nums[-1]
while i < j:
    if sum_right < sum_left or (sum_right == sum_left):
        if flag == True:
            sum_right = sum_right + nums[j-1]
            j = j - 2
            flag = False
        else:
            sum_right = sum_right + nums[j]
            j = j - 1
    elif sum_right > sum_left or (sum_right == sum_left):
        if flag == True:
            sum_left = sum_left + nums[i + 1]
            i = i + 2
            flag = False
        else:
            sum_left = sum_left + nums[i]
            i = i + 1
    print(sum_right,sum_left,i,j)'''

'''bits = [1,0,0,1]
list1 = []
str1 = ""
for i in range(len(bits)):
    if bits[i] == 1:
        str1 = str1 + str(bits[i])
    elif bits[i] == 0:
        str1 = str1 + str(bits[i])
        if str1 == "0":
            list1.append(str1)
            str1 = ""
    if len(str1) == 2:
        list1.append(str1)
        str1 = ""
if str1 != "":
    list1.append(str1)
if list1[-1] == "0":
    print(True)
else:
    print(False)
print(list1)'''

'''nums = [1,2,2,3,1,4,2]
mydict = {}
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
maxi = max(mydict.values())
count_maxi = 0
for item in set(nums):
    if mydict[item] >= maxi:
        count_maxi = count_maxi + 1
if count_maxi > 1:
    list1 = nums
    maincount = 0
    for i in range(len(nums)):
        count = 0
        list2 = []
        if maxi > 1:
            for j in range(i, len(nums)):
                if nums[j] == nums[i]:
                    count = count + 1
                if count == maxi and maincount <= count and len(list1) > len(list2):
                    maincount = count
                    list2.append(nums[j])
                    list1 = list2
                    list2 = []
                    count = 0
                else:
                    list2.append(nums[j])
        else:
            list1 = []
            list1.append(nums[i])
else:
    list1 = []
    count = 0
    flag = False
    for i in range(len(nums)):
        if mydict[nums[i]] == maxi:
            count = count + 1
            flag = True
        if count == maxi:
            list1.append(nums[i])
            print(list1)
            break
        if flag == True:
            list1.append(nums[i])
print(list1)
'''

'''nums = [1]
mydict = {}
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
maxi = max(mydict.values())
list1 = nums
maincount = 0
for i in range(len(nums)):
    count = 0
    list2 = []
    if maxi > 1:
        for j in range(i, len(nums)):
            if nums[j] == nums[i]:
                count = count + 1
            if count == maxi and maincount <= count and len(list1) > len(list2):
                maincount = count
                list2.append(nums[j])
                list1 = list2
                list2 = []
                count = 0
            else:
                list2.append(nums[j])
    else:
        list1 = []
        list1.append(nums[i])
print(list1)'''

'''img = [[4, 4, 5, 6, 7],
       [6, 7, 8, 9, 9],
       [9, 9, 10, 11, 12]]

rows = len(img)
cols = len(img[0])
list1 = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        sum1 = 0
        count = 0
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if 0 <= k < rows and 0 <= l < cols:
                    sum1 += img[k][l]
                    count += 1
        list1[i][j] = sum1 // count  # average based on actual neighbors
print(list1)
for row in list1:
    print(row)'''

'''img = [[4,4,5,6,7],[6,7,8,9,9],[9,9,10,11,12]]
list1 = []
for i in range(len(img)):
    list2 = []
    for j in range(len(img[i])):
        list2.append(0)
    list1.append(list2)
for i in range(len(img)):
    for j in range(len(img[i])):
        if (i > 0 and i < len(img) - 1 and j > 0 and j < len(img[i]) - 1):
            sum1 = 0
            for k in range(i-1,i+2):
                for l in range(j - 1,j + 2):
                    sum1 = sum1 + img[k][l]
            sum1 = sum1 // 9
            list1[i][j] = sum1
        elif i == 0 and 0 < j < len(img[i]) - 1:
            sum1 = 0
            sum2 = 0
            for k in range(i, i+2):
                for l in range(j-1, j+2):
                    if i == 0 and 0 < j < len(img[i]) - 1:
                        if k < len(img[i]) - 1 and j < len(img[i]) - 1:
                            sum1 = sum1 + img[k][l]
                        if k < len(img) - 1 and j < len(img) - 1:
                            sum2 = sum2 + img[l][k]
            if j < len(img[i]) - 1:
                list1[i][j] = sum1 // 6
            if j < len(img) - 1:
                list1[j][i] = sum2 // 6
        elif j == len(img[i]) - 1 and 0 < i < len(img) - 1:
            sum1 = 0
            sum2 = 0
            for k in range(i-1,j+1):
                for l in range(i-1,j+1):
            #         sum1 = sum1 + img[k][l]
            #         sum2 = sum2 + img[l][k]
            # list1[i][j] = sum1//6
            # list1[j][i] = sum2//6
        elif i == 0 and j == 0:
            sum1 = 0
            sum1 = sum1 + img[i][j]+ img[i][j+1] + img[i+1][j] + img[i+1][j+1]
            list1[i][j] = sum1 // 4
        elif i == 0 and j == len(img[i]) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i-1][j-1] + img[i+1][j-1] + img[i+1][j]
            list1[i][j] = sum1 // 4
        elif j == 0 and i == len(img) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1]
            list1[i][j] = sum1 // 4
        elif j == len(img[i]) - 1 and i == len(img) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1]
            list1[i][j] = sum1 // 4
print(list1)'''

'''img = [[ 1, 2], [ 6, 7], [11, 12]]
list1 = []
for i in range(len(img)):
    list2 = []
    for j in range(len(img[i])):
        list2.append(0)
    list1.append(list2)
for i in range(len(img)):
    for j in range(len(img)):
        if (i > 0 and i < len(img) - 1 and j > 0 and j < len(img[i]) - 1):
            sum1 = 0
            for k in range(i-1,i+2):
                for l in range(j - 1,j + 2):
                    sum1 = sum1 + img[k][l]
            sum1 = sum1 // 9
            list1[i][j] = sum1
        elif i == 0 and 0 < j < len(img[i]) - 1:
            sum1 = 0
            sum2 = 0
            for k in range(i, i+2):
                for l in range(j-1, j+2):
                    if i == 0 and 0 < j < len(img[i]) - 1:
                        if k < len(img[i]) - 1 and j < len(img[i]) - 1:
                            sum1 = sum1 + img[k][l]
                        if k < len(img) - 1 and j < len(img) - 1:
                            sum2 = sum2 + img[l][k]
            if j < len(img[i]) - 1:
                list1[i][j] = sum1 // 6
            if j < len(img) - 1:
                list1[j][i] = sum2 // 6
        elif j == len(img[i]) - 1 and 0 < i < len(img) - 1:
            sum1 = 0
            sum2 = 0
            for k in range(j-1,j+1):
                for l in range(j-2,j+1):
                    pass
                    sum1 = sum1 + img[k][l]
                    sum2 = sum2 + img[l][k]
            list1[i][j] = sum1//6
            list1[j][i] = sum2//6
        elif i == 0 and j == 0:
            sum1 = 0
            sum1 = sum1 + img[i][j]+ img[i][j+1] + img[i+1][j] + img[i+1][j+1]
            list1[i][j] = sum1 // 4
        elif i == 0 and j == len(img[i]) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i-1][j-1] + img[i+1][j-1] + img[i+1][j]
            list1[i][j] = sum1 // 4
        elif j == 0 and i == len(img) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1]
            list1[i][j] = sum1 // 4
        elif j == len(img[i]) - 1 and i == len(img) - 1:
            sum1 = 0
            sum1 = sum1 + img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1]
            list1[i][j] = sum1 // 4
print(list1)
'''

# img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
# list1 = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
#
# for i in range(len(img)):
#     for j in range(len(img[i])):
#         if (i > 0 and i < len(img) - 1 and j > 0 and j < len(img[i]) - 1):
#             sum1 = 0
#             for k in range(i - 1, i + 2):
#                 for l in range(j - 1, j + 2):  # Corrected this line
#                     sum1 += img[k][l]
#             list1[i][j] = sum1 // 9
#
# print(list1)


# elif j == 0 and 0 < i < len(img) - 1:
#     # print(k,l)
#     sum1 = sum1 + img[j][k]
#     sum1 = 0


'''img = [[100,200,100],[200,50,200],[100,200,100]]
for i in range(len(img)):
    sum1 = 0
    if i > 0 and i < len(img)-1:
        for j in range(i - 1, i + 2):
            for k in range(i - 1, i + 2):
                sum1 = sum1 + img[j][k]
        sum1 = sum1/9
        img[i][i] = sum1
print(img)'''

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

'''nums = [12,14,8,13,5,7]
add = 0
count = 0
i = 0
count = 0
while len(nums) != 1:
    j = 0
    k = 1
    while j < len(nums) and k < len(nums):
        total = nums[j] + nums[k]
        nums[j] = total
        if k == len(nums) - 1:
            nums.remove(nums[k])
        j = j + 1
        k = k + 1
    if len(nums) == 1:
        pass
    else:
        count = count + 1
print(count)'''

'''nums = [1,4,7,8,11,9,12,3]
target = 45
mydict = {}
for i in range(len(nums)):
    if nums[i] in mydict:
        print(nums[i],mydict[nums[i]])
    else:
        diff = target - nums[i]
        mydict[diff] = nums[i]
'''

'''img = [[1,1,1],[1,0,1],[1,1,1]]
add = 0
for i in range(len(img)):
    for j in range(len(img[i])):
        if i > 0 and i < len(img) - 1:
            if j == 0:
                add = img[i-1][j] + img[i][j] + img[i+1][j] + img[i-1][j+1] + img[i][j+1] + img[i+1][j+1]
                img[i][j] = add//6
            elif j > 0 and j < len(img[i]) - 1:
                add = img[i-1][j] + img[i+1][j] + img[i][j] + img[i-1][j-1] + img[i][j-1] + img[i+1][j-1] + img[i-1][j+1] + img[i][j+1] + img[i+1][j+1]
                img[i][j] = add//9
            elif j == len(img[i]) - 1:
                add = img[i-1][j-1] + img[i-1][j] + img[i][j] + img[i][j - 1] + img[i+1][j] + img[i+1][j -1]
                img[i][j] = add//6
print(img)
'''

'''nums = [1,2,2,4]
nums.sort()
list2 = []
range1 = nums[len(nums) - 1]-len(nums)
range2 = nums[len(nums)-1]+1
if range1 < 0:
    range1 = 0
    range2 = range2 + 1
mydict = {}
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
        list2.append(nums[i])
for i in range(range1+1, range2):
    if i not in mydict:
        list2.append(i)
print(list2)
'''

'''nums = [1,2,2,4]
list1 = []
mydict = {}
big_element = 0
for i in range(len(nums)):
    if nums[i] > big_element:
        big_element = nums[i]
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
        list1.append(nums[i])
list2 = mydict.keys()
print(list2)'''

# print(start)
# print(end)


'''list1 = [1,2,3,4]
righ = 2
list2 = []
b = len(list1) - righ
while b < len(list1):
    list2.append(list1[b])
    b = b + 1
for i in range(0,len(list1) - righ):
    list2.append(list1[i])
print(list2)
'''

'''n = 22
b = str(bin(n))
str1 = ""
for i in range(2,len(b)):
    str1 = str1 + b[i]
print(str1)
for i in range(len(str1)):
    for j in range(0, i+1):
        print(str1[j],end="")
    print()'''

'''str1 = "abc123xyz456"
str2 = ""
list1 = []
for i in range(len(str1)):
    if str1[i].isdigit():
        str2 = str2 + str1[i]
    elif str1[i].islower() and str2 != "":
        list1.append(int(str2))
        str2 = ""
    if i == len(str1) - 1 and str2 != "":
        list1.append(int(str2))
print(list1)'''

'''num = "3[a2[c]]"
i = 0
check = ""
str1 = ""
str2 = ""
integer = 0
while i < len(num):
    if num[i].isdigit():
        integer = int(num[i])
    elif num[i] == "[":
        check = check + num[i]
    elif check == "[" and num[i] != "]":
        str1 = str1 + num[i]
    else:
        check = check + num[i]
    while integer > 0 and check == "[]":
        str2 = str2 + str1
        integer = integer - 1
        if integer == 0:
            str1 = ""
            integer = 0
            check = ""
        #integer = integer - 1
    i = i + 1
print(str2)'''

'''nums = [4,0,4,3,3]
k = 5
current_sum = sum(nums[:k])
max_avearge = current_sum/k
for i in range(k, len(nums)):
    current_sum = current_sum + nums[i] - nums[i - k]
    max_avearge = max(max_avearge, current_sum/k)
print(max_avearge)'''

'''nums = [5]
k = 1
average = float("-inf")
list1 = []
for i in range(len(nums)):
    if i < k:
        list1.append(nums[i])
    elif i >= k:
        list1.append(nums[i])
        list1.pop(0)
    if len(list1) == k:
        print(list1)
        average1 = float(sum(list1)/k)
        if average1 > average:
            average = average1
print(average)'''

'''nums = [1,12,-5,-6,50,3]
k = 4
average = float("-inf")
for i in range(0,(len(nums) - k) + 1):
    average1 = ((sum(nums[i:k+i]))/k)
    if average1 > average:
        average = average1
print(average)



def hhd():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    average = 0
    for i in range(0, (len(nums) - k) + 1):
        average1 = ((sum(nums[i:k + i])) / k)
        if average1 > average:
            average = average1
    return average
print(hhd())'''

'''nums = [-3,-2,-1,0,0,0,0]
nums.sort()
product = 1
if len(nums) == 3:
    for i in nums:
        product = product * i
    print(product)
else:
    max1 = nums[len(nums) - 3:]
    min1 = nums[:2]
    product = product * min1[0] * min1[1]
    product2 = product
    i = 0
    flag = False
    while i < len(max1):
        current = product2
        current = current * max1[i]
        flag = True
        if current > product and flag == True:
            product = current
            current = product2
        else:
            current = product2
        i = i + 1
    product3 = 1
    for i in max1:
        product3 = product3 * i

    if product < product3:
        print(product3)
    else:
        print(product)'''

'''nums = [-1,-2,-3]
nums.sort() #[-100,-3,-2,1]
i = 0
j = len(nums)-1
count1 = 0
count = 0
product = 1
while count < 3 and nums[i]:
    if abs(nums[i]) > nums[j] and count1 < 2:
        product = product * nums[i]
        i = i + 1
        count1 = count1 + 1
    elif abs(nums[i]) < nums[j]:
        product = product * nums[j]
        j = j - 1
    elif abs(nums[i]) == nums[j] :
        if nums[j] > 0 and nums[i] < 0:
            product = product * nums[j]
            product = product * nums[i]
            # count = count + 2
        else:
            product = product * nums[j]
        i = i + 1
        j = j - 1
    count = count + 1
print(product)'''

'''nums = [-4,-3,-2,-1,60]
product = 1
nums.sort()
positive_list = []
negative_list = []
for i in range(len(nums)):
    if nums[i] < 0:
        negative_list.append(nums[i])
    else:
        positive_list.append(nums[i])
positive_list.sort(reverse=True)
flag = False
if len(positive_list) == 0:
    for j in range(3):
        product = product * negative_list[j]
elif len(negative_list) == 0:
    for j in range(3):
        product = product * positive_list[j]
elif len(nums) == 3:
    for i in range(len(nums)):
        product = product * nums[i]
else:
    print(positive_list)
    print(negative_list)
    i = 0
    j = 0
    count = 0
    count1 = 0
    if len(positive_list) == 1:
        product = product * positive_list[0]
        flag = True
    while count < 3:    # i < len(negative_list) and j < len(positive_list) and
        if abs(negative_list[i]) > positive_list[j] and count1 < 2:
            product = product * negative_list[i]
            i = i + 1
        elif abs(negative_list[i]) < positive_list[j] and flag == False:
            product = product * positive_list[j]
            j = j + 1
        elif abs(negative_list[i]) == positive_list[j]:
            product = product * positive_list[j]
            j = j + 1
            i = i + 1
        count = count + 1
print(product)'''

'''flowerbed = [1,0,0,0,0]
n = 2
i = 1
if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
    n = n - 1
if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
    flowerbed[0] = 1
    n = n - 1

while i < len(flowerbed) - 1:
    if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 and n > 0 and i == 1:
        flowerbed[i-1] = 1
        n = n - 1
    elif  flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 and n > 0:
        flowerbed[i] = 1
        n = n - 1
    elif i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i + 1] == 0 and n > 0:
        flowerbed[i + 1] = 1
        n = n - 1

    print(i)
    i = i + 1
if n <= 0:
    print("TRUE")
else:
    print("FALSE")
print(flowerbed)'''

'''n = 7
count = 0
for i in range(n):
    for j in range(n):
        if i < n//2+1:
            if j <= i or j >= (n - 1) - i:
                print(" *", end="")
            else:
                print("  ", end="")
        else:
            if i - 1 > j + count or i <= j:
                print(" *",end="")
            else:
                print("  ",end="")
    if i > n//2:
        count = count + 2
    print()'''

'''list1 =["vacag","KFC"]
list2 = ["fvo","xrljq","jrl","KFC"]
list3 = []
my_dict = {}
minimum = ((len(list1) - 1) + (len(list2) - 1))
for i in range(len(list1)):
    my_dict[list1[i]] = i
for j in range(len(list2)):
    if list2[j] in my_dict:
        if minimum > my_dict[list2[j]] + j:
            list3 = []
            list3.append(list2[j])
            minimum = my_dict[list2[j]] + j
        elif minimum == my_dict[list2[j]] + j:
            list3.append(list2[j])
print(list3)
'''

'''m = 3
n = 3
ops = []
min1 = ops[0][0]
min2 = ops[0][1]
for i in range(len(ops)):
    if min1 > ops[i][0]:
        min1 = ops[i][0]
    if min2 > ops[i][1]:
        min2 = ops[i][1]

print(min1 * min2)
'''

'''x1 = 2
v1 = 1
x2 = 1
v2 = 2
add = x1 + v1 + x2 + v2
match1 = x1
match2 = x2
match1_r = x1
match2_r = x2
if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):# or (v1 > x2) or (v2 > x2):
    print("No")
else:
    while match1 != match2:
        match1 = match1 + v1
        match2 = match2 + v2
        if match1 > match2 and match1_r < match2_r:
            print("NO")
            break
        elif match1 < match2 and match1_r > match2_r:
            print("No")
            break
        elif match1 == match2:
            print("YES")
            break
'''

'''def kangaroo(x1,v1,x2,v2):
    add = x1 + v1 + x2 + v2
    match1 = x1
    match2 = x2
    if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):  # or (v1 > x2) or (v2 > x2):
        return "No"
    else:
        if match1 < match2:
            while match1 != match2:
                match1 = match1 + v1
                match2 = match2 + v2
                if match1 > match2:
                    return " No"
                return "yes"
        elif match1 > match2:
            while match1 != match2:
                match1 = match1 + v1
                match2 = match2 + v2
                if match1 < match2:
                    return " No"
                return "yes"
print(kangaroo(x1,v1,x2,v2))'''

'''x1 = 63
v1 = 8
x2 = 94
v2 = 3
add = x1 + v1 + x2 + v2
match1 = x1
match2 = x2
match1_r = x1
match2_r = x2
if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):# or (v1 > x2) or (v2 > x2):
    print("No")
else:
    if match1_r < match2_r or match1_r > match2_r:
        while match1 != match2:
            match1 = match1 + v1
            match2 = match2 + v2
            if match1 > match2:
                print("NO")
                break
            if match1 == match2:
                print("Yes")
                break
    elif match1 > match2:
        while match1 != match2:
            match1 = match1 + v1
            match2 = match2 + v2
            if match1 < match2:
                print("NO")
                break
            if match1 == match2:
                print("yes")
                break
    else:
        print("YES")'''

'''n = 4
for i in range(n):
    for j in range(n+1):
        if i == n-1:
            print("* ",end="")
        else:
            if j < (n - i):
                print(" ", end="")
            else:
                print("* ", end="")
    print()
for i in range(n-1):
    for j in range(n):
        if i >= j:
            print(" ",end="")
        else:
            print(" *",end="")
    print()'''

'''m = 3
n = 3
ops =  [[2,2],[3,3]]
list2 = []
for i in range(n):
    list1 = []
    for j in range(m):
        list1.append(0)
    list2.append(list1)
print(list2)

j = 0
k = 0
count = 0
while j < len(ops):
    if k != len(ops[j]):
        if count != ops[j][k]:
            list2[k][count] = list2[k][count] + 1
            count = count + 1
        else:
            k = k + 1
            count = 0
    else:
        j = j + 1
        k = 0
mydict = {}
for i in range(len(list2)):
    for j in range(len(list2[i])):
        if list2[i][j] not in mydict:
            mydict[list2[i][j]] = 1
        else:
            mydict[list2[i][j]] = mydict[list2[i][j]] + 1

a = (max(mydict.keys()))
print(mydict[a])'''

'''    for j in range(len(ops[i])):
        print(0)
        if count < ops[i][j]:
            list2[i][j] = list2[i][j] + 1
            print(list2)
            count = count + 1'''

'''nums = [1,2,2,3,4,5,1,1,1,1]
mydict = {}
count2 = 0
count = 0
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
for num in nums:
    if num + 1 in mydict:
        count = mydict[num] + mydict[num + 1]
    if count2 < count:
        count2 = count
print(count2)'''

'''def yeil():
    for i in range(3):
        yield i

for j in range(3):
    result = yeil()
    print(next(result))'''

'''nums = [1,3,2,2,5,2,3,7]
mydict = {}
nums.sort()
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
nums = set(nums)
nums = list(nums)
count1 = 0
count2 = 0
flag = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            pass
        else:
            if abs(nums[i] - nums[j]) == 1 and flag == False:
                count1 = count1 + mydict[nums[j]]
                count1 = count1 + mydict[nums[i]]
                flag = True
            elif abs(nums[i] - nums[j]) == 1:
                count1 = count1 + mydict[nums[j]]
    print(count1)
    if count2 < count1:
        count2 = count1
    count1 = 0
    flag = False
#print(count2)'''

'''n = 22
str1 = str(n)
sum1 = 0
for i in range(len(str1)):
    for j in range(len(str1)):
        sum1 = sum1 + int(str1[j])
    if len(str(sum1)) == 1:
        print(sum1)
        break
    else:
        str1 = str(sum1)
        sum1 = 0'''

'''n = 600
str1 = str(n)
sum1 = 0
for i in range(len(str1)):
    j = 0
    while j < len(str1):
        sum1 = sum1 + int(str1[j])
        j = j + 1
    if len(str(sum1)) == 1:
        print(sum1)
        break
    else:
        str1 = str(sum1)
        sum1 = 0
        print(str1)'''

'''n = 50
for i in range(0,n+1,2):
    if i == n:
        print("the number is even")
        break
else:
    print("this number is odd")'''

'''nums = [1,2,2,3,4,5,1,1,1,1]
mydict = {}
for i in range(len(nums)):
    mydict[i] = i
    mydict[i] = nums[i]
j = 0
flag = False
list1 = []
list2 = []
k = j + 1
while j < len(nums)-1:
    if abs(nums[j] - mydict[k]) == 1 and flag == False:
        list1.append(nums[j])
        list1.append(mydict[k])
        flag = True
    elif abs(nums[j] - mydict[k]) == 1:
        list1.append(mydict[k])
    elif abs(nums[j] - mydict[k]) == 0:
        if abs(mydict[k] - mydict[k - 1]) == 1:
            list1.append(mydict[k])

    if k != len(nums) - 1:
        k = k + 1
    else:
        j = j + 1
        k = j + 1
        if len(list1) > len(list2):
            list2 = list1
        list1 = []
        flag = False

print(list2)'''

'''nums = [1,1,1,1]
list1 = []
list2 = []
flag = False
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if abs(nums[i] - nums[j]) == 1 and flag == False:
            list1.append(nums[i])
            list1.append(nums[j])
            flag = True
        elif abs(nums[i] - nums[j]) == 1:
            list1.append(nums[j])
            # print(nums[i],nums[j])
        elif abs(nums[i] - nums[j]) == 0:
            if abs(nums[j-1] - nums[j]) == 1:
                list1.append(nums[j])
    if len(list1) > len(list2):
        list2 = list1
    list1 = []
    flag = False

print(list2)'''

'''candytype = [1,1,2,3]
mydict = {}
half = len(candytype)/2
count = 0
for i in range(len(candytype)):
    if candytype[i] not in mydict and count < half:
        mydict[candytype[i]] = 1
        count = count + 1

print(len(mydict))'''

'''mat = [[1,2,3,4]]
r = 4
c = 2
count = 0
range1 = 0
list2 = []
list1 = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        count = count + 1
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if count == r * c:
            if range1 != c:
                list1.append(mat[i][j])
                range1 = range1 + 1
            if range1 == c:
                list2.append(list1)
                list1 = []
                range1 = 0
        else:
            print(mat)
            break
print(list2)
'''

'''def count_apple_oranges(s, t, a, b, apple, oranges):
    count_apple = 0
    count_oranges = 0
    for i in range(len(apple)):
        total = a + apple[i]
        if total >= s and total <= t:
            count_apple = count_apple + 1
    for j in range(len(oranges)):
        total = b + oranges[j]
        if total >= s and total <= t:
            count_oranges = count_oranges + 1

    return count_apple,count_oranges


s = 7
t = 10
a = 4
b = 12
apple = [2,3,-4]
oranges = [3,-2,-4]
print(count_apple_oranges(s,t,a,b,apple,oranges))'''

'''s = 4
t = 12
m = 7
n = 10
oranges = [3,-2,-4]
apple = [2,3,-4]
total_orange = 0
total_apple = 0
for i in range(len(apple)):
    total = s + apple[i]
    #print(total)
    if m <= total and total <= n:
        total_apple = total_apple + 1

for j in range(len(oranges)):
    total = t + oranges[j]
    print(total)
    if m <= total and total <= n:
        total_orange = total_orange + 1

print(total_orange)
print(total_apple)'''

'''mat = [[1,2,3,4]]
r = 1
c = 1
count = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
'''

'''arr = [1,4,4,3,6,7,10]
minimum = 0
maximum = 0
for i in range(len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i == j:
            pass
        else:
            sum = sum + arr[j]
    if sum > maximum:
        maximum = sum
    if i == 0:
        minimum = maximum
    if sum < minimum:
        minimum = sum
print(maximum,minimum)'''

'''arr = [6,2,6,5,1,2]
arr.sort() #1,2,2,5,6,6
sum1 = 0
i = 0
while i < len(arr):
    sum1 = sum1 + arr[i]
    i = i + 2
print(sum1)'''

'''arr = [6,2,6,5,1,2]
list1 = []
my_dict = {} # 1 2 3 4
i = 0
j = i + 1
list2 = []
while i < len(arr) and j < len(arr):
    list2.append(arr[i])
    list2.append(arr[j])
    list1.append(tuple(list2))
    list2 = []
    if j == len(arr) - 1:
        i = i + 1
        j = i + 1
    else:
        j = j + 1
i = 0
sum2 = 0
while i < len(list1) - (len(arr)/2):
    j = i
    sum1 = 0
    while j < len(arr)/2 + i:
        sum1 = sum1 + min(list1[j])
        print(list1[j])
        j = j + 1
    if sum2 < sum1:
        sum2 = sum1
    i = i + 1
print(sum2)
'''

# range1 = len(list1)-1
# sum1 = 0
# sum2 = 0
# i = 0
# while i < range1 and range1 < len(list1):
#     if i == 0:
#         sum1 = list1[i][0] + list1[range1][0]
#     if sum2 < sum1:
#         sum2 = sum1
#     sum1 = 0
#     i = i + 1
#     range1 = range1 + 1
# print(sum2)


'''arr = [5,4,3,2,1]
list1 = arr[:]
list1.sort(reverse=True)
mydict = {}
for i in range(len(list1)):
    if i == 0:
        mydict[list1[i]] = "Gold Medal"
    elif i == 1:
        mydict[list1[i]] = "Silver Medal"
    elif i == 2:
        mydict[list1[i]] = "Bronze Medal"
    else:
        mydict[list1[i]] = str(i + 1)
for j in range(len(arr)):
    arr[j] = mydict[arr[j]]
print(arr)'''

'''def findwords(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    list1 = []
    for word in words:
        set1 = set(word.lower())
        if set1.issubset(row1) or set1.issubset(row2) or set1.issubset(row3):
            list1.append(word)
    return list1
words = ["Hello","Alaska","Dad","Peace"]
print(findwords(words))'''

'''row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"
words = ["omk"]
list2 = []
for i in range(len(words)):
    list1 = []
    for j in range(len(words[i])):
        if words[i][j].isupper():
            d = words[i][j].lower()
            list1.append(d)
        else:
            list1.append(words[i][j])
    if list1[0] in row1:
        flag = True
        for k in range(len(list1)):
            if list1[k] in row1:
                pass
            else:
                flag = False
            if flag and k == len(list1) - 1:
                list2.append(words[i])
    elif list1[0] in row2:
        flag = True
        for k in range(len(list1)):
            if list1[k] in row2:
                pass
            else:
                flag = False
            if flag and k == len(list1) - 1:
                list2.append(words[i])
    elif list1[0] in row3:
        flag = True
        for k in range(len(list1)):
            if list1[k] in row3:
                pass
            else:
                flag = False
            if flag and k == len(list1) - 1:
                list2.append(words[i])

print(list2)'''

'''arr = [3,0,1,5]
max1 = 0
list1 = []
for i in range(len(arr)):
    if max1 < arr[i]:
        max1 = arr[i]
for i in range((max1 + 1)):
    if i not in arr:
        list1.append(i)
print(list1)'''

'''def nonrepeating(str1):
    count = 0
    for i in range(len(str1)):
        for j in range(len(str1)):
            if str1[i] == str1[j]:
                count = count + 1
        if count == 1:
            return str1[i]
        else:
            count = 0
    return

str1 = "zhhlww"
print(nonrepeating(str1))'''

'''arr = [1,2,3,4,5,6,7]
k = 3
lenght_array = len(arr)
list1 = []
range1 = lenght_array - k
while range1 < lenght_array:
    list1.append(arr[range1])
    range1 = range1 + 1
range1 = lenght_array - k
i = 0
while i < range1:
    list1.append(arr[i])
    i = i + 1
print(list1)'''

'''str1 = "aaabbccccdda"
str2 = ""
count = 0
i = 0
j = 0
while i < len(str1) and j < len(str1):
    if str1[i] == str1[j]:
        count = count + 1
        j = j + 1

    elif str1[i] != str1[j]:
        str2 = str2 + str(count) + str1[i]
        i = j
        count = 0
print(str2)
'''

'''for i in range(len(words)):
    if words[i][0].isupper():
        d = words[i].lower()
        words[i] = d
    '''

'''nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
list1 = []
mydict = {}
for i in range(len(nums1)):
    mydict[nums1[i]] = 1
for j in range(len(nums2)):
    if nums2[j] in mydict:
        range1 = j
        index = j
        while range1 < len(nums2):
            if nums2[index] < nums2[range1]:
                mydict[nums2[j]] = nums2[range1]
                range1 = len(nums2)
            elif range1 == len(nums2) - 1:
                mydict[nums2[j]] = -1
            range1 = range1 + 1
for values in mydict.values():
    list1.append(values)
print(list1)
'''

'''n = 6
store = 0
if n % 2 != 0:
    print("this number have not perfect")
else:
    for i in range(1,(n//2)+1):
        if n % i == 0:
            store = store + i
print(store)
'''

'''nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7] 
flag = False
list1 = []
index = 0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            index = j
            flag = True
        if index <= j:
            if nums2[index] < nums2[j] and flag == True:
                list1.append(nums2[j])
                flag = False
            elif j == len(nums2) - 1 and flag == True:
                list1.append(-1)
                flag = False
print(list1)
'''

'''nums1 = [4,1,2]
nums2 =  [1,3,4,2]
mydict = {}
for i in range(len(nums1)):
    if nums1[i] not in mydict:
        mydict[nums1[i]] = 1
for j in range(len(nums2)):
    if nums2[j] in mydict:
        if j == len(nums2)-1:
            mydict[nums2[j]] = -1
        elif nums2[j] < nums2[j+1]:
            mydict[nums2[j]] = nums2[j+1]
        else:
            mydict[nums2[j]] = -1
list1 = []
for value in mydict.values():
    list1.append(value)
print(list1)
'''

'''nums1 = [2,4]
nums2 = [1,2,3,4]
list1 = []
i = 0
j = 0
while i < len(nums1):
    if nums1[i] == nums2[j]:
        i = i + 1
        if j == len(nums2)-1:
            list1.append(-1)
            j = 0
        elif nums2[j] < nums2[j+1]:
            list1.append(nums2[j+1])
            j = 0
        else:
            list1.append(-1)
            j = 0
    else:
        j = j + 1
print(list1)'''

'''nums1 = [4,1,2]
nums2 = [1,3,4,2]
list1 = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            if j == len(nums2)-1:
                list1.append(-1)
            elif nums2[j] < nums2[j+1]:
                list1.append(nums2[j+1])
            else:
                list1.append(-1)
print(list1)'''

'''array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
list2 = []
for i in range(len(array)):
    list1 = []
    for j in range(len(array[i])):
        list1.append(array[j][i])
    list2.append(list1)
print(list2)'''

'''nums1 = [1,4]
duration = 0
count = duration
for i in range(1, len(nums1)):
    if nums1[i] > nums1[i-1] + duration - 1:
        count = count + duration
    else:
        count = count + nums1[i] - nums1[i-1]
print(count)
'''

'''nums1 = [1,2]
duration = 0
count = 0
list1 = []
mydict = {}
for i in range(len(nums1)):
    campare = nums1[i] + duration - 1
    list1.append(campare)                             # code ie right but time linit exceed----------------------
last = 0
for k in range(len(nums1)):
    count1 = 0
    store = nums1[k]
    while store <= list1[k]:
        if last < store:
            count1 = count1 + 1
        if store == list1[k]:
            last = store
        store = store + 1
    count = count + count1
print(count)'''

'''nums1 = [1,2]
duration = 3
count = 0
list1 = []
mydict = {}
for i in range(len(nums1)):
    campare = nums1[i] + duration - 1
    list1.append(campare)
# for j in range(len(list1)):
#     if nums1[j] not in mydict:
# 
#         value_store = list1[j] - nums1[j] + 1
#         if nums1[j] == value_store:
#             mydict[nums1[j]] = value_store - 1
#         if value_store not in mydict:
#             mydict[nums1[j]] = value_store
#         else:
#             mydict[nums1[j]] = value_store - 1


print(mydict)
print(list1)'''

'''nums1 = [1,4]
duration = 2
count = 0
count1 = 1
list1 = []
store = 0
for i in range(len(nums1)):
    campare1 = nums1[i] + duration - 1
    list1.append(campare1)
for j in range(len(nums1)):
    #count1 = 1
    store = store + nums1[j]
    if store != list1[j]:
        if list1[j - 1] == nums1[j]:
            count1 = count1 - 1
            count1 = count1 + 1
            store = store + 1
        else:
            count1 = count1 + 1
            store = store + 1
    if store == list1[j]:
        count = count + count1
        store = 0
        count1 = 1
print(count)
'''

'''list1 = ["fllower","flllow","flllight","flllll"]
campare1 = list1[0]
suffix1 = ""
suffix2 = ""
for i in list1:
    if len(i) < len(campare1):
        campare1 = i
for j in range(len(list1)):
    k = 0
    while k < len(campare1):
        if list1[j][k] == campare1[k]:
            suffix1 = suffix1 + campare1[k]
        k = k + 1
    campare1 = suffix1
    suffix2 = suffix1
    suffix1 = ""
print(suffix2)

'''

'''nums = [1,2,3,4,5,6,7,8,9]
duration = 3
i = 0
natural = True
odd = True
while i < len(nums):
    if i + 1 == nums[i]:
        pass
    else:
        natural = False

    i = i + 1
    if nums'''

'''nums = [1,3,5,7,9,11,13,15]
duration = 3
counting2 = 0
flag = False
i = 0
while i < len(nums):
    if i == 0:
        counting1 = nums[i] + duration - 1
        counting2 = counting2 + (counting1 - nums[i]) + 1
    elif i+1 == nums[i] and duration == 1:
        if flag == False:
            counting1 = nums[i] + duration - 1
            counting2 = counting2 + (counting1 - nums[i]) + 1
    elif i+1 == nums[i]:
        if flag == False:
            counting1 = nums[i] + duration - 1
            counting2 = 0
            counting2 = counting2 + counting1
            #counting2 = counting2 + (counting1 - nums[i])
    else:
        flag = True
        if (counting2 != nums[i] and duration != 1) or i == len(nums) - 1:
            counting1 = nums[i] + duration - 1
            #counting2 = 0
            counting2 = counting2 + (counting1 - nums[i] + 1)
            print(counting2)
        elif counting2 != nums[i] and duration == 1:
            counting1 = nums[i] + duration - 1
            counting2 = counting2 + (counting1 - nums[i]) + 1
            # counting2 = counting2 + (counting1 - nums[i]) + 1
        # else:
        #     counting1 = nums[i] + duration - 1

    i = i + 1

print(counting2)
'''

'''for i in range(len(nums)):
    counting1 = nums[i] + duration - 1
    counting2 = counting2 + abs(counting1 - nums[i]) + 1
print(counting2)'''

'''timeSeries = [1,3,5,7,9,11,13,15]
duration = 2
counting1 = 0
range1 = timeSeries[len(timeSeries)-1]
flag = False
i = 0
while i < len(timeSeries):
    if i+1 == timeSeries[i]:
        pass
    else:
        flag = True
    i = i + 1
if flag is False:
    counting1 = timeSeries[len(timeSeries)-1] + duration - 1
elif range1 <= duration:
    counting1 = range1 + duration - 1
else:
    counting1 = range1
print(counting1)
'''

'''timeSeries = [1,2,3,4,5,6,7,8,9]
duration = 5
rang1 = timeSeries[len(timeSeries)-1]
counting1 = timeSeries[len(timeSeries) - 1]
if counting1 <= duration:
    counting1 = counting1 + duration - 1
else:
    for i in range(1,rang1+1):
        if  i != timeSeries[i]:
            print(counting1)
if duration == 0:
    print(0)
else:
    print(counting1)'''

'''nums =  [1,2,3,4,5]
duration = 5
counting = 0
last = 0
for i in range(len(nums)):
    atacking = nums[i] + duration - 1
    for j in range(nums[i], atacking+1):
        if last >= j:
            pass
        else:
            counting = counting + 1
        if j == atacking:
            last = j
print(counting)
'''

'''nums = [1,1,0,1,1,0]
consec1 = 0
local_conse = 0
campare1 = 1
for i in range(len(nums)):
    if campare1 == nums[i]:
        local_conse = local_conse + 1
    if nums[i] == 0 or i == len(nums) - 1:
        if consec1 < local_conse:
            consec1 = local_conse
            local_conse = 0
        else:
            local_conse = 0

print(consec1)

'''

'''grid = [[0,0,0],[1,0,1],[1,1,1]]
perimeter = 0
for i in range(len(grid)):
    count = 0
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            if i == 0:
                if count == 0:
                    perimeter = perimeter + 4
                    count = count + 1
                elif count > 0 and grid[i][j] == grid[i][j-1]:
                    perimeter = perimeter + 2
                elif grid[i][j] != grid[i][j-1]:                                #---------------------------grid Problem --------------------------------------------
                    perimeter = perimeter + 4

            elif grid[i][j] == grid[i-1][j]:
                if j >= 1:
                    if grid[i][j - 1] != grid[i][j]:
                        perimeter = perimeter + 2
                        count = count + 1
                elif count == 0:
                    perimeter = perimeter + (grid[i][j] * 2)
                    count = count + 1
                elif count > 0:
                    perimeter = perimeter + 0
            elif grid[i][j] != grid[i - 1][j]:
                if count == 0:
                    perimeter = perimeter + ((grid[i][j] + grid[i][j])*2)
                    count = count + 1
                elif count > 0 and grid[i][j] == grid[i][j-1]:
                    perimeter = perimeter + 2
                elif grid[i][j] != grid[i][j-1]:
                    perimeter = perimeter + 4
print(perimeter)
'''

'''nums1 = [10,20,45,34,20,89,10,10]
freq = 0
number = 0
for i in range(len(nums1)):
    freq2 = 0
    for j in range(len(nums1)):
        if nums1[i] == nums1[j]:
            freq2 = freq2 + 1
    if freq2 > freq:
        number = nums1[i]
        freq = freq2
print(number, freq)
'''

'''nums1 = [10,9,8,7]
nums2 = [5,6,7,8]
nums1.sort()
nums2.sort()
maximum = 0
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        maximum = maximum + 1
        i = i + 1
        j = j + 1
    elif nums1[i] > nums2[j]:
        j = j + 1
print(maximum)
'''

'''def findContentChildren(g, s):
    maximum = 0
    flag = False
    item = 0
    while item < len(g[:]):
        j = 0
        while j < len(s[:]):
            if s[j] >= g[item]:
                maximum = g[item]
                g.remove(g[item])
                s.remove(s[j])
                j = len(s[:])
                flag = True
            else:
                j = j + 1
        if flag:
            flag = False
        else:
            item = item + 1
    return maximum
g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))'''

'''g = [1,2,3]
s = [1,1]
maximum = 0 + 954
item = 0
flag = False
while item < len(g[:]):
    j = 0
    while j < len(s[:]):
        if s[j] >= g[item]:
            maximum = maximum + 1
            g.remove(g[item])
            s.remove(s[j])
            j = len(s[:])
            flag = True
        else:
            j = j + 1
    if flag:
        flag = False
    else:
        item = item + 1
if maximum == 955:
    print(maximum+5)
else:
    print(maximum)
'''

'''nums1 = [10,9,8,7]
nums2 = [5,6,7,8]
mydict1 = {}
maximum = 0
for i in range(len(nums1)):
    if nums1[i] not in mydict1:
        mydict1[nums1[i]] = 1
    else:
        mydict1[nums1[i]] = mydict1[nums1[i]] + 1
for j in range(len(nums2)):
    if nums2[j] in mydict1 and mydict1[nums2[j]] >= 1:
        maximum = maximum + 1
        mydict1[nums2[j]] = mydict1[nums2[j]] - 1

print(maximum)
'''

'''nums  = [4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    j = i - 1
    key = nums[i]
    while j >= 0 and key < nums[j]:
        nums[j+1] = nums[j]
        j = j - 1

    nums[j+1] = key
print(nums)
'''

'''nums = [4,3,2,7,8,2,3,1]
i = 0
while i < len(nums):
    if nums[i] == nums[nums[i]-1]:
        i = i + 1
    elif i + 1 == nums[i]:
        i = i + 1
    elif nums[i] != nums[nums[i]-1]:
        nums[nums[i]-1], nums[i] = nums[i],  nums[nums[i]-1]
print(nums)'''

'''def findDisappearedNumbers(nums):
    i = 0
    j = 0
    index = 0
    list1 = []
    while i < len(nums):
        if index + 1 != nums[j]:
            if nums[nums[j] - 1] == nums[j]:             #---------------------------------------correct version of code-----------------------
                j = j + 1
                i = i + 1
                index = index + 1
            else:
                nums[nums[j] - 1], nums[j] = nums[j], nums[nums[j] - 1]
        elif index + 1 == nums[j]:
            index = index + 1
            j = j + 1
            i = i + 1

    for k in range(1, len(nums)):
        if k == nums[k - 1]:
            pass
        else:
            list1.append(k)
    return list1

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
'''

'''nums = [4,3,2,7,8,2,3,1]
i = 0
j = 0
index = 0
while i < len(nums):
    if index + 1 != nums[j]:
        if nums[nums[j]-1] == nums[j]:
            index = index + 1
            j = j + 1                                            #----------------------------cycle sorting------------------
            i = i + 1
        else:
            nums[nums[j] - 1],nums[j] = nums[j],nums[nums[j] - 1]
    elif index + 1 == nums[j]:
        index = index + 1
        j = j + 1
        i = i + 1

    #print(nums)

list1 = []
for k in range(1, len(nums)+1):
    if k == nums[k-1]:
        pass
    else:
        list1.append(k)

print(list1)
'''

'''nums = [4,2,8,2,3,7,1,6]
i = 0
j = 0
index = 0
for i in range(len(nums)):
    if index + 1 != nums[j]:
        if nums[nums[j]-1] == nums[j]:
            index = index + 1
            j = j + 1
            print("djh")
        else:
            nums[nums[j] - 1],nums[j] = nums[j],nums[nums[j] - 1]
    elif index + 1 == nums[j]:
        index = index + 1
        j = j + 1
    print(index,j)
    #print(nums)
print(nums)
'''

'''nums = [4,2,8,2,3,7,1]
index = 0
j = 0
for i in range(len(nums)):
    if index + 1 < nums[j]:
        nums[nums[j]-1],nums[j] = nums[j],nums[nums[j]-1]
    elif index + 1 > nums[j]:
        nums[len(nums)-1],nums[j] = nums[j], nums[len(nums)-1]
        index = index + 1
        j = j + 1
    elif index+1 == nums[j]:
        index = index + 1
        j = j + 1
print(nums)
'''

'''nums = [4,2,8,2,3,7,1,6]
index = 0
j = 0
for i in range(len(nums)):
    if index + 1 != nums[j]:
        nums[nums[j]-1],nums[j] = nums[j],nums[nums[j]-1]
        print(nums)
    elif index+1 == nums[j] or index >= nums[j]:
        j = j + 1
        index = index + 1       
print(nums)




list2 = []
for j in range(0, 7):
    if nums[j] == j + 1:
        pass
    else:
        list2.append(j)
print(list2)
'''

'''nums = [4,2,3,6,1,3]
index = 0
j = 0
for i in range(len(nums)):
    if index+1 != nums[j] and nums[j] != nums[nums[j]-1]:
        tempstore = nums[nums[j]-1]
        nums[nums[j]-1],nums[j] = nums[j],tempstore
    elif index + 1 == nums[j] or index >= nums[j]:
        j = j + 1
        index = index + 1
print(nums)
'''

'''nums = [4,3,2,8,2,3,7]
first_highest = nums[0]
second_highest = nums[0]
for i in range(len(nums)):
    if first_highest < nums[i]:
        if first_highest >= second_highest:
            second_highest = first_highest
            first_highest = nums[i]
    elif first_highest > nums[i] > second_highest:
        second_highest = nums[i]

print(second_highest)'''

'''nums = [4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key < nums[j]:  #-------------------------insertion sort-----------------------------------
        nums[j+1] = nums[j]
        j = j - 1
    nums[j+1] = key
print(nums)
'''

'''nums = [4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    j = i + 1
    while j < len(nums):      #sorting ------------------------------ insertion sort---------------------
        if nums[i] > nums[j]:
            nums.insert(i,nums[j])
            nums.pop(j+1)
        j = j + 1
print(nums)'''

'''nums1 = [3,2,1]
set1 = set(nums1)
if len(set1)<3:
    list2 = list(set1)
    list2.sort()
    print(list2[len(list2)-1])
else:
    list3 = list(set1)
    list3.sort(reverse=True)
    print(list3[2])
'''

'''nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
list1 = []
mydict = {}
for i in range(len(nums1)):
    if nums1[i] not in mydict:
        mydict[nums1[i]] = 1
    else:
        mydict[nums1[i]] = mydict[nums1[i]] + 1
for j in range(len(nums2)):
    if nums2[j] in mydict and mydict[nums2[j]] != 0:
        list1.append(nums2[j])
        mydict[nums2[j]] = mydict[nums2[j]] - 1
print(list1)
'''

'''nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
list1 = []
mydict = {}
for i in range(len(nums1)):
    mydict[nums1[i]] = 1
for i in range(len(nums2)):
    if nums2[i] in mydict:
        if nums2[i] not in list1:
            list1.append(nums2[i])

print(list1)
'''

'''nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
list1 = []
mydict1 = {}
mydict2 = {}
for i in range(len(nums1)):
    if nums1[i] not in mydict1:
        mydict1[nums1[i]] = 1
for i in range(len(nums2)):
    if nums2[i] not in mydict2:
        mydict2[nums2[i]] = 1
for key in mydict1.keys():
    if key in mydict2:
        list1.append(key)
print(list1)

'''

'''nums1 = [1,2,2,1]
nums2 = [2,2]
set1 = set(nums1)
set2 = set(nums2)
f = set1.intersection(set2)
print(list(f))
'''

'''nums = [0,1,2,3,4,5,6,7,8,9,10]
target = 16
index1 = None
index2 = None
start = 0
end = len(nums) - 1
for i in range(len(nums)):
    mid = (start + end)//2
    if nums[start] + nums[end] == target:
        index1 = start
        index2 = end
    elif nums[start] + nums[end] > target:
        end = mid
    elif nums[start] + nums[end] < target:
        start = mid
print(index1,index2)
'''

'''def nameprint(name, c):
    if c == 1:
        return
    print(name)
    nameprint(name,c-1)
nameprint("name",4)
'''

'''
def recusion(n):
    if n == 1:
        return 1
    print(n)
    n * recusion(n-1)

n = 5

recusion(n)

'''

'''nums = [1,2,5,78,90,10,6,30]
target = 16
finder = None
mydict = {}
key = 0
for i in range(len(nums)):
    if nums[i] in mydict:
        print(i,mydict[nums[i]])
        break
    else:
        key = abs(nums[i] - target)
        mydict[key] = i

'''

'''class Numarray():
    def __init__(self,nums):
        self.nums = nums
    def sumofrange(self,left,right):

        sum1 = 0
        for k in range(left, right + 1):
            sum1 = sum1 + self.nums[k]
        if sum1 == 0:
            return None
        else:
            return sum1
nums =
nums1 =
left = 0
right = 0
list1 = []
c1 = Numarray(nums1)
for i in range(len(nums)):
    j = 0
    while j < 1:
        if i == 0:
            left = 0
            right = -1
            j = j + 1
        else:
            left = nums[i][j]
            right = nums[i][j + 1]
            j = j + 1
    list1.append(c1.sumofrange(left,right))

print(list1)
'''

'''class Numarray():
    def __init__(self,nums):
        self.nums = nums
    def sumofrange(self,left,right):
        sum1 = 0
        for k in range(left, right+1):
            sum1 = sum1 + self.nums[k]
        return sum1




nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5],[2,4]]
nums1 = nums[0][0]
left = 0
right = 0
list1 = []
c1 = Numarray(nums1)
for i in range(len(nums)):
    j = 0
    while j < 1:
        if i == 0:
            left = 0
            right = -1
            j = j + 1
        else:
            left = nums[i][j]
            right = nums[i][j + 1]
            j = j + 1
    list1.append(c1.sumofrange(left,right))

print(list1)

'''

'''class Numarray():
    def __init__(self,nums):
        self.nums = nums
        self.list1 = []

    def sumofrange(self,left,right):
        sum1 = None
        for i in range(len(self.nums)):
            for j in range(1):
                self.left = nums[i][j]
                self.right = nums[i][j+1]
            for k in range(left,right + 1):
                sum1 = sum1 + nums[0][0][k]
            self.list1.append(sum1)
            sum1 = None
    def printlist(self):
        return self.list1



nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
n1 = Numarray(nums)

print(n1.printlist())
'''

'''class Numarray:
    def __init__(self,nums):
        self.nums = nums
    def acces(self):
        return nums

class Animal(Numarray):
    def __init__(self,nums):
        super().__init__(nums)
        print(nums)

nums = [6,1,0,3,12]
c1 = Animal(nums)
print(c1.acces())
'''

'''nums = [6,1,0,3,12]
left = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[left],nums[i] = nums[i],nums[left]
        left = left + 1
print(nums)'''

'''nums = [0,1,0,3,12]
for item in nums:
    if item == 0:
        nums.remove(item)
        nums.append(item)
print(nums)'''

'''nums = [9,6,4,2,3,5,7,0,1]
nums.sort() #[0,1,2,3,4,5,6,7,9]
if len(nums) not in nums:
    print(len(nums))
else:
    start = nums[0] #[0,1,2,3,4,5,6,7,8,9]
    end = nums[0]
    for i in range(len(nums)):
        if start > nums[i]:
            start = nums[i]
        elif end < nums[i]:
            end = nums[i]
    while start <= end:
        if start == nums[start]:
            start = start + 1
        elif start != nums[start]:
 '''

'''nums = [9,6,4,2,3,5,7,0,1]
nums.sort()
if len(nums) not in nums:
    print(len(nums))
else:
    j = nums[0]
    end = nums[0]
    for i in range(len(nums)):
        if j > nums[i]:
            j = nums[i]
        elif end < nums[i]:
            end = nums[i]

    i = 0
    while i < len(nums) and j <= end:
        if nums[i] == j:
            i = i + 1
            j = j + 1
            pass
        elif nums[i] != j:
            print(j)
            j = j + 1
'''

'''nums = [-2147483648,-2147483647,2147483647]
if len(nums) == 0:
    pass
else:
    i = 0
    j = nums[0]  # [0,1,2,3,4,5,6,7]
    end = nums[len(nums) - 1]
    string_range = ""
    list1 = []
    while i <= len(nums) and j <= end:
        if string_range == "" and nums[i] == j:
            string_range = string_range + str(nums[i])
            i = i + 1
            j = j + 1
        elif nums[i] == j:
            i = i + 1
            j = j + 1
        elif nums[i] != j and string_range != "":
            if int(string_range) == nums[i - 1]:
                list1.append(string_range)
                string_range = ""
                j = nums[i]
            else:
                string_range = string_range + "->" + str(nums[i - 1])
                list1.append(string_range)
                string_range = ""
                j = nums[i]                 
        elif nums[i] != j and string_range == "":
            j = j + 1

        if i == len(nums):
            if int(string_range) == nums[i - 1]:
                list1.append(string_range)
            else:
                string_range = string_range + "->" + str(nums[i - 1])
                list1.append(string_range)

    print(list1)
'''
'''end = nums[len(nums) - 1]
string_range = ""
list1 = []
i = nums[0]
count = 0
while i <= end:
    #print(nums[i - count])
    if nums[i - count] != i:
        string_range = string_range + "->" + str(nums[(i - 1)-count])
        list1.append(string_range)
        string_range = ""
        i = i + 1
        count = count + 1
    elif string_range == "" and nums[i - count] == i:
        string_range = string_range + str(nums[i-count])
        i = i + 1
    elif nums[i-count] == i:
        i = i + 1
    if i == end + 1:
        list1.append(string_range)
print(list1)'''

'''nums = [1,0,1,1]
k = 1
mydict = {}
for i in range(len(nums)):
    if nums[i] in mydict:
        if abs(mydict[nums[i]] - i) <= k:
            print(True)
    mydict[nums[i]] = i
'''

'''list1 = [0, 2, 3]
k = 1
total = None
i = 0
j = i+1
while i < len(list1):
    if j < len(list1) and abs(list1[i] - list1[j]) <= k:
            print(True)
    i = i + 1
    j = j + 1

'''

'''
nums = [1,0,1,1]
k = 1
mydict = {}
listfind = []
flagfind = False
flag1 = False
list1 = []
for i in range(len(nums)):
    if nums[i] not in mydict:
        mydict[nums[i]] = 1
    else:
        mydict[nums[i]] = mydict[nums[i]] + 1
for key,value in mydict.items():
    if value >= 2: #and flagfind == False:
        listfind.append(key)

i = 0
j = 0
while i < len(nums) and j < len(listfind):
    if listfind[j] == nums[i]:
        list1.append(i)
        print(list1)
    if i == len(nums) - 1:
        if abs(list1[j] - list1[j+1]) <= k:
            print(True)
            j = j + 1
        else:
            i = 0
            j = j + 1
            if len(list1) % 2:
                list1 = []
            else:
                pass
    else:
        i = i + 1

print(list1)
print(listfind)
'''

'''for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            if abs(i - j) <= k:
                print("true")
                break
            else:
                print(False)'''

'''arr = [5,0,6]
arr.sort()
k = 1
i = 0
sum1 = 0
while i < len(arr):
    j = i
    while j < len(arr):
        if j == (i + k):
            if k == 1:
                j = len(arr)
            else:
                sum1 = sum1 + (arr[i] + arr[j])
                j = len(arr)
            #break
        else:
            sum1 = sum1 + (arr[i]+arr[j])
            j = j + 1
    i = i + 1

print(sum1%10**9)
'''

'''arr = [3,1,1,2] 
i = 0
sum = 0
while i < len(arr):
    j = max(0, i-arr[i])
    while j <= i:
        sum = sum + arr[j]
        j = j + 1
    else:
        i = i + 1


print(sum)

'''

'''arr = [1,2,3,1,2,2,2,2]
mydict = {}
for i in range(len(arr)):
    if arr[i] not in mydict:
        mydict[arr[i]] = [i]
    else:
        mydict[arr[i]].append(i)
print(mydict)
'''

'''arr =[3,3,4]
dict1 = {}
for i in range(len(arr)):
    if arr[i] not in dict1:
        dict1[arr[i]] = 1
    else:
        dict1[arr[i]] = dict1[arr[i]] + 1
frequency_value = 0
frequency_key = 0
for key, value in dict1.items():
    if value > frequency_value:
        frequency_value = value
        frequency_key = key
print(frequency_key)
'''

'''arr = [3,2,3,1,1,1,3,3,3,3]
tofindelement = 0
for i in arr:
    if i > tofindelement:
        tofindelement = i

emptylist = [0]*(tofindelement + 1)
for i in range(len(arr)):
    emptylist[arr[i]] = emptylist[arr[i]] + 1

lastelement = 0
lastidx = 0
for i in range(len(emptylist)):
    if emptylist[i] > lastelement:
        lastelement =emptylist[i]
        lastidx = i
print(emptylist)
print(lastidx)'''
# print(last)


'''def palindrome(str1):
    str2 = ""
    if len(str1) == 0:
        str2 = str1 + str2
        return str2
    mid = len(str1)//2
    left = palindrome(str1[:mid+1])
    right = palindrome(str1[mid:])

str1 = "madam"
print(palindrome(str1))'''

'''arr = [2,4,6,8,10]
list1 = [0]*len(arr)
sum = 0
for i in range(len(arr)-1,-1,-1):
    sum = sum + arr[i]
    list1[i] = sum
print(list1)
'''

'''arr = [4,1,2,1,2]
mydict = {}
for i in range(len(arr)):
    if arr[i] not in mydict:
        mydict[arr[i]] = 1
    else:
        mydict[arr[i]] = mydict[arr[i]] + 1
for keys,values in mydict.items():
    if values == 1:
        print(keys)


'''

'''arr1 = [3,2,6,5,0,3,1,20]
profit1 = 0
profit2 = 0
min1 = arr1[0]
max2 = arr1[0]
for i in range(len(arr1)):
    if min1 > arr1[i]:
        min1 = arr1[i]
        max2 = arr1[i]
    if max2 < arr1[i]:
        max2 = arr1[i]
        profit1 = 0
        profit1 = profit1 + (max2 - min1)
        if profit2 < profit1:
            profit2 = profit1

print(profit2)
'''

'''n = 12
str1 = ""
if n == 1:
    print(1)
else:
    while n // 2 != 1:
        m = n % 2
        str1 = str(m) + str1
        n = n // 2
    if n % 2 == 1:
        str1 = str(1) + str1
    elif n % 2 == 0:
        str1 = str(0) + str1
    str1 = str(1) + str1
total = 0
i = len(str1) - 1
j = 0
while i >= 0:
    total = total + (int(str1[j]) * 2**i)
    j = j + 1
    i = i - 1
print(total)
'''

'''def xorAllNums(nums1, nums2):
    total1 = 0
    total2 = 0
    if len(nums1) == len(nums2) and (len(nums1) % 2 == 0 and len(nums2) % 2 == 0):
        return 0
    elif len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
        return 0
    elif len(nums1) % 2 == 0:
        mainnums = nums1
    else:
        mainnums = nums2
    sumofxor = 0
    for i in range(len(mainnums)):
        sumofxor = sumofxor ^ (mainnums[i])
    return sumofxor




list1 = [1,2,3]
list2 = [537,817,983]
print(xorAllNums(list1,list2))
'''

'''nums1 = [2,1,3]
nums2 = [10,2,5,0]
list1 = []
sumxor = 0
sum1 = 0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        sumxor = sumxor ^ (nums1[i] ^ nums2[j])
print(sumxor)
'''

#         sum1 = sum1 ^ nums1[i] ^ nums2[j]
#         list1.append(sum1)
#         sum1 = 0
# total = 0
# for k in range(len(list1)):
#     total = total ^ list1[k]
#
# print(total)


'''str1 = "abc"
str2 = "de"
xor_sum = 0
mainstr = ""
if len(str1)%2 == 0:
    mainstr = str1
else:
    mainstr = str2
for i in range(len(mainstr)):
    if i == 0 and len(mainstr) == 2:
        xor_sum = xor_sum + (ord(mainstr[i])^ord(mainstr[i + 1]))
    else:
        xor_sum = xor_sum + (xor_sum ^ ord(mainstr[i]))
print(xor_sum)
'''

'''m = 1
n = m + 1
list1 = []
list2 = []
for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            list1.append(1)
        else:
            list1.append(list2[i-1][j-1] + list2[i - 1][j])
    if i == n-1:
        print(list1)
    else:
        list2.append(list1)
        list1 = []

'''

'''n = 5
i = 0
list1 = []
list2 = []
count = 0
while i < n:
    for j in range(i+1):                               ######################################----very imp----#####################################
        if j == 0 or j == i:
            list1.append(1)
        else:
            list1.append(list2[i-1][count] + list2[i-1][count+1])
            count = count + 1
    count = 0
    list2.append(list1)
    list1 = []
    i = i + 1
print(list2)
'''

'''def binarysearchtree(nums):
    if not nums:
        return None
    mid = len(nums)//2
    tree = Tree
    binarysearchtree(nums[:mid])
    binarysearchtree(nums[mid+1:])
    return tree


nums = [-10,-3,0,5,9]
'''

'''def factorial(n):
    if n == 1:
        return n
    return (n*factorial(n-1))

n = 5
print(factorial(5))
'''

'''arr = [1,3,4,2]
duplicate = 0
index = 0
i = 0
while i < len(arr):
    index = arr[i]
    if arr[i] == i+1:
        index = 0                             # its very important algo cycle sorting
        i = i + 1
    else:
        if arr[i] == arr[index-1]:
            duplicate = arr[i]
            i = i + 1
        else:
            arr[i], arr[index-1] = arr[index-1], arr[i]
            index = 0
print(duplicate)
print(arr)
'''

'''def fibo(n):
    if n  < 2:
        return 1

    else:
        #list1.append(n)
        add = (fibo(n-1) + fibo(n-2))
        return add


print(fibo(35))
'''

'''#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root



def pre_order_traversal(node):
    if not node:
        return None
    print(node.val, end=" ")  # Print the value of the current node
    pre_order_traversal(node.left)  # Recursively visit the left subtree
    pre_order_traversal(node.right)

arr = [-10,-3,0,5,9]
Solution = Solution()
root = Solution.sortedArrayToBST(arr)
print(pre_order_traversal(root))
'''

'''matrix = [[[1,2],
           [3,4]],
          [[5,6],
          [7,8]]]

ans = [[0,0],
       [0,0]]
i = 0
for j in range(len(matrix[i])):
    for k in range(len(matrix[i][j])):
        ans[j][k] = matrix[i][j][k] * matrix[i+1][k][j]
print(ans)
'''

'''matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
list2 = []
list1 = []
i = len(matrix) - 1
j = 0
while i >= 0 and j < len(matrix[i]):
    list1.append(matrix[i][j])
    if i == 0:
        j = j + 1
        i = len(matrix) - 1
        list2.append(list1)
        list1 = []
    else:
        i = i - 1
print(list2)
'''

'''matrix = [[1,0,1],
          [1,1,1],
          [1,1,1]]
index_i = None
index_j = None
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            index_j = j
            index_i = i

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == index_j:
            matrix[i][j] = 0
        if i == index_i:
            matrix[i][j] = 0
            
print(matrix)
'''

'''list1 = [1,2,7,0,0,0]
list2 = [2,5,6]
m = 3
n = 3
i = m -1
j = n -1
k = (m+n) - 1
while i >= 0 and j >= 0:
    if list1[i] > list2[j]:
        list1[k] = list1[i]
        i = i - 1
    else:
        list1[k] = list2[j]
        j = j - 1
    k = k - 1
while j >= 0:
    list1[k] = list2[j]
    j = j - 1
    k = k - 1
print(list1)
'''

'''list1 =[0] #[1,2,7,0,0,0]
list2 = [1] #[2,5,6]
m = 0
n = 1
j = 0
for i in range(m,len(list1)):
    list1[i] = list2[j]
    j = j + 1
list1.sort()
print(list1)'''

'''list1 = [1]#[1,2,7,0,0,0]
list2 = []#[2,5,6]
m = 1
n = 0
i = 0
j = 0
while i < m and j < n:
    if list1[i] < list2[j]:
        i = i + 1
    elif list1[i] > list2[j]:
        list1[i],list2[j] = list2[j],list1[i]
        i = i + 1
    elif list1[i] == list2[j]:
        list2[j],list1[i+1] = list1[i+1],list2[j]
        i = i + 1
if j != n:
    for k in range(m, len(list1)):
        list1[k] = list2[j]
        j = j + 1

print(list1)
'''

'''class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        for i in range(len(nums)):
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            elif nums[mid] == target:
                start = mid
                return start
        return start
'''

'''nums = [3,2,2,3]
val = 3
for item in nums[:]:
    if item == val:
        nums.remove(item)
print(nums)'''

'''class Solution(object):
    def removeDuplicates(self, nums):
        dict = {}
        list1 = []
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = dict[nums[i]] + 1
        for key in dict.keys():
            list1.append(key)
        return list1

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(nums))
'''

'''def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                list1 = []
                list1.append(i)
                list1.append(j)
                return list1
'''

'''class Solution(object):
    def twoSum(self, nums, target):
        arr1 = []
        for item in nums:
            arr1.append(item)
        nums.sort()
        start = 0
        end = len(nums) - 1
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            mid = (start + end) // 2
            if nums[start] + nums[end] == target:
                index1 = nums[start]
                index2 = nums[end]
            elif nums[start] + nums[end] < target:
                start = mid
            elif nums[start] + nums[end] > target:
                end = mid
        a = arr1.index(index1)
        b = arr1.index(index2)
        return [a, b]


arr = [3,3]
target = 6
solution = Solution()
print(solution.twoSum(arr,target))
'''

'''arr = [3,2,4]
arr1 = []
for item in arr:
    arr1.append(item)
target = 6
arr.sort()
start = 0
end = len(arr) - 1
index1 = 0
index2 = 0
for i in range(len(arr)):
    mid = (start + end)//2
    if arr[start] + arr[end] == target:
        index1 = arr[start]
        index2 = arr[end]
    elif arr[start] + arr[end] < target:
        start = mid
    elif arr[start] + arr[end] > target:
        end = mid
a = arr1.index(index1)
b = arr1.index(index2)
print(a, b)
'''

'''class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    list1 = []
                    list1.append(i)
                    list1.append(j)
                    return list1


nums = list(map(int, input().split(" ")))
target = int(input())
solution = Solution()
print(solution.twoSum(nums, target))
'''
'''class Solution:
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i , j
a = list(map(int,input().split(" ")))
b = int(input())
'''

'''arr = ["f", "z", "x", "j", "e", "v", "p"]
target = "a"
str1 = None
i = 0
while i < len(arr):
    if ord(arr[i]) > ord(target):
        if str1 is None or ord(arr[i]) < ord(str1):
            str1 = arr[i]
    i += 1
'''

'''arr = ["f","z","x","j","e","v","p"]
target = "i"
str1 = ""
i = 0
while i < len(arr):
    if i == 0:
        str1 = arr[i]
    else:
        if ord(arr[i]) > ord(target) and ord(arr[i]) < ord(str1):
            str1 = arr[i]
        if ord(arr[i]) > ord(target) and ord(arr[i]) > ord(str1):
            str1 = arr[i]
    i = i + 1

print(str1)
'''

'''for i in range(len(arr)):
    if i == 0:
        str1 = arr[i]
    if ord(arr[i]) > ord(str1):
        if ord(target) > ord(arr[i]):
            if ord(arr[i]) > ord(str1):
                str1 = arr[i]
            else:
                str1 = arr[i]
    else:
        if ord(arr[i]) > ord(target):
            str1 = arr[i]
'''

'''arr = [2, 3, 4, 10, 40]
x = 10
low = 0
hight = len(arr)
while low <= hight:
    if low == hight:
        print(low)
        break
    mid = (low + hight) // 2
    if x >= arr[mid]:
        low = mid
    if x <= arr[mid]:
        hight = mid'''

'''def binary1(arr,low, hight,x):
    while low < hight:
        mid = (low + hight) // 2
        if x > arr[mid]:
            low = mid + 1
        else: #x < arr[mid]:
            hight = mid
    return hight

arr = [2, 3, 4, 10, 40]
x = 10
low = 0
hight = len(arr)
print(binary1(arr,low,hight,x))
'''

'''arr1 = [1, 3, 2, 4,4,4 ]
arr2 = [3, 1, 2, 4,4,4]
dict = {}
count = 0
list1 = []

for i in range(len(arr1)):
    if arr1[i] not in dict:
        dict[arr1[i]] = 1
    else:
        dict[arr1[i]] = dict[arr1[i]] + 1
        if dict[arr1[i]]%2 == 0:
            store = dict[arr1[i]]/2
            count = count + int(store)
            dict[arr1[i]] = 0
    if arr2[i] not in dict:
        dict[arr2[i]] = 1
    else:
        dict[arr2[i]] = dict[arr2[i]] + 1
        if dict[arr2[i]]%2 == 0:
            store = dict[arr2[i]]/2
            count = count + int(store)
            dict[arr2[i]] = 0
    list1.append(count)
print(list1)
'''

'''arr1 = [1, 3, 2, 4,7]
arr2 = [3, 1, 2, 4,7]
dict = {}
count = 0
list1 = []

for i in range(len(arr1)):
    if arr1[i] not in dict:
        dict[arr1[i]] = 1
    else:
        dict[arr1[i]] = dict[arr1[i]] + 1
        if dict[arr1[i]]%2 == 0:
            store = dict[arr1[i]]/2
            count = count + int(store)
    if arr2[i] not in dict:
        dict[arr2[i]] = 1
    else:
        dict[arr2[i]] = dict[arr2[i]] + 1
        if dict[arr2[i]]%2 == 0:
            store = dict[arr2[i]]/2
            count = count + int(store)
    list1.append(count)
print(list1)
'''

'''arr1 = [1, 3, 2, 4,3, 1, 2, 4]
dict = {}
for i in range(len(arr1)):
    if arr1[i] not in dict:
        dict[arr1[i]] = 1
    else:
        dict[arr1[i]] = dict[arr1[i]] + 1
    if dict.get(arr1[i])//2:
        store = dict.get(arr1[i])//2
        right = store/2
        print("yes")
'''

'''arr1 = [1, 3, 2, 4]
arr2 = [3, 1, 2, 4]
list1 = [0] * (max(arr1) + 1)
for i in range(len(arr1)):
    list1[arr1[i]] = list1[arr1[i]] + 1

print(list1)
'''

'''arr1 = [1, 3, 2, 4]
arr2 = [3, 1, 2, 4]
count = 0
list1 = []
for i in range(len(arr1)):
    if arr1[i] in arr2[:i+1]:
        count = count + 
    list1.append(count)
    count = 0
    arr2.remove(arr1[i])
print(list1)
'''

'''str1 = "abaacbcbb"
dict = {}
total_len = 0
for i in range(len(str1)):
    dict[str1[i]] = 0
for i in range(len(str1)):
    dict[str1[i]] = dict[str1[i]] + 1
for key,values in dict.items():
    if values%2 == 0:
        dict[key] = 2
    else:
        dict[key] = 1
for valu in dict.values():
    total_len = total_len + valu
print(total_len)
'''

'''str1 = "abaacbcbb"
dict = {}
total_len = 0
for i in range(len(str1)):
    if str1[i] not in dict:
        dict[str1[i]] = 1
    else:
        dict[str1[i]] = dict[str1[i]] + 1
for key,values in dict.items():
    if values%2 == 0:
        dict[key] = 2
    else:
        dict[key] = 1
for valu in dict.values():
    total_len = total_len + valu
print(total_len)
'''

'''str1 = "abbb"
arr = [i for i in str1]
index1 = 0
flag = False
i = 0
while i < len(arr):
    j = 0
    while j < len(arr):
        if i > j:
            if arr[i] == arr[j]:
                index1 = j
                #print(arr[i])
                #print(index1)
                flag = True
        if i < j:
            if arr[i] == arr[j] and flag == True:
                arr.remove(arr[j])
                arr.remove(arr[index1 + 1])
                index1 = 0
                if flag == True:
                    flag = False
                    break
        index1 = 0
        j = j + 1
    i = i + 1
print(arr)
'''

'''str1 = "abaacbcbb"
arr = [i for i in str1]
index1 = 0
flag = False
for i in range(1,len(arr) - 1):
    for j in range(len(arr)):
        if i > j:
            if arr[i] == arr[j]:
                index1 = j
                #print(arr[i])
                #print(index1)
                flag = True
        if i < j:
            if arr[i] == arr[j] and flag == True:
                arr.remove(arr[j])
                arr.remove(arr[index1])

                flag = False
                index1 = 0
    index1 = 0
'''

'''arr = ["mas","as","hero","superhero"]
i = 0
j = 1
while i < len(arr) and j < len(arr):
    if arr[i] > arr[j]:
        substring = arr[j]
        if substring in arr[i]:
            #print(i)
            print(substring)
    elif arr[i] < arr[j]:
        substring = arr[i]
        if substring in arr[j]:
            print(substring)
    i = i + 1
    j = j + 1
'''

'''arr1 = [4,3,2,7,8,2,3,1]
i = 0
small = 0
large = 0
list1 = []
while i < len(arr1):
    if i == 0:
        small = arr1[i]
        large = arr1[i]
    if arr1[i] > large:
        large = arr1[i]
    if arr1[i] < small:
        small = arr1[i]
    i = i + 1
for i in range(small,large+1):
    if i not in arr1:
        list1.append(i)
'''

'''arr1 = ["aba","abab","xyz"]
len1 = len(arr1[0])
prefix_list = []
suffix_list = []
substring = arr1[0]
str1 = ""
str2 = ""
prefix = 0
suffix = 0
i = 1
while i < len(arr1):
    str1 = arr1[i][0:len1]
    str2 = arr1[i][len(arr1[i])-len1:]
    prefix_list.append(str1)
    suffix_list.append(str2)
    if str1 == substring and str2 == substring:
        prefix = prefix + 1
        suffix = suffix + 1
    elif str1 == substring:
        prefix = prefix + 1
    elif str2 == substring:
        suffix = suffix + 1
    str1 = ""
    str2 = ""
    i = i + 1

print(suffix,prefix)
print(prefix_list)
print(suffix_list)
'''

'''arr1 = [2,4,6,8,10]
list1 = []
sum1 = 0
sum1 = sum(arr1)
list1.append(sum1)
for i in range(len(arr1)-1):
    sum1 = sum1 - arr1[i]
    list1.append(sum1)
print(list1)
'''

'''arr1 = [2,4,6,8,10]
list1 = []
sum1 = 0
for i in range(len(arr1)):
    sum1 = sum1 + arr1[i]
    list1.append(sum1)
print(list1)
'''

'''str1 = "abcaax"
len1 = 3
list1 = []
for i in range(len(str1)):
    calcu = i+len1
    #print(i)
    if i == len(str1) - len1:
        list1.append(str1[i:calcu])
        break
    list1.append(str1[i:calcu])
print(list1)
'''

'''str1 = "abcaax"
i = 0
j = 0
list1 = []
count = 1
str2 = ""
while i < len(str1) and j < len(str1):
    #print(i)
    if count == 4:
        list1.append(str2)
        str2 = ""
        count = 1
        j = j - 2
        #print(j)
        if j == len(str1)-1:
            pass
        else:
            i = i + 1
    else:
        str2 = str2 + str1[j]
        count = count + 1
        j = j + 1
    if i == len(str1) - 3 and j == len(str1):
        list1.append(str2)
print(list1)
'''

'''arr1 =["pay","attention","practice","attend"]
prefix = "at"
count = 0
dcount = 0
i = 0
j = 0
while i < len(arr1) and j < len(prefix):
    if arr1[i][j] == prefix[j]:
        count = count + 1
        j = j + 1
        if count == j:
            count = 0
            dcount = dcount + 1
            i = i + 1
            j = 0
    else:
        i = i + 1
        j = 0
print(dcount)
'''

'''arr1 =["pay","attention","practice","attend"]
count = 0
for i in range(len(arr1)):
    if arr1[i].startswith("at"):
        count = count + 1

'''

'''str = "LOVELEETO"
dict = {}
first_ooc = ""
index = 0
for i in range(len(str)):
    if str[i] not in dict:
        dict[str[i]] = 1
    else:
        dict[str[i]] = dict[str[i]] + 1
for key,value in dict.items():
    #index = index + 1
    if value == 1:
        first_ooc = key
        break
    index = index + 1

print(first_ooc)
print(str.index(first_ooc))
'''

'''s = "LOwELEETO"
maincount = 0
str2 = ""
str4 = ""
count = 1
str1 = ""
flag = False
index = 0
for i in range(len(s)-1):
    if flag == True:
        break
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            #print(s[i])
            count = count + 1
            #print(count)
            if s[i] not in str1:
                str1 = str1 + s[i]
                str4 = str4 + s[i]
        if count == 1 and j == len(s) -1 and s[i] not in str4:
            #print(s[i])
            flag = True
            str2 = ""
            str2 = str2 + s[i]
            index = i
            #break
            #print(s[i])
    if maincount == 0 or count < maincount:
        maincount = 0
        str2 = ""
        maincount = maincount + count
        str2 = str2 + str1
        str1 = ""
        count = 1
    else:
        count = 1
        str1 = ""

print(maincount)
print(str2)
print(index)
'''
'''n = 121
str1 = str(n)
str2 = ""
for i in range(len(str1)):
    str2 = str1[i] +str2
if int(str2) == int(str1):
    print(True)
else:
    print(False)'''
'''n = 123
original = n
reversed = 0
while n > 0:
    digit = n%10
    reversed = reversed * 10 + digit
    n = n//10
if reversed == original:
    print(True)
else:
    print(False)
'''

'''n = 121
str1 = str(n)
str2 = ""
for i in range(len(str1)):
    str2 = str1[i] +str2
if int(str2) == int(str1):
    print(True)
else:
    print(False)

'''

'''arr2 = ["flight","flower","flow"]
arr2.sort()
str1 = ""
i = arr2[0]
j = arr2[len(arr2)-1]
k = 0
l = 0
while k < len(i) and l < len(j):
    if i[k] == j[l]:
        str1 = str1 + i[k]
    k = k + 1
    l = l + 1

print(str1)
'''

'''arr1 = ["amazon","apple","facebook","google","leetcode"]
arr2 = "o
list1 = []
count = 0
str1 = ""
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        #print(str1)
        if len(str1) == 2:
            list1.append(str1)
            str1 = ""
            if j == len(arr1[i][j]) - 1:
                str1 = ""
            else:
                str1 = str1 + arr1[i][j-1]
        if j <= 1:
            str1 = str1 + arr1[i][j]
        elif j > 1:
            str1 = str1 + arr1[i][j]
            #print(j)
print(list1)
'''

'''    j = 0
    while j < len(arr1[i]):
        if len(str1) == len(arr2):
            if str1 == arr2:
                print(str1)
            print(str1)
            str1 = ""

        str1 = str1 + arr1[i][j]
        j = j + 1

'''

'''arr1 = ["amazon","apple","facebook","google","leetcode"]
arr2 = ["e","o","bo"]
str2 = ""
count = 0
list1 = []
for i in range(len(arr1)):
    k = 0
    dict = {}
    while k < len(arr2):
        j = 0
        while j < len(arr1[i]):
            if len(arr2[k]) > 1:
                str2 = str2 + arr1[i][j]
                j = j + 1
                #print(str2)
                if len(arr2[k]) == len(str2):
                    if str2 == arr2[k]:
                        #print(str2)
                        #k = k + 1
                        if arr2[k] not in dict:
                            dict[arr2[k]] = 1
                        else:
                            dict[arr2[k]] = dict[arr2[k]] + 1
                        str2 = ""
                        str2 = str2 + arr1[i][j]
                    else:
                        str2 = ""
                if len(arr1[i]) == j:
                    #print(str2)
                    str2 = ""
            else:
                if arr2[k] == arr1[i][j]:
                    if arr2[k] not in dict:
                        dict[arr2[k]] = 1
                    else:
                        dict[arr2[k]] = dict[arr2[k]] + 1
                j = j + 1
        k = k + 1
    #print(dict)
    for u in range(len(arr2)):
        if arr2[u] in dict.keys():
            #print(count)
            #print(arr1[i])
            count = count + 1
            #print(count)
            #count = count+1
            if count == len(arr2):
                #print(count)
                list1.append(arr1[i])
                count = 0
            if u == len(arr2) - 1:
                count = 0
        else:
            count = 0

print(list1)
'''

'''arr1 = ["amazon","apple","facebook","google","leetcode"]
arr2 = ["e","o","oo"]
str2 = ""
count = 0
list1 = []
for i in range(len(arr1)):
    k = 0
    dict = {}
    while k < len(arr2):
        j = 0
        while j < len(arr1[i]):
            if len(arr2[k]) > 1:
                str2 = str2 + arr1[i][j]
                j = j + 1
                #print(str2)
                if len(arr2[k]) == len(str2):
                    if str2 == arr2[k]:
                        #k = k + 1
                        if arr2[k] not in dict:
                            dict[arr2[k]] = 1
                        else:
                            dict[arr2[k]] = dict[arr2[k]] + 1
                        str2 = ""
                    else:
                        str2 = ""
                if len(arr1[i]) == j:
                    str2 = ""
            else:
                if arr2[k] == arr1[i][j]:
                    if arr2[k] not in dict:
                        dict[arr2[k]] = 1
                    else:
                        dict[arr2[k]] = dict[arr2[k]] + 1
                j = j + 1
        k = k + 1
    #print(dict)
    for u in range(len(arr2)):
        if arr2[u] in dict.keys():
            #print(count)
            #print(arr1[i])
            count = count + 1
            #print(count)
            #count = count+1
            if count == len(arr2):
                #print(count)
                list1.append(arr1[i])
                count = 0
            if u == len(arr2) - 1:
                count = 0
        else:
            count = 0

print(list1)
'''

'''str2 = ""
if len(arr2[k]) > 1:
str2 = str2 + arr1[i][j]
if str2 == arr2[k]:
    k = k + 1
    if arr2[k] not in dict:
        dict[arr2[k]] = 1
    else:
        dict[arr2[k]] = dict[arr2[k]] + 1

if arr2[k] == arr1[i][j]:
    if arr2[k] not in dict:
        dict[arr2[k]] = 1
    else:
        dict[arr2[k]] = dict[arr2[k]] + 1
j = j + 1

'''

'''arr2 = ["e","o","oo","e"]
dict = {}
for i in range(len(arr2)):
    dict[arr2[i]] = dict[arr2[i]] + 1
    # if arr2[i] not in dict:
    #     dict[arr2[i]] = 1
    # else:
    #     dict[arr2[i]] = dict[arr2[i]] + 1

print(dict)
'''

'''def akwargs(**kwargs):
    for i, j in kwargs.items():
        print(i,j)
g = akwargs(sawan = "jb",patel = "hvdh")
'''

'''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    leftarray = merge_sort(arr[:mid])
    rightarray = merge_sort(arr[mid:])
    return merge(leftarray,rightarray)
def merge(lefarray, rightarray):
    sorted_array = []
    i = 0
    j = 0
    while len(lefarray) > i and len(rightarray) > j:
        if lefarray[i] > rightarray[j]:
            sorted_array.append(rightarray[j])
            j = j + 1
        else:
            sorted_array.append(lefarray[i])
            i = i + 1
    sorted_array.extend(lefarray[i:])
    sorted_array.extend(rightarray[j:])
    return sorted_array


arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
'''

'''list1 = [3,5,2,10]
list2 = []
i = 0
j = 1
while i < len(list1) and j < len(list1):
    xor = list1[i] ^ list1[j]
    list2.append(xor)
    i = i + 1
    j = j + 1
print(list2)

'''

'''n = 1
binary = bin(n)
str1 = str(binary)
binary2 = ""
for i in range(2,len(str1)):
    binary2 = binary2 + str1[i]
print(int(binary2))
'''

'''str1 = "a3b5c2ayshdfywwie7752hsdhgdhhs2"
str2 = ""
for i in range(len(str1)):
    if 97 <= ord(str1[i]) <= 122 and str1[i] not in str2:
       str2 = str2 + str1[i]
print(str2)
'''

'''n = 5
factor = 1
for i in range(1,n+1):
    factor = factor * i
    print(factor)

'''

'''def hcm(m,n):
    high = 0
    factor = 0
    if m > n:
        high = high + n
    else:
        high = high + m
    for i in range(1,high+1):
        if m%i == 0 and n%i == 0:
            factor = 0
            factor = factor + i
    return factor

m,n = input("enter a number").split(" ")
print(hcm(m,n))
'''

'''n = 75
m = 25
high = 0
factor = 0
if n > m:
    high = high + m
else:
    high = high + n
for i in range(1,high+1):
    if n % i == 0 and m % i == 0:
        factor = 0
        factor = factor + i
print(factor)
'''

'''def isValid(s):
    #s = "abc"
    my_dict = {}
    for i in range(len(s)):
        my_dict[s[i]] = 0
    for i in range(len(s)):
        my_dict[s[i]] = my_dict[s[i]] + 1
    list1 = []
    for key, values in my_dict.items():
        list1.append(values)
    count = list1[0]
    count1 = 0
    # for key,values in my_dict.items():
    for i in range(len(list1)):
        if list1[i] == count:
            pass
        else:
            count1 = count1 + 1
            new = list1[i] - 1
            # print(new)
            if new == count:
                pass
            else:
                count1 = count1 + 1
                break
    if count1 > 1:
        return ("NO")
    else:
        return ("YES")


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    #fptr.write(result + '\n')

    #fptr.close()
'''

'''def isValid(s):
    str2 = ""
    count1 = 0
    for i in range(len(s)):
        if s[i] not in str2:
            str2 = str2 + s[i]
            # count1 = count1 + 1
        elif s[i] in str2:
            count1 = count1 + 1
    if count1 > 1:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    #fptr.write(result + '\n')

    #fptr.close()
'''

'''def isValid(s):
    str2 = ""
    count1 = 0
    for i in range(len(s)):
        if s[i] not in str2:
            str2 = str2 + s[i]
            # count1 = count1 + 1
        elif s[i] in str2:
            count1 = count1 + 1
    if count1 > 1:
        print("NO")
    else:
        print("YES")

s = "abc"
isValid(s)
'''

'''s = "abc"
str2 = ""
count1 = 0
for i in range(len(s)):
    if s[i] not in str2:
        str2 = str2 + s[i]
        #count1 = count1 + 1
    elif s[i] in str2:
        count1 = count1 + 1
if count1 > 1:
    print("NO")
else:
    print("YES")
'''

'''arr = [[27, 38], [3, 43], [9, 82], [2, 10]]
list4 = []
list3 = []
for d in range(len(arr)//2):
    i = 0
    j = 1
    while i < len(arr) and j < len(arr):
        k = 0
        l = 0
        while k < len(arr[i]) and l < len(arr[j]):
            if arr[i][k] > arr[j][l]:
                list3.append(arr[j][l])
                l = l + 1
                if l == len(arr[i]):
                    list3.append(arr[i][k])
            elif arr[i][k] < arr[j][l]:
                list3.append(arr[i][k])
                k = k + 1
                if k == len(arr[k]):
                    list3.append(arr[j][l])
        list4.append(list3)
        list3 = []
        i = i + 2
        j = j + 2
'''

'''arr = [[27, 38], [3, 43], [9, 82], [2, 10]]
list4 = []
list3 = []
i = 0
j = 1
while i < len(arr) and j < len(arr):
    k = 0
    l = 0
    while k < len(arr[i]) and l < len(arr[j]):
        if arr[i][k] > arr[j][l]:
            list3.append(arr[j][l])
            l = l + 1
            if l == len(arr[i]):
                list3.append(arr[i][k])
        elif arr[i][k] < arr[j][l]:
             list3.append(arr[i][k])
             k = k + 1
             if k == len(arr[k]):
                 list3.append(arr[j][l])
    list4.append(list3)
    list3 = []
    i = i + 2
    j = j + 2
'''

'''arr = [38, 27, 43, 3, 82, 9, 10,2]
subarr = 1
list1 = []
list2 = []
j = 1
divide = len(arr)
for i in range(len(arr)//2):
    if subarr == 1:
        for i in range(0, divide, 2):
            if j > len(arr) - 1:
                pass
            else:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    list1.append(arr[i])
                    list1.append(arr[j])
                    list2.append(list1)
                    list1 = []
                    if i == len(arr) - 1:
                        if (len(arr) - 1) % 2 == 0:
                            break
                    else:
                        j = j + 2
                else:
                    list1.append(arr[i])
                    list1.append(arr[j])
                    list2.append(list1)
                    list1 = []
                    if i == len(arr) - 1:
                        if (len(arr) - 1) % 2 == 0:
                            break
                    else:
                        j = j + 2
        subarr = subarr * 2
    else:
        list3 = []
        list4 = []
        # [[27, 38], [3, 43], [9, 82], [2, 10]]
        i = 0
        k = 1
        while i < len(list2) and j < len(list2):
            g = 0
            m = 0
            while g < len(list2[i]) and m < len(list2[k]):
                if list2[i][g] < list2[k][m]:
                    list3.append(list2[i][g])
                    g = g + 1
                elif list2[i][g] > list2[k][m]:
                    list3.append(list2[k][m])
                    m = m + 1
                else:
                    pass
            list4.append(list3)
            list3 = []
            i = i + 2
            k = k + 2
        print(list3)

'''

'''if subarr == 1:
    for i in range(0, divide, 2):
        if j > len(arr) - 1:
            pass
        else:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                list1.append(arr[i])
                list1.append(arr[j])
                list2.append(list1)
                list1 = []
                if i == len(arr) - 1:
                    if (len(arr) - 1) % 2 == 0:
                        break
                else:
                    j = j + 2
            else:
                list1.append(arr[i])
                list1.append(arr[j])
                list2.append(list1)
                list1 = []
                if i == len(arr) - 1:
                    if (len(arr) - 1) % 2 == 0:
                        break
                else:
                    j = j + 2
    subarr = subarr * 2
else:
    list3 = []
    list4 = []
    #[[27, 38], [3, 43], [9, 82], [2, 10]]
    i = 0
    k = 1
    while i < len(list2) and j < len(list2):
        g = 0
        m = 0
        while g < len(list2[i]) and m < len(list2[k]):
            if list2[i][g] < list2[k][m]:
                list3.append(list2[i][g])
                g = g + 1
            elif list2[i][g] > list2[k][m]:
                  list3.append(list2[k][m])
                  m = m + 1
            else:
                pass
        list4.append(list3)
        list3 = []
        i = i + 2
        k = k + 2
    print(list3)
'''

'''
for i in range(0,divide, 2):
    if j > len(arr)-1:
        pass
    else:
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            list1.append(arr[i])
            list1.append(arr[j])
            list2.append(list1)
            list1 = []
            if i == len(arr) - 1:
                if (len(arr) - 1) % 2 == 0:
                    break
            else:
                j = j + 2
        else:
            list1.append(arr[i])
            list1.append(arr[j])
            list2.append(list1)
            list1 = []
            if i == len(arr) - 1:
                if (len(arr) - 1) % 2 == 0:
                    break
            else:
                j = j + 2
divide = divide//2
print(list2)
'''

'''    if i == len(arr) - 1:
        if (len(arr) -1) %2 == 0:
            print(j)
        break
    else:
        j = j + 2'''
# print(j)
'''   if arr[i] > arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        if len(arr) - 1 % 2 == 0:
            break
        else:
           j = j + 2
   else:
       if len(arr) - 1 % 2 == 0:
           break
       else:
           j = j + 2
'''

'''def to_verify(arr,k):
    return arr,k
arr = [1, 2, 3]
k = 3
print(to_verify(k,arr))'''

'''def tochecknumber(arr,k):
    count = 0
    list1 = []
    list2 = []
    if arr[len(arr) - 1] == k:
        arr.append(0)
        count = count + 1
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] ^ arr[j] == k:
                    list1.append(arr[i])
                    list1.append(arr[j])
                    list2.append(tuple(list1))
                    list1 = []
        list2 = tuple(list2)
        #return list2
    else:
        for i in range(k):
            if arr[0] + arr[len(arr) - 1] == k:
                pass
            else:
                arr.append(arr[len(arr) - 1] + 1)
                count = count + 1
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] ^ arr[j] == k:
                    list1.append(arr[i])
                    list1.append(arr[j])
                    list2.append(tuple(list1))
                    list1 = []
        list2 = tuple(list2)
        #return count,list2
    return count,list2


arr = [1, 2, 3]
k = 3
print(tochecknumber(arr,k))
'''

'''arr = [1,2,3]
k = 3
count = 0
list1 = []
list2 = []
if arr[len(arr)-1] == k:
    arr.append(0)
    count = count + 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                list1.append(arr[i])
                list1.append(arr[j])
                list2.append(tuple(list1))
                list1 = []
    list2 = tuple(list2)
else:
    for i in range(k):
        if arr[0] + arr[len(arr) -1] == k:
            pass
        else:
            arr.append(arr[len(arr) - 1] + 1)
            count = count + 1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == k:
                list1.append(arr[i])
                list1.append(arr[j])
                list2.append(tuple(list1))
                list1 = []
    list2 = tuple(list2)

print(count)
print(list2)
'''

'''import math

def is_smart_number(num):
    if num == 2:
        return False
    val = int(math.sqrt(num))
    if num%val == 0:
        return True
    return False


list1 = []
for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        list1.append("YES")
        #print("YES")
    else:
        list1.append("NO")
        #print("NO")
#print(list1)
for item in list1:
    print(item)
'''

'''list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10,12,89,90]
list3 = []
lengh1 = len(list1)
i = 0
j = 0
while i < len(list1) and j < len(list2):
    list3.append(list1[i])
    list3.append(list2[j])
    if i == lengh1:
        lengh1 = lengh1 + 1
        print(i)
        print(lengh1)
    i = i + 1
    j = j + 1
    print(lengh1)
    if i == lengh1 and j != len(list2):
        print(list2[j])


print(list3)
'''

'''list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10,12]
list3 = []
i = 0
j = 0
while i < len(list1) -1 and j < len(list2) - 1:
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i = i + 1

    if list1[i] > list2[j]:
        list3.append(list2[j])
        j = j + 1
    if i == len(list1) - 1 or j == len(list2) - 1:
        if list1[i] < list2[j]:
            #print(list3)
            list3.append(list1[i])
            list3.append(list2[j])

if i == len(list1) - 1 and j != len(list2) - 1:
    list3.append(list2[j])
    j = j + 1
if j == len(list2) - 1 and i != len(list1) - 1:
    list3.append(list1[i])
    i = i + 1

print(list3)
'''

'''# prgram of calculator
x = int(input("welcome how many items customer purchase:"))
dict1 = {}
for i in range(1,x+1):
    a,b = input(f"enter item name and price of {i}th  ---if you giving name and then please give space before enter price---:").split(" ")
    b = int(b)
    dict1[a] = b
total = 0
for key,value in dict1.items():
    total = total + value
print("this is total bill",total)
print("Thankyou ---visit again in our store---")
'''

'''def func(**kwargs):
    for k , value in kwargs.items():
        d = lambda value : value + 5
        print(k ,"=", value,d(value))
b = func(a = 1, b = 9)
'''

'''def bigSorting(unsorted):
    list1 = []
    for i in range(len(unsorted)):
        list1.append(int(unsorted[i]))
    for j in range(len(list1)):
        for k in range(j+1,len(list1)):
            if list1[j]> list1[k]:
                list1[j],list1[k] = list1[k],list1[j]
    for l in list1:
        print(l)
    


n = int(input().strip())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    if int(unsorted_item) < 0:
        break
    else:
      unsorted.append(unsorted_item)

result = bigSorting(unsorted)
'''

'''def bigSorting(unsorted):
    list1 = []
    for i in range(len(unsorted)):
        list1.append(int(unsorted[i]))
    for j in range(len(list1)):
        for k in range(i+1,len(list1)):
            if list1[j]> list1[k]:
                list1[j],list1[k] = list1[k],list1[j]
    return list1


unsorted = ["10","70","1","100000","78"]
print(bigSorting(unsorted))
'''

'''unsorted = ["10","70","1","100000","78"]
list1 = []
for i in range(len(unsorted)):
    list1.append(int(unsorted[i]))
for j in range(len(list1)):
    for k in range(j+1,len(list1)):
        if list1[j] > list1[k]:
            list1[j],list1[k] = list1[k],list1[j]
print(list1)
'''

'''def unsorted1(unsorted):
    list1 = []
    for i in range(len(unsorted)):
        list1.append(int(unsorted[i]))
    for j in range(len(list1)):
        for k in range(j+1,len(list1)):
            if list1[j]> list1[k]:
                list1[j],list1[k] = list1[k],list1[j]
    return list1

unsorted = ["10","70","1","100000","78"]
print(unsorted1(unsorted))
'''

'''grid = list(map(str, input().split(" ")))
print(grid)
'''
# import os
'''def gridChallenge(grid):
    list2 = []
    b = ""
    for i in range(len(grid)):
        list1 = []
        for j in range(len(grid[i])):
            b = b + str(ord(grid[i][j]))
            list1.append(int(b))
            b = ""
        list1.sort()
        list2.append(list1)
    # print(list2)
    str3 = ""
    list5 = []
    for k in range(len(list2)):
        list4 = []
        for l in range(len(list2[k])):
            str3 = str3 + chr(list2[k][l])
            list4.append(str3)
            str3 = ""
        list5.append(list4)

    # print(list5)
    list6 = []
    str6 = ""
    for m in range(len(list5)):
        for n in range(len(list5[m])):
            str6 = str6 + list5[m][n]
        list6.append(str6)
        str6 = ""
    # print(list6)
    o = 0
    p = 1
    count = 0
    dcount = 0
    while o < len(list6) and p < len(list6):
        q = 0
        if count == 1:
            break
        if len(list6[o]) != len(list6[p]):
            #print("NO")
            break
        else:
            while q < len(list6[o]):
                if ord(list6[o][q]) < ord(list6[p][q]):
                    q = q + 1
                else:
                    # print("there is not grid match between them in strings")
                    count = count + 1
                    break
            o = o + 1
            p = p + 1
    if p == len(list6):
        print("YES")
    else:
        print("NO")




t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)
'''

'''grid = ["abcd","efgh","ijkl"]
list2 = []
b = ""
for i in range(len(grid)):
    list1 = []
    for j in range(len(grid[i])):
        b = b + str(ord(grid[i][j]))
        list1.append(int(b))
        b = ""
    list1.sort()
    list2.append(list1)
#print(list2)
str3 = ""
list5 = []
for k in range(len(list2)):
    list4 = []
    for l in range(len(list2[k])):
        str3 = str3 + chr(list2[k][l])
        list4.append(str3)
        str3 = ""
    list5.append(list4)

#print(list5)
list6 = []
str6 = ""
for m in range(len(list5)):
    for n in range(len(list5[m])):
        str6 = str6 + list5[m][n]
    list6.append(str6)
    str6 = ""
#print(list6)
o = 0
p = 1
count = 0
dcount = 0
while o < len(list6) and p < len(list6):
    dcount = dcount + 1
    q = 0
    if count == 1:
        break
    if len(list6[o]) != len(list6[p]):
        print("NO")
        break
    else:
        while q < len(list6[o]):
            if ord(list6[o][q]) < ord(list6[p][q]):
                q = q + 1
            else:
                #print("there is not grid match between them in strings")
                count = count + 1
                break
        o = o + 1
        p = p + 1
if dcount == len(list6) - 1:
    print("YES")
else:
    print("NO")
'''

'''
    while q < len(list6[o]):
        if ord(list6[o][q]) < ord(list6[p][q]):
            q = q + 1
        else:
            print("there is not grid match between them in strings")
            count = count + 1
            break

    o = o + 1
    p = p + 1

'''

'''for i in range(len(a)):
    b = b + str(ord(a[i]))
    list1.append(int(b))
    b = ""
list1.sort()
print(list1)

'''

'''def totalprice(keyboard_price,drives_price):
    total = 0
    for i in range(len(keyboard_price)):
        for j in range(len(drives_price)):
            temp_total = 0
            temp_total = temp_total + keyboard_price[i] + drives_price[j]
            if temp_total >= b:
                break
            if temp_total > total:
                total = 0
                total = total + temp_total
    return "This is total price where is max as campare to b ",total

b, total_keyboard, total_drives = list(map(int, input("enter the content").split(" ")))
keyboard_price = list(map(int,input("enter  price of keyboard").split(" ")))
drives_price = list(map(int,input("enter price of drives").split(" ")))
if total_keyboard != len(keyboard_price) or total_drives != len(drives_price):
    raise "you have need to enter a proper number pf elements"
print(totalprice(keyboard_price,drives_price))
'''

'''b = 10
keyboard = [3,1]
drives = [5,2,8]
total = 0
for i in range(len(keyboard)):
    for j in range(len(drives)):
        temp_total = 0
        temp_total = temp_total + keyboard[i] + drives[j]
        if temp_total >= b:
            #print(i)
            #print(j)
            break
        if temp_total > total:
            total = 0
            total = total + temp_total
print(total)
'''

# temp_total = 0
# else:
# temp_total = temp_total + keyboard[i] + drives[j]


'''str1 = "UDDDUDUU"
s = 0
for item in str1:
    if item == "U":
        s = s + 1
        #print(s)

    else:
        print(s)
        s = s - 1
        print(s)
#print(s)
'''

'''arr = list(map(int,input("enter a number").split(" ")))
print(arr)

'''

'''arr = [1,2 ,100,4,5,6,7]
for i in range(1,len(arr)):
    if arr[i] < arr[i -1]:
        print(i - 1)
        break
else:
    print(-1)

'''

'''def toarray(arr):
    # arr = list(map(int,input()))
    arr = list(map(int,arr))
    for i in range(len(arr)):
        if arr[i] > arr[i] - 1:
            return i - 1
    return -1

#arr = list(map(int,input("enter a number")))

print(toarray(input().split(" ")))'''
'''list1 = ["sawan",1,"patel",2]
dict1 = {}
count = 0
for i in range(len(list1)):
    #count = count + 1
    if i%2 == 0 or i == 0:
        dict1[list1[i]] = list1[i + 1]
print(dict1)
'''
# else:
# dict1[list1[i]] = list1[i + 1]


'''n = 10
total = 0
count = 0
for i in range(1,n+1):
    total = total + i
    print(total)
    count = count + 1
average = total/count
print(total)
print(average)
'''

'''list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
list2 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
list3 = []
add = 0
for i in range(len(list1)):
    list4 = []
    for j in range(len(list1[i])):
        list4.append(list1[i][j] + list2[i][j])
    list3.append(list4)
print(list3)
'''

'''
str1 = "hello world"
str2 = ""
str3 = ""
for i in range(len(str1)):
    if str1[i] == " ":
        str3 = str3 + str2 + " "
        str2 = ""
    else:
        str2 = str1[i] + str2
    if i == len(str1) -1:
        str3 = str3 + str2


print(str3)

'''

'''n = 10
for i in range(2,n):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
'''

'''arr = [1,2,3,4,5]
arr2 = []
for i in arr:
    arr2.append(i)
arr.sort()
if arr2 == arr:
    print(True)
else:
    print(False)

'''

'''arr = [1,2,3,4,5]
arr2 = []
for i in arr:
    arr2.append(i)
list1 = []
for i in range(len(arr)):
    j = 0
    k = 1
    while j < len(arr) - (1+i) and k < len(arr) -i :
        if arr[j] > arr[k]:
            arr[j],arr[k] = arr[k],arr[j]
        j = j + 1
        k = k + 1
if arr == arr2:
    print(True)
else:
    print(False)
'''

'''arr = [1,2,3,4,5]
minimum = 0
maximum = 0
total = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            pass
        else:
            total = total + arr[j]
    if i == 0:
        maximum = maximum + total
        minimum = minimum + total
    elif total > maximum:
        maximum = 0
        maximum = maximum + total
    elif total < minimum:
        minimum = 0
        minimum = minimum + total
    total = 0
print(maximum,minimum)
'''

'''try:
    a = int(input("enter a number"))
    b =  int(input("enter a number"))
    c = a + b
    print(c)
except:
    print("there is error")
finally:
    print("try catch run succesfully")

'''

'''n = 5
list1 = [1,1,0,-1,-1]
postive_count = 0
negative_count = 0
zero_count = 0
for item in list1:
    if item < 0:
        negative_count = negative_count + 1
    elif item > 0:
        postive_count = postive_count + 1
    else:
        zero_count = zero_count + 1

postive_ratio = postive_count/n
negative_ratio = negative_count/n
zero_ratio = zero_count/n
print(postive_ratio," ",negative_ratio," ",zero_ratio)
'''

'''a,c = map(int,input("enter a number").split(" "))
b = list(map(int,input("enter a list of bill").split(" ")))
d_charged = int(input("enter the charged split"))
total = 0
for i in range(len(b)):
    if c == i:
        pass
    else:
        total = total + b[i]
split = total/2
if d_charged == split:
    print("Bon Apetite")
else:
    actual_split = d_charged - split
    print(int(actual_split))

'''

'''n = 5
for i in range(n):
    for j in range(0,n):
        if i == 0:
            print("*",end="")
        elif i == n-1:
            print("*",end="")
        else:
            if j == 0 or j == n - 1:
                print("*",end="")
            else:
                print(" ",end="")
    print()
'''

'''n = 10
for i in range(2,n):
    for j in range(2,i):
        print(j)
        if i%j == 0:
            break
   else:
        print(i)'''

'''str1 = "aaabccdddee"
str2 = ""
i = 0
while i < len(str1):
    j = i
    if j == len(str1)-1:
        if str1[j-1] == str1[j]:
            break
        else:
            str2 = str2 + str1[j]
    k = i + 1
    while j < i+1:
        if str1[j] == str1[k]:
            j = j + 1
        else:
            str2 = str2 + str1[j]
            str2 = str2 + str1[k]
            j = j + 1
    i = i + 2
print(str2)
'''

'''str1 = "aaabccddd"
str2 = ""
for i in range(0,len(str1)-1):
    for j in range(i+1,i+2):
        print(str1[j])'''

'''arr =[4, 5, 3, 7, 2]
left = []
equal = [arr[0]]
right = []
for i in range(1,len(arr)):
    if arr[i] > equal[0]:
        right.append(arr[i])
    elif arr[i] < equal[0]:
        left.append(arr[i])
    else:
        pass
'''

'''a = [1, 2, 3]
b = [3, 2, 1]
alicerate = 0
bobrate = 0
for i in range(len(a)):
    if a[i] > b[i]:
        alicerate = alicerate + 1
    elif a[i] < b[i]:
        bobrate = bobrate + 1
    else:
        pass

print(alicerate,"    " ,bobrate)

'''

'''n = 4
for i in range(n):
    count = n-1
    for j in range(n):
        if i < count:
            count = count - 1
            print(" ",end="")
        else:
            print("#",end="")
    print()
'''

'''x1 = 0
v1 = 2
x2 = 5
v2 = 3
flag = True
jump1 = x1
jump2 = x2
if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1):
    print("No")
else:
    while flag:
        jump1 = jump1 + v1
        jump2 = jump2 + v2
        if jump1 == jump2:
            flag = False
    print("this is jump where the two kangoroes meeet",jump1)
'''

'''list1 = [3 ,4 ,21 ,36, 10, 28, 35, 5 ,24, 42]
highest = 0
minimum = 0
high_count = 0
mini_count = 0
for i in range(len(list1)):
    if i == 0:
        highest = highest + list1[i]
        minimum = minimum + list1[i]
    if list1[i] > highest:
        highest = 0
        highest = highest + list1[i]
        high_count = high_count + 1
    if list1[i] < minimum:
        minimum = 0
        minimum = minimum + list1[i]
        mini_count = mini_count + 1

print(mini_count, high_count)

'''

'''list1 = [10, 20, 20, 10,30, 50, 10, 20]
pair = 0
lenght = len(list1)
for i in range(lenght):
    for j in range(i+1,lenght):
        if list1[i] == list1[j]:
            pair = pair + 1
            list1.remove(list1[j])
            list1.remove(list1[i])
            #lenght = lenght - 2
            lenght = len(list1)
            break
print(pair)

'''

'''
list1 = [10, 20, 20, 10,30, 50, 10, 20]

#length = len(list1)
pair = 0
i = 0
while i < len(list1):
    j = i + 1
    #print(i)
    while j < len(list1):
        #print(j)
        if list1[i] == list1[j]:
            pair = pair + 1
            list1.pop(j)
            list1.pop(i)
            break
        j = j + 1
    else:
        i = i + 1
print(pair)
print(list1)
'''

'''list1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pair = 0
lenght = len(list1)
for i in range(lenght):
    #print(lenght)
    j = i+1

    while j < lenght:
        #print(i)
        #print(j)
        if list1[i] == list1[j]:
            pair = pair +1
            list1.remove(list1[i])
            #list1.remove(list1[j])
            lenght = lenght - 2
            break
        j = j + 1

print(list1)
print(pair)
'''

'''import json as js
x = '{"name":"sawan","age": 78}'
y = js.loads(x)
print(y["age"])
'''

'''class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def move(self):
        print("move1")
class car(Vehicle):
    pass

class boat(Vehicle):
    def move(self):
        print("sail")
class aeroplane(Vehicle):
    def move(self):
        print("fly")


car1 = car("mahindra", 2008)
boat1 = boat("hodo", 60779)
aeroplane1 = aeroplane("boeing",2018)
for x in (car1,boat1,aeroplane1):
    print(x.model, x.year), x.move()
'''

'''class car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def move(self):
        print("run")
class boat:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def move(self):
        print("waving")
class jet:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def move(self):
        print("fly")


car1 = car("hundyai","2018")
boat1 = boat("hodo","7883")
jet1 = jet("boeing","2021")
for x in(car1,boat1,jet1):
    x.move()
'''

'''count = False
try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    try:
        divide = a/b
        print(divide)
        count = True
    except:
        print("there is error in inner block of try")
except:
    print("this is error in outer block try")

if count is True:
    print("try block succesfully run")
'''

'''list1 = list(map(int,input("enter number").split(" ")))
fre = [0] * (max(list1) + 1)
for item in list1:
    fre[item] = fre[item] + 1
count = 0
index = 0
for i in range(len(fre)):
    if count < fre[i]:
        #print("chvh")
        #print(index)
        count = 0
        index = 0
        count = count + fre[i]
        index = index + i

'''

'''n = int(input())
str1 = str(input())
replace = str(input())
str2 = str(input())
list1 = []
str4 = ""
index = 0
for item in range(len(str1)):
    if str1[item] == " ":
        list1.append(str4)
        str4 = ""
    else:
        str4 = str4 + str1[item]
        if item == len(str1) - 1:
            list1.append(str4)
for i in range(len(list1)):
    if replace == list1[i]:
        index = i
        list1.remove(replace)
        list1.insert(index,str2)
for item in list1:
    print(item, end=" ")

'''

'''list1 = [4,4,2,1,11]
add = 0
for i in range(len(list1)):
    for j in range(0,len(list1)):
        if list1[i] == list1[j]:
            pass
        else:
            add = add + list1[j]
    if add == list1[i]:
        print(i+1)
    else:
        add = 0
'''

'''n1,n2 = map(int,input("enter").split(" "))
count = 0
armstrong = 0
for number in range(n1,n2+1):
    str1 = str(number)
    lenght = len(str1)
    #print(str1)
    for item in str1:
        armstrong = armstrong + int(item) ** lenght
    #print(armstrong)
    if armstrong == number:
        print("this number is armstrong",number)
        count = count + 1
    armstrong = 0
if count == 0:
    print("there is no armstrong")
'''

# armstrong = armstrong + int(item) ** lenght


'''n = 153
armstrong = 0
str1 = str(n)
lenght = len(str1)
for i in str1:
    armstrong = armstrong + int(i)**lenght
    print(armstrong)
if armstrong == n:
    print("this is armstrong")'''

'''str1 = "hello world sawan patel"
str2 = "sawan patel"
count = 0
j = 0
k = 0
index = 0
while j < len(str1):
    if str1[j] == " " and str1[j] != str2[k]:
        j = j + 1
        #k = k + 1
        pass
    else:
        # print(j)
        if str1[j] == str2[k]:

            if index == 0:
                index = j+1
            count = count + 1

            j = j + 1
            k = k + 1
            if count == len(str2) - 1:
                print(index)
        else:
            index = 0
            count = 0
            j = j + 1
            k = k + 1
        if k == len(str2):
            k = 0
'''

'''arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
c = 0
#for i in range(1):
j = 1
# print(j)
while j < len(arr):
    # print(j)
    if arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        if j > 1:
            # print(j)
            j = j - 1
        else:
            j = j + 1
    else:
        j = j + 1

    print(arr)
    c = c + 1

#print(arr)
print(c)
'''

'''arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr.insert(i,arr[j]),arr.pop(j+1)
            print(arr)
'''

'''arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)

#print(arr)
'''

'''no = 11
print("even number" if no%2 == 0 else "odd")'''

'''arr = [13,46,24,52,20,9]
n = len(arr)
for i in range(n-1):
    mini = i
    for j in range(i+1,n):
        if arr[mini] > arr[j]:
            arr[mini],arr[j] = arr[j],arr[mini]
        #print(arr)
            #break

print(arr)
'''

"""list1 = [89,45,34,24,13,32,90]
count = 0
for i in range(len(list1)):
    j = 0
    k = 1
    while j < len(list1) - (i + 1) and k < len(list1) - i:
        if list1[j] < list1[k]:
            list1[k],list1[j] = list1[j],list1[k]
        j = j + 1
        k = k + 1
print(list1)
"""

'''str1  = "sawan patels"
# str2 = ""
# for i in range(len(str1)):
#     str2 = str1[i] + str2
# print(str2)
str2 = ""
set1 = set(str1)
print(set1)
sort = list(set1)
sort.sort()
print(sort)
'''

'''list1 = [89,45,34,24,13,32,90]
list_max = 0
list_min = 0
for i in range(1):
    for j in range(i, len(list1)):
        print(i)
        if i == 0 and j == 0:
            list_max = list_max + list1[i]
            list_min = list_min + list1[i]
        if list_min > list1[j]:
            list_min = 0
            list_min = list_min + list1[j]
        if list_max < list1[j]:
            list_max = 0
            list_max = list_max + list1[j]
print(list_max)
print(list_min)
'''

'''list1 = [89,45,34,24,13,32,90]
list_max = 0
list_min = 0
for j in range(0, len(list1)):
    if j == 0:
        list_max = list_max + list1[j]
        list_min = list_min + list1[j]
    if list_min > list1[j]:
        list_min = 0
        list_min = list_min + list1[j]
    if list_max < list1[j]:
        #print(list_max)
        list_max = 0
        #print(list_max)
        list_max = list_max + list1[j]
print(list_max)
print(list_min)
'''

'''def fibo(n):
    if n <= 2:
        return 1
    else:
        fibo(n-2) + fibo(n-1)
        print()'''

'''list1 = [89,45,34,24,13,32,90]
i = 0
count = 0
for i in range(1,(len(list1) - count) + 1):
    #print(i)
    j = 0
    k = 1
    while j < len(list1) - (i + 1) and k < len(list1) - i:
        #print(j)
        #print(k)
        if list1[j] > list1[k]:
            list1[j], list1[k] = list1[k], list1[j]
            print(list1[j])
            print(list1[k])
        j = j + 1
        k = k + 1

print(list1)
'''

'''list1 = [89,45,34,24,13,32,90]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
           list1[i] , list1[j] = list1[j], list1[i]
           print(list1)

'''

'''str1 = "abcdea"
blank_list = [0]*5
list2 = []
for i in range(len(str1)):
    blank_list[ord(str1[i]) - ord("a")] = blank_list[ord(str1[i]) - ord("a")] + 1
print(blank_list)

'''

'''list1 = [[1,2,8],
         [3,4,9]]
list2 = [[5,6],
         [7,8],
         [10,11]]
list3 = []
add = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1)):
            list3 = list1[i][j]*list2[j][k]
            add = add + list3
            if k == len(list1) - 1:
                print(add,end=" ")
                add = 0
    print()
'''

'''list1 = []
list2 = []
i = 0
while i < 3:
    list1 = list(map(int,input("enter a number").split()))
    list2.append(list1)
    i = i + 1
print(list2)'''

'''def forzero(list1):
    list2 = []
    index = ("-inf")
    index2 = ("-inf")
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][j] == 0:
                index2 = i
                index = j
    for i in range(len(list1)):
        list3 = []
        for j in range(len(list1[i])):
            if index2 != i:
                if j == index:
                    list1[i][j] = 0
                    list3.append(list1[i][j])
                else:
                    list3.append(list1[i][j])
        if list3 == []:
            pass
        else:
            list2.append(list3)
        list4 = []
        if i == index2:
            for k in range(len(list1[i])):
                list1[i][k] = 0
                list4.append(list1[i][k])
            list2.append(list4)
    print(list2)


list1 = []
list2 = []
i = 0
while i < 3:
    list1 = list(map(int,input("enter a number").split()))
    list2.append(list1)
    i = i + 1
forzero(list2)
'''

'''list1 = [[1,1,1],
         [1,0,1],
         [1,1,1]]'''

'''list1 = [[1,1,1],
         [1,0,1],
         [1,1,1]]
list2 = []
index = ("-inf")
index2 = ("-inf")
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] == 0:
            index2 = i
            index = j
for i in range(len(list1)):
    list3 = []
    for j in range(len(list1[i])):
      if index2 != i:
        if j == index:
            list1[i][j] = 0
            list3.append(list1[i][j])
        else:
            list3.append(list1[i][j])
    if list3 == []:
        pass
    else:
        list2.append(list3)
    list4 = []
    if i == index2:
        for k in range(len(list1[i])):
            list1[i][k] = 0
            list4.append(list1[i][k])
        list2.append(list4)
print(list2)
'''

'''list1 = [[1,1,1],
         [1,0,1],
         [1,1,1]]
list2 = []
index = ("-inf")
index2 = ("-inf")
for i in range(len(list1)):
    list3 = []
    for j in range(len(list1[i])):
        if list1[i][j] == 0:
            index2 = i
            index = j
        if j == index:
            list1[i][j] = 0
            list3.append(list1[i][j])
        else:
            list3.append(list1[i][j])
    list2.append(list3)

print(list2)
print(index)
'''

'''#list1 =  ["flower","flow","flight"]
list1 = ["cow","cower","cowex"]
str1 = list1[0]
str2 = ""
for i in range(1,len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] in str1:
            str2 = str2 + list1[i][j]
        else:
            str1 = ""
            str1 = str1 + str2
    str1 = ""
    str1 = str1 + str2
    if i == len(list1) - 1:
        print(str2)
    if str2 == "":
        print("there is no common prefix in this array")
        break
    else:
        str2 = ""
'''

'''#list1 =  ["flower","flow","flight"]
list1 = ["cow","cower","cowex"]
str1 = list1[0]
str2 = ""
for i in range(1,len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] in str1:
            str2 = str2 + list1[i][j]
        if list1[i][j] not in str1:
            print("there is no common prefix in this list")
            break
    if i == len(list1) - 1:
        print(str2)
    else:
        str2 = ""
'''

'''list1 = [1,2,3,4]
product = 1
list2 = []
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            pass
        else:
            product = product*list1[j]
    list2.append(product)
    product = 1
print(list2)'''

'''n = 9
str1 = str(n)
len_str1 = len(str1)
sum = 0
for i in str1:
    sum = sum + int(i)**len_str1
if sum == n:
    print("the number is armstrong number")
else:
    print("this is number is not armstrong number")

'''

'''list1 = [12,1,5,8,9,1,2]
frequency = [0] * 13
for i in list1:
    frequency[i] = frequency[i] + 1
print(frequency)

'''

'''str1 = "abcdefghijklmnopqrstumvwxyz"
frequncy_array = [0]*26
for i in str1:
    frequncy_array[ord(i) - ord("a")] = frequncy_array[ord(i) - ord("a")] + 1
print(frequncy_array)'''

'''s = "geeksforgeeks"
freqency_array = [0] * 26
for char in s:
    freqency_array[ord(char) - ord("a")] += 1
print(freqency_array)'''

'''str1 = "abcabopicbb"
i = 0
str2 = ""
list1 = []
list2 = []
for i in range(len(str1)):
    for j in range(i,len(str1)):
        if str1[j] not in str2:
            str2 = str2 + str1[j]
        else:
            list1.append(str2)
            list2.append(len(str2))
            #list2.append(list1)
            #list1 = []

            str2 = ""
            str2 = str2 + str1[j]
        if j == len(str1) - 1:
            str2 = ""
count = 0
str4 = ""
str5 = ""
for i in range(len(list1)):

    if list2[i] > count:
        str4 = str4 + (list1[i])
        str5 = str5 + str4
        count = count + list2[i]
        print(str4e)
        str4 = ""
print(str4)




print(list1)
print(list2)
'''

'''str1 = "abcabopicbb"
i = 0
str2 = ""
list1 = []
list2 = []
for i in range(len(str1)):
    for j in range(i,len(str1)):
        if str1[j] not in str2:
            str2 = str2 + str1[j]
        else:
            list1.append(str2)
            list1.append(len(str2))
            list2.append(list1)
            list1 = []
            str2 = ""
            str2 = str2 + str1[j]
        if j == len(str1) - 1:
            str2 = ""
print(list2)
count = 0
str3 = ""
for i in range(len(list2)):
    for j in range(len(list2[i])):
        if list2[i][1] > count:
            count = count + list2[i][1]
            str3 = str3 + list2[i][0]
            
'''

'''n = 10
list1 = [10,57,24,10,56,2,24]
my_dict = {}
for i in range(len(list1)):
    if list1[i] not in my_dict:
        my_dict[list1[i]] = 1
    else:
        my_dict[list1[i]] = my_dict.get(list1[i]) + 1
print(my_dict.get(n))
'''

'''def non_repeating(str1):
    str2 = ""
    for i in range(len(str1)):
        for j in range(i + 1, len(str1)):
            if str1[i] != str1[j]:
                # str2 = str2 + str1[i]
                if str1[i] not in str2:
                    return str1[i]
            else:
                if str1[i] not in str2:
                    str2 = str2 + str1[i]
        if i == len(str1) - 1:
            return "-"

str1 =  "ssiskks"
print(non_repeating(str1))
'''

'''def non_repeating(input):
    for i in range(len(input)):
        for j in range(0,len(input)):
            if input[i] == input[j]:
                break
        else:
            return input[i]


input = "swisws"
print(non_repeating(input))
'''

'''list1 = [2,8,1,4,9]
list2 = [10,15,3,16,19]
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] < list2[j]:
            pass
            #list3.append(list1[i])
        else:
            break
    else:
        list3.append(list1[i])

print(list3)
'''

'''n = 8
for i in range(n):
    for j in range(i):
        if i == j + i :
         print(" "*(n-i),"*",end="")
        else:
            print(" *",end="")
    print()
'''

'''n = 8
f1 = 0
f2 = 1
list = []
if n == 1 or n  == 0:
    print(0)
for i in range(n):
    res = f1 + f2
    f1 = f2
    f2 = res
    list.append(res)
print(list)'''

'''n = 50
i = 2
while i < n:
    j = 2
    while i > j:
        if i%j == 0:
            #j = j + 1
            break
        else:
            j = j + 1
    else:
        print(i)
    i = i + 1'''

'''n = 20
i = 2
while i < n:
    j = 2
    while i > j:
        if i%j == 0:
            break
        else:
           j = j + 1
    else:
        print(i)
    i = i + 1
'''

'''n =  50
if n == 1:
    print(1)
if n == 2:
    print(2)
f1 = 1
f2 = 1
for i in range(n):
    res = f1 + f2
    f1 = f2
    f2 = res
    print(res)'''

'''str1 = "abcd"
count = 0
dcount = 1
for k in range(len(str1)):
    for i in range(len(str1)):
        for j in range(count, len(str1) - i):
            if i == len(str1) - dcount:
                count = count + 1
                dcount = dcount + 1
            print(str1[j], end="")
        print(end=" ")

'''

'''list1 = [11,1,2,8,10,11,15,7,12,6]
target = 18
list2 = []
max_product = 0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] + list1[j] == target:
            if list1[i] in list2:
                break
            if list1[i] * list1[j] > max_product:
                list2 = []
                max_product = list1[i] * list1[j]
                list2.append(list1[i])
                list2.append(list1[j])
for k in list2:
    print(k,end=" ")
'''

'''n = 5
list1 = []
for j in range(1,n+1):
    binary = bin(j)[2:]
    list1.append(binary.replace("0","1"))
    list1.append(binary.replace("1","2"))
print(list1)'''

# print(bin(n)[2:])


'''number = 54
str1 = str(number)
to_check = 0
for i in str1:
    to_check = to_check + int(i)

for j in range(2,to_check):
    if to_check % j == 0:
        print("No")
        break
else:
    print("Yes")
'''

'''list1 = [11,1,2,8,10,11,15,7]
target = 18
list2 = []
max_product = 0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] + list1[j] == target:
            if list1[i] and list1[j] not in list2:
                list2.append(list1[i])
                list2.append(list1[j])
i = 0
j = 1
max_product = 0
list3 = []
while i < len(list2) and j < len(list2):
    list3.append(list1[i])
    list3.append(list1[j])
    if (list2[i] * list2[j]) > max_product:
        print()
        list3 = []
        list3.append(list1[i])
        list3.append(list1[j])
        #print(list2[i], list2[j])
    i = i + 2
    j = j + 2
'''

'''list1 = [11,1,2,8,10,11,15,7]
target = 18
list2 = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] + list1[j] == target:
            if list1[i] and list1[j] not in list2:
              list2.append(list1[i])
              list2.append(list1[j])
i = 0
j = 1
product1 = {}
while i < len(list2) and j < len(list2):
    product = list2[i] * list2[j]
    product1[product] = list2[i], list2[j]
    i = i + 2
    j = j + 2
for key, values in product1.items():
    print(product1.values())
'''

'''str1 = "hello i am developer"
k = 3
str2 = ""
count = 0
n = len(str1)
for i in range(n):
    if str1[i] == " ":
        print(str2, end=" ")
        count = count + 1
        str2 = ""
        if count == k:
            break
    else:
        str2 = str2 + str1[i]
'''

'''string = "examinations"
str2 = ""
count = 0
for char in range(len(string)):
    if char == 0:
        str2 = str2 + string[char]
    else:
        count = count + 1
    if char == len(string) - 1:
        count = count - 1
        str3 = str(count)
        str2 = str2 + str3
        str2 = str2 + string[char]
print(str2)
'''

'''m = 5
n = m*2j
for i in range(1, n + 1):
    if i % 2 != 0:
        for k in range(n - i, 0, -1):
            if k == n - i:
              print(" "*k, "* "*i,end=" ")
        print()
'''

'''print()
    else:
        for k in range(n - i, 0, -1):
            print(" ")
           for j in range(1, i + 1):
            print("&", end="")
print()
'''

'''for i in range(5 ,0, -1):
    for j in range(0, i):
        print(i,end="")
    print()
'''

'''n = 20
i = 2
while i < n:
    j = 2
    while i > j:
        if i%j == 0:
            break
        else:
           j = j + 1
    else:
        print(i)
    i = i + 1'''

'''list1 = [0, -1, 2, -3, 4]
target = -1
for i in range(len(list1)):
    if i == len(list1) - 1:
        if target == list1[len(list1)-1]:
            print(list1[len(list1)-1])
        break
    for j in range(i+1,i+2):
        if list1[i] + list1[j] == target:
            print(list1[i],list1[j])
'''

'''low = 10
high = 15
arr = [10,10, 12, 11, 15]
hash_list = [0] * (high + 1)
for i in range(len(arr)):
    print(hash_list[arr[i]])
    print(arr[i])'''

'''   if arr[i] not in hash_list[arr[i]]:
        hash_list[arr[i]] = 1
    else:
        hash_list[arr[i]] = hash_list[arr[i]] + 1
        print(i)'''

'''    if i in hash_list:
        hash_list[arr[i]] = hash_list[arr[i]] + 1'''

# else:
# hash_list[arr[i]] = hash_list[arr[i]] + 1
# print(i)


'''low = 10
high = 15
arr = [10,10, 12, 11, 15]
n = len(arr)
my_dict =  {10:1}
i = 0
count = 0
for i in range(low, high+1):
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] = my_dict.get(i) + 1
print(my_dict)

for key, value in my_dict.items():
    if key not in arr:
        print(key)
 '''

'''low = 10
high = 15
arr = [10,10, 12, 11, 15]
n = len(arr)
count = 0
for i in range(low, high+1):
    count = count + 1
'''

'''arr = [10, 12, 11, 15]
high =15
low = 10
n = len(arr)
for i in range(low, high+1):
    for j in range(n):
        if i not in arr:
            print(i)
            break
'''

'''n = 50
i = 2
while i < n:
    j = 2
    while j < i:
        if i%j == 0:
          break
        if j == i - 1:
           print(i)
        j = j + 1
    i = i + 1
'''

'''for i in range(2,n):
    for j in range(2,i):
        if i%j == 0:
            break
            
        if j == i - 1:
            print(i)

'''

'''#two array and i need to find union both of them

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
list1 = []
for i in range(len(a)):
    if a[i] not in list1:
        list1.append(a[i])
        for j in range(len(b)):
            if a[i] != b[j] and b[j] not in list1:
                list1.append(b[j])

print(list1)


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2,4]
list1 = []
for i in range(len(a)):
    if a[i] not in list1:
        list1.append(a[i])
        #for j in range(len(b)):
    if a[i] != b[i] and b[i] not in list1:
        list1.append(b[i])

print(list1)
'''

'''arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
freq = [0] * 22
for n in arr1:
    freq[n] = freq[n] + 1
for j in arr2:
    if freq[j] == 0:
        print("its not subset")
        break
else:
    print("set")
'''

'''s = "geeksforgeeks"
freqency_array = [0] * 26
for char in s:
    freqency_array[ord(char) - ord("a")] += 1
print(freqency_array)
'''

'''def norepeating(str1):
    my_dict = {}
    for i in range(len(str1)):
        if str1[i] not in my_dict:
            my_dict[str1[i]] = 1
        else:
            my_dict[str1[i]] = my_dict[str1[i]] + 1
    for key,value in my_dict.items():
        if value == 1:
           return str1.index(key)

s = "geeksorgeeks"
print(norepeating(s))
'''

'''str1 = "geeksforgeeks"
my_dict = {}
for i in range(len(str1)):
    if str1[i] not in my_dict:
        my_dict[str1[i]] = 1
    else:
        my_dict[str1[i]] = my_dict.get(str1[i]) + 1
for key,value in my_dict.items():
    print(key, value)

'''

'''arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
# arr2 is subset of arr1 or not
my_dict = {}
hash_set = set(arr1)
for j in arr2:
    if j not in hash_set:
        print("this not subset")
        break
else:
    print("this is subset")'''

'''arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 4,7, 1]
arr1.sort()
arr2.sort()
print(arr1)   #[1, 3, 7, 11, 13, 21]
print(arr2)  #[1, 3, 4, 7, 11]
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i = i + 1
    elif arr1[i] == arr2[j]:
        i = i + 1
        j = j + 1
    else:
        print("this not subset")
        break
'''

'''list1 = [10,10,5,15,5,5,5]
my_dict = {}
for j in range(len(list1)):
    if list1[j] not in my_dict:
        my_dict[list1[j]] = 1
    else:
        my_dict[list1[j]] = my_dict.get(list1[j])+1
values_max = max(my_dict.values())
for key,val in my_dict.items():
    if val == values_max:
        print(key,"this max in dict")
values_min = min(my_dict.values())
for key,val in my_dict.items():
    if val == values_min:
        print(key,"this is min dict")
'''

'''list1 = [10,5,15,5,5,5]
my_dict = {}
for j in range(len(list1)):
    if list1[j] not in my_dict:
        my_dict[list1[j]] = 1
    else:
        my_dict[list1[j]] = my_dict.get(list1[j])+1
list = sorted(my_dict.values())
count = 1
for key,values in my_dict.items():
    if values == list[0]:
        print("this is least item in dictionary",key)
    if values == list[len(my_dict)-1]:
        print("this is most item in dictionary",key)
'''

'''list1 = [10,5,10,15,10,5]
list3 = []
list2 = []
for i in range(len(list1)):
    count = 0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            count = count + 1
        if j == len(list1) - 1:
            if list1[i] not in list2:
                list2.append(list1[i])
                list2.append(count)
                if list2 not in list3:
                    list3.append(list2)
                list2 = []
#print(list3)
list9 = []
for k in list3:
    k.sort()
    list9.append(k)
#print(list9)
list9.sort()
for l in range(len(list9)):
    if l == 0 or l == len(list9) - 1:
        print(list9[l][1])

'''

'''for i in list3:
    for j in range(len(i)):
        print(i[j],end= " ")
    print()'''

'''list1 = [10,5,10,15,10,5]
my_dict = {}
for i in range(len(list1)):
    if list1[i] not in my_dict:
        my_dict[list1[i]] = 1
    else:
        my_dict[list1[i]] = my_dict.get(list1[i]) + 1
for key, values in my_dict.items():
    print(key,values)
for j in my_dict:
   print(my_dict[j])
'''

'''list1 = [10,5,10,15,10,5]
list3 = []
list2 = []
for i in range(len(list1)):
    count = 0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            count = count + 1
        if j == len(list1) - 1:
            if list1[i] not in list2:
                list2.append(list1[i])
                list2.append(count)
                if list2 not in list3:
                    list3.append(list2)
                list2 = []
for i in list3:
    for j in range(len(i)):
        print(i[j],end= " ")
    print()'''

'''string1 ="abcdabefc"
my_dict = {}
for i in range(len(string1)):
    if string1[i] not in my_dict:
        my_dict[string1[i]] = 1
    else:
        my_dict[string1[i]] = (my_dict.get(string1[i])) + 1

print(my_dict)
'''

'''string1 = "abcdabefc"
target = ""
count = 0
for i in range(len(string1)):
    if string1[i] == target:
        count = count + 1
print(target,count)

'''

'''def l():
    p = ""
print(l())
'''

'''def fibo(n):
    if n == 1 or n == 0:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibo(4))
'''

'''def palindrome(str1, str2, b):
    if b == len(str2):
        return
    str1 = str2[b] + str1
    palindrome(str1,str2,b+1)
    if b == len(str2)-1:
        #print(str1)
        if str1 == str2:
            print("this is palindrome")
        else:
            print("this is not palindrome")
    
str1 = ""
str2 = "abcba"
#b = 0
palindrome(str1,str2,0)
'''

'''def palindrome(i,string):
    if i >= len(string)/2:
        return True
    if string[i] != string[len(string) - i -1]:
        return False
    return palindrome(i+1,s)

s = "madasm"
print(palindrome(0,s))
'''

'''def palindrome(string,b):
    str1 = ""
    if b == len(string):
        return "a"
    f = palindrome(string,b+1)
    str1 = str1 + f
    print(str1)


palindrome("name",0)
'''

'''def reversearray(list ,index = 0):
    if index == len(list):
        return
    reversearray(list, index + 1)
    #return (list[index])                        #**********************************
    print(list[index])
array = [1,2,3]
reversearray(array)
'''

'''def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
'''

'''def sum_of_N(c,d):
    if c == d:
        return 0
    return  (c + sum_of_N(c+1,d))



print(sum_of_N(1,4))

'''

'''def print_num(c,d):
    if c == d:
        return
    print_num(c+1,d)
    print(c)

print_num(1,101)
'''

'''def nameprint(name, c):
    if c == 1:
        return
    print(name)
    nameprint(name,c-1)
nameprint("name",4)
'''

'''def list(q):
    count = 0
    if len(q)-1 == count:
        return
    count = count + 1
    print(q[count])
    list(q[count+1])

'''
'''l = [1,2,3,4,5]
print(len(l))'''

'''#recursive
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
'''

'''n1 = int(input("enter a  number"))
n2 = int(input("enter a number"))
list1 = []
list2 = []
for i in range(1,n1+1):
    if n1%i == 0:
        list1.append(i)
for j in range(1,n2+1):
    if n2%j == 0:
        list2.append(j)

list1 = set(list1)
list2 = set(list2)

set3 = list(list1.intersection(list2))
print(set3)
'''

'''list1 = [2, 7, 11, 15, 6, 3]
target = 9
seen = {}
for i, num in enumerate(list1):
    complement = target - num
    if complement in seen:
        print([seen[complement],i])

    seen[num] = i
'''

'''#naive  approach
list1 = [4,0, 7, 1,8, 2]
n = len(list1)
list2 = []
list3 = []
target = 8
for i in range(0,n):
    for j in range(i+1, n):
        if list1[i]+list1[j] == target:
            list2.append(i)
            list2.append(j)
            list3.append(list2)
            list2 = []
print(list3)
'''

'''list1 = [1,2,3, 8 ,1]
find = 1
count = 0
for item in list1:
    if find == item:
        count = count+1
print(count)




list1 = [1,2,3,3, 8 ,1]
n = 10
mydict = {}
for i in range(0, len(list1)):
    if list1[i] not in mydict:
        mydict[list1[i]] = 1
    else:
        mydict[list1[i]] = (mydict.get(list1[i]))+1

if n in mydict:
  print(mydict.get(n))
'''

'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
'''

'''list1 = [2, 5, 4]
list2 = [3,7, 8, 9]
list3 = [5, 5, 7, 8, 9, 10]
list4 = []
total = 0
list5 = []
list6 = []
for i  in range(len(list1)):
   for j in range(len(list2)):
      for k in range(len(list3)):
          list4.append(list1[i]**2)
          list4.append(list2[j]**2)
          list4.append(list3[k]**2)
          for item in list4:
              total = total + item
          list5.append(total)
          total = 0
          list4 = []
for item1 in list5:
    modulo = item1%1000
    list6.append(modulo)
print(max(list6))'''

'''list4 = []
list4.append(list1)
list4.append(list2)
list4.append(list3)
print(list4)
total = 0
for i in range(len(list4)):
   max_ele = max(list4[i])
   square = max_ele**2
   total += square
print(total)
last = total%1000
print(last)
'''

'''K = 3
M = 10
list2 = []
list3 = []
max_modulo = 0
for i in range(K):
    list1 = list(map(int, input("enter the number:").split()))
    for i in range(len(list1[1:])):
        #print(i)
        square = list1[i]**2
        modulo = square%M
        max_modulo = max(max_modulo,modulo)
        if i == len(list1) - 2:
            list2.append(max_modulo)
print(list2)'''

'''from itertools import product   #[2, 5, 4] #[3,7, 8, 9]  #[5, 5, 7, 8, 9, 10]
K = 3                    #K,M = map(int,input().split())
M = 10
nums = []
for _ in range(K):
   # a = input().split()[1:]
   # print (a)
    row = map(int,input().split()[1:])
    #print(list(row))
    nums.append(list(map(lambda x:x**2%M, row)))
    #print(nums)
    #print(list(product(*nums)))
print(max(map(lambda x: sum(x)%M, product(*nums))))
'''

'''def average(array):
    set1 = set(array)
    total = 0
    for item in set1:
        total = total + item
    ave = (total/len(set1))
    return round(ave, 3)

a = int(input())
b = list(map(int,input().split()))
print(average(b))
'''

'''n = 5
list_of_number = {150, 120, 670, 345, 511,900}
set1 = list_of_number
total = 0
for  item in set1:
    total = total + item

average = (total/len(set1))
print(round(average,3))
'''

'''from itertools import permutations
string1 ,n = input().split()
string = sorted(string1)
str1 = ""
list2 = []
count = 0
permutations = list(permutations(string, int(n)))
for item in range(len(permutations)):
    for j in range(len(permutations[item])):
        str1 = str1 + permutations[item][j]
        count = count + 1
        if count == int(n):
            list2.append(str1)
            str1 = ""
            count = 0
for item1 in list2:
    print(item1)

'''

'''string , n = input().split()
string2 = sorted(string)
string3 = "" #ACHK
list1 = []
str1 = ""
count = 0
for item in string2:
    string3 = string3 + item
for i in range(len(string3)):
    for j in range(0, len(string3)):
      if string3[i] != string3[j]:
          str1 = str1 + string3[i]
          str1 = str1 + string3[j]
          list1.append(str1)
          str1 = ""

for item2 in list1:
    print(item2)
'''

'''from collections import Counter
my_list = [2,3,4,5,6,8,7,6,5,18]    #{5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1}
customer = 6
count = Counter(my_list)
my_dict = {}
my_dict.update(count)
price_and_size = [(6,55),(6,45),(6,55),(4,40),(18,60),(10,50)]               #[(6,55),(6,45),(6,55),(4,40),(18,60),(10,50)]
n = len(price_and_size)
total_price = []
for i in range(n):
    if price_and_size[i][0] in my_dict:
        total_price.append(price_and_size[i][1])
        my_dict = my_dict 1

print(my_dict.values())
print(my_dict)
print(total_price)
'''

'''my_list = list(map(int, input().split()))              #2 3 4 5 6 8 7 6 5 18  #[2,3,4,5,6,8,7,6,5,18]
customer = 6                                #int(input())#6
size = list(map(int, input().split()))                 # 6 6 6 4 18 10   [6, 6, 6, 4, 18, 10]
n = len(size)
price = list(map(int,input().split()))                 # 55 45 55 40 60 50  [55, 45, 55, 40, 60, 50]
total = 0
total_price = []
for i in range(n):
    if size[i] in my_list:
        total_price.append(price[i])
        my_list.remove(size[i])
for item in total_price:
    total = total + item
print(total)'''
'''my_list = list(map(int, input().split())) 
customer = int(input())'''

'''numbers = int(input())
my_list = list(map(int,input().split()))
customer = int(input())
list_of_size_price = []
for i in range(customer):
  size_price = tuple(map(int, input().split()))
  list_of_size_price.append(size_price)
n = len(list_of_size_price)
total_price = []
for j in range(n):
    if list_of_size_price[j][0] in my_list:
       my_list.remove(list_of_size_price[j][0])
         #print(list_of_size_price[j][0])
       total_price.append(list_of_size_price[j][1])
total = 0
for item in total_price:
    total = total + item
print(total)
'''

'''A = list(map(int ,input().split()))
B = list(map(int, input().split()))
list3 = []
list2 = []
for i in range(len(A)):
    for j in range(len(B)):
        list2.append(A[i])
        list2.append(B[j])
        list2 = tuple(list2)
        list3.append(list2)
        list2 = []
for item in list3:
    print(item, end=" ")
'''

'''from collections import OrderedDict
def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n,k):
        print("".join(OrderedDict.fromkeys(string[i:i + k])))

string, k = input(), int(input())
merge_the_tools(string, k)'''

'''string = "AABCAAAD"
k = 2'''
'''def merge_the_tools(string, k):
    n = len(string)
    list1 = []
    str2 = ""
    count = 0
    for i in range(0, n):
        str2 = str2 + string[i]
        count = count + 1
        if count == n / k:
            list1.append(str2)
            str2 = ""
            count = 0
    m = len(list1)
    list2 = []
    count2 = 0
    for j in range(m):
        str3 = ""
        for k in range(len(list1[j])):
            if list1[j][k] not in str3:
                str3 = str3 + list1[j][k]
        if j == count2:
            count2 = count2 + 1
            list2.append(str3)
    for item in list2:
        print(item)'''

'''string, k = input(), int(input())
merge_the_tools(string, k)'''

'''string , k = input(), int(input())  #AAABCADDE
# k = int(input("enter a integer value"))
n = len(string)
list1 = []
str2 = ""
count = 0
for i in range(0, n):
    str2 = str2 + string[i]
    count = count + 1
    if count == n/k:
        list1.append(str2)
        str2 = ""
        count = 0
#print(list1)
m = len(list1)
list2 = []
count2 = 0
for j in range(m):
    str3 = ""
    for k in range(len(list1[j])):
        if list1[j][k] not in str3:
            str3 = str3 + list1[j][k]
    if j == count2:
        count2 = count2 + 1
        list2.append(str3)
for item in list2:
    print(item)
'''

'''def solve(s):
    list1 = []
    for i in s.split():
        new_string = ""
        for j in range(len(i)):
            if j == 0 and i[j].isalpha() and i[j].islower():
                k = i[j].upper()
                new_string = new_string + k
            else:
                new_string = new_string + i[j]
            if j == len(i) - 1:
                list1.append(new_string)
    result = " ".join(list1)
    return result

print(solve("hello world"))
'''

'''s = input().split()
list1 = []
for i in s:
    new_string = ""
    for j in range(len(i)):
        if j == 0 and i[j].isalpha() and i[j].islower():
            k = i[j].upper()
            new_string = new_string + k
        else:
            new_string = new_string + i[j]
        if j == len(i)-1:
            list1.append(new_string)

for item in list1:
    print(item,end=" ")'''

'''n,m = map(int, input("enter rows and colomns").split())
j = 1
d = ".|."
for i in range(n//2):
    print((j*d).center(m,"-"))
    j = j+2
print("WELCOME".center(m,"-"))
j = j-2
for k in range(n//2-1,-1,-1):
    print((j*d).center(m,"-"))
    j = j-2
'''

'''n,m = map(int,input("enter number of rows and colomn").split())
d = ".|."
for i in range(n//2):
    print((d*(2 * i +1)).center(m,"-"))
print("Welecome".center(m,"-"))
for j in range((n//2)-1, -1, -1):
    print((d*(2*j+1)).center(m,"-"))

'''

'''n = 7
m = 21
d = ".|."
j = 1
for i in range((n//2)-1):
    j = j + 2
    if i == 0:
        print(d.center(m,"-"))
    print((j*d).center(m,"-"))
    if i == 1:
        print("WELCOME".center(m,"-"))
    if i == 1:
        j = j + 2
        for k in range(n//2):
            j = j-2
            print((j*d).center(m,"-"))'''

'''n = 7
m = 21
d = ".|."
j = 1
for i in range((n//2)-1):
    j = j + 2
    if i == 0:
        print(d.center(m,"-"))
    print((j*d).center(m,"-"))
    if i == (n//2)-3:
        print("WELCOME".center(m,"-"))
    if i == (n//2)-3:
        j = j + 2
        range_k = (n//2)-1
        for k in range(range_k):
            if k == range_k-1:
                j = 0
                print(d.center(m,"-"))
                break
                print("jhdjh")
            j = j-2
            print((j*d).center(m,"-"))
'''

'''str1 = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n = len(str1)
width = 4
count = 0
str2 = ""
for item in range(n):
    count = count+1
    str2 = str2 + str1[item]
    if item == n-1:
        print(str2)
    if count == width:
        print(str2)
        str2 = ""
        count = 0
'''

'''def towarap(string, max_width):
    n = len(string)
    count = 0
    str2 = ""
    for i in range(n):
        count = count + 1
        str2 = str2 + string[i]
        if i == n-1:
            return str2
        if count == max_width:
            print(str2)
            count = 0
            str2 = ""

str1 = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
m_width = 4
print(towarap(str1,m_width))
'''

'''n = 5
width = 11
j = 1
for i in range(0,n-1):
    j = j + 2
    if i == 0:
        print('H'.center(width,' '))
    print((j*'H').center(width, ' '))
Width = 25
diff = 35
for i in range(n+1):
    if i == 1:
        break
    for j in range(0, n+1):
            print(" ",(n*"H").ljust(Width),(n*'H').ljust(Width))
for i in range(n):
    if i == 3:
        break
    print(" ",(diff-4)*"H")

for i in range(n+1):
    if i == 1:
        break
    for j in range(0, n+1):
            print(" ",(n*"H").ljust(Width),(n*'H').ljust(Width))

new_width = 58
s = 11
for i in range(0,n):
    s = s -2
    print("",(s*"H").center(new_width," "))
'''

'''str1 = "qA2"
print(any(i.isalnum()for i in str1))
print(any(i.isalpha()for i in str1))
print(any(i.isdigit()for i in str1))
print(any(i.isupper()for i in str1))
print(any(i.islower()for i in str1))
'''

'''s = input("Enter a string: ")
has_alnum = False
has_digit = False
has_alpha = False
has_upper = False
has_lower = False

for item in s:
    if item.isalnum():
        has_alnum = True
    if item.isdigit():
        has_digit = True
    if item.isalpha():
        has_alpha = True
    if item.isupper():
        has_upper = True
    if item.islower():
        has_lower = True

print(has_alnum)
print(has_digit)
print(has_alpha)
print(has_upper)
print(has_lower)
'''

'''s = input()
has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for item in s:
    if item.isalnum():
        has_alnum = True
    if item.isalpha():
        has_alpha = True
    if item.isdigit():
        has_digit = True
    if item.islower():
        has_lower = True
    if item.isupper():
        has_upper = True

print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)
'''

'''s = input()
alnumcount = 0
digitcount = 0
alphacount = 0
uppercount = 0
lowercount = 0
n = len(s)
for item in s:
    if item.isalnum():
        if True and alnumcount == 0:
          print(True)
          alnumcount = alnumcount + 1
    if item.isalnum() == False and alnumcount == 0:
        print(False)
        alnumcount = alnumcount + 1
    if item.isdigit():
        if True and digitcount == 0:
            print(True)
            digitcount = digitcount +1
    if item.isdigit() == False and digitcount == 0:
        print(False)
        digitcount = digitcount + 1
    if item.isalpha():
        if True and alphacount == 0:
            print(True)
            alphacount = alphacount +1
    if item.isalpha() == False and alphacount == 0:
        print(False)
        alphacount = alphacount +1
    if item.isupper():
        if True and uppercount == 0:
            print(True)
            uppercount = uppercount+1
    if item.isupper() == False and uppercount == 0:
        print(False)
        uppercount = uppercount + 1
    if item.islower():
        if True and  lowercount == 0:
           print(True)
           lowercount = lowercount +1
    if item.islower() == False and lowercount == 0:
        print(False)
        lowercount = lowercount+1
'''
'''str1 = "qA2"
alnumcount = 0
digitcount = 0
alphacount = 0
uppercount = 0
lowercount = 0
n = len(str1)
#for item in str1:
if str1.isalnum():
    if True and alnumcount == 0:
        print(True)
        alnumcount = alnumcount + 1
if alnumcount == 0:
    print(False)
if str1.isdigit():
    if True and digitcount == 0:
        print(True)
        digitcount = digitcount + 1
if digitcount == 0:
    print(False)
if str1.isalpha():
    if True and alphacount == 0:
        print(True)
        alphacount = alphacount + 1
if alphacount == 0:
    print(False)
if str1.isupper():
    if True and uppercount == 0:
        print(True)
        uppercount = uppercount + 1
if uppercount == 0:
    print(False)
if str1.islower():
    if True and lowercount == 0:
        print(True)
        lowercount = lowercount + 1
if lowercount == 0:
    print(False)
'''

'''def to_check_substring(string1, sub):
    count = 0
    n = len(string1)
    for i in range(n):
        if string1[i:n].startswith(sub):
            count = count+1
    return count


a = "ABCDCJKCDCDC"
b = "CDC"
print(to_check_substring(a,b))
'''

'''string1 = "abcdefg"
list1 = list(string1)
list1[5] = "h"
string1 = "".join(list1)
print(string1)
'''

'''def mutation(string, position, character):
    list1 = list(string)
    list1[position] = character
    string = "".join(list1)
    print(string)



s = input("enter a full string")
i, c = input("enter position and character").split()
new_string = mutation(s, int(i), c)
print(new_string)
'''

'''def mutation(string, position, character):
    n = len(string)
    str2 = ""
    for i in range(n):
        if i == position:
            str2 = str2 + character
        else:
            str2 = str2 + string[i]
    return str2



s = input("enter full string")
i , c = input("eneter position and  character" ).split()
new_string = mutation(s, int(i), c)
print(new_string)
'''

'''def tohello(first, last):
    print("Hello",first,last,"! You just delved into python")



tohello("city", "name")
'''

'''def tohello(first, last):
    string1 = f"Hello {first} {last}! You just delved into python"
    print(string1)


first_name  = input()
last_name = input()
tohello(first_name,last_name)
'''

'''string1 = "this is a string"
string1 = string1.split( )
string2 = ""
n = len(string1)
for i in range(n):
    if i == n-1:
        string2 = string2 +string1[i]
        break
    else:
        string2 = string2 + (string1[i] + "-")
print(string2)

'''
'''def split_and_join(string1):
    string1 = string1.split()
    string2 = ""
    n = len(string1)
    for i in range(n):
        if i == n-1:
            string2 = string2 + string1[i]
            break
        else:
            string2 = string2 + (string1[i] + "-")

    return string2


str1 = "this is a string"
print(split_and_join(str1))
'''

'''def swap_case(s):
    str2 = ""
    for item in s:
        if item.isupper():
            lower1 = item.lower()
            str2 = str2 + lower1
        else:
            upper1 = item.upper()
            str2 = str2 + upper1

    return str2


str1 = 'HackerRank.com presents "Pythonist 2"'
print(swap_case(str1))

'''

'''n = input()
integer_list = map(int, input().split())
tuple1 = tuple(integer_list)
print(tuple1)
print(hash(tuple1))'''

'''n = int(input("enter a number"))
list1 =[]
for i in range(n):
    command = input().split()
    if command[0] == "insert":
        list1.insert(int(command[1]),int(command[2]))
    elif command[0] == "print":
        print(list1)
    elif command[0] == "remove":
        list1.remove(int(command[1]))
    elif command[0] == "append":
        list1.append(int(command[1]))
    elif command[0] == "sort":
        list1.sort()
    elif command[0] == "pop":
        list1.pop()
    elif command[0] == "reverse":
        list1.reverse()
    else:
        print("write a valid input")
'''

'''n = int(input("enter a number of student"))
student = { }
for i in range(n):
   s_name , *allsubjects = input("enter value of first student\n").split( )
   #size = len(allsubjects)
   student[s_name] = map(float, allsubjects)
search = input("enter name of student\n")
sum = 0
size = 0
for s in student[search]:
    #print(s)
    size = size+1
    sum = sum+s
print(sum/size)'''

'''list3 = []
sorted_list = []
last_list = []
for i in range(int(input())):
    name = input()
    score = float(input())
    list3.append([name,score])
for name,score in list3:
    sorted_list.append(score)
set1 = set(sorted_list)
sorted3 = sorted(set1)
for name,score in list3:
    if sorted3[1] == score:
        last_list.append(name)
last_list.sort()
for item in last_list:
    print(item)
'''