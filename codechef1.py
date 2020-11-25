a, b = map(int, input().split())
print(a,b)
# for inp in range(b):

lst = []
for i in range(1, a+1):
    lst.append(i)

print(lst)   

if b in lst :
    lst[0], lst[-1] = lst[-1], lst[0]

else :
    lst[-1] = b

print(lst)

sum_lst = 0

for item in lst :
    sum_lst = sum_lst + item

print(sum_lst)    







    