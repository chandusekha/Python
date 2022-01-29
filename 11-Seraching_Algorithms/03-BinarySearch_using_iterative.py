
def binearySearch(arr,search):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid]>search:
            high=mid-1
        elif arr[mid]<search:
            low=mid+1
        else:
            return mid
    return -1



arr=[11,19,22,34,38,39,41,46,48,52,55,58,59,71,75,79]
print(arr)
search=int(input("enter the number to search in an array : "))
print(binearySearch(arr,search))