def is_mozan_list(list):
    minos = 0
    plos = 0
    for i in list:
        if i > 0:
            plos += 1
        elif i < 0:
            minos += 1
        elif i == 0:
            print(" not good")
            return False


    if plos == minos:
        print(" ".join(map(str, list)))
    else:
        print("not good2 ")


list = [2,4,-4,-2,-1-4]
is_mozan_list(list)

