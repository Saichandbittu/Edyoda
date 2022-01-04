inputstring = input("comma seperated integers : ").split(',')
lst = map(int,inputstring)
outputlist = list(map(lambda x: x**2, lst))
print(outputlist)
