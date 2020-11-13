money = []

for i in range(int(input())):
    num = int(input())
    if num == 0 : money.pop()
    else: money.append(num) 
    
print(sum(money))