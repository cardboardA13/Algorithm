n=int(input())
l=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    l[i]=[a,b]
l.sort(key=lambda x:(x[1], x[0]))
e=0
a=0
for start,end in l:
    if start>=e:
        a+=1
        e=end
print(a)
