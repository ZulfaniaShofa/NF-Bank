import random
import string

# kelompok 
# ~ SABIQ MUHAMMAD ANTEBING MAME
# ~ MUHAMAD RIYANDI
# ~ JIHAD ROBBANI
# ~ DADEN DHARMAWAN


# Membuka file  nasabah
Pengguna = open("nasabah.txt", 'r+')
dataPengguna = {}
for line in Pengguna:
    arr = line.split(',')
    dataPengguna[arr[0]] = arr

# Membuka file  transfer
Transfer = open("transfer.txt", 'r+')
dataTransfer = {}
for line in Transfer:
    arr = line.split(',')
    dataTransfer[arr[1]] = arr

# ----- Fungsi operasi pada file -----

# - Fungsi menulis data baru ke file nasabah dan transfer -
def overwrite():
    Pengguna.seek(0)
    for data in dataPengguna.values():
        Pengguna.write(f"{data[0]},{data[1]},{int(data[2])}\n")
    Transfer.seek(0)
    for data in dataTransfer.values():
        Transfer.write(f"{data[0]},{data[1]},{data[2]},{int(data[3])}\n")

# ----- Fungsi fitur pada menu utama -----
# - Fungsi Buka Rekening -


def buka_rekening():
    print("\n*** BUKA REKENING ***")  # tampilan  dari program
    nama = input("Masukkan nama: ")  # masukan nama untuk nasabah
    # masukan setoran awal untuk tabungan
    saldo = int(input("Masukkan setoran awal: "))
    # mengacak no REK agar tidak ada yang sama
    noRekening = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    # data yang akan di maksukan ke file
    dataPengguna[noRekening] = [noRekening, nama, saldo]
    overwrite()  # masukan data menggunakan fungsi overwrite di atas
    # tanda kalau data berhasil masuk
    print(
        f"Pembukaan rekening dengan nomor {noRekening} atas nama {nama} berhasil.\n")
    main()  # kembali ke menu awal

# - Fungsi Setoran Tunai -


def setor_tunai():
    print("\n*** SETORAN TUNAI ***")  # tampilan  dari program
    # mengecek no rek yang akan menyetor
    noRekening = input("Masukkan nomor rekening: ").upper()
    # menginput saldo yang akan di setor
    saldo = int(input("Masukkan nominal yang akan disetor: "))
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data = dataPengguna.get(noRekening, False)
    if data != False:  # proser data untuk mengecek no rek
        # jika sudah data ketemu baru ditambahkan data baru
        dataPengguna[noRekening][2] = int(data[2]) + saldo
        overwrite()  # menulis data baru ke dalam file dengan fungsi diatas
        # tanda kalau data berhasil masuk
        print(f"Setoran tunai sebesar {saldo} ke rekening {noRekening} berhasil.\n")
    else:
        # tanda kalau data tidak ditemukan
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal.\n")
    main()  # kembali ke menu awal

# - Fungsi Tarik Tunai -


def tarik_tunai():
    print("\n*** TARIK TUNAI ***")  # tampilan  dari program
    # mengecek no rek yang akan menarik atau mengambil uang
    noRekening = input("Masukkan nomor rekening: ").upper()
    # menginput saldo  yang akan di tarik
    saldo = int(input("Masukkan nominal yang akan ditarik: "))
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data = dataPengguna.get(noRekening, False)
    if data != False:  # proser data untuk mengecek no rek
        if int(data[2]) >= saldo:
            dataPengguna[noRekening][2] = int(data[2]) - saldo
            overwrite()
            # tanda kalau data berhasil masuk
            print(
                f"Tarik tunai sebesar {saldo} dari rekening {noRekening} berhasil.")
        else:
            # saldo tidak cukup
            print("Saldo tidak mencukupi. Tarik tunai gagal.")
    else:
        # tanda kalau data yang di input tidak sesuai yang ada di file
        print("Nomor rekening tidak terdaftar. Tarik tunai gagal.\n")
    main()  # kembali ke menu awal

# - Fungsi Transfer -


def transfer_uang():
    print("\n*** TRANSFER ***")  # tampilan  dari program
    # mengecek no rek yang akan mentransfer
    noRekening0 = input("Masukkan nomor rekening sumber: ").upper()
    # mengecek no rek yang akan di transfer
    noRekening1 = input("Masukkan nomor rekening tujuan: ").upper()
    # menginput saldo yg di transfer
    saldo = int(input("Masukkan nominal yang akan ditransfer: "))
    trf = "TRF" + ''.join(random.choice(string.digits)
                          for _ in range(3))  # membuat no transfer dengan no acak
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data0 = dataPengguna.get(noRekening0, False)
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data1 = dataPengguna.get(noRekening1, False)
    if data0 != False:  # proser data untuk mengecek no rek
        if data1 != False:  # proser data untuk mengecek no rek
            if int(data0[2]) >= saldo:
                dataPengguna[noRekening0][2], dataPengguna[noRekening1][2] = int(
                    data0[2]) - saldo, int(data1[2]) + saldo
                dataTransfer[noRekening0] = [trf, noRekening0, noRekening1, saldo]
                overwrite()
                # tanda kalau data berhasil masuk
                print(
                    f"Transfer sebesar {saldo} dari rekening {noRekening0} ke rekening {noRekening1} berhasil.\n")
            else:
                # saldo tidak cukup
                print("Saldo tidak mencukupi. Transfer gagal.\n")
        else:
            # tanda kalau data yang di input tidak sesuai yang ada di file
            print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.\n")
    else:
        # tanda kalau data yang di input tidak sesuai yang ada di file
        print("Nomor rekening sumber tidak terdaftar. Transfer gagal.\n")
    main()  # kembali ke menu awal

# - Fungsi Daftar data Transfer -


def daftar_transfer():
    print("\n*** LIHAT DATA TRANSFER ***")  # tampilan  dari program
    # mengecek no rek yang akan menapilkan daftar transfer
    noRekening = input("Masukkan nomor rekening sumber transfer: ").upper()
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data0 = dataPengguna.get(noRekening, False)
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data1 = dataTransfer.get(noRekening, False)
    if data0 != False:  # proser data untuk mengecek no rek
        if data1 != False:  # proser data untuk mengecek no rek
            # tanda kalau data berhasil akan ditampilkan
            print(f"Daftar transfer dari rekening {noRekening} :")
            # tanda kalau data berhasil akan ditampilkan
            print(f"{data1[0]} {data1[1]} {data1[2]} {int(data1[3])}\n")
        else:
            # tanda kalau data yang di input tidak sesuai yang ada di file
            print("Tidak ada data yang ditampilkan.\n")
    else:
        # tanda kalau data yang di input tidak sesuai yang ada di file
        print("Nomor rekening sumber tidak terdaftar.\n")
    main()  # kembali ke menu awal

# - fungsi sisa saldo nasabah - #


def sisa_saldo():
    print("\n*** LIHAT SISA SALDO ***")  # tampilan  dari program
    # mengecek no rek yang akan menapilkan sisa saldo
    noRekening = input("masukan nomor rekening sumber : ").upper()
    # mengambil data dari file untuk mengecek no rek yg akan di proses oleh code di bawah ini
    data = dataPengguna.get(noRekening, False)
    if data != False:  # proser data untuk mengecek no rek
        # tanda kalau data berhasil akan ditampilkan
        print(f"Lihat Sisa saldo terkini {noRekening} :")
        # tanda kalau data berhasil akan ditampilkan
        print(f"{data[0]} {data[1]} {data[2]} \n")
    else:
        # tanda kalau data yang di input tidak sesuai yang ada di file
        print("Nomor rekening sumber tidak terdaftar. \n")
    main()  # kembali ke menu awal


# - Fungsi Keluar dan Menutup File -
def keluar():
    Pengguna.close()
    Transfer.close()
    print("Terima kasih atas kunjungan Anda...")

# - Fungsi Menu Utama -


def main():
    print(
        "***** SELAMAT DATANG DI NF BANK *****\nMENU:\n[1] Buka rekening\n[2] Setoran tunai\n[3] Tarik tunai\n[4] Transfer\n[5] Lihat daftar transfer\n[6] lihat saldo\n[7] keluar")
    option = input("Masukkan menu pilihan anda: ")
    while option not in ['1', '2', '3', '4', '5', '6', '7']:
        option = input(
            "Pilihan Anda salah. Ulangi.\nMasukkan menu pilihan anda: ")
    switch = {'1': buka_rekening, '2': setor_tunai, '3': tarik_tunai,
              '4': transfer_uang, '5': daftar_transfer, '6': sisa_saldo, '7': keluar}
    switch[option]()


if __name__ == "__main__":
    main()
