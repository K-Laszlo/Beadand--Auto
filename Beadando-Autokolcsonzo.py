from datetime import datetime
from abc import ABC, abstractmethod

class Auto(ABC):
    @abstractmethod
    def __init__(self, rendsz, dij):
        self.rendsz = rendsz
        self.dij = dij


class Szemelyauto(Auto):
    def __init__(self, rendsz, hajtas):
        super().__init__(rendsz, dij=15000)
        self.hajtas = hajtas


class Teherauto(Auto):
    def __init__(self, rendsz, suly):
        super().__init__(rendsz, dij=27000)
        self.suly = suly


class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berl_ek = []


    def plus_auto(self, auto):
        self.autok.append(auto)


    def berl(self, rendsz, datum):
        for berl in self.berl_ek:
            if berl.auto.rendsz == rendsz and berl.datum == datum:
                print("\nA választott Autót már kibérelték erre a napra. \nKérjük válasszon másik Autót vagy másik Dátumot!")
                return
        for auto in self.autok:
            if auto.rendsz == rendsz:
                self.berl_ek.append(Berles(auto, datum))
                print("Sikeres foglalás!")
                return auto.dij
        print("\nA megadott rendszámú Autó nem elérhető az Autókölcsönzöben.")

    def lemond(self, rendsz, datum):
        for berl in self.berl_ek:
            if berl.auto.rendsz == rendsz and berl.datum == datum:
                self.berl_ek.remove(berl)
                return True
        return False

    def list_berl_ek(self):
        for berl in self.berl_ek:
            print(f"Autó: {berl.auto.rendsz}, Időpont: {berl.datum}")


kolcsonzo = Autokolcsonzo("Rapid Cars")

kolcsonzo.plus_auto(Szemelyauto("HKX-110", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("MKT-452", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("KKM-240", "Elsőkerék"))
kolcsonzo.plus_auto(Szemelyauto("HKX-110", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("MTT-132", "Elsőkerék"))
kolcsonzo.plus_auto(Szemelyauto("HMM-267", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("HPV-198", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("TGK-233", "Összkerék"))
kolcsonzo.plus_auto(Szemelyauto("IJT-266", "Elsőkerék"))
kolcsonzo.plus_auto(Szemelyauto("GKV-623", "Elsőkerék"))
kolcsonzo.plus_auto(Teherauto("PPS-220", "3,5T"))
kolcsonzo.plus_auto(Teherauto("PPT-222", "3,5T"))
kolcsonzo.plus_auto(Teherauto("PBT-112", "7,5T"))
kolcsonzo.plus_auto(Teherauto("BPT-186", "7,5T"))
kolcsonzo.plus_auto(Teherauto("KKT-211", "7,5T"))
kolcsonzo.plus_auto(Teherauto("PKT-152", "3,5T"))
kolcsonzo.plus_auto(Teherauto("PPT-222", "3,5T"))


kolcsonzo.berl("HKX-110", datetime(2024, 10, 10))
kolcsonzo.berl("MKT-452", datetime(2024, 11, 15))
kolcsonzo.berl("KKM-240", datetime(2024, 9, 21))
kolcsonzo.berl("PPT-222", datetime(2024, 8, 15))


while True:

    print("\nÜdv, a RAPID CARS-nál Miben segíthetünk?:")
    print("1. Autó / Teherauto bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Autók listázása")
    print("5. Kilépés")
    case = input("Kérem választásszon a következő lehetőségek közül (1_2_3_4_5): ")

    if case == "1":
        rendsz = input("\nA bérelendő Autó rendszáma: ")
        datum = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN, jelenleg csak egy napra lehetséges bérelni): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nHibás dátum! A bérlés csak jövőbeni időpontra lehetséges.")

            else:
                dij = kolcsonzo.berl(rendsz, datum)
                if dij:
                    print(f"A bérlés sikeres! A bérlési dij: {dij} Ft")
                else:
                    print("\nHibás adat!")

        except ValueError:
            print("\nHibás a dátum formátuma!")
    elif case == "2":
        rendsz = input("\nLemondandó Autó rendszáma?: ")
        datum = input("Lemondandó bérlési dátum? (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = kolcsonzo.lemond(rendsz, datum)
            if siker:
                print("\nA bérlésed sikeresen lemondva.")
            else:
                print("\nNincs ilyen bérlés.")

        except ValueError:
            print("\nA dátum formátuma hibás!")

    elif case == "3":
        kolcsonzo.list_berl_ek()
    elif case == "4":
        print("Bérelhető Autók száma:")
        print(len(kolcsonzo.autok))
        print("Személyautók:")
        for auto in kolcsonzo.autok:
            if isinstance(auto, Szemelyauto):
                print(f"Rendszám: {auto.rendsz}, Dij: {auto.dij} Ft, (Hajtás: {auto.hajtas})")
        print("\nTeherautók:")
        for auto in kolcsonzo.autok:
            if isinstance(auto, Teherauto):
                print(f"Rendszám: {auto.rendsz}, Ár: {auto.dij} Ft, (Teherbirás: {auto.suly})")
    elif case == "5":
        break
    else:
        print("\nHibás választás!")
