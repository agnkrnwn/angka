# Buka file untuk dibaca
with open('syd.txt', 'r') as file:
    # Baca semua baris dalam file
    lines = file.readlines()

# Inisialisasi list untuk menyimpan nomor
nomor_list = []

# Loop melalui setiap baris dalam file (mulai dari baris kedua)
for line in lines[1:]:
    # Pecah baris menjadi bagian-bagian: tanggal, hari, nomor
    parts = line.split('\t')
    
    # Jika bagian-bagian cukup panjang dan memiliki lebih dari 2 elemen
    if len(parts) >= 3:
        nomor = parts[2].strip()  # Ambil nomor dan hapus spasi di awal/akhir
        nomor_list.append(nomor)  # Tambahkan nomor ke dalam list

# Simpan hasil ekstraksi nomor ke dalam file
with open('nomor_result.txt', 'w') as output_file:
    for nomor in nomor_list:
        output_file.write(nomor + '\n')

print("Hasil ekstraksi nomor telah disimpan dalam file 'nomor_result.txt'")
