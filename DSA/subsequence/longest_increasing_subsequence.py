def _lis(arr, n):
    # To allow access of global variable 
    global maximum

    # Base case 
    if n == 1:
        return 1
    
    maxEndingHere = 1

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1
    
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

def lis(arr):
    # to allow the access of global variable 
    global maximum

    # Length of arr 
    n = len(arr)

    # maximum varialble holds the result 
    maximum = 1

    # the funnction _lis stores its result in maximum
    _lis(arr, n)
    return maximum

# Driver program to test the above function 
if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(arr)

    # function call 
    print("Lenght of lis is", lis(arr))
    