# membuat variabel
Nama = "Sekar Zaneta Amirulputri"
Asal = "SMA Islam Al-Azhar 4"
Status = "Mahasiswa"
Tempat = "Universitas Sebelas Maret"
ProgramStudi = "Teknik Industri"
TahunMasuk = 2020
TinggiBadan = 160
BeratBadan = 47.9
UkuranSepatu = 39
Alamat = "Taman Galaxy,Bekasi Selatan"

# Tanggal, Bulan dan Tahun Lahir
TanggalLahir = 9
BulanLahir = 9           # 9 = September
TahunLahir = 2002

# Tanggal, Bulan dan Tahun Sekarang
TanggalSekarang = 11
BulanSekarang = 3             # 3 = Maret
TahunSekarang = 2021

# menghitung jumlah bulan
JumlahBulanLahir = 12 * TahunLahir + BulanLahir + TanggalLahir / 30               # 12 = jumlah bulan tiap tahun
JumlahBulanSekarang = 12 * TahunSekarang + BulanSekarang + TanggalSekarang / 30   # 30 = jumlah tanggal tiap bulan

# menghitung usia dalam satuan bulan
UsiaDalamBulan = int(JumlahBulanSekarang - JumlahBulanLahir)


#tampilan
print("===== Biodata =====")
print("Nama lengkap   :", Nama)
print("Usia           :", UsiaDalamBulan, "bulan")
print("Asal SMA       :", Asal)
print("Pekerjaan      :", Status)
print("Universitas    :", Tempat)
print("Program Studi  :", ProgramStudi)
print("Tahun Masuk    :", TahunMasuk)
print("Tinggi badan   :", TinggiBadan, "cm")
print("Berat  badan   :", BeratBadan, "kg")
print("Tempat tinggal :", Alamat)
print("Ukuran sepatu  :", UkuranSepatu)
