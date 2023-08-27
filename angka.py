from bs4 import BeautifulSoup

# Baca file HTML
with open('angka.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Buat objek BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Temukan tabel "Keluaran SGP" berdasarkan header
table = soup.find('table')
keluaran_sgp_index = None

# Temukan indeks kolom "KELUARAN SGP"
headers = table.find_all('th')
for index, header in enumerate(headers):
    if 'KELUARAN SGP' in header.get_text():
        keluaran_sgp_index = index
        break

# Ekstrak angka dari kolom "KELUARAN SGP" dan simpan dalam format .txt
with open('hasil_ekstraksi_sgp.txt', 'w', encoding='utf-8') as output_file:
    rows = table.find_all('tr')
    for row in rows[1:]:  # Melewati baris judul
        columns = row.find_all('td')
        keluaran_sgp = columns[keluaran_sgp_index].get_text().strip()
        output_file.write(f"{keluaran_sgp}\n")

print("Ekstraksi selesai. Data KELUARAN SGP disimpan dalam hasil_ekstraksi_sgp.txt")
