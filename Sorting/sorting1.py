import sys
def bubbleSorting (l):
    if type(l) != list:
        l = list(l)
    temp = 0
    needSort = True
    while needSort == True:
        needSort = False
        for i in range (len(l)-1):
            if l[i]>l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                needSort = True
    return l

# print(bubbleSorting([2,4,1,3,8,5,9,-85,4,1,3,-5,7,1,2,-4,9,2,-3,8,4,6]))

def sorting(l):
    i = 0    
    while i < len(l):
        mini = sys.maxsize
        miniInd = 0
        for j in range(i, len(l)):
            if l[j] < mini:
                mini = l[j]
                miniInd = j
                
        temp = l[i]
        l[i] = l[miniInd]
        l[miniInd] = temp
        i += 1
    return l

# print(sorting([2,4,1,3,8,5,9,-85,4,1,3,-5,7,1,2,-4,9,2,-3,8,4,6]))
# print(bubbleSorting("fadgfdg sdfdgadgsdg"),end=" ")   

def alphaSort(s):
    
    l = s.lower().split(" ")
    l.sort()  
    for i in l:
        print (i)     

# alphaSort(" method returns the lowercase string from the given string. It converts all uppercase characters to lowercase. If no uppercase characters exist, it returns the original string.")
            
def sortByVowels(s):
    l = s.lower().split(" ")
    def vowelCount(st):
        count = 0
        li = ["a", "e", "i", "o", "u"]
        for i in st:
            if i in li:
                count +=1
        return count
    ln = sorted(l, key=vowelCount,reverse=True)
    
    return ln

print(sortByVowels("method returns the lowercase string from the given string. It converts all uppercase characters to lowercase. If no uppercase characters exist, it returns the original string."))


