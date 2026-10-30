# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Herfi Maulidya  
**NIM:** 2225250129  
**Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan
Mempelajari cara membaca, menulis, dan mengolah file menggunakan Python serta menangani error dasar.

## Format File Input
Data disimpan dalam file `data/nilai.txt` dengan format:

`NIM,nilai`

Contoh:
- A001,85
- A002,78

## Cara Menjalankan
Jalankan perintah berikut melalui terminal VS Code:

`py tugas/rekap_nilai_file.py`

## Error yang Ditangani
1. **FileNotFoundError:** Menangani kondisi ketika file input tidak ditemukan.
2. **ValueError:** Menangani data nilai yang bukan berupa angka.

## Hasil Pengujian
1. Data normal: berhasil membaca dan merekap 5 data valid.
2. Data tidak valid: baris A004,abc dilewati.
3. File tidak ditemukan: program menampilkan pesan error.
4. Nilai batas 60: dihitung sebagai lulus.
5. Nilai di bawah 60: tidak dihitung sebagai lulus.

## Refleksi
Melalui praktikum ini, saya mempelajari penggunaan file I/O untuk membaca dan menulis data, penggunaan fungsi untuk mengelola program, serta penanganan error menggunakan FileNotFoundError dan ValueError agar program dapat berjalan dengan lebih baik.