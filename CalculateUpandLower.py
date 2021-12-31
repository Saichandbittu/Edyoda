def fun(string):
    lowerChar = 0
    upperChar = 0
    for ch in string:
        if(ch.isupper()):
            upperChar+=1
        if(ch.islower()):
            lowerChar+=1
    return lowerChar,upperChar

string = input("string : ")
lower,upper = fun(string)
print("No. of Upper case characters :",upper)
print("No. of Lower case Characters :",lower)
