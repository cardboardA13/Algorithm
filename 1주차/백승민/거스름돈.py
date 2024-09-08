n=int(input())
c2=0
c5=0

c5+=n//5
n-=5*(n//5)
c2+=n//2
n-=2*(n//2)

if n==0:
    print(c5+c2)
elif n==1 and c5!=0:
    c5-=1
    c2+=3
    print(c5+c2)
else:
    print(-1)
