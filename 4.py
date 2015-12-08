class Point:
    def __init__(self,strk='0,0'):
        self.x=float(strk[:strk.index(',')])
        self.y=float(strk[strk.index(',')+1:])
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return Point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return Point(str(self.x-other.x)+','+str(self.y-other.y))
    def russt(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def Perimetr(self,other,onemore):
        return self.russt(other)+self.russt(onemore)+other.russt(onemore)
N=int(input())
A=[]
maxx=None
B=[Point()]*3
for i in range(N):
    A.append(Point(input()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if maxx==None or maxx<A[i].Perimetr(A[j],A[k]):
                B[0],B[1],B[2]=A[i],A[j],A[k]
                maxx=A[i].Perimetr(A[j],A[k])
                
print(*B)
