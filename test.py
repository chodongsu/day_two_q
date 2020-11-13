e=r=0
for b,a in sorted([*map(int,input().split()[::-1])]for _ in[0]*int(input())):
 if a>=e:r+=1;e=b
print(r)