def pal(x,y):
    list = []

    flag =0

    for i in range(x,y):
        for j in range(2,i):
            if(i%j == 0):
                flag =1
                break
            else:
                flag =0

        if (flag == 0):
            list.append(i)
    return list



start = int(input("Enter the number as starting range: "))
end = int(input("Enter the number as ending range: "))

list = pal(start,end)
if len(list) == 0:
    print(f"there is no prime number between{start} & {end}")
else:
    print(f"The prime number between {start} & {end} are: ",list)
