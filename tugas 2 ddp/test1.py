import random, string


print('***** SELAMAT DATANG DI NF BANK *****')
print('MENU')
print('[1] Buka Rekening')
print('[2] Setoran Tunai')
print('[3] Tarik tunai')
print('[4] Transfer')
print('[5] Lihat daftar transfer')
print('[6] Keluar')

menu = int(input('Masukan menu pilihan anda : '))

if menu==1:
    print('\n*** BUKA REKENING ****')
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    nama_nasabah = str(input('Masukan nama : '))
    saldo = int(input('Masukan Setoran awal : '))
    nasabah_new = "{},{},{}\n".format(norek,nama_nasabah,saldo)
    file_nasabah = open("nasabah.txt", "a")
    file_nasabah.write(str(nasabah_new))
    file_nasabah.close()
    print('Pembukaan rekening dengan nomor {} atas nama {} berhasil'.format(norek, nama_nasabah))
elif menu==2:
    print('\n*** SETORAN TUNAI ***')
    norek = str(input('Masukan nomor rekening : '))
    setoran = int(input('Masukan nominal yang akan disetor :'))
    file_nasabah = open("nasabah.txt")
