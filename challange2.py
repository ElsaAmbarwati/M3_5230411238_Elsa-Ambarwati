class DaftarMenu:
    def __init__(self):  
        self.menu_makanan = {}
        self.menu_minuman = {}

    def tambah_makanan(self, makanan, harga):
        self.menu_makanan[makanan] = harga
        print(f"{makanan} telah ditambahkan ke daftar menu makanan dengan harga Rp {harga}")

    def tambah_minuman(self, minuman, harga):
        self.menu_minuman[minuman] = harga
        print(f"{minuman} telah ditambahkan ke daftar menu minuman dengan harga Rp {harga}")

    def tampilkan_menu_makanan(self):
        if self.menu_makanan:
            print("\nDaftar Menu Makanan:")
            for makanan, harga in self.menu_makanan.items():
                print(f"{makanan} ==> Rp {harga}")
        else:
            print("Belum ada makanan di daftar menu.")

    def tampilkan_menu_minuman(self):
        if self.menu_minuman:
            print("\nDaftar Menu Minuman:")
            for minuman, harga in self.menu_minuman.items():
                print(f" {minuman} ==> Rp {harga}")
        else:
            print("Belum ada minuman di daftar menu.")

    def tampilkan_semua_menu(self):
        print("\n--- Daftar Menu ---")
        self.tampilkan_menu_makanan()
        self.tampilkan_menu_minuman()

    def keluar(self):
        print("Terima kasih! Sampai jumpa.")
        exit()

class TambahMenu:
    def __init__(self, daftar_menu):
        self.daftar_menu = daftar_menu

    def tambah_makanan(self, makanan, harga):
        self.daftar_menu.menu_makanan[makanan] = harga
        print(f"{makanan} telah ditambahkan ke menu makanan.")

    def tambah_minuman(self, minuman, harga):
        self.daftar_menu.menu_minuman[minuman] = harga
        print(f"{minuman} telah ditambahkan ke menu minuman.")

    def menu_keluar(self):
        print("Kembali ke menu utama.")

def main():
    daftar_menu = DaftarMenu()
    tambah_menu = TambahMenu(daftar_menu)

    while True:
        print("\nMenu:")
        print("1. Tampilkan Menu Makanan")
        print("2. Tampilkan Menu Minuman")
        print("3. Tambah Menu")
        print("0. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/0): ")

        if pilihan == '1':
            daftar_menu.tampilkan_menu_makanan() 
        elif pilihan == '2':
            daftar_menu.tampilkan_menu_minuman() 
        elif pilihan == '3':
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")
            print("0. Kembali")  
            jenis_pilihan = input("Pilih jenis yang ingin ditambahkan (1/2/0): ")
            
            if jenis_pilihan == '1':
                item = input("Masukkan nama makanan: ")
                if not item.strip(): 
                    print("Nama makanan tidak boleh kosong.")
                    continue
                harga = input("Masukkan harga makanan: ")
                try:
                    harga = int(harga) 
                    tambah_menu.tambah_makanan(item, harga)
                except ValueError:
                    print("Harga harus berupa angka.")
            elif jenis_pilihan == '2':
                item = input("Masukkan nama minuman: ")
                if not item.strip():
                    print("Nama minuman tidak boleh kosong.")
                    continue
                harga = input("Masukkan harga minuman: ")
                try:
                    harga = int(harga)
                    tambah_menu.tambah_minuman(item, harga) 
                except ValueError:
                    print("Harga harus berupa angka.")
            elif jenis_pilihan == '0': 
                print("Kembali ke menu utama.")
            else:
                print("Pilihan tidak valid. Kembali ke menu utama.")

        elif pilihan == '0':
            daftar_menu.keluar()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
