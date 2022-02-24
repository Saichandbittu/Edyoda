#question no 1

l = [4,5,6,31,4,6,78,5,0,4,2,2,35,6,54,29,6,8,4]
sumvalue = 35
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i] + l[j] == sumvalue:
            print('({0},{1})'.format(l[i],l[j]))

#question 2
data = [1,2,3,4,5,6,7,8,9,10]
n = len(data)
for i in range(n//2):
    var = data[i]
    data[i] = data[n-1-i]
    data[n-1-i] = var
print(data)


#question 3
stringa = "qwerty"
stringb = 'ytrewq'
print(stringa[::-1] == stringb)


#question 4
from collections import Counter as c
string = 'abcdefghabcfgh'
d = c(string)

for i in string:
    if d[i] == 1:
        print(i)
        break


#question 5
def fun(n , s, d, a):
    if n==1:
        print ("Move disk 1 from source",s,"to destination",d)
        return
    hanoi(n-1, s, a, d)
    print ("Move disk",n,"from source",s,"to destination",d)
    hanoi(n-1, a, d, s)

fun(4,'a','b','c')

#question 6
def converttoprefix(expression):
    stack = []
    for i in range(len(expression)):
        if expression[i] not in '+-*/':
            stack.append(expression[i])
        else:  
            val1 = stack.pop()
            val2 = stack.pop()
            exp = expression[i] + val2 + val1
            stack.append(exp)
    return stack.pop()
print(converttoprefix('AB*C-'))

#question 7
def converttoinfix(expression):
    stack = []
    i = len(expression) - 1
    while i >= 0:
        if expression[i] not in "*+-/^":
            stack.append(expression[i])
            i -= 1
        else:
            stack.append("{}{}{}".format(stack.pop(), expression[i], stack.pop()))
            i -= 1
    return stack.pop()


print(converttoinfix("-*ABC"))


#question 8
from collections import Counter
exp = '[{a*(b+c)}*{a+b}]'
stack = []
for i in exp:
    if i in '(){}[]':
        if i in '({[':
            stack.append(i)
        else:
            try:
                popv = stack.pop()
                if popv == '(' and i == ')':
                    pass
                elif popv == '[' and i == ']':
                    pass
                elif popv == '{' and i == '}':
                    pass
                else:
                    print('invalid expression')
            except:
                print('invalid expression')
if stack != []:
    print('invalid expression')
else:
    print('valid expression')

#question 9
stack = [1,2,3,4,5,6]
def Reverse(stack):
    if stack == []:
        return stack
    else:
        popval = stack.pop()
        Reverse(stack)
        stack.insert(0,popval)
Reverse(stack)
print(stack)

#question 10

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
        
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
    

    def MinValue(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element = {0}" .format(self.minimum))


    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node


    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print(self.minimum)
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print (removedNode)


s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.MinValue()

