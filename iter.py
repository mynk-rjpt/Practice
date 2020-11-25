from itertools import combinations
N = int(input())
list1 = input().split()
K = int(input())
print(list1)

comb = combinations(list1,K)
total = 0
for i in comb :
    total = total + 1
    print(i)

print(total)    
count = 5
for e in comb :
    count = count + 1
    print(e)
    # for n in range(len(e)) :
        # add = add + 1
        # if e[n] == 'a':
        #     pass
        # else :
        #     pass

print(count)        