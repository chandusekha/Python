
def linearSearch(array,seraching_element,n):
    for x in range(n):
        if array[x]==searching_element:
            return x
    return -1

array=[12,55,44,77,15,95,85,42,26,78,67]
print(array)
searching_element=int(input("enter the number to serach in element : "))
length=len(array)
result=linearSearch(array,searching_element,length)
print(result)