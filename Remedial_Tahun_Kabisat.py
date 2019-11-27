def tahunkabisat(a):
    if a % 4 == 0:
        print("Hasil : TAHUN KABISAT")
    elif a % 4 != 0:
        print("Hasil : BUKAN TAHUN KABISAT")
    else:
        print("ERROR! HARAP MASUKKAN ANGKA!")

if __name__ == "__main__":
    tahun = int(input("Input tahun : "))
    tahunkabisat(tahun)