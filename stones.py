N = int(input())
lst = list(map(int,input().split()))
# print(lst)
sum1 = 0
i = 0
while i < len(lst):
    sum1 = sum1 + lst[i]
    i+=2
# print(sum1)     

sum2 = 0
j = 1
while j < len(lst):
    sum2 = sum2 + lst[j]
    j+=2
# print(sum2) 

if sum1 >= sum2 :
    print(2*sum2)
else :
    print(2*sum1)