# heapsort

# func heapify :: heapify a node
# arr :: heap
# n :: size of heap
# i :: node
def heapify(arr,n,i):
    larggest = i
    l = 2*i+1
    r = 2*i+2

    # judge i.left
    if l<n and arr[larggest]<arr[l]:
        #arr[larggest],arr[l]=arr[l],arr[larggest]
        larggest = l
    
    # judge i.right
    if r<n and arr[larggest]<arr[r]:
        #arr[larggest],arr[r]=arr[r],arr[larggest]
        larggest = r
    
    if larggest!=i:
        arr[larggest],arr[i]=arr[i],arr[larggest]
        heapify(arr,n,larggest)

def heapmax(arr):
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,len(arr),i)

    for tail in range(len(arr)-1,0,-1):
        arr[0],arr[tail]=arr[tail],arr[0]
        heapify(arr,tail,0)


if __name__ == "__main__":
    # TEST CASE
    arr = [ 12, 11, 13, 5, 6, 7] 
    heapmax(arr)
    print (arr) 