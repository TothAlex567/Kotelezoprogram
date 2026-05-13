import requests
import json
import os


def konyv_adatok_lekerese(isbn):
    """Lekéri a könyv adatait az Open Library API-tól."""
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"

    try:
        valasz = requests.get(url)
        valasz.raise_for_status()
        adatok = valasz.json()

        isbn_kulcs = f"ISBN:{isbn}"
        if isbn_kulcs in adatok:
            konyv = adatok[isbn_kulcs]
            return {
                "isbn": isbn,
                "cim": konyv.get("title", "Ismeretlen cím"),
                "szerzo": konyv.get("authors", [{"name": "Ismeretlen"}])[0]["name"],
                "ev": konyv.get("publish_date", "Nincs adat"),
                "oldalszam": konyv.get("number_of_pages", "Nincs adat")
            }
        else:
            print(f"[-] Nem található könyv ezzel az ISBN számmal :( : {isbn}")
            return None
    except Exception as e:
        print(f"[!] Hiba történt a lekérés során: {e}")
        return None


def mentes_json_fajlba(katalogus, fajlnev="konyveim.json"):
    """Elmenti a listát egy JSON fájlba."""
    try:
        with open(fajlnev, "w", encoding="utf-8") as f:
            json.dump(katalogus, f, ensure_ascii=False, indent=4)
        print(f"[+] Adatbázis frissítve: {fajlnev}")
    except IOError as e:
        print(f"[!] Hiba volt a mentés során: {e}")


def main():
    print("--- Üdvözöllek a Mini Könyvtáramban :) ---")
    katalogus = []

    # Ha már van korábbi mentés, töltsük be (opcionális, de profi)
    if os.path.exists("konyveim.json"):
        try:
            with open("konyveim.json", "r", encoding="utf-8") as f:
                katalogus = json.load(f)
                print(f"({len(katalogus)} könyv betöltve a korábbi listából)")
        except:
            katalogus = []

    while True:
        isbn = input("\nAdj meg egy ISBN számot (pl. 0451526562) vagy 'q' a kilépéshez: ").strip()

        if isbn.lower() == 'q':
            break

        if not isbn:
            continue

        adatok = konyv_adatok_lekerese(isbn)

        if adatok:
            print(f"\nTalált könyv:")
            print(f"  Cím: {adatok['cim']}")
            print(f"  Szerző: {adatok['szerzo']}")

            katalogus.append(adatok)
            # Automatikus mentés minden találat után
            mentes_json_fajlba(katalogus)

    print("Viszlát!")


if __name__ == "__main__":
    main()
