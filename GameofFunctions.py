def fun(l):
    s = 0
    for v in l:
        s += v
    return s
        
string = input("enter comma seperated integers : ").split(',') 
lists = list(map(int, string))
print(fun(lists))
