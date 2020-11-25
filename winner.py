N = int(input())
for i in range(N) :
    ni = int(input())
    strng = input()
    abc = list(strng)
    lst1 = list(map(int, abc))
 
  
# Traverse through all array elements 
arr = [16, 25, 34, 22]
n = len(arr)
times = 0
for i in range(n-1): 
    # times += 1
# range(n) also work but outer loop will repeat one time more than needed. 
  
    # Last i elements are already in place 
    for j in range(0, n-i-1): 
        times+=1
        # times = times + 1
  
        # traverse the array from 0 to n-i-1 
        # Swap if the element found is greater 
        # than the next element 
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
                # times += 1
    
# print(times)    
  
print ("Sorted array is:") 
for i in range(n) :
    print ("%d" %arr[i])

print(times)    

# print(tim.24es)    