






'''class Greeting:
    def say_hello(self):
        print("hii hello")
def new_patching():
    print("hii patchers")
g = Greeting()
g.say_hello = new_patching
print(g.say_hello())'''






# def lcm(x,y):
#     for i in range(2,x*y):
#         if i % x == 0 and i % y == 0:
#             return i
#
#
# print(lcm(12,6))






'''def median(list1):
    list1.sort()
    print(list1)
    sum1 = ""
    if len(list1) % 2 == 0:
        sum1 = (list1[int(len(list1)/2)] +  list1[int((len(list1)/2)-1)])/2
    else:
        sum1 = list1[int(len(list1)/2)]
    return sum1
list1 = [1,2,5,14,6]
print(median(list1))'''



# def buble_sort(list1):
#     for i in range(len(list1)):
#         for j in range(len(list1)-i-1):
#             if list1[j] > list1[j+1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]
#     return list1
# list1 = [12,45,71,1,6,2,4]
# print(buble_sort(list1))




# def celcius_to_ferehenit(c):
#     return (c * (9/5)) + 32
# print(celcius_to_ferehenit(0))


# def circle(r):
#     return  (22/7) * (r ** 2)
# r = 5
# print(circle(r))



# def fibo(n):
#     list1 = []
#     if n == 0:
#         list1.append(0)
#     else:
#         list1.append(0)
#         list1.append(1)
#     p1 = 0
#     p2 = 1
#     res = p1 + p2
#     for i in range(n):
#         res = p1 + p2
#         p1 = p2
#         p2 = res
#         list1.append(res)
#
#     return list1
# print(fibo(5))



# def greatest_common(x,y):
#     for i in range(2,x):
#         if x % i == 0 and y % i == 0:
#             print(i)
#     else:
#         return f"their is {1} and self {x} and {y}"
# print(greatest_common(10,15))


#
#
#
# def genrato(n):
#     i = 0
#     value = 5
#     while i < value:
#         i = i + 1
#         yield (i)
# my_obj = genrato(5)
#
# for num in my_obj:
#     print(num)



'''dict1 = {"Science":[88,89,62,95], "Language":[77,78,84,80]}
list1 = []
len1 = len(dict1["Science"])
for key,value in dict1.items():
    hash1 = {}
    for j in range(len1):
        hash1 = {}
        hash1[key] = value[j]
        list1.append(hash1)
list2 = []
j = len(list1)//2
for i in range(len(list1)//2):
    list1[i].update(list1[j])
    j = j + 1
print(list1[:len(list1)//2])
'''













'''dict1 = {"Science":[88,89,62,95], "Language":[77,78,84,80]}
list1 = []
flag = True
i = 0
len1 = len(dict1["Science"])
while flag:
    hash1 = {}
    if i < len1:
        for item in dict1:
            hash1[item] = dict1[item][i]
        list1.append(hash1)
        i = i + 1
    else:
        flag = False

print(list1)'''



# -------------question 61------------

'''data = [{"item":"item1","amount":400},{"item":"item2","amount":300}, {"item":"item1","amount":750}]
hash2 = {}
for dict1 in data:
    hash1 = {}
    for key,value in dict1.items():
        if key == "item":
            hold = value
            hash1[value] = 0
        if key == "amount":
            hash1[hold] = value
    for key1, value1 in hash1.items():
        if key1 not in hash2:
            hash2[key1] = value1
        else:
            hash2[key1] = hash2[key1] + value1
print(hash2)'''






# set1 = {1,2,3,4,5}
# set2 = set()
# for i in set1:
#     if i < 3:
#         set2.add(i)
# print(set2)






'''s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
list1 = [0] * len(indices)
for i in range(len(s)):
    list1[indices[i]] = s[i]
str1 = ""
for item in list1:
    str1 += item
print(str1)'''








'''data = {"1":["a","b"],"2":["c","d"]}
x = ""
y = ""
for key,value in data.items():
    if x == "":
        x = value
    elif y == "":
        y = value
for item in x:
    str1 = ""
    for item1 in y:
        str1 = item
        str1 = str1 + item1
        print(str1)'''






'''list1 = [{"v":23},{"h":90},{"j":23}]
list2 = []
for item in list1:
    for item1 in item.items():
        list2.append(item1[1])
print(set(list2))'''



'''d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict1 = {}
set1 = set()
for key, value in d2.items():
    if key in d1:
        set1.add(key)
        val = d1[key]
        val = val + d2[key]
        dict1[key] = val
    else:
        dict1[key] = value
for key,value in d1.items():
    if key not in set1:
        dict1[key] = value
print(dict1)
'''



'''dict1 = {1: 1, "a": 4, 3: 9, 4: 16, 5: 25}
list1 = ()
for item in dict1.items():
    list1 = list1 + item
print(list1)'''




'''n = 5
dict1 = {}
for i in range(1,n+1):
    dict1[i] = i * i
print(dict1)'''


'''dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)'''



'''a = ['a','b','c']
b = [1,2,3]
dict1 = {}
for key, value in zip(a,b):
    dict1[key] = value
print(dict1)'''

'''dict1 = {'a':100, 'b':200}
for key,value in dict1.items():
    chan = (value * 10)/100
    chan = chan + value
    dict1[key] = chan
print(dict1)'''




'''list1 = [{'a':1,'b':2},{'b':3,'c':4}]
set1 = set()
list2 = []
for item in list1:
    for key, value in item.items():
        if key not in set1:
            list2.append(key)
            set1.add(key)
print(list2)
'''









'''dict1 = {"a":1,"b":2}
dict2 = {"a":1,"b":2}
print(dict1 == dict2)'''




'''dict1 = {"a":10,"b":20}
dict1.setdefault("b",0)
print(dict1.get("b"))
print(dict1)
'''



'''dict1 = {}
print(dict1 == {})
print(dict1 is {})'''

'''a = {'a':1, 'b':2}
a.clear()
print(a)'''


'''d = {'a':1, 'b':2, 'c':1,"d":8}
dict1 = {}
set1 = set()
for a, b in d.items():
    if b not in set1:
        dict1[a] = b
        set1.add(b)
print(dict1)'''






'''a = {"a":1,"b":2}
dict1 = {}
for key ,value in a.items():
    dict1[value] = key
print(dict1)'''




'''dict1 = {"a":1,"b":2,"c":1,"d":3}
dict2 = {}
for key, value in dict1.items():
    if value not in dict2:
        dict2[value] = [key]
    else:
        dict2[value].append(key)

print(dict2)'''




'''dict1 = {"a":5,"b":10}
if "c" in dict1:
    print(dict1["c"])
else:
    print(0)'''


'''a = {"a":10,"b":5,"c":20,"e":0,"r":-1}
min1 = ""
min_key1 = ""
for key, value in a.items():
    if min1 == "" and min_key1 == "":
        min1 = value
        min_key1 = key
    else:
        if value < min1:
            min1 = value
            min_key1 = key
print(min_key1)
print(min1)'''


'''a = {'a':1, 'b':2}
list1 = []
for item in a.items():
    list1.append(item)
print(list1)
'''


'''tup1 =  [('a',1), ('b',2)]
dict1 = {}
for item in tup1:
    dict1[item[0]] = item[1]
print(dict1)'''




'''dict1 = {'emp1':{"name":"john","age":30}}
for key, value in dict1.items():
    value.pop("age")
print(dict1)
'''

'''dict1 = {'a':1, 'b':{'x':2,'y':3}}
count = len(dict1)
for key, value in dict1.items():
    if type(value) == dict:
        count += len(value)
print(count)'''










'''dict1 = {'emp1':{"name":"john","age":30}}
dict2 = {}
for key, value in dict1.items():
    dict2[key] = {}
    for key1, value1 in value.items():
        if key1 == "age":
            pass
        else:
            dict2[key][key1] = value1
print(dict1)
print(dict2)'''







'''dict1 = {'emp1':{"name":"john","age":30}}
for key,value in dict1.items():
    for key1, value1 in value.items():
        if key1 == "name":
            print(value1)'''






'''mydict1 = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = sorted(mydict1.items(),key= lambda items:items[1])
print(dict(sorted_dict))
'''






'''dict1 = {'a':3, 'b':1, 'c':2,"d":0,"y":2}
list1 = []
for key,value in dict1.items():
    d = [key,value]
    c = tuple(d)
    list1.append(c)
for i in range(len(dict1)):
    for j in range(len(dict1) - i - 1):
        if list1[j][1] > list1[j+1][1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
hash1 = {}
for item in list1:
    hash1[item[0]] = item[1]
    # hash1.update({item[0]:item[1]})
print(hash1)'''





# -------------------doctionary









'''arr1 = [[1,2,3],[2,3,4],[2,4,5]]
list1 = arr1[0]
for i in range(len(list1)):
    count = 0
    for j in range(len(arr1)):
        for k in range(len(arr1)):
           if list1[i] == arr1[j][k]:
               count = count + 1
    print(count,list1[i])'''




'''arr1 = [1,3,5]
arr2 = [9,10,11,9000,77734]
list1 = []
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        list1.append(arr1[i])
        i = i + 1
    elif arr1[i] > arr2[j]:
        list1.append(arr2[j])
        j = j + 1
    else:
        list1.append(arr1[i])
        list1.append(arr2[j])
        i = i + 1
        j = j + 1
if i < len(arr1):
    for k in range(i,len(arr1)):
        list1.append(arr1[i])
elif j < len(arr2):
    for l in range(j,len(arr2)):
        list1.append(arr2[l])
print(list1)'''




'''list1 = []
for i in range(10,51):
    if i % 7 == 0:
        list1.append(i)
print(list1)'''






'''arr = [2,3,4]
list1 = []
for i in range(len(arr)):
    tup1 = [arr[i],arr[i] * arr[i]]
    tup1 = tuple(tup1)
    list1.append(tup1)
print(list1)
'''







'''arr = [2,3]
for i in range(len(arr)):
    arr[i] = arr[i] ** arr[i]
print(arr)
'''


'''arr = [5,3,1,2,1,4]
min1 = arr[0]
for i in arr:
    if min1 > i:
        min1 = i
list1 = []
flag = False
for j in arr:
    if j == min1 and flag == False:
        flag = True
    else:
        list1.append(j)
print(list1)'''








'''list1 = [1,3,2,2,3,2,1]
list2 = {}
for i in range(len(list1)):
    if list1[i] not in list2:
        list2[list1[i]] = 1
    else:
        list2[list1[i]] = list2[list1[i]] + 1
for j in range(len(list1)):
    if list2[list1[j]] > 1:
        list2[list1[j]] = -1
    elif list2[list1[j]] == -1:
        list1[j] = -1



print(list1)'''






'''list1 = [1,2,2,3,2,1]
list2 = [0] * len(list1)
for i in range(len(list1)):
    if list2[i] != -1:
        list2[i] = list1[i]
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j] and list2[i] != -1:
            list2[j] = -1
print(list2)'''











'''list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = []
for i in range(len(list1)):
    list2.append(list1[i][i])
print(list2)'''






'''list1 = [5,100,2,8,1,90]
for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(list1)
'''




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





'''list1 = ['h','e','l','l','o']
str1 = "aeiou"
list2 = []
for item in list1:
    if item not in str1:
        list2.append(item)
print(list2)'''






'''list1 = ['a','b','e','i','o']
str1 = "aeiou"
count = 0
for item in list1:
    if item in str1:
        count = count + 1
print(count)'''


'''arr = [2, 3, 4, 5, 6]
prod = 1
for i in range(0,len(arr),2):
    prod = prod * arr[i]
print(prod)'''








'''list1 = [10,20,30,40,50]
max1 = list1[0]
min1 = list1[0]
total = 0
for item in list1:
    if item > max1:
        max1 = item
    elif min1 > item:
        min1 = item
    total = total + item
total = total - max1
total = total - min1
aveg = total/ (len(list1)-2)
print(aveg)
'''



'''str1 = "123456"
list1 = []
for item in str1:
    list1.append(int(item))
print(list1)'''



'''list1 = ["hello","world"]
d = []
for item in list1:
    f = item.upper()
    d.append(f)
print(d)'''




'''list1 = [2,3,4,5,6]
list2 = []
for item in list1:
    if item % 2  == 0:
        list2.append(item)
print(list2)'''



'''list1 = [5,8,12,20,25,30]
list2 = []
for i in range(4):
    list2.append(list1[i])
print(list2)'''



'''list1 = [10, 20, 5, 40]
max1 = list1[0]
min1 = list1[0]
for item in list1:
    if item > max1:
        max1 = item
    elif item < min1:
        min1 = item
print(max1 - min1)'''



'''list1 = [2, 3, 4]
mul = 1
for item in list1:
    mul = mul * item
print(mul)'''




'''Input = [10, 13, 15, 18, 20]
sum1 = 0
for item in Input:
    if item % 2 == 0:
        sum1 += item
print(sum1)'''