inputstring = input("comma seperated integers : ").split(',')
lst = map(int,inputstring)
outputlist = list(map(lambda x : 3*x, lst))
print(outputlist)
