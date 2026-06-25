import csv
import os

FILE_CSV = "inventori.csv"

def buat_file_csv():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama Barang", "Stok", "Harga"])
        print("Database CSV berhasil dibuat!")

def tambah_data():
    print("\n=== TAMBAH DATA ===")

    id_barang = input("ID Barang : ")
    nama = input("Nama Barang : ")
    stok = input("Stok        : ")
    harga = input("Harga       : ")

    with open(FILE_CSV, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([id_barang, nama, stok, harga])

    print("Data berhasil ditambahkan!")

def tampilkan_data():
    print("\n=== DATA INVENTORI ===")

    with open(FILE_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i == 0:
                print("-" * 60)
                print(
                    f"{row[0]:<10}{row[1]:<20}{row[2]:<10}{row[3]:<10}"
                )
                print("-" * 60)
            else:
                print(
                    f"{row[0]:<10}{row[1]:<20}{row[2]:<10}{row[3]:<10}"
                )

def cari_data():
    keyword = input("\nMasukkan ID Barang yang dicari: ")

    ditemukan = False

    with open(FILE_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == keyword:
                print("\nData ditemukan!")
                print("ID    :", row["ID"])
                print("Nama  :", row["Nama Barang"])
                print("Stok  :", row["Stok"])
                print("Harga :", row["Harga"])
                ditemukan = True
                break

    if not ditemukan:
        print("Data tidak ditemukan!")

def update_data():
    id_cari = input("\nMasukkan ID yang ingin diubah: ")

    data_baru = []
    ditemukan = False

    with open(FILE_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == id_cari:
                ditemukan = True

                print("\nData ditemukan!")

                nama = input("Nama Barang Baru : ")
                stok = input("Stok Baru        : ")
                harga = input("Harga Baru       : ")

                data_baru.append([id_cari, nama, stok, harga])

            else:
                data_baru.append(row)

    if ditemukan:
        with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data_baru)

        print("Data berhasil diupdate!")
    else:
        print("ID tidak ditemukan!")

def hapus_data():
    id_hapus = input("\nMasukkan ID yang ingin dihapus: ")

    data_baru = []
    ditemukan = False

    with open(FILE_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == id_hapus:
                ditemukan = True
                continue

            data_baru.append(row)

    if ditemukan:
        with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data_baru)

        print("Data berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")

def menu():
    buat_file_csv()

    while True:
        print("\n")
        print("=" * 40)
        print(" SISTEM MANAJEMEN INVENTORI ")
        print("=" * 40)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Update Data")
        print("5. Hapus Data")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            tampilkan_data()

        elif pilihan == "3":
            cari_data()

        elif pilihan == "4":
            update_data()

        elif pilihan == "5":
            hapus_data()

        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid!")

menu()