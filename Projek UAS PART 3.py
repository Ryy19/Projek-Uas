import os

Run = True
tutup = True

def Clear():
    os.system('cls')
def Garis():
    print("-----------------------------------------------------------------") 
def Awal():
    Clear()
    print("                     Bimbel Online (BO)")
    Garis()
    print("Paket SD/MI 4 Mapel Rp. 550.000")
    print("Paket SMP/MTs 5 Mapel Rp. 850.000")
    print("Paket SMA/MA 6 Mapel Rp. 1.100.000")
    Garis()
    print("Pilih tingkatan anda:")
    Garis()
    print("1.   SD/MI")
    print("2.   SMP/MTs")
    print("3.   SMA/MA IPA")
    print("4.   SMA/MA IPS")
    print("5.   Keluar")
    print("")
    print("Masukkan angka 1,2,3,4,5")
def Konfirm():
    print("                        Konfirmasi")
    Garis()
def yakin():
    Garis()
    print("")
    konfirmasi=input("Masukkan y/n= ")
    if konfirmasi=="y":
        Closed()
def Paket_SD():
    Clear()
    Konfirm()
    print("Apakah anda ingin membeli Paket BO tingkat SD/MI?")
    print("Harga Rp. 550.000")
    yakin()
def Paket_SMP():
    Clear()
    Konfirm()
    print("Apakah anda ingin membeli paket BO tingkat SMP/MTs?")
    print("Harga Rp. 550.000")
    yakin()
def Paket_IPA():
    Clear()
    Konfirm()
    print("Apakah anda ingin membeli paket BO tingkat SMA/MA IPA?")
    print("Harga Rp. 1.100.000")
    yakin()
def Paket_IPS():
    Clear()
    Konfirm()
    print("Apakah anda ingin membeli paket BO tingkat SMA/MA IPS?")
    print("Harga Rp. 1.100.000")
    yakin()
def Closed():
    while tutup:
        Clear()
        Garis()
        print("Terimakasih sudah menggunakan layanan kami")
        Garis()
        balik=input("Tekan apa saja untuk kembali ke menu")
        if balik==(""):
            break
def salah():
    Clear()
    print("Maaf, anda memasukkan angka yang salah")
    print("Mohon masukkan angka yang benar")
    Garis()
    back= input("Tekan enter untuk kembali ke menu")
    if back==(""):
        run()

def run():
    while Run:
        Awal()
        masukkan=input("Masukkan nomor : ")
        if masukkan=="1":
            Paket_SD()
        elif masukkan=="2":
            Paket_SMP()
        elif masukkan=="3":
            Paket_IPA()
        elif masukkan=="4":
            Paket_IPS()
        elif masukkan=="5":
            Clear()
            print("Apakah anda ingin keluar")
            konfirmasi=input("Tekan y/n= ")
            if konfirmasi=="y":
                break
            elif konfirmasi=="n":
                run()
        else:
            salah()
run()               