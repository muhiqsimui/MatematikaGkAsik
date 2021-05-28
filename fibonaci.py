#fibonaci 

# OLD CODE NOT GOOD TO SLOW
def fibonaci(n):
    a,b = 0,1
    while a<n:
        print(a, end=' ')
        a,b=b,a+b
    print()
    
fibonaci(100)

# THIS IS BETTER VERY FAST LIKE USAIN BOLTZ I RECOMENDED TO YOU TRUST ME XD USE TO YOUR PROJECT
def fibonacci(num):
  if (num <= 1):
    return num
  return fibonacci(num - 2) + fibonacci(num - 1);

fibonacci(100)
