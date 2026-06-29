patterns = ["a","a","iik"]
word = "iiik"
ans = 0
for i in range(len(patterns)):
    if len(patterns[i]) > len(word):
        pass
    else:
        flag = False
        j = 0
        k = 0
        count = 0
        while k < len(word) :
            if patterns[i][j] != word[k]:
                if flag == True:
                    j = 0
                    k = k - count + 1
                    count = 0
                    flag = False
                else:
                    k = k + 1
            else:
                if flag == False:
                    flag = True
                j = j + 1
                k = k + 1
                count += 1
            if j >= len(patterns[i]):
                break
        if j == len(patterns[i]):
            ans += 1
print(ans)



'''arr = [1,2,3,4,5]
arr.sort()
for i in range(1,len(arr)):
    if abs(arr[i-1]-arr[i]) <= 1:
        pass
    else:
        arr[i] = arr[i-1] + 1
print(arr)'''








'''nums = [48841,358801,28561,18974736,4356,221,358801,599,13,4356,66,48841,28561,815730721,13,815730721,18974736,66,169,599,169,221]
hash1 = {}
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = [1,True]
    else:
        hash1[nums[i]][0] += 1
print(hash1)
ans = 1
for i in range(len(nums)):
    cal = nums[i]
    if cal == 0:
        continue
    count = 0
    if cal in hash1:
        if hash1[cal][1] == False:
            print(cal)
            continue
    while True:
        if cal in hash1:
            if hash1[cal][0] > 1:
                count += 2
                hash1[cal][1] = False
            else:
                count += 1
                break
        else:
            count -= 1
            break
        cal = cal ** 2
    ans = max(ans,count)
print(ans)'''



'''nums = [4,2,2,3]
target = 1
validleft = 0
hash1 = {0:1}
ans = 0
cumsum = 0
for i in range(len(nums)):
    # print(validleft)
    if nums[i] == target:
        validleft += hash1[cumsum]
        cumsum += 1
    else:
        cumsum -= 1
        if cumsum >= 0:
            validleft-= hash1[cumsum]

    if cumsum not in hash1:
        hash1[cumsum] = 1
    else:
        hash1[cumsum] += 1
    ans += validleft
print(ans)
print(hash1)'''





'''nums = [1,1,1,1]
target = 1
ans = 0
for i in range(len(nums)):
    count_target = 0
    sub_arr_len = 0
    for j in range(i,len(nums)):
        sub_arr_len += 1
        if target == nums[j]:
            count_target += 1
        if (sub_arr_len//2) < count_target:
            ans += 1
print(ans)'''









'''arr = [[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]
min1 = float('inf')
index_min = 0
max1 = float('-inf')
index_max = 0
min_for_max = 0
max_for_min = 0
for i in range(len(arr)):
    if arr[i][-1] >= max1:
        max1 = arr[i][-1]
        min_for_max = arr[i][0]
        index_max = i
for i in range(len(arr)):
    if arr[i][0] <= min1 and i != index_max:
        min1 = arr[i][0]
        max_for_min = arr[i][-1]
        index_min = i

a = abs(max1- min1)
print(max1,min1)
print(a)'''
# c = abs(max1 - min_for_max)
# d = abs(min_for_max - min1)
# print(max1,min_for_max)
# print(max_for_min,min_for_max)




# n = 10
# restrictions = [[5,3],[2,5],[7,4],[10,3]]
# if restrictions is None or restrictions[-1][0] != n:
#     restrictions.append([n,n-1])
# restrictions.append([1,0])
# for i in range(len(restrictions)):
#     if restrictions[i][0] <= restrictions[i][1]:
#         restrictions[i][1] = restrictions[i][0] - 1
# restrictions.sort()
# print(restrictions)
# for i in range(len(restrictions)-1,0,-1):
#     restrictions[i][1] = min(restrictions[i][1],restrictions[i-1][1]    )






'''costs = [10,6,8,7,7,8]
coins = 5
max1 = max(costs)
frequency = [0] * max1
for i in range(len(costs)):
    frequency[costs[i]-1] += 1
total = 0
for i in range(len(frequency)):
    cal = (frequency[i] * (i + 1))
    if cal <= coins:
        total += frequency[i]
        coins = coins - cal
    else:
        cal = (frequency[i])
        cal2 = 0
        while cal:
            if (cal * (i+1)) <= coins:
                coins = coins - (cal * (i+1))
                total += cal
                cal = cal2
            else:
                cal1 = cal//2
                cal2 = cal - cal1
                cal = cal1




print(total)'''









'''n = 5
restrictions = [[2,1],[4,1]]
if restrictions[-1][0] != n:
    restrictions.append([n,n-1])
restrictions.append([0,1])
restrictions.sort()
i = len(restrictions) - 1
count = 0
for k in range(restrictions[-1][0],0,-1):
    if k == restrictions[i][0]:
        if restrictions[i][1] >= k - 1:
            count += 1
        else:
    else:'''



















'''n = 5
restrictions = [[2,1],[4,1]]
if restrictions[-1][0] != n:
    restrictions.append([n,n-1])
restrictions.append([1,0])
restrictions.sort()
print(restrictions)
# [[2, 5], [5, 3], [7, 4], [10, 3]]
i = len(restrictions) -  2
prev = restrictions[-1][1]
max_height = prev
max_local = max_height
curr = 0
count = 0
flag = False
for k in range(restrictions[-1][0] - 1,0,-1):
    if restrictions[i][0] == k:
        if abs(max_local - restrictions[i][1]) <= 1:
            max_local = min(max_local,restrictions[i][1])
            if i == 0:
                flag = True
            count += 1

        else:
            if restrictions[i][1] > max_local:
                count += 1
                if i == 0:
                    flag = True
            else:
                curr = restrictions[i][1]
                min_point = min(curr, prev)
                cal = count // 2
                cal2 = min_point + cal
                max_height = min(cal2, max_height)
                max_local = curr
                prev = curr
                curr = 0
                count = 0
        i = i - 1
    else:
        max_local += 1
        count += 1
if abs(0 - max_local) > 1 and flag == False:
    curr = 0
    min_point = 0
    cal = count//2
    cal2 = min_point + cal
    max_height = min(cal2,max_height)
    max_local = 0
max_height = max(max_height,max_local)
print(max_height)'''

















'''nums = [1,2,3]
def backtrack(list1,i,nums,set1):
    if i >= len(nums):
        set1.add(tuple(list1))
        return
    else:
        list1.append(nums[i])
        set1.add(tuple(list1))
        backtrack(list1,i+1,nums,set1)
        print(list1,"before")
        list1.pop()
        print(list1,"after")
        backtrack(list1,i+1,nums,set1)
list1 = []
set1 = set()
backtrack(list1,0,nums,set1)
print(set1)'''







'''from collections import Counter
nums = [1,1,1,2,2,3]
k = 2
dict1 = {}
list1 = []
for item in nums:
    if item not in dict1:
        dict1[item] = 1
    else:
        dict1[item] += 1
for tuple1 in dict1.items():
    list1.append(tuple1)
# print(list1)
count = Counter(list1)
print(count.get)
heap = []
a = heapq.nlargest(k,count.keys(),key= count.get)
print(a)'''
import heapq











'''s = "cd%#*#"
k = 3
lenght = 0
for i in range(len(s)):
    if s[i] == "*":
        if lenght:
            lenght -= 1
    elif s[i] == "#":
        lenght *= 2
    else:
        lenght += 1
if k >= lenght:
    print(".")
for i in reversed(s):
    if i == "*":
        lenght += 1
    elif i == "#":
        lenght = lenght // 2
        if k >= lenght:
            k = k - lenght
    elif i == "%":
        k = lenght - k - 1

    else:
        lenght -= 1
    if k == lenght:
        print(i)
        break
else:
    print(".")'''














'''s = "fviefuro"
hash1 = {}
for item in s:
    if item not in hash1:
        hash1[item] = 1
    else:
        hash1[item] += 1
list1 = ["zero","one","two","three","four","five","six","seven","eight","nine"]
str1 = ""
# i = 0
print(hash1)
while True:
    count = 0
    for i in range(len(list1)):
        # print(hash1,"before")
        flag = False
        print(list1)
        for j in range(len(list1[i])):
            if list1[i][j] in hash1 and hash1[list1[i][j]] > 0:
                # print(i,j,"jhjjh")
                hash1[list1[i][j]] -= 1
            else:
                # print(j,"hjvv",i,list1[i][j],hash1)
                for k in range(0,j):
                    hash1[list1[i][k]] += 1
                # print(list1[i])
                list1.pop(i)
                count += 1
                flag = True
                break
        else:
            str1 = str1 + str(count)
            count += 1
        if flag == True:
            break
        # print(hash1)3
    count_freq = 0
    # print(hash1)
    for item in hash1.values():
        if item > 0:
            count_freq += 1
    if count_freq > 0:
        pass
    else:
        break
ans = [0] * 10
for item in str1:
    print(item)
    ans[int(item)] += 1
str1 = ""
for i in range(len(ans)):
    str1 = str1 + (str(i) * ans[i])
print(str1)'''










'''s = "fviefuro"
hash1 = {}
for i in range(len(s)):
    if s[i] not in hash1:
        hash1[s[i]] = 1
    else:
        hash1[s[i]] += 1
list1 = ["zero","one","two","three","four","five","six","seven","eight","nine"]
list_ans = []
for item in list1:
    dict1 = {}
    for j in item:
        if j not in dict1:
            dict1[j] = 1
        else:
            dict1[j] += 1
    list_ans.append(dict1)
str1 = ""
count = 0
for i in range(len(list_ans)):
    sam = list_ans[i]
    for key in sam.keys():
        # print(key,list_ans[i])
        if key in hash1:
            if hash1[key] >= sam[key]:
                hash1[key] -= 1
            else:
                break
        else:
            break
    else:
        str1 = str1 + str(count)
    count += 1
print(str1)
'''







'''words = ["abcw","baz","foo","bar","xtfn","abcdef"]

max1 = float('-inf')
max2 = float('-inf')

for i in range(len(words)):
    #external
    alph = [0] * 26
    for k in range(len(words[i])):
        cal1 = ord(words[i][k]) - 97
        if alph[cal1] != 0:
            break
        else:
            alph[cal1] = 1
    for j in range(i+1, len(words)):
        alph2 = [0] * 26
        for l in range(len(words[j])):
            cal2 = ord(words[j][l]) - 97
            if alph2[cal2] != 0:
                break
            else:
                alph2[cal2] = 1


'''













'''import heapq
arr =[3,2,1,5,6,4,12,14,9]
k = 4
heap = []
for item in arr:
    heapq.heappush(heap,item)
    if len(heap) > k:
        heapq.heappop(heap)
print(heap)'''






'''ans_list = []
def insert(value):
    ans_list.append(value)
    current = len(ans_list) - 1
    while current > 0:
        parent = (current - 1)//2
        # print(current,parent,ans_list)
        if ans_list[current] < ans_list[parent]:
            ans_list[current],ans_list[parent] = ans_list[parent],ans_list[current]
            current = parent
        else:
            break
def pop():
    if len(ans_list) == 0:
            return None
    print(ans_list)
    root = ans_list[0]
    ans_list[0] = ans_list[-1]
    ans_list.pop()
    current = 0
    while True:
        left = (2 * current) + 1
        right = (2 * current) + 2
        smallest = current
        if left < len(ans_list) and ans_list[left] < ans_list[smallest]:
            smallest = left
        if right < len(ans_list) and ans_list[right] < ans_list[smallest]:
            smallest = right
        if smallest == current:
            break
        ans_list[smallest],ans_list[current] = ans_list[current],ans_list[smallest]
        current = smallest
    return root


arr =[3,2,1,5,6,4,12,14,9]
k = 4
def kth_largest(arr):
    global ans_list
    ans_list = []
    for item in arr:
        insert(item)
        if k < len(ans_list):
            pop()
kth_largest(arr)
print(ans_list)'''





# nums = [9,12,5,10,14,3,10]
# pivot = 10
# list1 = [0] * len(nums)
# j = len(nums) - 1
# for i in range(len(nums)):







'''nums = [2,2]
nums.sort()
window = (len(nums)//3)
ans = []
i = 0
j = window
last = ""
while j < len(nums):
    print(i,j)
    if nums[i] == nums[j] and nums[i] != last:
        last = nums[i]
        ans.append(nums[i])
        i = i + window + 1
        j = j + window + 1
    else:
        i = i + 1
        j = j + 1
print(ans)'''


















'''nums = [1]
sum1 = 0
list1 = []
for i in range(len(nums)):
    list1.append(sum1)
    sum1 += nums[i]
sum1 = 0
for i in range(len(nums)-1,-1,-1):
    abs1 = abs(list1[i] - sum1)
    list1[i] = abs1
    sum1 += nums[i]
print(list1)'''









'''# matrix = [[1,3,5,7],
#           [10,11,16,20],
#           [23,30,34,60],
#           [70,72,81,89]]
matrix = [[1,3,5]]
target = 1
i = 0
j = len(matrix) - 1
print(i,j)
while i <= j:
    mid = (i+j)//2
    if target >= matrix[mid][0] and target <= matrix[mid][-1]:
        mid_arr = matrix[mid]
        a = 0
        b = len(mid_arr) - 1
        flag = False
        while a <= b:
            mid1 = (a + b)//2
            if target == mid_arr[mid1]:
                flag = True
                print(True)
                break
            elif target < mid_arr[mid1]:
                print()
                b = mid1 - 1
                print(a,b)
            elif target > mid_arr[mid1]:
                a = mid1 + 1
        else:
            print(False)
            break
        if flag == True:
            break
    elif target < matrix[mid][0]:
        j = mid - 1
    elif target > matrix[mid][0] and target > matrix[mid][-1]:
        i = mid + 1
'''




'''nums = [1,3,4,2,2]
i = 0
while i < len(nums):
    find = nums[i] - 1

    if nums[i] != nums[find]:
        nums[i],nums[find] = nums[find],nums[i]
    else:
        if i != find:
            print(nums[i])
            break
        else:
            # print(nums[i])
            i = i + 1'''




'''num1 = 4848
num2 = 4848
count = 0
for i in range(num1,num2+1):
    str1 = str(i)
    for k in range(1,len(str1)-1):
        if int(str1[k-1]) < int(str1[k]) > int(str1[k+1]) or int(str1[k-1]) > int(str1[k]) < int(str1[k+1]):
            count += 1
print(count)'''







'''landStartTime = [99]
landDuration = [59]
waterStartTime = [99,54]
waterDuration = [85,20]
land_arr = []
for i in range(len(landStartTime)):
    check1 = landStartTime[i] + landDuration[i]
    land_arr.append(check1)
land_arr.sort()
min1 = float('inf')
for i in range(len(waterStartTime)):
    check1 = waterStartTime[i] + waterDuration[i]
    a = 0
    b = len(land_arr) - 1
    while a <= b:
        mid = (a + b)//2
        if land_arr[mid] > waterStartTime[i]:
            total = land_arr[mid] + waterDuration[i]
            min1 = min(min1,total)
            b = mid -1
        else:
            min1 = min(min1,check1)
            a = mid + 1

water_arr = []
for i in range(len(waterStartTime)):
    check1 = waterStartTime[i] + waterDuration[i]
    water_arr.append(check1)
water_arr.sort()
for i in range(len(landStartTime)):
    check1 = landStartTime[i] + landDuration[i]
    a = 0
    b = len(water_arr) - 1
    while a <= b:
        mid = (a+b)//2
        if water_arr[mid] > landStartTime[i]:
            total = water_arr[mid] + landDuration[i]
            min1 = min(min1,total)
            b = mid - 1
        else:
            min1 = min(min1,check1)
            a = mid + 1
print(min1)'''





# copy_watestartime = waterStartTime.copy()
# copy_waterduration = waterDuration.copy()
#
# print(land_arr)



















'''nums = [0,0,2,0,0,0,2,0,1,2,1,2,2,2,1,2,0,2,0,1,0,0,2,0,2,0,1,1,1,1,1,1,0,1,1,0,1,2,0,0,1,2,0,1,2,2,0,2,2,1,1,2,2,1]
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] == 0:
        i = i + 1
    if nums[j] == 0:
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
    else:
        # flag = True
        j = j - 1
print(nums)
print(nums[i+1])
print(i,j)
j = len(nums) - 1
while i < j:
    if nums[i] == 1:
        i = i + 1
    # if nums[i] == 0 and i+1 == j and nums[j] ==  1:
    #     i = i + 1
    #     j = j - 1
    if nums[j] == 1:
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
    else:
        j = j - 1
    # print(nums)
print(nums)'''

















'''nums = [1,2,3,2,-9,12]
max_sum = float('-inf')
toatl_sum1 =  0
main_list1 = []
list1 = []
for i in range(len(nums)):
    toatl_sum1 = toatl_sum1 + nums[i]
    list1.append(nums[i])
    if toatl_sum1 < 0:
        if max_sum < toatl_sum1:
            main_list1 = list1
        max_sum = max(max_sum,toatl_sum1)
        toatl_sum1 = 0
        list1 = []
    else:
        if toatl_sum1 > max_sum:
            main_list1 = list1
        max_sum = max(max_sum,toatl_sum1)
print(max_sum)
print(main_list1)
'''















'''landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]


min1 = float('inf')
for i in range(len(landStartTime)):
    a = landStartTime[i]
    b = landDuration[i]
    check1 = a+b
    for j in range(len(waterStartTime)):
        a = waterStartTime[j]
        b = waterDuration[j]
        if check1 > a:
            total = check1 + b
            min1 = min(min1,total)
        else:
            total = a + b
            min1 = min(min1,total)
for i in range(len(waterStartTime)):
    a = waterStartTime[i]
    b = waterDuration[i]
    print(a, b)
    check1 = a + b
    for j in range(len(landStartTime)):
        a = landStartTime[j]
        b = landDuration[j]
        if check1 > a:
            total = check1 + b
            print(total)
            min1 = min(min1,total)
        else:
            total = a + b
            min1 = min(min1,total)
print(min1)
'''













# nums = [1,1,5,1,1]
# str1 = ""
# for i in nums:
#     str1 = str1 + str(i)
# int1 = int(str1)
# i = 0
# j = len(nums) - 1
# while i <= j:
#     if nums[i] < nums[j]:
#         if i+1 == j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i = i + 1
#         else:
#             # nums[i], nums[j] = nums[j], nums[i]
#             i = i + 1
#             # j = j - 1
#     elif nums[i] == nums[j]:
#         j = j - 1
#     else:
#         i = i + 1
#         # j = j - 1
#     str2 = ""
#     int2 = 0
#     for item in nums:
#         str2 = str2 + str(item)
#         int2 = int(str2)
#     if int1 < int2:
#         print(nums)
#         break
# else:
#     print(nums)








'''numRows = 5
def rec(n):
    if n == 0 or n == 1:
        return 1
    return rec(n-1) + rec(n-2)'''







'''matrix = [[1,2,3,4],
          [5,0,7,8],
          [0,10,11,12],
          [13,14,15,0]]
list1_row = []
list2_col = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            list1_row.append(i)
            list2_col.append(j)
while list1_row:
    last = list1_row.pop()
    for i in range(len(matrix[0])):
        matrix[last][i] = 0
while list2_col:
    last = list2_col.pop()
    for i in range(len(matrix)):
        matrix[i][last] = 0
print(matrix)'''











'''mass = 1
asteroids = [1,2,3,4,5,6,7,8]
asteroids.sort()
print(asteroids)
stack = []
for i in range(len(asteroids)):
    if mass > asteroids[i]:
        mass = mass + asteroids[i]
    else:
        stack.append(asteroids[i])
print(stack)
while stack:
    last_one = stack.pop()
    if mass >= last_one:
        mass = mass + last_one
    else:
        print(False)
        break
else:
    print(True)'''








# sum1 = sum(asteroids)
# for i in range(len(asteroids)-1,-1,-1):
#     check1 = asteroids[i]
#     cal1 = sum1 - check1
#     cal = cal1 + mass
#     if cal < check1:
#         print(False)
#         break
# else:
#     print(True)







'''s ="PAYPALISHIRING"
numRows = 2
count = 0
flag = True
list1 = []
list2 = [""] * numRows
i = 0
while i < len(s):
    if count == 0:
        if flag == True:
            # sample1 = [""] * numRows
            # if list2 != sample1:
            #     list1.append(list2)
            flag = False
            list2 = [""] * numRows
        else:
            flag = True
    elif count == numRows:
        list1.append(list2)
        list2 = [""] * numRows
        flag = True
        count -= 2
    if flag == False:
        list2[count] = s[i]
        count += 1
    else:
        # sample1 = [""] * numRows
        # if sample1 != list2:
        #     list1.append(list2)
        list2 = [""] * numRows
        list2[count] = s[i]
        list1.append(list2)
        list2 = [""] * numRows
        count -= 1
    i = i + 1
if list2 != ([""] * numRows):
    print("df")
    list1.append(list2)
# print(list1)
str1 = ""
for i in range(len(list1[0])):
    for j in range(len(list1)):
        if list1[j][i] != "":
            str1 = str1 + list1[j][i]

print(str1)
'''







#
# s = "PAYPALISHIRING"
# numRows = 4
# count = 0
# list1 = []
# i = 0
# flag = False
# list2 = []
# while i < len(s):
#     if count == 0:
#         list2 = [""] * numRows
#         flag = False
#     if flag == False:
#         list2[count] = s[i]
#         i = i + 1
#         count += 1
#     else:
#         list1.append(list2)
#         list2 = [""] * numRows
#         count = count - 1
#         list2[count] = s[i]
#         i = i + 1
#     if count == numRows-1:
#         # count = count - 1
#         if i < len(s):
#             list2[count] = s[i]
#         i = i + 1
#         count -= 1
#         list1.append(list2)
#         flag = True
#         # count = count - 1
#         list2 = [""] * numRows
#         if i < len(s):
#             list2[count] = s[i]
#         i = i + 1
# sample1 = [""] * numRows
# if list2 != sample1:
#     list1.append(list2)
# print(list1)














'''
    # def longestPalindrome(self, s: str) -> str:
s = "fkwwkkf"
max_length = 0
max_str1 = ""
set1 = set()
for i in range(len(s)):
    j = i
    k = i + 1
    str1 = ""
    flag = False
    while j > -1 and k < len(s):
        if s[j] == s[k]:
            str1 = s[j] + str1
            str1 = str1 + s[k]
            j = j - 1
            k = k + 1
        else:
            if str1 != "":
                if s[j + 1] == s[k] and flag == False and s[j+2] == s[k-1]:
                    str1 = str1 + s[k]
                    flag = True
                    k = k + 1
                    # break
                elif s[j] == s[k - 1] and flag == False and s[k-2] == s[j+1]:
                    str1 = s[j] + str1
                    flag = True
                    j = j - 1
                    # break
                else:
                    break
            elif str1 == "":
                if flag == False:
                    str1 = str1 + s[k]
                    k = k + 1
                    flag = True
                else:
                    break
    if j == -1 and k < len(s) and flag == False:
        j = 0
        if s[j] == s[k]:
            str1 = s[j] + str1
    elif k == len(s) and j > -1 and flag == False:
        k = len(s) - 1
        if s[j] == s[k]:
            str1 = str1 + s[k]

    if max_length < len(str1):
        max_length = len(str1)
        max_str1 = str1
print(max_str1)
'''

'''nums = [1,2,3,4,5,6,7,8]
k = 2
check1 = k % len(nums)
k = check1
flag = False
if len(nums) // 2 <= k:
    i = 0
    j = len(nums) - 1
    for _ in range(len(nums)//2):
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
        j = j - 1
    flag = True
else:
    i = 0
    j = len(nums) - 1
    for _ in range(k):
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
        j = j - 1
i = 0
j = k - 1
for _ in range(k//2):
    nums[i],nums[j] = nums[j],nums[i]
    i = i + 1
    j = j - 1
if flag == True:
    i = k
    j = len(nums) - 1
    while j > i:
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
        j = j - 1
else:
    print(nums)
    j = (len(nums) - 1) - k
    i = k
    while j > i:
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
        j = j - 1
    i = k
    j = len(nums)-1
    while j > i:
        nums[i],nums[j] = nums[j],nums[i]
        i = i + 1
        j = j - 1'''
    # j = len(nums) - 1
    # i = (len(nums) - 1) - k
    # print(nums)
    # print(i,j)
    # while i > k:
    #     nums[i],nums[j] = nums[j],nums[i]
    #     i = i - 1
    #     j = j - 1
    # print(i,j,nums)
    # while j > i:
    #     nums[i],nums[j] = nums[j],nums[i]
    #     i = i + 1
    #     j = j - 1
    # print(nums)


'''    # print(nums)
    # i = len(nums) - k
    # j = len(nums) - 1
    # while j > i:
    #     nums[i],nums[j] = nums[j],nums[i]
    #     i = i + 1
    #     j = j - 1'''



'''cost = [5,3,4,1,3,2]
min1 = float('inf')
arr = []
for i in range(len(cost)):
    min1 = min(cost[i],min1)
    arr.append(min1)
print(arr)'''








'''hash1 = {}
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = ""
j = 0
k = 2

for i in range(len(str2)):
    str3 = str3 + str2[i]
    if k == 7 or k == 9:
        if j == 3:
            hash1[str(k)] = str3
            j = 0
            k = k + 1
            str3 = ""
        else:
            j = j + 1
    else:
        if j == 2:
            hash1[str(k)] = str3
            k = k + 1
            j = 0
            str3 = ""
        else:
            j = j + 1

digits = "23"
lenght = 0
list1 = []
str1 = ""
ans = []
def backtracking(lenght,list1,ans):
    if lenght == len(digits):
        ans.append("".join(list1))
        return

    key = hash1[digits[lenght]]
    for i in range(len(key)):
        list1.append(key[i])
        print(backtracking(lenght+1,list1,ans))
        list1.pop()

backtracking(lenght,list1,ans)

print(ans)'''



'''nums = [10,12,13,14]
min1 = float('inf')
for i in range(len(nums)):
    str1 = str(nums[i])
    sum1 = 0
    for j in range(len(str1)):
        sum1 = sum1 + int(str1[j])
    min1 = min(min1,sum1)
print(min1)'''







'''nums = [1,3,2]
flag = False
max1 = nums[0]
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        if flag == False:
            if nums[i+1] <= max1:
                flag = True
            else:
                print(False)
                break
        elif flag == True:
            print(False)
            break
    elif nums[i] < nums[i+1]:
        if flag == True:
            if max1 >= nums[i+1]:
                pass
            else:
                print(False)
                break
else:
    print(True)
'''










'''class TrieNode:
    def __init__(self):
        self.children = {}
        self.End_of_word = False
root = TrieNode()
def insert(word):
    node = root
    for key in word:
        if key not in node.children:
            node.children[key] = TrieNode()
        node = node.children[key]
    node.End_of_word = True
def prefix(word):
    node = root
    count = 0
    for key in word:
        # print(root.children["1"].children)
        if key not in node.children:
            break
            # return count
        else:
            count += 1
        node = node.children[key]
    return count


arr1 = [1,10,100]
arr2 = [1000]
for item in arr2:
    item = str(item)
    insert(item)
max1 = 0
for item in arr1:
    item = str(item)
    a = prefix(item)
    max1 = max(max1,a)
print(max1)'''












'''a = [2,3,1]
b = [3,1,2]
set1 = set()
set2 = set()
list1 = []
pre = 0
for i in range(len(a)):
    if a[i] not in set2:
        set1.add(a[i])
    else:
        pre += 1
    if b[i] not in set1:
        set2.add(b[i])
    else:
        pre += 1
    list1.append(pre)
print(list1)
'''







'''x = 1534236469
flag = False
if x < 0:
    x = 0 - (x)
    flag = True
ans = 0
while x != 0:
    rem = x % 10
    ans = (ans*10) + rem
    x = x // 10
if flag == True:
    ans = 0 - ans
if ans >= -2147483648 and ans <=  2147483647:
    print(ans)
else:
    print(0)'''






'''words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
hash1 = {}
str1 = "abcdefghijklmnopqrstuvwxyz"
j = 25
for i in range(len(str1)):
    hash1[i] = str1[j]
    j = j - 1
str1 = ""
for item in words:
    total = 0
    for j in item:
        cal = ord(j) - 97
        total += weights[cal]
    check1 = total % 26
    str1 = str1 + hash1[check1]
print(str1)'''









'''import requests
from bs4 import BeautifulSoup

def diagram(tokens):
    entries = []
    i = 0
    while i < len(tokens) - 2:
        try:
            x = int(tokens[i])
            char = tokens[i + 1]
            y = int(tokens[i + 2])
            entries.append((x, y, char))
            i += 3
        except Exception as e:
            i += 1
    max_x = max(x1 for x1, a,b in entries)
    max_y = max(y1 for a, y1, b in entries)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in entries:
        grid[y][x] = char
    for row in grid:
        def print1(row):
            return ("".join(row))
        print(print1(row))
def decode(doc_url):
    response = requests.get(doc_url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ")
    tokens = text.split()
    diagram(tokens)

link = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
decode(link)'''





# import requests
# from bs4 import BeautifulSoup
#
#
# def decode_secret_message(doc_url):
#     # Fetch document HTML
#     response = requests.get(doc_url)
#     response.raise_for_status()
#
#     soup = BeautifulSoup(response.text, "html.parser")
#     text = soup.get_text(" ")
#     print(text)
#
#     # Extract rows containing: x y character
#     entries = []
#
#     for line in text.splitlines():
#         parts = line.strip().split()
#         print(parts)
#
#         # Expect format: x y char
#         if len(parts) >= 3:
#             try:
#                 x = int(parts[0])
#                 y = int(parts[1])
#                 char = parts[2]
#
#                 entries.append((x, y, char))
#             except ValueError:
#                 continue
#     if not entries:
#         print("No valid data found.")
#         return
#
#     # Find grid size
#     max_x = max(x for x, _, _ in entries)
#     max_y = max(y for _, y, _ in entries)
#
#     # Create empty grid
#     grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
#
#     # Fill grid
#     for x, y, char in entries:
#         grid[y][x] = char
#
#     # Print correctly oriented letters
#     for row in grid:
#         print("".join(row))
#
#
# # Example usage
# decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")
#



'''nums = [6,1,4]
k = 5
min_arr = [0] * len(nums)
min1 = float('inf')
for i in range(len(nums)-1,-1,-1):
    if nums[i] < min1:
        min1 = nums[i]
    min_arr[i] = min1
max_arr = [0] * len(nums)
max1 = 0
for i in range(len(nums)):
    if nums[i] > max1:
        max1 = nums[i]
    max_arr[i] = max1
cal1 = float('inf')
index_min = float('inf')
for i in range(len(min_arr)):
    cal2 = max_arr[i] - min_arr[i]
    if cal1 >= cal2:
        if cal2 <= k:
            if index_min >= i:
                cal1 = cal2
                index_min = i
print(index_min)'''








'''nums = [2,0,1,2,2,2,2,2]
start = 0
end = len(nums)-1
while start < end:
    if'''

















'''nums =  [2,0,0,1,0,0,2]
i = 0
j = 0
min_abs = float('inf')
while i < len(nums) and j < len(nums):
    if nums[i] == 1 and  nums[j] == 2:
        check1 = abs(i - j)
        min_abs = min(min_abs,check1)
        if i > j:
            j = j + 1
        else:
            i = i + 1
    if nums[i] == 1:
        pass
    else:
        i = i + 1
    if nums[j] == 2:
        pass
    else:
        j = j + 1
print(min_abs)'''









'''nums = [2,3,2,4,5,6,2]
def func(i):
    if i == -1:
        return nums[-1]
    elif i < -1:
        return 0
    return max(func(i-1), nums[i] + func(i-2))
print(func(len(nums)-1))'''



'''nums = [11,13,15,17]
start = 0
end = len(nums)-1
last = nums[-1]
while start < end:
    mid = (start + end)//2
    if nums[mid] > last:
        start = mid+1
    else:
        end = mid
        last = nums[mid]
print(last)'''














'''nums = [20744,7642,19090,9992,2457,16848,3458,15721]
limit = 22891
list1 = []
j = len(nums) - 1
for i in range(len(nums)//2):
    list1.append((nums[i],nums[j]))
    j = j - 1
ans = float('inf')
for i in range(2,(limit*2)+1):
    count = 0
    for a,b in list1:
        if i == (a+b):
            continue
        elif 1 <= i-a <= limit or 1 <= i-b <= limit:
            count += 1
        else:
            count += 2
    ans = min(ans,count)
print(ans)'''




'''nums = [20744,7642,19090,9992,2457,16848,3458,15721]
limit = 22891
count_less_limit = 0
count_more_limit = 0
hash1_less_limit = {}
hash1_more_limit = {}
max_less_limit = 0
min_more_limit = float('inf')
j = len(nums) - 1
for i in range(len(nums)//2):
    cal = nums[i] + nums[j]
    if cal > limit:
        if cal not in hash1_more_limit:
            hash1_more_limit[cal] = 1
        else:
            hash1_more_limit[cal] += 1
        count_more_limit += 1
        min_more_limit = min(min_more_limit,cal)
    else:
        if cal not in hash1_less_limit:
            hash1_less_limit[cal] = 1
        else:
            hash1_less_limit[cal] += 1
        count_less_limit += 1
        max_less_limit = max(max_less_limit,cal)
    j = j - 1
dict1 = {}
value1 = 1
rounding = 0
print(hash1_more_limit,hash1_less_limit)
if count_less_limit < count_more_limit:
    dict1 = hash1_more_limit
    rounding = min_more_limit
else:
    dict1 = hash1_less_limit
    rounding = max_less_limit
flag = False
for key, value in dict1.items():
    if value > value1:
        flag = True
        value1 = value
        rounding = key
if flag == False:
    print(len(nums)//2)
ans = 0
print(rounding)
j = len(nums)- 1
for i in range(len(nums)//2):
    cal = nums[i] + nums[j]
    if cal == rounding:
        pass
    else:
        if cal > rounding:
            print(cal, nums[i], nums[j])
            max2 = max(nums[i],nums[j])
            cal2 = abs(cal - rounding)
            max2 = max2 - cal2
            if max2 <= 0:
                print("vhd")
                ans += 2
            else:
                ans += 1
        elif cal < rounding:
            # print(cal,nums[i],nums[j])
            min2 = min(nums[i],nums[j])
            cal2 = abs(rounding - cal)
            min2 = min2 + cal2
            if min2 > limit:
                print("uururu")
                ans += 2
            else:
                ans += 1
    j = j - 1
print(ans)'''












'''capacity = [1,5,3,7]
itemSize = 3
min1 = -1
capacity_box = float('inf')
for i in range(len(capacity)):
    if capacity[i] >= itemSize:
        if capacity_box > capacity[i]:
            min1 = i
            capacity_box = capacity[i]
print(min1)'''




'''nums = [28,50,76,80,64,30,32,84,53,8]
limit = 84
half = limit//2
hash1 = {}
j = len(nums)-1
sum1 = 0
for i in range(len(nums)//2):
    cal = nums[i] + nums[j]
    if cal not in hash1:
        hash1[cal] = 1
    else:
        hash1[cal] += 1
    j = j - 1
if limit %  2 != 0:
    half += 1
max1 = 0
value1 = 0
for key, value in hash1.items():
    # sum1 = sum1 + key
    # sum1 = sum1 + nums[j]
    if value > value1:
        max1 = key
        value1 = value
max1 = 36
ans = 0
j = len(nums) - 1
for i in range(len(nums)//2):
    cal = nums[i] + nums[j]
    min1 = min(nums[i],nums[j])
    max2 = max(nums[i],nums[j])
    if cal == max1:
        pass
    else:
        if cal > max1:
            if min1 > max1:
                ans += 2
            else:
                ans += 1
        elif cal < max1:
            if max2 < max1:
                ans += 2
            else:
                ans += 1


    j = j - 1
print(ans)
print(hash1)
print(max1)''











'''
'''nums = [2, 1, 1, 2]
dp = [0] * (len(nums) + 1)
for i in range(len(nums)):
    cal1 = dp[i]
    cal2 = nums[i]
    if i > 0:
        cal2 = nums[i] + dp[i-1]
    dp[i+1] = max(cal1,cal2)
print(dp[-1])'''


'''nums = [1, 2, 3]
dp = [-1] * len(nums)
i = len(nums) - 1
def func(i):
    print(i)
    if i == 0:
        dp[i] = nums[i]
        return dp[i]
    elif i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] =  max(func(i-1), (nums[i] + func(i-2)))
    return dp[i]
print(func(i))'''




'''nums = [1, 2, 3, 2, 1, 4,5,6,7]
def func(i):
    if i == 0 or i == 1:
        return nums[i]
    elif i == 2:
        return nums[i] + nums[i-2]
    check1 = func(i-2)
    check2 = func(i-3)
    a = nums[i] + max(func(i-2),func(i-3))
    list1.append(a)
    i = i - 1
    if i == 3:
        b = nums[i] + max(func(i - 2), func(i - 3))
        list1.append(b)
        return b
    return (a)

list1 = []
print(func(len(nums)-1))
print(list1)'''

# nums = [1, 2, 3, 2, 1, 4,5,6,7]


# def func(i):
#     if i == 0:
#         return nums[i]







'''nums = [1, 1, 2, 2]
hash1 = {}
for i in range(len(nums)):
    if nums[i] not in hash1:
        hash1[nums[i]] = 1
    else:
        hash1[nums[i]] += 1
find_num = float('inf')
freq = 0
for key, value in hash1.items():
    if key < find_num:
        find_num = key
        freq = value
second_num = float('inf')
for key, value in hash1.items():
    if freq != value:
        if second_num > key > find_num:
            second_num = key
print(find_num,second_num)'''





'''grid = [[40,10],[30,20]]
k1 = 1

# [[3,4,8,12],
# [2,11,10,16],
# [1,7,6,15],
# [5,9,13,14]]

# k1 = 2
m = len(grid)
n = len(grid[0])
div = 0
if m < n:
    div = m // 2
else:
    div = n//2
matrix = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
matrix2 = []
count = 0
while count < div:
    list1 = []
    for j in range(count,len(grid[0])-count):
        list1.append(grid[count][j])
    for k in range(count+1,len(grid) - count):
        list1.append(grid[k][len(grid[0])-1-count])
    for k in range((len(grid[0])-1)-count-1, count-1,-1):
        list1.append(grid[(len(grid)-1)-count][k])
    for k in range((len(grid)-1)-count-1,count-1+1,-1):
        list1.append(grid[k][count])
    count += 1
    matrix2.append(list1)
count = 0
l = 0
while l < div:
    len_inner_list= len(matrix2[l])
    rem = k1 % len_inner_list
    start = rem
    for j in range(count,len(grid[0])-count):
        matrix[count][j] = matrix2[l][start]
        print(matrix,start)
        # print(matrix2[l][start])
        start += 1
        if start == len_inner_list:
            start = 0
    for k in range(count+1,len(grid) - count):
        matrix[k][len(grid[0])-1-count] = matrix2[l][start]
        start += 1
        if start == len_inner_list:
            start = 0
    for k in range((len(grid[0])-1)-count-1, count-1,-1):
        matrix[(len(grid)-1)-count][k] = matrix2[l][start]
        start += 1
        if start == len_inner_list:
            start = 0
    for k in range((len(grid)-1)-count-1,count-1+1,-1):
        matrix[k][count] = matrix2[l][start]
        start += 1
        if start == len_inner_list:
            start = 0
    l = l + 1
    count += 1
print(matrix)'''











'''bulbs = [100,100]
hash1 = {}
for i in range(len(bulbs)):
    if bulbs[i] not in hash1:
        hash1[bulbs[i]] = 1
    else:
        hash1[bulbs[i]] += 1
list1 = []
for key, value in hash1.items():
    if value % 2 != 0:
        list1.append(key)
print(list1)'''






'''words =["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
str1 = "abcdefghijklmnopqrstuvwxyz"
# print(len(str1))
count = 0
hash1 = {}
for i in range(len(str1) -1,-1,-1):
    hash1[count] = str1[i]
    count += 1
k = 0
str_ans = ""
for i in range(len(words)):
    sum1 = 0
    for j in range(len(words[i])):
        print(weights[k])
        sum1 += weights[k]
        k = k + 1
    cal = sum1 % 26
    # print(sum1)
    str_ans += hash1[cal]
print(str_ans)
print(hash1)'''







# grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# k = 2
# matrix = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
# list1 = []








'''nums = [4,1,2]
numb = len(nums)
sum1 = sum(nums)
count = 0
for i in range(len(nums)-1):
    sum1 = sum1 - nums[i]
    numb = numb - 1
    ave = (sum1//numb)
    if nums[i] > ave:
        count += 1
print(count)'''









'''from collections import deque
sequence = "bababa"
word = "aba"
list1 = [0] * (len(sequence) + 1)
word_freq = deque()
for i in word:
    word_freq.append(i)
window_freq = deque()
i = 0
max1 = 0
for j in range(len(sequence)):
    if j < len(word):
        window_freq.append(sequence[j])
    else:
        window_freq.popleft()
        window_freq.append(sequence[j])
        i = i + 1
    if window_freq == word_freq:
        i = i + 1
        j = j + 1
        ith_index = list1[i-1]
        list1[j] = ith_index + 1
        max1 = max(max1,list1[j])
        i = i - 1
        j = j - 1
print(list1)
print(max1)'''






'''
from collections import deque
sequence = "aaaabab"
word = "aa"
list1 = [0] * len(sequence)
set1 = set(list(sequence))
set2 = set(list(word))
if len(set1) == 1 and set1 == set2:
    cal = len(sequence)// len(word)
    print(cal)
word_freq = deque()
for i in word:
    word_freq.append(i)
window_freq = deque()
i = 0
boudry = 0
count = 0
max1 = 0
for j in range(len(sequence)):
    if j < len(word):
        window_freq.append(sequence[j])
    else:
        window_freq.popleft()
        window_freq.append(sequence[j])
        i = i + 1
    if window_freq == word_freq:
        if boudry > i:
            max1 = max(max1,count)
            count = 0
            count += 1
            boudry = j+1
        elif boudry < i:
            max1 = max(max1, count)
            count = 0
            count += 1
            boudry = j+1
        elif boudry == i:
            count += 1
            boudry = j+1
max1 = max(max1,count)
print(max1)'''















'''boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]

for i in range(len(boxGrid)):
    count = 0
    for j in range(len(boxGrid[i])):
        if boxGrid[i][j] == "*":
            boxGrid[i][j] = count
            count = 0
        elif boxGrid[i][j] == "#":
            count += 1
    boxGrid[i].append(count)
for i in range(len(boxGrid)-1,-1,-1):
    check1 = 0
    for j in range(len(boxGrid[i])-1,-1,-1):
        if boxGrid[i][j] != "." and boxGrid[i][j] != "#":
            check1 = boxGrid[i][j]
            boxGrid[i][j] = "*"
        elif check1 > 0:
            boxGrid[i][j] = "#"
            check1 -= 1
        else:
            boxGrid[i][j] = "."
    boxGrid[i].pop()
main_lsit1 = []
for i in range(len(boxGrid[0])):
    list1 = []
    for j in range(len(boxGrid)-1,-1,-1):
        list1.append(boxGrid[j][i])
    main_lsit1.append(list1)
print(main_lsit1)'''










# s = ""
# max1 = 0
# i = 0
# j = 0
# count1 = 0
# list1 = [-1] * 256
# while j < len(s):
#     cal = ord(s[j]) - 97
#     list1[cal] += 1
#     set1 = set(list1)
#     if len(set1) == 2 and 0 in set1 and -1 in set1:
#         count1 += 1
#         j = j + 1
#     else:
#         cal = ord(s[i]) - 97
#         list1[cal] -= 1
#         i = i + 1
#         j = j + 1
#     max1 = max(max1, count1)
#     if count1 < 0:
#         count1 = 0
# print(max1)







# list1_alphabet = []
# str1 = ""
# for i in range(len(s)):
#     if "a"<= s[i] <= "z":
#         str1 += s[i]
#     else:
#         list1_alphabet.append(str1)
#         str1 = ""
# if str1 != "":
#     list1_alphabet.append(str1)
#
# max1 = 0
# for item in list1_alphabet:
#     s = item


'''n = 4
dp = [-1] * (n+1)
def stair(dp,n):
    print(dp)
    if n <= 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = stair(dp,n-1) + stair(dp,n-2)
    return dp[n]
print(stair(dp,n))
print(dp)

n = 7
def fibo(dp,n):
    print(dp)
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(dp,n-1) + fibo(dp,n-2)
    return dp[n]
dp = [-1] * (n+1)
print(fibo(dp,n))
print(dp)'''





'''str1 = "ABCABC"
str2 = "ABC"
set1 = set(list(str1))
set2 = set(list(str2))

int_str1 = 0
int_str2 = 0
hash1 = {}
list1 = ""
for i in str1:
    cal = ord(i) - 64
    int_str1 = (int_str1 * 10) + cal
    list1 = list1 + i
    hash1[int_str1] = list1
for i in str2:
    cal = ord(i) - 64
    int_str2 = (int_str2 * 10) + cal
# print(int_str1,int_str2)
divide = 0
larget = 0
for i in range(len(str1)):
    cal = ord(str1[i]) - 64
    divide = (divide * 10) + cal
    if int_str1 % divide == 0 and int_str2 % divide == 0:
        larget = divide
check1 = ""
if larget in hash1:
    alph = hash1[larget]

    alphh_list = set(list(alph))
    if len(alphh_list) == 1:
        if len(set1) == 1 and len(set2) == 1:
            print(alph)
        else:
            print("")
    else:
        check1 = alph
else:
    print("")
list1 = list(set1)
list2 = list(set2)
hash1 = {}
hash2 = {}
for item in list1:
    hash1[item] = False
for item in list2:
    hash2[item] = False
for item in check1:
    if item in hash1:
        hash1[item] = True
    if item in hash2:
        hash2[item] = True
for value in hash1.values():
    if value == False:
        print("")
        break
for value in hash2.values():
    if value == False:
        print("")
        break
print(check1)'''

'''matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
m = len(matrix)
n = len(matrix[0])
dp = [["false" for i in range(n)] for j in range(m)]
k = 0
count = 0
ans = []
while k < m*n:
    for i in range(count, n - count):
        if dp[count][i] != "false":
            count += 1
            break
        else:
            ans.append(matrix[count][i])
            dp[count][i] = True
            k = k + 1

    for i in range(count + 1, m - count):
        if dp[i][n - count - 1] != "false":
            count += 1
            break
        else:
            ans.append(matrix[i][n - count - 1])
            dp[i][n - count - 1] = True
            k = k + 1
    for i in range((n - count - 2), count - 1, -1):
        print(i)
        if dp[m - count - 1][i] != "false":
            count += 1
            break
        else:
            ans.append(matrix[m - count - 1][i])
            dp[m - count - 1][i] = True
            k = k + 1

    for i in range((m - count - 2), count - 1, -1):
        if dp[i][count] != "false":
            count += 1
            break
        else:
            ans.append(matrix[i][count])
            dp[i][count] = True
            k = k + 1

print(dp,ans)'''








# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# k = len(matrix) - 1
# inre = 0
# if len(matrix) % 2 != 0:
#     inre += 1
# for i in range((len(matrix)//2)):
#     l = len(matrix[i]) - 1
#     for j in range((len(matrix[i])//2)+inre):
#         matrix[i][j],matrix[j][k],matrix[k][l],matrix[l][i] = matrix[l][i], matrix[i][j],matrix[j][k],matrix[k][l]
#         l = l - 1
#     k = k - 1
# print(matrix)

# a = matrix[i][j]
# b = matrix[j][k]
# c = matrix[k][l]
# d = matrix[l][i]
# print(a,b,c,d)
# matrix[j][k] = a
# matrix[k][l] = b
# matrix[l][i] = c
# matrix[i][j] = d


# matrix[i][j],matrix[i][l],matrix[k][l],matrix[l][i] = matrix[l][i],matrix[i][j],matrix[i][l],matrix[i][j]



'''from collections import deque
s = "defdefdefabcabc"
goal = "defdefabcabcdef" 
if len(s) == len(goal):
    pass
else:
    print(False)
list1 = []
queue1 = deque()
for i in range(len(s)):
    queue1.append(s[i])
    list1.append(goal[i])
if list1 == list(queue1):
    print(True)
print(list1,queue1)
for i in range(len(s)):
    pop1 = queue1.popleft()
    queue1.append(pop1)
    if list(queue1) == list1:
        print(True)
        break
else:
    print(False)

print(list1,queue1)'''










'''name = "zlexya"
typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"
if len(name) <= len(typed):
    pass
else:
    print(False)
i = 0
j = 0
flag = False
last = 0
rev = ""
forw = ""
while j < len(typed) and i < len(name):
    if name[i] == typed[j]:
        i = i + 1
        j = j + 1
        flag = True
    elif name[i] != typed[j]:
        if i > 0:
            if name[i-1] == typed[j]:
                pass
            else:
                print(name[i-1],typed[j])
                print(False)
                break
        j = j + 1
if j < len(typed):
    hold = typed[j-1]
    for k in range(j,len(typed)):
        if typed[k] == hold:
            pass
        else:
            print(False)
            break
if i == len(name):
    print(True)
else:
    print(False)
print(i,j)'''


# name_arr = [0] * 26
# typed_arr = [0] * 26
# for i in range(len(name)):
#     cal = ord(name[i]) - 97
#     name_arr[cal] += 1
# for i in range(len(typed)):
#     cal = ord(typed[i]) - 97
#     typed_arr[cal] += 1
# for i in range(len(name_arr)):
#     if name_arr[i] <= typed_arr[i]:
#
#         pass
#     else:
#         print(False)
#         break
# else:
#     print(True)




'''sequence = "ababc"
word = "ab"
list1 = [0] * 26
for item in word:
    index = 97 - ord(item)
    list1[index] += 1
i = 0
j = 0
while j < len(sequence):'''








# n = 23
# list1 = set()
# count = 0
# for i in range(1,n+1):
#     str1 = str(i)
#     ans = ""
#     flag = False
#     for j in range(len(str1)):
#         if str1[j] == "2":
#             ans += "5"
#         elif str1[j] == "5":
#             ans += "2"
#         elif str1[j] == "6":
#             ans += "9"
#         elif str1[j] == "9":
#             ans += "6"
#         else:
#             if str1[j] == "3" and str1[]
#             # if str1[j] != "0":
#             #     print(i)
#             #     flag = True
#             ans += str1[j]
#     # if flag == False:
#     if i != int(ans):
#         # list1.add(int(ans))
#         list1.add(i)
#         count += 1
# print(count)
# print(list1)
# print(len(list1))





'''num = 7
str1 = ""
while num:
    cal = num % 7
    str1 = str(cal) + str1
    num = num//7
    print(num)
print(str1)'''


'''nums = [4,3,2,6]
f = 0
numsum = sum(nums)
for i in range(len(nums)):
    f = f + (i * nums[i])
# print(f)
res = f
for i in range(len(nums)-1,0,-1):
    # print(numsum - (len(nums)*nums[i]))
    # print(f)
    f = f + (numsum - (len(nums)*nums[i]))
    print(f)
    # print(f)'''










'''num = 342003
k = 3
num2 = str(num)
sub = ""
for i in range(k):
    sub += num2[i]
sub = int(sub)
total = 0
i = 0
j = k
while j < len(num2):
    if sub and num % sub == 0:
        total += 1
    sub = sub - int(num2[i])*(10 **(k-1))
    sub = (sub * 10) + int(num2[j])
    j = j + 1
    i = i + 1
if sub and num % sub == 0:
    total += 1

print(total)
'''



# for i in range((len(num2)-k)+1):
#     str1 = ""
#     for j in range(i, i + k):
#         str1 += num2[j]
#     cal = int(str1)
#     if cal and num % cal == 0:
#         total += 1
# print(total)










'''sequence ="aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
if len(word) > len(sequence):
    print(False)
i = 0
j = 0
k = 0
# flag = False
count = 0
max1 = 0
while j < len(sequence):
    if word[k] == sequence[j]:
        k = k + 1
        count += 1
        # flag = True
    else:
        print(j)
        i = j + 1
        # flag = False
        cal = count//len(word)
        max1 = max(max1,cal)
        k = 0
        count = 0
    if k == len(word):
        i = j + 1
        k = 0
    j = j + 1
cal = count // len(word)
max1 = max(max1,cal)
print(max1)'''








'''# grid = [[596,904,960,232,120,932,176],[372,792,288,848,960,960,764],[652,92,904,120,680,904,120],[372,960,92,680,876,624,904],[176,652,64,344,316,764,316],[820,624,848,596,960,960,372],[708,120,456,92,484,932,540]]
grid = [[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]]
x = 84
list1 = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        list1.append(grid[i][j])
list1.sort()
mid_int = 0
mid_values = []
if len(list1) % 2 == 0:
    mid = len(list1) // 2
    mid_int = (list1[mid-1] + list1[mid])//2
    for i in range(len(list1)):
        if list1[i] == mid_int:
            mid_values.append(mid_int)
            break
    else:
        mid_int = list1[mid-1]
        mid_int1 = list1[mid]
        mid_values.append(mid_int)
        mid_values.append(mid_int1)
else:
    mid = len(list1) // 2
    mid_int = list1[mid]
    for i in range(len(list1)):
        if list1[i] == mid_int:
            mid_values.append(mid_int)
            break
    else:
        mid_int = list1[mid]
        mid_int1 = list1[mid + 1]
        mid_values.append(mid_int)
        mid_values.append(mid_int1)
if len(list1) == 1:
    print(0)
min1 = float('inf')
total = 0
for mid_int in mid_values:
    for j in range(len(list1)):
        now = abs(list1[j] - mid_int)
        if now == 0:
            pass
        if now % x == 0:
            count = now // x
            total += count
        else:
            total = 0
            break
    else:
        min1 = min(min1, total)
    if type(min1) == float:
        print(-1)
print(min1)
print(mid_values)
'''




'''s = "pfpfgi"
hash1 = {}
for item in s:
    if item in hash1:
        hash1[item] += 1
    else:
        hash1[item] = 1
hash2 = {}
for key,value in hash1.items():
    if value not in hash2:
        hash2[value] = key
    else:
        hash2[value] += key
max_group_len = 0
max_group = ""
max_freq = ""
for key,value in hash2.items():
    if len(value) > max_group_len:
        max_group_len = len(value)
        max_freq = key
        max_group = value
    elif len(value) == max_group_len:
        if key > max_freq:
            max_group = value
            max_freq = key
print(max_group)'''






'''import math
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# len_str1 = len(str1)
# len_str2 = len(str2)
# root_val = math.ceil(math.sqrt(len_str1)) + 1
# gcd = 0
# for i in range(2,root_val+1):
#     if len_str2 % i == 0 and len_str1 % i == 0:
#         gcd = i
# print(gcd)





list2 = []
max1 = ""
min1 = ""
if len(str1) > len(str2):
    max1 = str1
    min1 = str2
else:
    max1 = str2
    min1 = str1
list1 = []
list2 = []
for i in range(len(min1)):
    list2.append(min1[i])
i = 0
count = 1
min_count = 0
while i < len(max1):
    if min_count == len(min1):
        min_count = 0
        if list1 == list2:
            list1 = []
        else:
            print("")
            break
    else:
        list1.append(max1[i])
        i = i + 1
        min_count += 1
if len(list1) == len(list2):
    if list1 == list2:
        ans = "".join(list1)
        print(ans)
    else:
        print("")

else:
    str_ans = "".join(list1)
    len_str = len(str_ans)
    print(len_str)'''









'''str1 = "AAAAAB"
str2 = "AAA"
str1_int = ""
str2_int = ""
for item in str1:
    cal = ord(item) - 64
    str1_int += str(cal)
for item in str2:
    cal = ord(item) - 64
    str2_int += str(cal)
max1 = ""
min1 = ""
if len(str1_int) > len(str2_int):
    max1 = str1_int
    min1 = str2_int
else:
    max1 = str2_int
    min1 = str1_int
cal = int(max1) % int(min1)
if cal == 0:
    print(min1)
else:
    if int(min1) % cal == 0:
        print(cal)
    else:
        print("")'''







'''command = "(al)G(al)()()G"
stack = []
ans = ""
for i in range(len(command)):
    if command[i] == "G":
        ans += command[i]
        stack.append("G")
    else:
        if command[i] == "(":
            stack.append(command[i])
        elif command[i] == "l":
            stack.append("al")
            ans += "al"
        elif command[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                ans += "o"
print(ans)'''








'''str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
max1 = ""
min1 = ""
if len(str1) > len(str2):
    max1 = str1
    min1 = str2
else:
    max1 = str2
    min1 = str1
# i = 0
# j = 0
# while i < len(max1):
#     if max1[i] == min1[j]:
#         pass
#     else:
#         print(False)
#         break
#     i = i + 1
#     j = j + 1
#     if j == len(min1):
#         j = 0
# if i == len(max1) and j < len(min1):
#     print(i ,j)
#     print(False)
hash1 = set()
ans_list1 = []
temp_list = []
for item in min1:
    if item not in hash1:
        hash1.add(item)
        ans_list1.extend(temp_list)
        temp_list = []
        ans_list1.append(item)
    else:
        temp_list.append(item)
join1 = "".join(ans_list1)
print(ans_list1)
ans = ""
while len(ans) < len(max1):
    ans +=join1
print(ans,max1)
if ans == max1:
    print(join1)
else:
    print("")'''



'''s = "a0bcd33"
list1 = []
list2 = []
for item in s:
    if "a" <= item <= "z":
        list1.append(item)
    else:
        list2.append(item)
ans = ""
i = 0
j = 0
diff1 = abs(len(list1) - len(list2))
if diff1 <= 1:
    max1 = ""
    min1 = ""
    if len(list1) > len(list2):
        max1 = list1
        min1 = list2
    else:
        max1 = list2
        min1 = list1
    i = 0
    j = 0
    flag = False
    while True:
        if flag == False:
            ans += max1[i]
            i = i + 1
            flag = True
        else:
            ans += min1[j]
            j = j + 1
            flag = False
        if i == len(max1) and j == len(min1):
            break
print(ans)'''




'''str1 = "AAAAAB"
str2 = "AAA"
str3 = ""
str4 = ""
for item in str1:
    cal = ord(item) - 64
    str3 += str(cal)
for item in str2:
    cal = ord(item) - 64
    str4 += str(cal)
str3 = int(str3)
str4 = int(str4)
max1 = max(str3,str4)
min1 = min(str3,str4)
cal = max1 % min1
hash1 = set()
min1 = str(min1)
ans_list1 = []
temp_list = []
for item in min1:
    if item not in hash1:
        hash1.add(item)
        ans_list1.extend(temp_list)
        temp_list = []
        ans_list1.append(item)
    else:
        temp_list.append(item)
print(ans_list1)'''











'''s = "Test1ng-Leet=code-Q!"
alph = ""
for i in range(len(s)):
    if "a" <= s[i] <= "z" or "A" <= s[i] <=  "Z":
        alph += s[i]
j = len(alph) - 1
ans = ""
for i in range(len(s)):
    if "a" <= s[i] <= "z" or "A" <= s[i] <=  "Z":
        ans += alph[j]
        j = j - 1
    else:
        ans += s[i]
print(ans)'''







'''moves = "_R__LL_"
count_l = 0
count_r = 0
count_space = 0
for i in range(len(moves)):
    if moves[i] == "R":
        count_r += 1
    elif moves[i] == "L":
        count_l += 1
    else:
        count_space += 1
sum1 = 0
if count_r > count_l:
    sum1 = sum1 + (count_r - count_l) + count_space
else:
    sum1 = sum1 + (count_l - count_r) + count_space
print(sum1)'''






'''nums = [1,4,6,8,10]
rightsum = sum(nums)
leftsum = 0
result = [0] * len(nums)
for i in range(len(nums)):
    rightsum = rightsum - nums[i]
    left_cal = i * nums[i]
    right_cal = ((len(nums) - 1) - i) * nums[i]
    cal1 = abs(leftsum - left_cal)
    cal2 = abs(rightsum - right_cal)
    leftsum = leftsum + nums[i]
    ans = cal2 + cal1
    result[i] = ans
print(result)
'''












'''from  collections import  defaultdict
nums = [1,3,1,1,2]
hash1 = defaultdict(list)
for i in range(len(nums)):
    hash1[nums[i]].append(i)
ans = [0] * len(nums)
for value in hash1.values():
    prefix = 0
    total = sum(value)
    size = len(value)
    for j in range(len(value)):
        ans[value[j]] = total - prefix * 2 + value[j] * (2 * j - size)
        prefix += value[j]
print(ans)
'''


'''n = 4
str1 = ""
while n > 0:
    rem = n % 2
    str1 = str(rem) + str1
    n = n // 2
print(str1)'''




'''num = "4206"
str1 = []
str2 = []
index = ""
for i in range(len(num)):
    if int(num[i]) % 2 != 0:
        str2.append(num[i])
        # str1 = str1 + str2
        index = i

    else:
        str2.append(num[i])
if index == "":
    print("")
print("".join(str2[:index+1]))'''









# list1 = []
# for i in range(len(num)-1,-1,-1):
#     list1.append(num[i])
# str1 = "".join(list1)
# int1 = int(str1)
# print(list1)
# # while int1 > 0:
# #     pass




# num = "35427"
# int1 = int(num)
# prev = 0
# max1 = 0
# while int1 > 0:
#     if int1 % 2 != 0:
#         max1 = max(max1,int1)
#     if prev % 2 != 0:
#         max1 = max(max1,prev)
#     rem = int1 % 10
#     prev = (prev * 10) + rem
#     int1 = int1 // 10
# if max1 == 0:
#     print(0)
# else:
#     print(str(max1))




'''words = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
hash1 = {}
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] not in hash1:
            hash1[words[i][j]] = 1
        else:
            hash1[words[i][j]] += 1
print(hash1)
check1 = 0
str1 = ""
for key, value in hash1.items():
    if check1 == 0:
        check1 = value
        str1 = key
    elif value != check1:
        print(False)
        break
    elif value == check1:
        if value == 1:
            if key == str1:
                pass
            else:
                print(False)
                break
else:
    print(True)'''









'''nums = [0,1]
check1 = nums[0]
max1 = 0
for i in range(len(nums)-1,0,-1):
    if nums[i] != check1:
        cal = abs(i - 0)
        max1 = max(max1,cal)
check2 = nums[-1]
for i in range(len(nums)-1):
    if nums[i] != check2:
        cal = abs(i - (len(nums)-1))
        max1 = max(max1,cal)
print(max1)'''





# list1 = []
# main_list1 = []
# i = 0
# j = 0
# max1 = 0
# prev = nums[0]
# while j < len(nums):
#     if nums[i] == nums[j]:
#         if list1 == []:
#             list1 = [nums[i],i,j]
#         else:
#             list1[2] += 1
#         j = j + 1
#     else:
#         main_list1.append(list1)
#         i = j
#         list1 = []
# if list1 != []:
#     main_list1.append(list1)
# print(main_list1)

# max_diff = 0
# for item in





'''nums1 = [2]
nums2 = [2,2,1]
i = len(nums1) - 1
j = len(nums2) - 1
start = -1
end = -1
max1 = 0
count = 0
while i >= 0 and j >= 0:
    if i > j:
        i = i - 1
    elif nums1[i] <= nums2[j]:
        if end == -1:
            end = j
            start = i
        else:
            start = i
        i = i - 1
    else:
        if start != -1 and end != -1:
            cal = end - start
            max1 = max(max1,cal)
        start = -1
        end = -1
        max1 = max(max1,count)
        j = j - 1

if start != -1 and end != -1:
    cal = end - start
    max1 = max(max1,cal)
print(max1)'''









'''s = "xyzzaz"
count = 0
for i in range(len(s) - 2):
    a = s[i]
    b = s[i+1]
    c = s[i+2]
    print(a,b,c)
    if a != b != c != a:
        count += 1
print(count)
'''





'''nums = [12,21,45,33,54]
hash1 = {}
min1 = float('inf')
for i in range(len(nums)):
    if nums[i] in hash1:
        cal = i - hash1[nums[i]]
        min1 = min(min1,cal)
    n = nums[i]
    int1 = 0
    while n > 0:
        rem = n % 10
        int1 = (int1 * 10) + rem
        n = n // 10
    hash1[int1] = i
print(min1)'''








# nums =  [21,120]
# hash1 = {}
# for i in range(len(nums)):
#     if nums[i] not in hash1:
#         hash1[nums[i]] = [i]
#     else:
#         hash1[nums[i]].append(i)
# list1 = []
# for i in range(len(nums)):
#     n = nums[i]
#     int1 = 0
#     while n > 0:
#         rem = n % 10
#         int1 = (int1 * 10) + rem
#         n = n // 10
#     list1.append(int1)
# min1 = float('inf')
# for i in range(len(list1)):
#     if list1[i] in hash1:
#         list2 = hash1[list1[i]]
#         if len(list2) == 1:
#             if list2[0] > i:
#                 cal = abs(list2[0] - i)
#                 min1 = min(min1, cal)
#         else:
#             left = 0
#             right = len(list2)-1
#             while left < right:
#                 mid = (left + right) // 2
#                 print(mid,list2)
#                 if mid > 0:
#                     if list2[mid] > i:
#                         right = mid
#                     elif list2[mid] > i and list2[mid - 1] <= i:
#                         cal = abs(list2[mid] - i)
#                         min1 = min(min1, cal)
#                         break
#                     else:
#                         left = mid + 1
#                 elif mid == 0 and len(list2) == 2:
#                     if list2[mid] > i:
#                         cal = abs(list2[mid] - i)
#                         min1 = min(min1, cal)
#                     elif list2[mid+1] > i:
#                         cal = abs(list2[mid+1] - i)
#                         min1 = min(min1,cal)
#                     break
#
# print(min1)





# print(hash1)
# min1 = float('inf')
# for i in range(len(nums)):
#     if nums[i] in hash1:
#         list1 = hash1[nums[i]]
#         for j in range(len(list1)):
#             if list1[j] != i:
#                 cal = abs(list1[j] - i)
#                 min1 = min(min1, cal)
# print(min1)








'''nums = [1,2,3,4]
queries = [0,1,2,3]
hash1 = {}
hash2 = {}
for i in queries:
    hash1[nums[i]] = []
    hash2[i] = nums[i]
for i in range(len(nums)):
    if nums[i] in hash1:
        hash1[nums[i]].append(i)
for value in hash1.values():
    value.append(0)
print(hash1)
ans = [-1] * len(queries)
index = 0
for key, value in hash2.items():
    if value in hash1:
        if len(hash1[value]) == 1:
            pass
        else:
            min1 = float('inf')
            for j in range(len(hash1[value])):
                if hash1[value][j] == key:
                    if j == 0:
                        prev = (len(nums) - hash1[value][j-1]) + hash1[value][j]
                        next = abs(hash1[value][j] - hash1[value][j+1])
                        min1 = min(min1,prev,next)
                    elif j == len(hash1[value]) - 1:
                        prev = abs(hash1[value][j-1] - hash1[value][j])
                        next = hash1[value][0] + (len(nums) - hash1[value][j])
                        min1 = min(min1,prev,next)
                    else:
                        prev = abs(hash1[value][j] - hash1[value][j-1])
                        next = abs(hash1[value][j] - hash1[value][j+1])
                        min1 = min(min1, prev, next)
            ans[index] = min1
    index += 1
print(ans)'''



# index = 0
# for key, value in hash1.items():
#     if len(value) == 1:
#         ans[index] = -1
#     else:
#         min1 = float('inf')
#         for j in range(len(value)-1):
#             prev = value[j] + (len(nums) - value[j-1])
#             next = abs(value[j] - value[j+1])
#             min1 = min(min1,prev,next)
#         ans[index] = min1
#     index += 1
# print(ans)





'''s =  "1"
list1 = [[0,0] for i in range(len(s))]
max1 = 0
max0 = 0
if s[0] == "0":
    list1[0][1] = 1
    max0 = 1
else:
    list1[0][0] = 1
    max1 = 1
for i in range(1,len(s)):
    if s[i] == "1":
        cal = list1[i-1][0] + 1
        list1[i][0] = cal
        max1 = max(max1,cal)
    else:
        cal = list1[i-1][1] + 1
        list1[i][1] = cal
        max0 = max(max0,cal)
if max0 >= max1:
    print(False)
else:
    print(True)'''





#
# words = ["ibkgecmeyx","jsdkekkjsb","gdjgdtjtrs","jsdkekkjsb","jsdkekkjsb","jsdkekkjsb","gdjgdtjtrs","msjlfpawbx","pbgjhutcwb","gdjgdtjtrs"]
# target ="pbgjhutcwb"
# startIndex = 0
# min1 = float('inf')
# next = startIndex
# prev = startIndex - 1
# if words[next] == target:
#     print(0)
# elif words[prev] == target:
#     print(1)
# next_count = 0
# prev_count = 0
# for i in range(len(words)):
#     next_count += 1
#     prev_count += 1
#     if words[prev] == target:
#         print(min(prev_count,next_count))
#         break
#     if words[next] == target:
#         print(min(prev_count, next_count))
#         break
#     prev -= 1
#     next += 1
#     if prev == -1:
#         prev = len(words) - 1
#     if next == len(words):
#         next = 0
# else:
#     print(min1)










'''s = "is2 sentence4 This1 a3"
list1 = s.split(" ")
hash1 = {}
for item in list1:rds = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
    num = int(item[-1])
    hash1[num] = item
list2 = []
for item in hash1.items():
    list2.append(item)
list2.sort(key=lambda x:x[0])
print(list2)
str2 = ""
for item in range(len(list2)):
    # print(list2[item][1])
    sam = list2[item][1][:len(list2[item][1])-1]
    if item < len(list2) - 1:
        str2 = str2 + sam + " "
    else:
        str2 = str2 + sam
print(str2)'''














'''s = "a1b2c3d4e"
list1 = list(s)
for i in range(1,len(list1),2):
    cal = ord(s[i-1]) + int(s[i])
    ch1 = chr(cal)
    list1[i] = ch1
print(list1)
'''






# nums = [1,1,1,1,1,1,1,1,1,1]
# target = 1
# start = 0
# min1 = float('inf')
# for i in range(len(nums)):
#     if nums[i] == target:
#         min2 = abs(i - start)
#         min1 = min(min2,min1)
# print(min1)




'''str1 = "1900-01-01"
list1 = str1.split("-")
str2 = ""
for item in range(len(list1)):
    bin1 = str(bin(int(list1[item])))[2:]
    if item < 2:
        str2 = str2 + bin1 + "-"
    else:
        str2 += bin1
print(str2)
'''


'''import math
nums = [1,1,1]
queries = [[0,2,1,4]]
chunk = math.ceil(len(nums) ** (1/2))
hash1 = {}
m = (10 ** 9 + 7)
for item in queries:
    l = item[0]
    r = item[1]
    k = item[2]
    v = item[3]
    if chunk <= k:
        i = l
        while i <= r:
            nums[i] = (nums[i] * v) % m
            i = i + k
    else:
        if k not in hash1:
            hash1[k] = [item]
        else:
            hash1[k].append(item)
for key, value in hash1.items():
    diff = [1] * len(nums)
    for j in range(len(value)):
        l = value[j][0]
        r = value[j][1]
        v = value[j][3]
        diff[l] = (diff[l] * v) % m
        steps = (r - l) // key
        next = (l + (steps + 1) * key)
        inv_v = pow(v, m - 2, m)
        if next < len(nums):
            # if diff[next] > 1:
            diff[next] = (diff[next] * inv_v) % m
        print(diff)
    for i in range(len(diff)):
        if (i - key) >= 0:
            diff[i] = (diff[i] * diff[i-key]) % m
    for i in range(len(nums)):
        nums[i] = (nums[i] * diff[i]) % m
result = 0
for item in nums:
    result = result ^ item
print(result)'''





'''s = "abcd"
k = 2
str1 = ""
for i in range(k):
    str1 = s[i] + str1
for i in range(k,len(s)):
    str1 = str1 + s[i]
print(str1)'''





'''s = "bbbb"
max1 = 1
flag = False
diff_ch = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if flag == False:
            diff_ch += 2
            flag = True
        else:
            diff_ch += 1
        a = diff_ch % 3
        if diff_ch == a:
            max1 += 1
print(max1)'''













'''s = "1112"
list1 = []
for item in s:
    list1.append(item)
for i in range(len(list1)):
    a = list1[-1]
    if int(a) % 2 == 0:
        pass
    else:
        list1.pop()
print(list1)'''








# print(2%6)


'''commands = [6,-1,-1,6]
obstacles = [[0,0]]
hash1 = {}
pair = [0,0]
max1 = 0
problem = False
problem_direction = "Y"
for item in obstacles:
    tuple1 = tuple(item)
    hash1[tuple1] = 1
directions = "+Y"
for item in commands:
    if  item == -1 or item == -2:
        if directions == "+Y":
            if item == -1:
                directions = "+X"
            elif item == -2:
                directions = "-X"
        elif directions == "+X":
            if item == -1:
                directions = "-Y"
            elif item == -2:
                directions = "+Y"
        elif directions == "-X":
            if item == -1:
                directions = "+Y"
            elif item == -2:
                directions = "-Y"
        elif directions == "-Y":
            if item == -1:
                directions = "-X"
            elif item == -2:
                directions = "+X"
        if problem == True and problem_direction == directions:
            pass
        else:
            problem = False
    else:
        for j in range(item):
            if  problem == False:
                if directions == "+Y" or directions == "-Y":
                    if directions == "+Y":
                        pair[1] += 1
                        if tuple(pair) in hash1:
                            problem = True
                            problem_direction = directions
                            pair[1] -= 1
                    else:
                        pair[1] -= 1
                        if tuple(pair) in hash1:
                            problem = True
                            problem_direction = directions
                            pair[1] += 1
                    cal = (pair[0] * pair[0]) + (pair[1] * pair[1])
                    max1 = max(max1, cal)
                elif directions == "+X" or directions == "-X":
                    if directions == "+X":
                        pair[0] += 1
                        if tuple(pair) in hash1:
                            problem = True
                            problem_direction = directions
                            pair[0] -= 1
                    else:
                        pair[0]-= 1
                        if tuple(pair) in hash1:
                            problem = True
                            problem_direction = directions
                            pair[0] += 1
                    cal = (pair[0] * pair[0]) + (pair[1] * pair[1])
                    max1 = max(max1, cal)
print(max1)'''












'''s = "au 123"
set1 = {"a","e","i","o","u"}
count_v = 0
count_c = 0
for item in s:
    if "a" <= item <= "z":
        if item in set1:
            count_v += 1
        else:
            count_c += 1
if count_c > 0:
    print(count_v // count_c)
print(0)'''




'''moves = "UD"
side1 = 0
side2 = 0
for item in moves:
    if item == "U":
        side1 += 1
    elif item == "D":
        side1 -= 1
    elif item == "R":
        side2 += 1
    elif item == "L":
        side2 -= 1
print(side1,side2)'''




'''encodedText = "ch   ie   pr"
rows = 3
cells_count = len(encodedText)
coloumn = cells_count // rows
matrix = []
k = 0
for i in range(rows):
    list1 = []
    for j in range(coloumn):
        list1.append(encodedText[k])
        k = k + 1
    matrix.append(list1)
print(matrix)
print(coloumn,rows)
main_ans = ""
start = 0
flag = False
for i in range(coloumn):
    m = 0
    n = i
    for j in range(start,rows):
        text = matrix[m][n]
        main_ans += text
        m = m + 1
        n = n + 1
        if m == rows and n == coloumn:
            flag = True
        elif n == coloumn:
            break
    if flag == True:
        start += 1
    print(main_ans)
list1 = []
for i in range(len(main_ans)):
    list1.append(main_ans[i])
for j in range(len(list1)-1,-1,-1):
    if list1[j] != " ":
        break
    else:
        list1.pop()
print(list1)'''









'''def check1(s):
    total_a = 0
    for item in s:
       if item == "a":
           total_a += 1
    limit = 0
    if total_a % 3 == 0:
        limit = total_a // 3
    else:
        return 0
    list1 = []
    for i in range(len(s)):
        if s[i] == "a":
            list1.append(i)
    count_a = 1
    total = 1
    print(list1)
    for i in range(len(list1)-1):
        if count_a == limit:
            total = total *  (list1[i+1] - list1[i])
            count_a = 1
        else:
            count_a += 1
    return total
s = "babaa"
print(check1(s))'''

# list1 = [limit]
# count_a = 0
# total = 0
# flag = False
# for i in range(len(s)):
#     if s[i] == "a":
#         count_a += 1
#     if list1[-1] == count_a and count_b > 0:
#         flag = True
#         total += 1
#     elif list1[-1] < count_a:
#         if flag == True:
#             list1.append(1)
#             count_a -= 1
#             flag = False
#         else:
#             list1[-1] += 1
#             count_a -= 1
#         if list1[-1] == count_a and count_b > 0:
#             total += 1
#     if s[i] == "b":
#         if list1[-1] == count_a:
#             total += 1
#         count_b -= 1
# return total

'''s = "z"
special = []
word = []
for item in s:
    if "a" <= item <= "z":
        word.append(item)
    else:
        special.append(item)
i = len(special) - 1
j = len(word) - 1
list1 = []
for k in range(len(s)):
    if "a" <= s[k] <= "z":
        list1.append(word[j])
        j = j - 1
    else:
        list1.append(special[i])
        i = i - 1
print(list1)'''





'''grid = [[0,10,-1],[1,-2,-3],[2,-3,-4]]
mat = [[(0,0) for i in range(len(grid[0]))]for j in range(len(grid))]
if grid[0][0] < 0:
    mat[0][0] = (0,1)
else:
    mat[0][0] = (grid[0][0], 0)
for i in range(1,len(grid[0])):
    if grid[0][i] >= 0:
        add = mat[0][i-1][0] + grid[0][i]
        mat[0][i] = (add,mat[0][i-1][1])
    else:
        if mat[0][i-1][1] >= 2:
            cal = mat[0][i-1][0] - abs(grid[0][i])
            mat[0][i] = (cal,mat[0][i-1][1]+1)
        else:
            mat[0][i] = (mat[0][i-1][0], mat[0][i-1][1]+1)
for i in range(1,len(grid)):
    if grid[i][0] >= 0:
        add = mat[i-1][0][0] + grid[i][0]
        mat[i][0] = (add,mat[i-1][0][1])
    else:
        if mat[i-1][0][1] >= 2:
            cal = mat[i-1][0][0] - abs(grid[i][0])
            mat[i][0] = (cal, mat[i - 1][0][1] + 1)
        else:
            mat[i][0] = (mat[i-1][0][0], mat[i-1][0][1] + 1)
for i in range(1,len(grid)):
    for j in range(1,len(grid[0])):
        if grid[i][j] < 0:
            #left
            minus_count_left = mat[i][j-1][1] + 1
            current_val_left = mat[i][j-1][0]
            # print(current_val_left,"vh")
            if minus_count_left > 2:
                current_val_left = current_val_left - abs(grid[i][j])
            #right
            minus_count_right = mat[i-1][j][1] + 1
            current_val_right = mat[i-1][j][0]
            if minus_count_right > 2:
                current_val_right = current_val_right - abs(grid[i][j])
                # print(current_val_right,minus_count_right)

            if current_val_left > current_val_right:
                mat[i][j] = (current_val_left,minus_count_left)
            elif current_val_left < current_val_right:
                mat[i][j] = (current_val_right,minus_count_right)
            else:
                # print(current_val_left,current_val_right)/
                if minus_count_left < minus_count_right:
                    mat[i][j] = (current_val_left,minus_count_left)
                else:
                    mat[i][j] = (current_val_right,minus_count_right)
        else:
            left_val = mat[i][j-1][0]
            left_val += grid[i][j]
            right_val = mat[i-1][j][0]
            right_val += grid[i][j]
            if left_val > right_val:
                mat[i][j] = (left_val,mat[i][j-1][1])
            elif left_val < right_val:
                mat[i][j] = (right_val,mat[i-1][j][1])
            else:
                if mat[i][j-1][1] < mat[i-1][j][1]:
                    mat[i][j] = (left_val, mat[i][j-1][1])
                else:
                    mat[i][j] = (right_val, mat[i-1][j][1])
print(mat)'''







'''positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"
ans = ["false1"] * len(positions)
tuple1 = []
for i in range(len(positions)):
    tuple1.append((positions[i],i))
tuple1.sort()
checking = []
for i in range(len(positions)):
    checking.append((positions[i],healths[i],directions[i]))
checking.sort(key=lambda x:x[0])
healths = []
directions = []
for item in checking:
    a = item[1]
    b = item[2]
    healths.append(a)
    directions.append(b)
directions_stack = []
positions_stack = []
for i in range(len(tuple1)):
    if directions[i] == "L":
        while directions_stack:
            if positions_stack[-1][0] < healths[i]:
                positions_stack.pop()
                directions_stack.pop()
                healths[i] = healths[i] - 1
            elif positions_stack[-1][0] > healths[i]:
                positions_stack[-1][0] = positions_stack[-1][0] - 1
                break
            elif positions_stack[-1][0] == healths[i]:
                positions_stack.pop()
                directions_stack.pop()
                break
        else:
            ans[tuple1[i][1]] = healths[i]
    elif directions[i] == "R":
        directions_stack.append("R")
        positions_stack.append([healths[i],tuple1[i][1]])
for item in positions_stack:
    a = item[1]
    if ans[a] == "false1":
        ans[a] = item[0]
list1 = []
for item in ans:
    if item != "false1":
        list1.append(item)
print(list1)'''






'''from collections import  deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

arr = [3,5,1,6,2,0,8,7,4]
def tree(root,val):
    list1 = deque([root])
    while list1:
        pop1 = list1.popleft()
        if pop1.left is not None:
            list1.append(pop1.left)
        elif pop1.left is None:
            pop1.left = Node(val)
            return root
        if pop1.right is not None:
            list1.append(pop1.right)
        elif pop1.right is None:
            pop1.right = Node(val)
            return root

root = Node(arr[0])

for i in range(1,len(arr)):
    root = tree(root,arr[i])
print(root.left.left.right.val)'''


# def tree(root,val):
#     if p
#
# root = Node(arr[0])
# for i in range(1, len(arr)):
#     root = tree(root, arr[i])
