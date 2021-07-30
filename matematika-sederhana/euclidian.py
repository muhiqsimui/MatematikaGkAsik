import math
uji=[6.3,2.3,4.4,1.3]
iv=[[5,2,3.5,1],[5.5,2.4,3.7,1],[5.2,4.4,1.7,1.3]]

jarak=[]
for i in iv:
  for j in range(len(i)):
    jarak.append(math.sqrt((uji[j]-i[j])**2))

print(jarak)
