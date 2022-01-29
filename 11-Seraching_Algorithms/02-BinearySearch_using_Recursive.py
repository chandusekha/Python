# This binary Search is by using Recursive method....

def binearySearch(arr,searching_element,low,high):
    if low==high:
        if arr[low]==searching_element:
            return low
        else:
            return -1
    else:
        mid=low+(high-low)//2
        if arr[mid]==searching_element:
            return mid
        elif arr[mid]>searching_element:
            return binearySearch(arr,searching_element,low,mid-1)
        else:
            return binearySearch(arr, searching_element, low+1,high)




arr=[1,22,28,36,42,49,55,57,59,61,65,68,79,82,88,99]
print(arr)
low = 0
high=len(arr)-1
searching_element=int(input("Enter the element to search : "))
result=binearySearch(arr,searching_element,low,high)
print(result)