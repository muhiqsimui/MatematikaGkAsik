



function hitungSegitiga() {
    var alas = document.getElementById("alas").value
    var tinggi = document.getElementById("tinggi").value
    luas = alas * tinggi * 0.5
    document.getElementById("luas").value = luas

}


function hitungPersegi() {
    var panjang = document.getElementById("panjang").value
    var lebar = document.getElementById("lebar").value
    luas = panjang * lebar
    document.getElementById("luas").value = luas

}

function kelilingPersegi() {
    var panjang = document.getElementById("panjang").value
    var lebar = document.getElementById("lebar").value
    keliling = 2 * (panjang * lebar)
    document.getElementById("keliling").value = keliling
}

function hk() {
    // fungsi untuk memanggil keliling dan luas persegi bersamaan
    hitungPersegi()
    kelilingPersegi()

}