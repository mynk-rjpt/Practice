from itertools import combinations
N = int(input())
list1 = input().split()
K = int(input())
# print(list1)

comb = combinations(list1,K)

count = 0
total = 0 

for i in list(comb) :
    total += 1
    bEqual = False 
    for e in i :
        if 'a' == e :
            bEqual = True
            break
    if bEqual :
            count = count + 1
    else :
            count = count + 0   

    # print(i)

# print(total)
# print(count)

prob = count/total
print(prob)





     