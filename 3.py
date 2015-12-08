class Point:
    def __init__(self,strk='0,0',mas=1):
        self.x=float(strk[:strk.index(',')])
        self.y=float(strk[strk.index(',')+1:])
        self.mas=mas
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return Point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return Point(str(self.x-other.x)+','+str(self.y-other.y))
    def russt(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def c_mas(self,other):
        x=self.x+(other.x-self.x)/(self.mas+other.mas)
        y=self.y+(other.y-self.y)/(self.mas+other.mas)
        return Point(str(x)+','+str(y),self.mas+other.mas)
N=int(input())
A=Point(input())
for i in range(N-1):
    B=Point(input())
    if B.mas<A.mas:
        B,A=A,B
    A=B.c_mas(A)
print(A)
