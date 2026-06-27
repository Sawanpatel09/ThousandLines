'''numbers = [2,3,4,5,2,3,4]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            print(numbers[i] , "is duplicate")
            break
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(numbers[i])'''