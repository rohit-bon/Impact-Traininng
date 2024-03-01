#heap sort with min heap
def heapify(arr,n,i):
    smallest=i #largest as root
    l=2*i+1
    r=2*i+2
    if l<n and arr[l] < arr[smallest]:
        smallest=l

    if r<n and arr[r] < arr[smallest]:
        smallest= r
    #change if need
    if smallest != i:
        (arr[i],arr[smallest])=(arr[smallest],arr[i])
        heapify(arr,n,smallest)

def heapSort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr, n, i)

    for i in range(n-1,-1,-1):
        (arr[i],arr[0])=(arr[0],arr[i])
        print(i,arr)
        heapify(arr,i,0)

arr =[12,11,13,5,6,7]
heapSort(arr)
n=len(arr)
print("sorted array: ")
for i in range(n):
    print(arr[i])