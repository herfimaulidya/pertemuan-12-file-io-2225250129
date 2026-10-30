teks_nilai = "abc"

try:
    nilai = float(teks_nilai)
    print("Nilai:", nilai)

except ValueError:
    print("Error: Nilai harus berupa angka.")