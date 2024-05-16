import random

class Power:
    def __init__(self):
        self.player_power = random.randint(5, 10)
        self.monster_power = random.randint(1, 5)

    def fights(self, player_power, monster_power):
        if player_power > monster_power:
            print(f"Kamu mengalahkan monster! (Power Kamu: {player_power}, Power Monster: {monster_power})")
            return True
        
        elif player_power == monster_power:
            print(f"Kamu dan monster mundur dari pertandingan. (Power Kamu: {player_power}, Power Monster: {monster_power})")
            return False

        else:
            print(f"Kamu kalah dan mati di tangan monster. (Power Kamu: {player_power}, Power Monster: {monster_power})")
            return False

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_inventory(self):
        return self.items

class Story:
    pwr = Power()
    inv = Inventory()
    def line(self):
        player_power = self.pwr.player_power
        monster_power = self.pwr.monster_power
        print(f"Selamat datang dalam petualangan mencari harta karun! Power kamu saat ini: {player_power}")
        print("\nBab 1: Memasuki Hutan Gelap")
        choice1 = input("Kamu menemukan jalan bercabang. Pilih kiri (1) atau kanan (2): ")
        if choice1 == "1":
            print("Kamu memilih jalan kiri dan bertemu dengan monster pertama!")
            choice1_fights = input(f"Monster muncul dengan power {monster_power}. Apakah kamu ingin melawan (y/n)? ")
            if choice1_fights == "y":
                if not Power.fights(self, player_power, monster_power):
                    return
        else:
            print("Kamu memilih jalan kanan dan menemukan tempat peristirahatan. Kamu mendapatkan tambahan power.")
            player_power += random.randint(1, 5)
            print(f"Power kamu sekarang: {player_power}")

        choice_1 = input("Kamu melanjutkan perjalanan. Lanjutkan (1) , Buka Tas (2) , atau Tukar Barang (3): ")
        if choice_1 == "3":
            print("Kamu bertemu pedagang yang menjual barang ajaib.")
            print()
            print("Barang yang dijual:")
            print("1. Pedang Ajaib (10-20 power) = 10 coin")
            print("2. Perisai Ajaib (1-5 power) = 2 coin")
            print("3. Kembali ke Game")
            ch1 = input("Pilih barang yang ingin kamu beli: ")
            if ch1 == "1":
                power1 = random.randint(10, 20)
                print(f"Kamu mendapatkan power: {power1}")
                player_power += power1
                self.inv.add_item("Pedang Ajaib")
                print(f"Power kamu sekarang: {player_power}") 
            if ch1 == "2":
                power2 = random.randint(1, 5)
                print(f"Kamu mendapatkan power: {power2}")
                player_power += power2
                self.inv.add_item("Perisai Ajaib")

        elif choice_1 == "2":
            print("=========================================")
            print("Isi Tas Kamu: ", self.inv.show_inventory())
            print("=========================================")
            print(f"Power kamu sekarang: {player_power}")

        elif choice_1 == "1":
            print("Kamu memutuskan untuk melanjutkan perjalanan.")
            
        else:
            print("Kamu salah memasukan pilihan")
            return self.line() 
            

        print("\nBab 2: Menyusuri Sungai")
        choice2 = input("Kamu melihat sesuatu berkilauan di sungai. Ambil (1) atau lanjutkan perjalanan (2): ")
        if choice2 == "1":
            print("Kamu menemukan kristal yang meningkatkan power kamu!")
            player_power += random.randint(5, 10)
            print(f"Power kamu sekarang: {player_power}")
        else:
            print("Kamu memutuskan untuk tidak mengambilnya dan melanjutkan perjalanan.")

        choice_2 = input("Kamu melanjutkan perjalanan. Lanjutkan (1) , Buka Tas (2) , atau Tukar Barang (3): ")
        if choice_2 == "3":
            print("Kamu bertemu pedagang yang menjual barang ajaib.")
            print()
            print("Barang yang dijual:")
            print("1. Pedang Ajaib (10-20 power) = 10 coin")
            print("2. Perisai Ajaib (1-5 power) = 2 coin")
            print("3. Kembali ke Game")
            ch2 = input("Pilih barang yang ingin kamu beli: ")
            if ch2 == "1":
                power1 = random.randint(10, 20)
                print(f"Kamu mendapatkan power: {power1}")
                player_power += power1
                self.inv.add_item("Pedang Ajaib")
                print(f"Power kamu sekarang: {player_power}") 
            if ch2 == "2":
                power2 = random.randint(1, 5)
                print(f"Kamu mendapatkan power: {power2}")
                player_power += power2
                self.inv.add_item("Perisai Ajaib")

        elif choice_2 == "2":
            print("=========================================")
            print("Isi Tas Kamu: ", self.inv.show_inventory())
            print("=========================================")
            print(f"Power kamu sekarang: {player_power}")

        elif choice_2 == "1":
            print("Kamu memutuskan untuk melanjutkan perjalanan.")
            
        else:
            print("Kamu salah memasukan pilihan")
            return self.line() 

        print("\nBab 3: Gua Berhantu")
        choice3 = input("Kamu memasuki gua dan bertemu dengan monster kedua. Apakah kamu ingin melawan (y/n)? ")
        if choice3 == "y":
            monster_power = random.randint(1, 20)
            if not Power.fights(self, player_power, monster_power):
                return
            
        choice_3 = input("Kamu melanjutkan perjalanan. Lanjutkan (1) , Berhenti (2) , atau Tukar Barang (3): ")
        if choice_3 == "3":
            print("Kamu bertemu pedagang yang menjual barang ajaib. Kamu menukarkan coin kamu dengan tersebut.")
            player_power = random.randint(10, 20)
            print(f"Power kamu sekarang: {player_power}") 

        elif choice_3 == "2":
            print("Kamu memutuskan untuk beristirahat sejenak sebelum melanjutkan perjalanan.")
            player_power += random.randint(1, 5)
            print(f"Power kamu sekarang: {player_power}")

        elif choice_3 == "1":
            print("Kamu memutuskan untuk melanjutkan perjalanan.")
            
        else:
            print("Kamu salah memasukan pilihan")
            return self.line() 
        print()
        print("Selama perjalanan kamu yang cukup panjang dengan dari kejauhan terlihat ada seseorang memanggilmu, ternyata seseorang tersebut adalah seorang petualang.")
        prolgoue = input("Kamu bertemu dengan seorang petualang yang ingin bertukar barang. Apakah kamu ingin bertukar (y/n)? ")
        if prolgoue == "y":
            print("Kamu bertukar barang dengan petualang tersebut.")
            print("=========================================")
            print("Isi Tas Kamu: ", self.inv.show_inventory())
            print("=========================================")
            print(f"Power kamu sekarang: {player_power}")
            ntp = input("Barang apa yang ingin kamu tukar?: ")
            self.inv.remove_item(ntp)
            self.inv.add_item("Patung Emas")
            print("Kamu tidak kehilangan power dan mendapatkan Patung Emas.")
            print(f"Power kamu sekarang: {player_power}")
        else:
            print("Kamu memilih untuk tidak bertukar barang.")

        print()
        print("\nBab 4: Harta Karun Terakhir")
        print("Kamu menemukan peti harta karun, tetapi dijaga oleh monster terakhir yang sangat kuat!")
        monster_final_power = random.randint(10, 25)
        choice_final = input(f"Monster muncul dengan power {monster_final_power}. Apakah kamu ingin melawan (y/n)? ")
        if choice_final == "y":
            if player_power > monster_final_power:
                print("Selamat! Kamu telah mengalahkan semua monster dan menemukan harta karun!")
            else:
                print("Kamu kalah melawan monster terakhir. Petualanganmu berakhir di sini.")
        else:
            print("Kamu memilih untuk tidak melawan dan meninggalkan harta karun. Petualanganmu berakhir di sini.")

        choice_4 = input("Selamat Kamu telah menyelesaikan petualanganmu. Apakah kamu ingin bermain kembali (1) atau keluar (2)?: ")
        if choice_4 == "1":
            print("Kamu memutuskan untuk bermain kembali.")
            return self.line()
        elif choice_4 == "2":
            print("Kamu memutuskan untuk keluar dari petualangan.")
            return 
        else:
            print("Kamu salah memasukan pilihan")
            
if __name__ == "__main__":
    game = Story()
    game.line() 