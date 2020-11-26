from itertools import combinations
N = int(input())
list1 = input().split()
K = int(input())
print(list1)

comb = combinations(list1,K)

for i in list(comb) :  
    print(i)


for e in list(comb) :
    print(e)
     