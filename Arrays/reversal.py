
def reversal(arr,d):
    c =(arr[d:])+(arr[:d])
    return c

arr =[1,2,3,4,5,6,10]
d =2
print(reversal(arr,d))