class Point:
    def __init__(self, s='0,0'):
        coord=list(map(float, s.split()))
        self.x=coord[0]
        self.y=coord[1]
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __mul__(self,other):
        return Point(self.x * other.x, self.y + other.y)
N=int(input())
xm=0
ym=0
rmax=0
cmx=0
cmy=0
for i in range(0,N):
    for k in range(i+1,N):
        for j in range(i+2,N):
            P=((A[i]-A[j])**2 + (A[j]-A[k])**2 + (A[k]-A[i])**2 + 
    s=input()
    a=Point(s)
    rm=((a.x)**2 + (a.y)**2)**0.5 
    cmx=cmx + a.x
    cmy=cmy + a.y
    if 
    if rm>rmax:
        rmax=rm
        xm=a.x
        ym=a.y       
print(xm,ym,cmx/N,cmy/N)
