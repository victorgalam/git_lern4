def count_num():
    list = []
    while True:
        num = int(input("enter a num : "))
        if num >= 100:
            break
        list.append(num)

    return  print(max(list) , min(list))


count_num()