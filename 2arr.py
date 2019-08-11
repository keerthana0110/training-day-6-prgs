def isSubset(arr1, arr2, m, n): 
    i = 0; 
  
    quickSort(arr1, 0, m-1); 
    for i in range(n): 
        if (binarySearch(arr1, 0, m - 1,arr2[i]) == -1): 
            return 0;  
    return 1; 
def binarySearch(arr, low, high, x): 
    if(high >= low): 
        mid = (low + high)//2; 
        if(( mid == 0 or x > arr[mid-1]) and (arr[mid] == x)): 
            return mid; 
        elif(x > arr[mid]): 
            return binarySearch(arr, (mid + 1), high, x); 
        else: 
            return binarySearch(arr, low, (mid -1), x); 
  
    return -1; 
  
