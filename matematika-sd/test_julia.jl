

function persegi(panjang,lebar)
    luas=panjang*lebar
    println("luas persegi : ",luas)
end

function segitiga(alas,tinggi)
    luas=(alas*tinggi)/2
    println("luas segitiga : ",luas)
end

function trapesium(a,b,t)
    luas = 1/2 * (a + b) * t
    println("luas trapesium : ",luas)
end

function lingkaran(r)
    pi=22/7
    luas=pi*(r*r)
    println("Luas lingkaran : ",luas)
end

persegi(2,4)
segitiga(4,4)
trapesium(4,5,4)
lingkaran(17)
