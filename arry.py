# n = int(input("enter n"))
# arr = map(int, input().split())
# arr = input("enter numbers").split()
arr = [1,-1,-2,-1]
abc = list(arr)
# great = max(abc)

abcd = set(abc)

# while(True):
#     if abc[i] == max(abc):
#         abc.remove(abc[i])
#         continue
#     i+=1     

    
abcd.remove(max(abcd))
                   
print(max(abcd))