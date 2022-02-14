index= 0
def fn(x):
    global index
    return x[index]
def splitfn(x):
    return x.split(',')
lines=[]
fname = input('ENTER FILE NAME: ')
with open(fname) as c:
    lines = c.readlines()
headers = lines[0]
lines = lines[1:]
data = []
for line in lines:
    data.append(line.split(','))

index = int(input("enter index no: "))
rev = input("enter 1 to reverse else 0: ")

revcond = False
if rev == '1':
    revcond = True
data.sort(key=fn, reverse = revcond)

for l in data:
    print(l)
with open(fname, 'w') as f:
    f.write(headers)
    for i in data:
        f.write(",".join(i))
