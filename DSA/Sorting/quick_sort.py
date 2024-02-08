def partition(i,j,l):
    pi = i
    pivot = l[i]
    while i<j:
        while l[i]<=pivot and i<len(l):
            i+=1
        while l[j]>pivot:
            j-=1
        if i<j:
            l[i], l[j] = l[j], l[i]
            print(l)
            
    l[j], l[pi] = l[pi], l[j]
    print(l)
    return j

def quick_sort(i,j,l):
    if i<j:
        p = partition(i,j,l)
        quick_sort(i, p-1, l)
        quick_sort(p+1, j, l)
        
l=[30,20,10,50,60,40]
print("Before Sortinng: ",l)
quick_sort(0,len(l)-1,l)
print("After Sorting: ",l)