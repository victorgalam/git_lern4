def is_valid(s):
    while True:
        if len(s) % 2 == 0:
            return False
        if s[0] != s[-1]:
            return False
        return True


def make_str():
    valid = 0
    not_valid = 0

    for i in range(5) :
       num = input("enter a str: ")
       if is_valid(num) == True:
           valid += 1
           print("valid")
       else:
           not_valid += 1
           print("not_valid")
       i += 1

    print(f"valid :{valid}, not_valid :{not_valid}")

make_str()