strng = input()
abc = list(strng)
lst1 = list(map(int, abc))

if all(ele == 1 for ele in lst1) :
    print(0)

elif all(ele == 0 for ele in lst1) :
    print(-1)    

else :    
        for i in range(len(lst1)) :
            if lst1[i] == 1 :
                break

        n = len(lst1) - 1 - i

        lst1 = (lst1[-n:] + lst1[:-n]) 
            

        count = 0 
        result = 0 
            
        for inn in range(len(lst1)): 

            if (lst1[inn] == 1): 
                count = 0
        
            else:  
                count+= 1 
                result = max(result, count)

        for a in range(0, len(lst1)) :
            if lst1[a] == 1 :
                count = 0
            else :
                count += 1
                if count == result :
                    indexx = a    

        d = len(lst1) - indexx - 1   

        lst1 = (lst1[-d:] + lst1[:-d]) 

        u = len(lst1) - 1
        while u < len(lst1) :
            if lst1[u] == 1 :
                break
            u-=1

        maxp = len(lst1) - 1 - u
        print(maxp)




