def func():
    n = int(input("Limit : "))
    ans = int(n*(n+1)/2)
    print("The consecutive sum: ", end = "")
    for i in range(1,n+1):
        if(i != n):
            print(f"{i} + ", end = "")
        else:
            print(f"{i} = {ans}")

func()
