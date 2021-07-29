
from statistics import mean
# cara mencari rata rata dari list bertipe string
list=[['1','2','3','4'],['2','2','3','4'],['1','2','7','4'],['8','2','3','4']]

for x in list:
  x = [int(i) for i in x] # ubah list string ke integer
  print(mean(x))
