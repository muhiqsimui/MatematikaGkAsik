def panggil(n):
  for i in range(2,10):
    for j in range(2,n):
      if n%j==0:
        print(n,'=',j,'*',n/j)
        break
panggil(21)
