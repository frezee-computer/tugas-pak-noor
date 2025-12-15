# Input dari pengguna
karakter = input("Masukkan karakter: ")
tinggi = int(input("Masukkan tinggi piramida: "))

# Membuat piramida
for i in range(1, tinggi + 1):
    # Spasi di sebelah kiri
    print(" " * (tinggi - i), end="")
    # Karakter piramida
    print(karakter * (2 * i - 1))
