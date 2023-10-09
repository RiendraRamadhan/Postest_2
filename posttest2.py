from prettytable import prettytable

# Definisikan role pembeli dan admin
class Pembeli:
    def __init__(self, username):
        self.username = username
        self.cart = []

class Admin:
    def __init__(self):
        self.barang = []

    def tambah_barang(self, barang):
        self.barang.append(barang)

    def tampilkan_barang(self):
        table = prettytable.PrettyTable()
        table.field_names = ["Nama", "Stok", "Harga"]
        for barang in self.barang:
            table.add_row([barang.nama, barang.stok, barang.harga])
        print(table)

    def ubah_barang(self, id, nama, stok, harga):
        for barang in self.barang:
            if barang.id == id:
                barang.nama = nama
                barang.stok = stok
                barang.harga = harga

    def hapus_barang(self, id):
        for barang in self.barang:
            if barang.id == id:
                self.barang.remove(barang)

class Barang:
    def __init__(self, id, nama, stok, harga):
        self.id = id
        self.nama = nama
        self.stok = stok
        self.harga = harga


# Buat objek admin
admin = Admin()
admin.barang.append(Barang(1, "Cat Tembok Putih", 100, 50000))
admin.barang.append(Barang(2, "Cat Tembok Biru", 50, 75000))
admin.barang.append(Barang(3, "Cat Tembok Merah", 25, 100000))
admin.barang.append(Barang(4, "Cat Tembok Hijau", 70, 80000))
admin.barang.append(Barang(5, "Cat Tembok Kuning", 30, 60000))

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Tampilkan menu
while True:
    print("1. Login Sebagai KOKO Riendra")
    print("2. Login Sebagai Pembeli")
    print("3. Keluar Toko")
    pilihan = input("Pilih menu peran: ")

    # Login admin
    if pilihan == "3":
        break
    if pilihan == "1":
        username = input("Username: ")
        password = input("Password: ")

        if username == "Riendra" and password == "riendra123":
            print("Login berhasil sebagai pemilik Toko!")
# Menu admin
            while True:
                print("1. Tampilkan barang")
                print("2. Tambah barang")
                print("3. Ubah barang")
                print("4. Hapus barang")
                print("5. Keluar")
                pilihan_admin = input("Pilih menu: ")

                # Tampilkan barang
                if pilihan_admin == "1":
                    admin.tampilkan_barang()

                # Tambah barang
                elif pilihan_admin == "2":
                    nama = input("Nama: ")
                    stok = input("Stok: ")
                    harga = input("Harga: ")

                    admin.tambah_barang(Barang(id=None, nama=nama, stok=stok, harga=harga))
                    print("Barang berhasil ditambahkan!")

                # Ubah barang
                elif pilihan_admin == "3":
                    id = input("ID barang: ")
                    nama = input("Nama: ")
                    stok = input("Stok: ")
                    harga = input("Harga: ")

                    admin.ubah_barang(id, nama, stok, harga)
                    print("Barang berhasil diubah!")
                
                # Hapus barang
                elif pilihan_admin == "4":
                    id = input("ID barang: ")
                    nama = input("Nama: ")
                    stok = input("Stok: ")
                    harga = input("Harga: ")

                    admin.hapus_barang(id, nama, stok, harga)
                    print("Barang berhasil dihapus")


                elif pilihan_admin == "5":
                    print("Terimakasih, Admin!")
                    break

    elif pilihan == "2":
        username = input("Username: ")
        password = input("Password: ")
        
        if username == "pembeli" and password == "pembelisetia":
            print("Selamat datang di Toko CAT Warna Koko Riendra")


            while True:
                print("\nPilih tindakan:")
                print("1. Transaksi")
                print("2. Keluar")
                pilihan_pembeli = input("Pilih menu: ")
                if pilihan_pembeli == "2":
                    print("Terima kasih, Pembeli!")
                    break
                if pilihan_pembeli == "1":
                    admin.tampilkan_barang()
                
                from prettytable import PrettyTable
                table = PrettyTable()
                table.field_names = ["Nama Barang", "Harga"]

# Input data dari pengguna
                while True:
                    nama = input("Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk mengakhiri): ")
                    if nama.lower() == 'selesai':
                        break
                    harga = float(input("Masukkan harga barang: "))

# Tambahkan data ke PrettyTable
                    table.add_row([nama, harga])

# Cetak PrettyTable
                    print("\nData Barang:")
                    print(table)

# Hitung total harga dari PrettyTable
                harga = sum(float(row[1]) for row in table._rows)
                print(f"Harga: {harga}")

# Tambahkan hasil perhitungan ke PrettyTable
                table.add_row(["Total Harga", harga])

# Cetak PrettyTable yang telah diperbarui
                print("\nData Barang (Diperbarui):")
                print(table)
