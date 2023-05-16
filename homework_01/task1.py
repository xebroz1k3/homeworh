string = 'hello hi q jjhsag gashk'
def counter(str):
    s = {}
    for i in str:
        if i in s.keys():
            s[i]+=1
        else:
            s[i] = 1
    return s
print(counter(string))
