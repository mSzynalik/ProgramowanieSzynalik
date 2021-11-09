class Magazyn:
    def __init__(self, ulica: str, miasto: str, pojemnosc: int, kierownik_imie: str, kierownik_nazwisko: str):
        self._ulica = ulica
        self._miasto = miasto
        self._pojemnosc = pojemnosc
        self._kierownik_imie = kierownik_imie
        self._kierownik_nazwisko = kierownik_nazwisko

    def __str__(self):
        return f"Magazyn znajduje się w {self._miasto} przy ul. {self._ulica}.\nPoj. magazynu: {self._pojemnosc} litrów"

    @property
    def ulica(self):
        return self._ulica

    @property
    def miasto(self):
        return self._miasto

    @property
    def pojemnosc(self):
        return self._pojemnosc

    @property
    def kierownik_imie(self):
        return self._kierownik_imie

    @property
    def kierownik_nazwisko(self):
        return self._kierownik_nazwisko


class Klient:
    def __init__(self, miasto: str, ulica: str, kod_pocztowy: str):
        self._miasto = miasto
        self._ulica = ulica
        self._kod_pocztowy = kod_pocztowy

    def __str__(self):
        return f"Adres klienta:\nul. {self._ulica}\n{self._kod_pocztowy},{self._miasto}"

    @property
    def miasto(self):
        return self._miasto

    @property
    def ulica(self):
        return self._ulica

    @property
    def kod_pocztowy(self):
        return self._kod_pocztowy


class KlientDetaliczny(Klient):
    def __init__(self, imie: str, nazwisko: str, miasto: str, ulica: str, kod_pocztowy: str):
        super().__init__(miasto, ulica, kod_pocztowy)
        self._imie = imie
        self._nazwisko = nazwisko

    def __str__(self):
        return f"{self._imie} {self._nazwisko}, z miasta {self._miasto}(kod pocz. {self._kod_pocztowy})"

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def miasto(self):
        return self._miasto

    @property
    def ulica(self):
        return self._ulica

    @property
    def kod_pocztowy(self):
        return self._kod_pocztowy


class KlientBiznesowy(Klient):
    def __init__(self, nazwa_firmy: str, nip: str, regon: str, przedstawiciel_imie: str, przedstawiciel_nazwisko: str,
                 miasto: str, ulica: str, kod_pocztowy: str):
        super().__init__(miasto, ulica, kod_pocztowy)
        self._nazwa_firmy = nazwa_firmy
        self._nip = nip
        self._regon = regon
        self._przedstawiciel_imie = przedstawiciel_imie
        self._przedstawiciel_nazwisko = przedstawiciel_nazwisko

    def __str__(self):
        return f"Firma: {self._nazwa_firmy}\nNIP: {self._nip}\nREGON: {self._regon}"

    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy

    @property
    def nip(self):
        return self._nip

    @property
    def regon(self):
        return self._regon

    @property
    def przedstawiciel_imie(self):
        return self._przedstawiciel_imie

    @property
    def przedstawiciel_nazwisko(self):
        return self._przedstawiciel_nazwisko


class Produkt(Magazyn):
    def __init__(self, ulica: str, miasto: str, pojemnosc: int, kierownik_imie: str, kierownik_nazwisko: str,
                 id_produktu: str, cena: float, kolor_produktu: str, lata_gwarancji: int):
        super().__init__(ulica, miasto, pojemnosc, kierownik_imie, kierownik_nazwisko)
        self._id_produktu = id_produktu
        self._cena = cena
        self._kolor_produktu = kolor_produktu
        self._lata_gwarancji = lata_gwarancji

    def __str__(self):
        return f"Prod. o id: {self._id_produktu} jest w magazynie w mieście {self._miasto}\nCena: {self._cena}zł."

    @property
    def ulica(self):
        return self._ulica

    @property
    def miasto(self):
        return self._miasto

    @property
    def pojemnosc(self):
        return self._pojemnosc

    @property
    def kierownik_imie(self):
        return self._kierownik_imie

    @property
    def kierownik_nazwisko(self):
        return self._kierownik_nazwisko

    @property
    def id_produktu(self):
        return self._id_produktu

    @property
    def cena(self):
        return self._cena

    @property
    def kolor_produktu(self):
        return self._kolor_produktu

    @property
    def lata_gwarancji(self):
        return self._lata_gwarancji


class Zamowienie:
    def __init__(self, produkt: Produkt, magazyn: Magazyn, klient: Klient, liczba_sztuk: int, obslugujacy_imie: str,
                 obslugujacy_nazwisko: str):
        self._produkt = produkt
        self._magazyn = magazyn
        self._klient = klient
        self._liczba_sztuk = liczba_sztuk
        self._obslugujacy_imie = obslugujacy_imie
        self._obslugujacy_nazwisko = obslugujacy_nazwisko

    def __str__(self):
        return f"Zamówiono {self._liczba_sztuk} sztuk produktu o id {self.produkt.id_produktu}" \
               f" o cenie jedn. {self.produkt.cena} zł\nProdukt znajduje się w magazynie" \
               f" w mieście {self.magazyn.miasto}" \
               f"\nDane klienta: {self._klient}\n" \
               f"Zamówienie obsługuje {self._obslugujacy_imie} {self._obslugujacy_nazwisko}."

    def wartosc_zamowienia(self):
        return f"Wartość zamówienia wynosi: {round(self._produkt.cena * self._liczba_sztuk, 2)} zł."

    def adres_do_wysylki(self):
        return f"Adres do wysyłki: {klient_detal1.ulica}, {klient_detal1.miasto}, {klient_detal1.kod_pocztowy} "

    @property
    def produkt(self):
        return self._produkt

    @produkt.setter
    def produkt(self, new_produkt: Produkt):
        self._produkt = new_produkt

    @property
    def magazyn(self):
        return self._magazyn

    @magazyn.setter
    def magazyn(self, new_magazyn: Magazyn):
        self._magazyn = new_magazyn

    @property
    def klient(self):
        return self._klient

    @klient.setter
    def klient(self, new_klient: str):
        self._klient = new_klient

    @property
    def liczba_sztuk(self):
        return self._liczba_sztuk

    @liczba_sztuk.setter
    def liczba_sztuk(self, new_liczba_sztuk: str):
        self._liczba_sztuk = new_liczba_sztuk

    @property
    def obslugujacy_imie(self):
        return self._obslugujacy_imie

    @obslugujacy_imie.setter
    def obslugujacy_imie(self, new_obslugujacy_imie: str):
        self._obslugujacy_imie = new_obslugujacy_imie

    @property
    def obslugujacy_nazwisko(self):
        return self._obslugujacy_nazwisko

    @obslugujacy_nazwisko.setter
    def obslugujacy_nazwisko(self, new_obslugujacy_nazwisko: str):
        self._obslugujacy_nazwisko = new_obslugujacy_nazwisko


magazyn1 = Magazyn("Kolorowa 4", "Jaworzno", 15_000, "Józef", "Wichura")
magazyn2 = Magazyn("Brzydka 1", "Jaworzno", 20_000, "Halina", "Kiepska")
klient1 = Klient("Jaworzno", "Biała 1", "43-600")
klient2 = Klient("Katowice", "Kopalniana 3", "42-500")
klient_detal1 = KlientDetaliczny("Adrian", "Kostka", klient1.miasto, klient1.ulica, klient1.kod_pocztowy)
klient_biz1 = KlientBiznesowy("Januszex", "63200011", "00005222", "Janusz", "Biznesman", klient2.miasto, klient2.ulica,
                              klient2.kod_pocztowy)
produkt1 = Produkt(magazyn1.ulica, magazyn1.miasto, magazyn1.pojemnosc, magazyn1.kierownik_imie,
                   magazyn1.kierownik_nazwisko, "A1", 30.00, "czarny", 5)
zamowienie1 = Zamowienie(produkt1, magazyn1, klient_detal1, 10, "Krzysztof", "Pracowniś")
print(zamowienie1)
print(zamowienie1.wartosc_zamowienia())
print(zamowienie1.adres_do_wysylki())
