t = int(input())
fibo = {}
a = 1;
b = 1;
r = 2
s = 5002
i = 2
while(len(str(b)) < s):
    c = a+b;
    a = b;
    b = c;
    i += 1
    while(len(str(b)) >= r):
        fibo[r] = i
        r += 1
        
for T in range(t):
    n = int(input())   
    print(fibo[n])
