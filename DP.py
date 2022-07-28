# part one is memorization 
# part 2 is tabulation 

# fibonnaci problem with memorization 

#O(2^n)
from asyncio.windows_events import NULL
from multiprocessing import Array


def fib(n, memo={}):
    if (n in memo):
        return memo[n]
    if n==1 or n==2:

        return 1

    else:
        memo[n]=fib(n-1, memo)+fib(n-2,memo)
        return memo[n]
print(fib(50))

# another fun
#O(2^n)
def dib(n):
    if (n<=1):
        return
    dib(n-1)
    dib(n-2)
print(dib(3))


# total no. of ways to move in a grid

# terminating cond. if any one n or m ==0 return 0
# if n or m =1 return 1
# if n=1 and m=1 return 
# from start we have two option down or right 
# as we move down the starting row decreases 
# as we move right the starting column decreases
# if we reach the end column we are left only with down option
# when it hits the base condition then only there is a way 

startrow=0
startcol=0
def gridTraveler (n,m, startrow=0, startcol=0):
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    if startrow==n-1 or startcol==m-1:
        return 1
    else:
        down=  gridTraveler(n,m, startrow+1, startcol)
        right= gridTraveler(n,m, startrow, startcol+1 )
        return down +right
print(gridTraveler(2,3))

# here we dont need to keep the row and column as constant 
# so 

def gridTraveler (n,m):
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    else:
        down=  gridTraveler(n-1,m)
        right= gridTraveler(n,m-1)
        return down +right
print(gridTraveler(2,3))


# as the tree formed having m, n or n,m is same therefore 

# def gridTraveler (n,m, memo={}):
#     key= str(m)+','+ str(n)
#     if key in memo:
#         return memo[key]
#     if n==0 or m==0:
#         return 0
#     if n==1 and m==1:
#         return 1
    
#     memo[key]= gridTraveler(n-1,m, memo)+gridTraveler(n,m-1, memo)
#     return memo[key]
# print(gridTraveler(18,18))


def gridTraveler (n,m, memo={}):
    key= str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if n==0 or m==0:
        return 0
    if n==1 and m==1:     # here we can also use n==1 or m==1 
        return 1
    memo[key]=gridTraveler(n-1,m, memo) +gridTraveler(n,m-1)
    return memo[key]
print(gridTraveler(18,18))

# find if the given number can be formed by summing the subset of the array

def cansum(arr, x, sum=0, point=0):
    if x in arr:
        return True
    # base condition 
    if sum==x:
        return True 
    if point==len(arr):
        return False 
    option1= cansum(arr, x, sum=sum+arr[point], point=point+1)
    option2= cansum(arr, x, sum, point=point+1)
    return option1 or option2 
    # or slicing or deleting first index 
array=[1,6,3,4,8,4,5,8,9]
num= 10

print(cansum(array,num))

# another approach 
# take target num and subract it by each number 
# until it cant be substracted by any elememt 


# it is code if it can be gernated by repeated elements 

def canSum(targetsum, numbers):
    #base case 
    if targetsum==0:
        return True
    if targetsum<0:
        return False
    for num in numbers:
      # we can use if targetsum>num)
        rem= targetsum - num
        if canSum(rem, numbers)== True:
            return True 
    return False

print(canSum(7,[2,4]))


# optimized solution 

def numnum(target, array, memo={}):
    
    #base condition
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for i in array:
        rem= target-i
        if numnum(rem, array, memo)==True:
            memo[rem]=True
            return True
    memo[target]=False
    return False

print(numnum(300,[7,14]))
        
#howsum takes targetsum and array and return the combination of elements to find the sum

# def numnum(target, array, memo={}):
    
#     #base condition
#     if target in memo:
#         return memo[target]
#     if target==0:
#         return []
#     if target<0:
#         return NULL
#     for i in array:
#         rem= target-i
#         remresult=numnum(rem, array, memo)
#         if remresult!= NULL:
#             remresult=remresult.append(i)


#             lst.append[i]
#             memo[rem]=True

#             return True
#     memo[target]=False
#     return False

# bruteforce
def howsum(targetnum, array):
    if targetnum ==0:
        return []
    if targetnum <0:
        return NULL 
    for i in array:
        rem= targetnum-i 
        result= howsum(rem,array)
        if result !=NULL: # not null is choosen becasue in upper level it is like [4] is returned from lower level 
            result.append(i)
            return result 
    return NULL
print(howsum(8,[2,3,5])) 
 

def howsum(targetnum, array, memo={}):
    if targetnum in memo:
        return memo[targetnum]
    if targetnum ==0:
        return []
    if targetnum <0:
        return NULL 
    for i in array:
        rem= targetnum-i 
        result= howsum(rem,array, memo)
        if result !=NULL: # not null is choosen becasue in upper level it is like [4] is returned from lower level 
            result.append(i)
            memo[targetnum]=result
            return result 
    memo[targetnum]=NULL
    return NULL
print(howsum(8,[2,3,5])) 

#write a function best sum that takes target number and array as arguments and returns the shortest combinations of numbers 
#that add up exactly yo targetsum 


# bruteforce O(n*m +m)
# space complxity=O(m*2)
def bestsum(targetnum, array):
    #base condition
    if targetnum==0:
        return []
    if targetnum <0:
        return NULL
    lst=NULL
    for i in array:
        rem= targetnum- i
        result= bestsum(rem, array)
        if result!= NULL:
            result.append(i)
            if lst==NULL or len(result)<len(lst):
                lst=result
    return lst

print(bestsum(8,[1,4,5]))


# with memorization 
def bestsum(targetnum, array, memo={}):
    #base condition
    if targetnum==0:
        return []
    if targetnum <0:
        return NULL
    lst=NULL
    for i in array:
        rem= targetnum- i
        result= bestsum(rem, array, memo)
        if result!= NULL:
            result.append(i)
            if lst==NULL or len(result)<len(lst):
                lst=result
    memo[targetnum]= lst
    return lst

print(bestsum(8,[1,4,5]))


# realizing time complexity 
#if we have 50 as targetsum then we can store maximum of 50 values in memo
# and for each value of memp the value of num of keys could be m
# therefore space complexity is O(m^2)
# time complexity= O(m^2)*(n) # extra m from copying the array


# cancontruct thatr accepts a target string and an array of strings and return the boolean indicating whether or not the target can be
# contructed by concateaniting elements of the wordbank
# can do it in two ways 
# using pointer 
# or subtracting from string 

# def canconstruct(target, wordbank):
#     # base condition 
#     if len(target)==0:
#         return True
#     for word in wordbank:
#         if (target.index(word)==0):
#             suffix=target[len(word):]
#             if canconstruct(suffix, wordbank):
#                 return True
#     return False

# print(canconstruct("abcdef",["ab","abc","cd","def","abcd"]))


#of single word :

def cando(target, wordbank):
    if target=="":
        return True
    if target[0] in wordbank:
        if cando(target[1:], wordbank):
            return True
    return False

print(cando("abcd",['a','g','h','b','r','c','d']))




#original cansum 
# if we dont use try except we will get error when we compare target string(abcd) with abd in wordlist 
# it will be valueerror " substing cant be formed"

def indexof(target,word):
    try:
        return target.index(word)
    except ValueError: # here we dont mention the error name it will count all errors thats also okay 
        return -1


# def canconstruct(target, wordbank, memo={}):

#     if target=="": # base condition 
#         return True
#     if target in memo:
#         return memo[target]
#     for word in wordbank:
#         if indexof(target, word)==0:
#             prefix= target[len(word):]
#             if canconstruct(prefix, wordbank, memo):
#                 memo[target]=True
#                 return True 
#     memo[target]= False 
#     return False
# print(canconstruct("abcdef",["ab","abc","cd","df","abcd"]))

# # write a function count construct to count the total no of ways the target can be made 

# def indexof(target, word):
#     try:
#         return target.index(word)
#     except:
#         return -1
# def countconstruct(target, wordlist, memo={}):

#     if target=="":
#         return 1
#     if target in memo:
#         return target[memo]
#     totalcount=0
#     for word in wordlist:
#         if indexof(target, word)==0:
#             result=countconstruct(target[len(word):], wordlist, memo)
#             if result:
#                 totalcount+=result
#                 return True
#     memo[target]=False 
#     return False 
            
# def countconstruct(target, wordlist):
#     #base case
    
#     if target=="":
#         return 1
#     totalcount=0
#     for word in wordlist:
#         if indexof(target, word)==0:
#             result= countconstruct(target, wordlist)
#             totalcount+=result
#     return totalcount


# return the 2D array for all the possibilities of construct possible

def insertinto(result, word):
    for i  in range(len(result)):
        result[i].append(word)
    return result
def allconstruct(target, wordlist):
    if target=="":
        return [[]]
    res=[]
    for word in wordlist:
        if indexof(target,word)==0:
            suffix= target[len(word):]
            result= allconstruct(suffix, wordlist)
            insertinto(result,word)
            res=res+ result
    return res

print(allconstruct('purple',['purp','p','ur','le','purpl']))



# TABULATION METHODS....
 
#fibonacci problem 
# adding i to i+1 and i+2 in n+1 array 
def fib(n):
    lst=[0]*(n+2)
    lst[1]=1
    for i in range(2,n+1):
        lst[i]=lst[i-1]+lst[i-2]

    return lst[n]
print(fib(50))

# while the memo method was 

def fiboo(n,memo={}):
    # base condition 
    if n in memo:
        return memo[n]
    if n==1:
        return 1
    if n==0:
        return 0
    result= fiboo(n-1,memo)+fiboo(n-2,memo)
    memo[n]=result
    return result
print(fiboo(50))




# Grid traveler using tabulation 
# m rows n columns 
def gridtraveller(m, n):
    lst=[[0]*(n+1)]*(m+1)
    # lst=[[0 for i in range((n+1)) ]in range(m+1)]
    lst[1][1]=1
    for j in range(1,m+1):
        for i in range(1,n+1):
            lst[j-1][i]+=lst[j-1][i-1]
            lst[j][i-1]=lst[j-1][i-1]
    return lst[m][n]
print(gridtraveller(18,18))


# grid traveler using memoization 

def gridt(m,n,memo={}):
    key= str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    # a grid can be transversed either right or down 
    # so if we go right the col decreases and if we go down then the row.
    result= gridt(m-1,n,memo)+ gridt(m, n-1,memo)
    memo[key]=result
    return result
print(gridt(18,18))



# Tabulation recipe 

#vizualize your problem as a table 
#size of table based on inputs 

#initialize the table with default values 

# seed the trival answer into the table 
# iterate through the table 
# fill further positions based on current positions 


#cansumm problem # whether it can gernate targetsum or not 

##memo method 

def cans(target, array):
    # base cond
    if target==0:
        return True
    if target<0:
        return False
    i= False
    for num in array:
        rem=target-num
        result=cans(rem, array)
        i=i or result
    return i
print(cans(7,[7,4,3,5]))

# Tabulation of cansum 

# take a 1D array of size targetsum+1 
# seed will be 0 i.e. if we have targetsum=0 then we can definitely construct it 
# add the elements from zero which can be constructed 


# target=7
# array=[3,5,6]
# newarr=[0]*(target+1)
# print(newarr)

# newarr[0]=1
# print(newarr)
# i=0

# while i<len(newarr):
#     if newarr[i]==1:
#         print(i)
#         for num in array:
#             print(num)
#             if i+num<len(newarr):
#                 newarr[i+num]=1
#                 print(newarr)
#             else:
#                 break
#     i+=1

# howsum using tabulation 

#take n+1 list of null elements 
# take 0th element as empty list 
# on iteration theough array and arr pass on the list and add the num 

def howwsum(target, array):
    table=[NULL]*(target+1)
    table[0]=[]

    for i in range(len(table)):
        if table[i]!=NULL:
            print(i)
            for nums in array:
                if nums+i<len(table):
                    table[i+nums]=table[i]+[nums]
    return table[target]
print(howwsum(7,[5,3,7,5]))


# bestsum using memo 

def besttsum(target, array):
    if target==0:
        return [[]]
    if target <0:
        return NULL
    lst=NULL
    for i in array:
        rem= target-i
        result= besttsum(rem, array)
        if result != NULL:
            res=result + [[i]]
            if lst==NULL or len(result)<len(lst): # for 1st iteration lst will be null therefore it will always be true 
                lst=result
            return result
            
    return NULL
        
# print(besttsum(7,[5,3,4,5]))

# def howsum(targetnum, array):
#     if targetnum ==0:
#         return []
#     if targetnum <0:
#         return NULL 
#     for i in array:
#         rem= targetnum-i 
#         result= howsum(rem,array)
#         if result !=NULL: # not null is choosen becasue in upper level it is like [4] is returned from lower level 
#             result.append(i)
#             return result 
#     return NULL
# print(howsum(8,[2,3,5])) 
 
# bestsum using tabulation 

def bestiesum(target, array):
    table=[NULL]*(target+1)
    if target==0:
        return []
    for i in range(len(table)):
        if target[i] !=NULL:
            for nums in array:
                table[i+nums]=table[i]+ [nums]
    return table[target]


print(bestiesum(7,[5,3,7,5]))

