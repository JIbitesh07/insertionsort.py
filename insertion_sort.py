
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]       
        j=i-1 
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1 
        arr[j+1]=key    

def printing(arr):
    for i in arr:
        print(i)
arr=[64,32,25,22,12]
insertion_sort(arr)
printing(arr)
