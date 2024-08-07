def what(a):
    length = len(a)
    for i in range(2,length-1,2):
        print(i)
        print(a[i],"<", a[i - 2])
        if a[i]<a[i-2]:

            print("False1")
            return False
        i+=1
        print(a[i],">", a[i - 2])
        if a[i]>a[i-2]:

            print("False2")
            return False

    print("True")
    return True


what([1, 25, 3, 8, 10, 4, 20, 5])
