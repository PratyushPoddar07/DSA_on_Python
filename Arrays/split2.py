from collections import deque

def split(a,n,k):
    q = deque(a)

    q.rotate(-k)
    return list(q)

arr = [12,10,5,6,52,36]
n= len(arr)

k = int(input("Enter position: "))

arr = split(arr,n,k)

for i in range(0,n):
    print(arr[i], end = ' ')