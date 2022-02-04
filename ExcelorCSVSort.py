filename = input("enter filename along with extension")
fieldlst = []
data = []
fieldid =  0
revcheck = False

def sortfield(data):
    global fieldid
    return data[fieldid]
try:
    with open(filename,'r') as fpt:
        lines = fpt.readlines()
        for line in lines:
            if fieldlst == []:
                fieldlst = (line.split(','))
            else:
                data.append(line.split(','))
        
    print("select sort field")
    for i,name in enumerate(fieldlst):
        print(" {0}) {1}".format(i+1,name))
    fieldid = int(input("enter no: ")) - 1
    if input("enter 1 to reverse sort or acending order, else enter 0: ") == '1':
        revcheck = True
    data.sort(key = sortfield, reverse=revcheck)

    with open(filename,'w') as fpt:
        line = ",".join(fieldlst)
        fpt.write(line)
        for line in data:
            fpt.write(",".join(line))
except Exception as ex:
    print(ex.args)
