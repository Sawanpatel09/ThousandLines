'''list1 = [0, 1 ,2 ,3]
list2 = [4, 5, 6, 7, 8]
n = len(list1)
m = len(list2)
list3 = []
i =  0
j =  0
while i < n and j < m:
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i = i+1
    else:

        list3.append(list2[j])
        j = j+1
if i < n:
    for item in range(i,n):
        list3.append(list1[item])
if j < m:
    for item in range(j, m):
        list3.append(list2[item])

''''''else:
    for item in range(j,m):
        list3.append(list2[item])
''''''

print(list3)
'''





'''list1 = [1,3, 5, 8]
list2 = [2,4, 6 ,7]
list3 = list1 +list2
for i in range(len(list3)):
    for j in range(len(list3) - i - 1):
        if list3[j] > list3[j+1]:
            list3[j], list3[j+1] = list3[j+1], list3[j]
print(list3)
'''
'''def prefix(strs):
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_lenght = min(len(first),len(last))
    i = 0
    while i < min_lenght and first[i] == last[i]:
         i = i+1
    if i == 0:
      return "-1"
    else:
           return first[:i]

strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(prefix(strs))'''



'''string1 = "XYABBCDXYXABC"
#string1 = "ABCDABXYZP"
n = len(string1)
list1 = []
my_dict = {}
start = 0
start_i = 0
start_j= 0
for i in range(n):
    # my_dict = {}
    if string1[i] in my_dict:
        if (my_dict.get(string1[i]) >= start):
            start = my_dict.get(string1[i])+1

    my_dict[string1[i]] = i
    if(start_j- start_i < i-start+1):
        start_i = start
        start_j = i


#print(list1)

#maxList = max(list1, key = len)
#ans = "".join(maxList)
print(string1[start_i:start_j+1])
'''












'''string1 = "XYABBD"
n = len(string1)
list1 = []
res = 0
for i in range(n):
    list2 = [string1[i]]
    
    for j in range(i+1,n):
        #if string1[i] != string1[j]:
            if string1[j] not in list2:
                list2.append(string1[j])
            else:
                #list1.append(list2)
              break
    list1.append(list2)

string2 = str(list1)

result = ""
for i in list1:
    if len(i) > len(result):
        result = i
print(result)
'''










'''str1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = len(str1)
list1 = []
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(len(str1[i])):
            for l in range(len(str1[j])):
                if str1[i][k] == str1[j][l]:
                    list1.append(str1[i][k])

'''


'''def tocountstr(s):
    n = len(s)
    res = s[0]
    count = 0

    for i in range(n):
        cur_count = 1
        for j in range(i+1,n):
            if s[i] == s[j]:
                cur_count = cur_count + 1

        if cur_count > count:
            count = cur_count
            res = s[i]
    return res
str = "aaaabbaaccbbbdebbbb"
print(tocountstr(str))
'''



'''def parenthsis(p):
    n = len(p)
    flag = True
    count = 0
    for i in range(n):
        if p[i] == "(":
            count = count+1
        else:
            count = count-1


    if count < 0:
        return False
    if count != 0:
        return False
    else:
        return flag


exp1 = "((()))()()"
print(parenthsis(exp1))
'''









'''def toanagramtogether(words):
    index = []

    for i in range(len(words)):
        index.append(i)
    words2 = words.copy()
    words2.sort()
    print(words2)
    words3 = []
    for i in words2:
        a = sorted(i)
        b = "".join(a)
        words3.append(b)
    print(words3)


words = ["cat", "dog", "tac", "god", "act"]
toanagramtogether(words)'''

'''
P = "RTICE"
S = "zoomlazapzo"
n = len(P)
m = len(S)
#dict1 = { }
i = 0
j = 0

g_start = -1;
g_end = -1;
diff = 999999
k = 0
for k in range(0 , len(S)):
#while(k < len(S)):
    i = 0;
    j = k;
    start = -1
    end = -1
    while (j < m and i < n):
        if P[i] == S[j]:
            i = i + 1
            if (start == -1):
                start = j
            if (i == n):
                end = j
        j = j + 1
    if(  start != -1 and end != -1 and end- start < diff):
        g_start = start
        g_end =end
        diff = end-start
  #      k = start +1
#    else:
 #       k = k+1
if (g_start == -1 and g_end == -1):
    print(-1)
print(S[g_start:g_end + 1])

'''



















# for i in range(n):
#     list1 = []
#     for j in range(m):
#         if P[i] == S[j]:
#             list1.append(j)
#             dict1[P[i]] = list1
# print(dict1)




'''def tocountpali(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i = i+1
        j = j-1
    return True
def ispali(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if tocountpali(s, i, j):
                res = res+1
    return res

s = "abbaeae"
print(ispali(s))
'''






'''def tofindword(w1,w2):
    list1 = []
    for i in range(len(w1)):
        for j in range(len(w2)):
            if w1[i] == w2[j]:
                list1.append(w1[i])
                break
    list2 = list(w1)
    if list1 == list2:
        return True
    else:
        return False
word1 = "TOC"
word2 = "TOPRACTICE"
print(tofindword(word1,word2))
'''


'''def anagram(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    if str1.sort() == str2.sort():
        return "strings are anagram"
    else:
        return "the strings are not anagram"

str1 = "listen"
str2 = "silent"
print(anagram(str1,str2))
'''
'''def anagram(str1, str2):
    return sorted(str1) == sorted(str2)



str1 = "listen"
str2 = "silent"
print(anagram(str1,str2))

'''



'''P = "TOCE"
S = "TIMETOPRACTICE"
n = len(P)
m = len(S)
dict1 = { }

for i in range(n):
    list1 = []
    for j in range(m):
        if P[i] == S[j]:
            list1.append(j)
            dict1[P[i]] = list1
print(dict1)
'''




'''def tosubstring(string1):
    n = len(string1)
    string2 = ""
    for i in range(n):
            if string1[i] not in string2:
             string2 = string2 + string1[i]
    print(string2)

    return len(string2)
string1 = "ABCCADD"
print(tosubstring(string1))

'''



'''s = "aaaabbaaccdebbboobb"
n = len(s)
count = 0
for i in range(n):
    curr_count = 1
    for j in range(i+1,n):
        if s[i] == s[j]:
            curr_count+=1
        else:
            pass
    if curr_count > count:
        count = curr_count
        res = s[i]
print(res)
'''
'''def tocheckstring(string1):
    n = len(string1)
    count = 0
    for i in range(n):
        curr_count = 1
        for j in range(i+1,n):
            if string1[i] == string1[j]:
                curr_count+=1
            else:
                pass
        if curr_count > count:
            count = curr_count
            res = string1[i]
    return res

string1 = "aaaaaabbaaccdebbboobb"
print(tocheckstring(string1))
'''







'''def stringoccurence(string1):
    n = len(string1)
    count = 0
    res = string1[0]
    for i in range(n):
        curr_count = 1
        for j in range(i+1,n):
            if string1[i] != string1[j]:
               break
            curr_count = curr_count + 1
        if curr_count > count:
            count = curr_count
            res = string1[i]
    return res

string1 = "aaaabbaaccde"
print(stringoccurence(string1))
'''





'''def fibo(n):
    list = [1]
    if n <=2:
        if n == 2:
         list.append(1)
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(2,n):
            res = f1 + f2
            f1 = f2
            f2 = res
            list.append(res)

    return list

print(fibo(8))
'''


'''def stringoccurence(string1):
    n = len(string1)
    my_dict = {  }

    for i in range(n):
        for j in range(i+1,n):
            if string1[i] == string1[j]:



    return my_dict


string1 = "aaaabbcbbb"
print(stringoccurence(string1))'''





















'''def lenghtofstring(string1):
    n = len(string1)
    string2 = ""
    for i in range(n):
        for j in range(i,n):
            if string1[i] and string1[j] not in string2:
                string2 = string2 + string1[j]
    return len(string2)

string1 ="geeksforgeeks"
print(lenghtofstring(string1))
'''



'''def sumofzero(arr):
    n = len(arr)
    triplets = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    triplets.append([arr[i],arr[j],arr[k]])
    return "this are numbers whose sum is 0",triplets

arr = [0, -1, 2, -3, 1]
print(sumofzero(arr))'''






'''def sumofzero(arr):
    n = len(arr)
    triplets = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    triplets.append([arr[i],arr[j],arr[k]])
    return triplets



arr = [0, -1, 2, -3, 1]
print(sumofzero(arr))
'''






'''def findindex(arr,key):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[j] == key:
                return j
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
key = 0
print(findindex(arr,key))'''






'''def minele(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        for j in range(i,n):
            res = min(res, arr[j])
    return res

arr = [5, 6, 2, 3, 4]
print(minele(arr))
'''



'''def maxrprodarray(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        prod = 1
        for j in range(i,n):
            prod = prod*arr[j]
            res = max(res, prod)
    return res


arr = list(map(int,input("enter a number").split()))
print(maxrprodarray(arr))'''











'''def maxsubarray(arr):
    n = len(arr)
    list1 = []
    res = -float('inf')
    for i in range(n):
        list2 = []
        sum = 0
        for j in range(i,n):
            sum = sum + arr[j]
            list2.append(arr[j])
            if sum > res:
                res = sum
                list1 = list2[:]

    return res,list1

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsubarray(arr))
'''









'''def productarray(arr):
    n = len(arr)
    product = [1]*n

    for i in range(n):
        for j in range(n):
            if arr[i] != arr[j]:
                product[i] = product[i]*arr[j]

    return product



arr = [10, 3, 5, 6, 2]
print(productarray(arr))'''











'''def  duplicate(arr):
    n = len(arr)
    list = []
    my_dict = { }
    for i in arr:
        my_dict[i] = my_dict.get(i, 0) + 1
    print(my_dict)
    for key,value in my_dict.items():
        if value > 1:
            list.append(key)
    return "this are duplicate items in array",list

arr = [1, 2, 3, 6, 3, 6, 1]
print(duplicate(arr))
'''



'''def duplicate(arr):
    n = len(arr)
    list1 = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                list1.append(arr[i])
    return "this are numbers are duplicate",list1

arr = [1, 2, 3, 6, 3, 6, 1]
print(duplicate(arr))'''



'''def maxprofit(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        sum = 0
        for j in range(i+1,n):
            sum = arr[j]-arr[i]
            res = max(res, sum)

    return res


arr = [7, 10, 1, 3, 6, 11, 2]
print(maxprofit(arr))'''









'''def pairofsum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return "target is match",target,"of", arr[i],"and",arr[j]

    return "target does'nt match"



arr = [0, -1, 2, -10, 1]
taget = -2
print(pairofsum(arr,taget))
'''



'''def maxprodsubarray(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        mul = 1
        for j in range(i,n):
            mul *= arr[j]
            res = max(res,mul)

    return res


arr = [-2, 6, -3, -10, 0, 2]
print(maxprodsubarray(arr))
'''


'''def maxproduct(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        mul = 1
        for j in range(i,n):
            mul*=arr[j]
            res = max(res,mul)

    return res

print(maxproduct(arr))
arr = [-2, 6, -3, -10, 0, 2]
'''





'''def maxsumofsubarray(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            res = max(res,sum)
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxsumofsubarray(arr))
'''







'''def subarray(arr):
    res = arr[0]

    n = len(arr)
    for i in range(n):
        cursum = 0
        for j in range(i,n):
            cursum = cursum + arr[j]

            res = max(res,cursum)
    return res


arr = [2, 3, -8, 7, -1, 2, 3]
print(subarray(arr))'''






'''def productofarray(arr):
    n = len(arr)
    prod = [1]*n
    for i in range(n):
        for j in range(n):
            if i != j:
                prod[i] = prod[i]*arr[j]
    return prod


arr = [10, 3, 5, 6, 2]
print(productofarray(arr))
'''





'''def duplicate(arr):
    freq_map = { }
    result = []
    for num in arr:
        freq_map[num] = freq_map.get(num,0)+1
    print(freq_map)
    for key,value in freq_map.items():
        if value > 1:
            result.append(key)

    print("this are duplicate values",result)


arr = [1, 6, 5, 2, 3, 3, 2, 5]
duplicate(arr)'''






'''a = [1, 6, 5, 2, 3, 3, 2]
list1 = []
for i in range(len(a)):
    for  j in range(i+1,len(a)):
        if a[i] == a[j]:
            list1.append(a[i])


print("this are element are duplicate",list1)'''



'''a = [1, 6, 5, 2, 3, 3, 2]
i = 0
while i < len(a):
    print(a[i])
    i+=1
'''






'''def max_profit(arr):
    n = len(arr)
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            res = max(res, arr[j]-arr[i])
    return res

arr = [7, 10, 1, 3, 6, 9, 2]
print(max_profit(arr))
'''






'''def tosumofpair(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return True
    else:
        return False



arr = [1,0,-1,3,2,0,1]
target = 5
print(tosumofpair(arr,target))'''







'''import time
start = time.time()

i = 1
while i < 101:
  print(i)
  i = i+1

print(time.time()-start )'''