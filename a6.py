def secret(s):

     for i in range(0, len(s), 2):
        if s[i]>='A' and s[i]<='Z':
             return False

     for i in range(1, len(s), 2):
        if s[i]<'A' or s[i]>'Z':
             return False

     return True

s = ['u','b','c','d','e','f']
print(secret(s))