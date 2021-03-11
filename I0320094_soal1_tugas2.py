### Menghitung Luas Persegi Panjang

# informasi program
print("===== Menghitung Luas Persegi Panjang =====")

# input panjang dan lebar
Panjang = float(input("Masukkan panjang: "))
Lebar = float(input("Masukkan lebar: "))

# proses hitung luas
LuasPersegiPanjang = Panjang * Lebar

# menampilkan hasil
print("Luas persegi panjang =", LuasPersegiPanjang, "\n")

### Menghitung Luas Lingkaran

# informasi program
print("===== Menghitung Luas Lingkaran =====")

# input jari-jari
r = float(input("Masukkan jari-jari: "))

# proses hitung luas

LuasLingkaran = 3.14 * (r ** 2)

# menampilkan hasil
print("Luas Lingkaran =", LuasLingkaran, "\n")

### Menghitung Luas Kubus

# informasi program
print("===== Menghitung Luas Kubus =====")

# input rusuk
s = float(input("Masukkan panjang rusuk: "))

# proses hitung luas
LuasKubus = 6 * (s ** 2)

# menampilkan hasil
print("Luas kubus =", LuasKubus, "\n")

### Menghitung konversi suhu celcius ke fahrenheit

# informasi program
print("===== Konversi suhu celcius ke fahrenheit =====")

# input celcius
celcius = float(input("Masukkan suhu celcius: "))

# proses hitung celcius ke fahrenheit
fahrenheit = (celcius * (9/5))+ 32

# menampilkan hasil
print(celcius, "celcius =", fahrenheit, "fahrenheit", "\n")

### Menghitung konversi suhu reamur ke kelvin

# informasi program
print("===== Konversi suhu reamur ke kelvin =====")

# input reamur
reamur = float(input("Masukkan suhu reamur: "))

# proses hitung celcius ke fahrenheit
kelvin = (reamur * (5/4)) + 273.15

# menampilkan hasil
print(reamur, "reamur =", kelvin, "kelvin")
