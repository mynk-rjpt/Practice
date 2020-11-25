# def merge_the_tools(string, k):
#     n = len(string)
#     m = n/k
#     for i in range(0,len(string),k):
#         lst = string[i : i+k]
#         print(lst) 


# st = "aabbbccaa"
list1 = ['aab', 'bbc', 'caa']
# for i in list1 :
#     for j in i :
#         print(j) 

# a =  set(st)
# b = "".join(set(st.split(' ')))
# print(a)
# print(b)
def remove_duplicates(st) :

    a = ""
    for i in st :
        if(i in a):
            pass
        else :
            a = a + i
    print(a)  
remove_duplicates("aab")

for e in list1 :
    remove_duplicates(e)
