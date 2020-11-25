strng = input()
# abc = list(map(int,strng.split()))
abc = list(strng)
print(abc)
lst1 = list(map(int, abc))
print(lst1)
# lst1 = list(map(int, str(res[0])))
# print(output)
lst1.sort(reverse = True)
print(lst1)

strings = [str(integer) for integer in lst1] 
string1 = "".join(strings)
integerss = int(string1)
print(integerss)

print(integerss)
def B_to_D(binaryy): 
      
    decimal, i, n = 0, 0, 0
    while(binaryy != 0): 
        dec = binaryy % 10
        decimal = decimal + dec * 2**i 
        binaryy = binaryy//10
        i += 1
    print(decimal)

B_to_D(integerss)    

# print(sum)    

maxp = 6
while(True):
    if integerss % (2**maxp) == 0 :
        break    
    maxp -= 1
    
print(maxp)
# print()
# print(ints)
# def maximumPower(s):


    # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = maximumPower(s)

#     fptr.write(str(result) + '\n')    

#     fptr.close()