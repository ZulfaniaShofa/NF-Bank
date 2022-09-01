#program perbankan NF
#---------------------------
#library
import os

#sub program
#PROGRAM BUAT REKENING
def buat_rekening():
    print('=========== BUKA REKENING ===========')
    nama = input ('Masukkan Nama Anda: ')
    import random, string
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    setoran = int(input('Masukkan Setoran Awal Anda: '))
    if (setoran < 1000000):
        print('Pembukaan rekening dengan nomor',norek, 'atas nama', nama, 'berhasil') 
    elif(setoran == 1000000):
        print('Pembukaan rekening dengan nomor',norek, 'atas nama', nama, 'berhasil')  
    elif(setoran > 1000000):
        print('Pembukaan rekening dengan nomor',norek, 'atas nama', nama, 'berhasil')\

    
    #mengisi data ke dictionary
    data_rek = {"Rek" : norek,
                "Nama": nama,
                "Saldo": setoran,}

    #memasukan data dictionary ke dalam list
    data_semua_rek.append(data_rek)

#sup program ke 2
#program setor tunai
def setor_tunai(Rek):
    setor = int(input('Silahkan masukkan nominal yang ingin di setor : '))
    saldo = Saldo + setor
    ketemu = 0
    for rek in data_semua_rek:
        if (rek['Saldo'] == saldo):
            #update ketemu
            ketemu = 1
            #tambah saldo
            data_semua_rek.append(saldo)
            print('setor tunai berhasil')

    if (ketemu == 0):
        print("Data yang dicari tidak ditemukan!")
    print()
    print(f'Sisa saldo anda : {saldo}')

#sub program ke 3
#program tarik tunai
def tarik_tunai():
    if Saldo < 50000:
            print('Maaf, saldo anda tidak mencukupi.')
            print('Silahkan isi saldo terlebih dahulu.')
    else:
        print('Jumlah nominal penarikan sebesar 50000, 100000, 250000, 500000, 1000000')
        tunai = int(input('Jumlah penarikan anda : '))
        if (tunai == 50000) or (tunai == 100000) or (tunai == 250000) or (tunai == 500000) or (tunai == 1000000):
            Saldo == Saldo - tunai
            print()
            print(f'Saldo ditarik : {tunai}')
            print(f'Sisa saldo anda : {Saldo}')
        else:
            print('Nominal tidak diketahui')


#sub program ke 4 
#program transfer
def transfer():
    pass

#sub program ke 5
#program daftar transfer
def lihat_data_transfer():
    pass

#program utama
#inisialisasi variabel global (variabel yang bisa diakses lewat manapun)
data_rek = {}       #dictionary
data_semua_rek = [] #list
menu = 0            #variabel biasa
Saldo = 0

#mulai program
while (menu != 6):
    #membersihkan layar command prompt
    os.system("cls")

    #menampilkan menu
    print('* SELAMAT DATANG DI NF BANK **')
    print('MENU')
    print('[1] Buka Rekening')
    print('[2] Setoran Tunai')
    print('[3] Tarik Tunai')
    print('[4] Transfer')
    print('[5] Lihat Data Transfer')
    print('[6] Keluar')
    print('=====================================')
    def getInteger(message):
        while True:
            try:
                userInt = int(input(message))
                return userInt
            except ValueError:
                print('Pilihan Anda Salah. Ulangi')


    menu = getInteger('Masukkan menu pilihan Anda: ')
    menu = input('Masukkan ulang menu pilihan Anda: ')
    #cek menu
    if (menu == '1'):
        buat_rekening()
    elif (menu == '2'):
        cari = input('Masukkan No REK : ')
        setor_tunai(cari)
    elif (menu == '3'):
        tarik_tunai()
    elif (menu == '4'):
        transfer()
    elif (menu == '5'):
        lihat_data_transfer()
    elif(menu == '6'):
        print('Terima Kasih Atas Kunjungan Anda')
    #menunggu user menekan enter untuk melanjutkan
    input('\nTekan ENTER untuk melanjutkan')
