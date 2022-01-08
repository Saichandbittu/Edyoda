class PowerClass():
    def power(self,x,n):
        return x**n
x = int(input("x value : "))
n = int(input("n value : "))

power = PowerClass()
print(power.power(x,n))
