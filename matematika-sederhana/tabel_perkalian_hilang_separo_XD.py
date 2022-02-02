def test(n):

    L1 = list(range(1,n+1))

    for x in range(n):
        temp = []
        
        for y in range(n):
            score = L1[x]*L1[y]
            if (y<x):
                temp.append("x")
            else:
                temp.append(score)

        print(temp)

test(100)
