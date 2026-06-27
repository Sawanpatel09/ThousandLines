






'''n = 30
list1 = []
for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list1.append(i)
print(list1)'''

'''list1 = [4,5,8,2,9]
list2 = [3,9,2,1,6]
set1 = set(list1)
set2 = set(list2)
set3 = set1.difference(set2)
set4 = set2.difference(set1)
set5 = set3.union(set4)
list3 = list(set5)
print(list3)'''


'''list1 = [10,20,40,10,30]
l = []
list1.sort()
print(list1[-2])'''






'''for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            l.append(list1[i])
'''







'''dictionary = {
    "name" : 1,
    "age" : 8,
    "class" : 3
}

list1 = list(dictionary.keys())
list1.sort(reverse=True)
#sorted_dict = {i : dictionary[i] for i in list1}
sorted_dict = { }
for  i in list1:
    sorted_dict.update({i : dictionary[i]})

print(sorted_dict)
'''



'''string1 = "namr"
list1 = list(string1)
list1.sort()
string2 = ""
for  i in list1:
    string2 = string2+i
print(string2)

string1 = "enma"
list1 = list(string1)
list1.sort()
string3 = ""
for  i in list1:
    string3 = string3+i
print(string3)

if string2 == string3:
    print("the number is anagram")
else:
    print("the numbber is not anagram")'''

'''string2 = str(list1)
print(string2)
print(string1)'''



'''def reversestring(string1):
    rever_string1 = ""
    for item in string1:
        rever_string1 = item + rever_string1
    print(rever_string1)


reversestring("hello")'''


'''def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n*factorial(n-1)

print(factorial(5))'''




'''def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
    
    
        return fibo(n - 1) + fibo(n - 2)
print(fibo(4))'''





'''def sumofdigiit(n):

    if n == 0:
       return 0
    if n == 1:
        return 1
    else:
        return n+sumofdigiit(n-1)

print(sumofdigiit(5))
'''









'''def power(m, n):
    if m == 0:
        return 0
    if n == 1:
        return m
    if m == 1:
        return 1
    if n == 0:
        return 1
    return m * power(m,n-1)


print(power(2,4))'''








'''def factorial(n):

    if n == 1:
        return 1
    if  n == 0:
        return 0
    else:
        return n * factorial(n-1)

print(factorial(5))
'''


'''def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return n*factorial(n-1)

(factorial(5))'''





