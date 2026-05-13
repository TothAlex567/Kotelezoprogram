# Mini Könyvtár Program

Ez a program az **Open Library API** segítségével keres könyveket ISBN szám alapján, majd egy helyi JSON adatbázisba menti őket.

## Választott téma
**1. Könyvkereső program az Open Library API használatával**

## Funkciók
- Könyv adatok (cím, szerző, év, oldalszám) lekérése az internetről.
- Hibakezelés hiányzó adatok vagy hálózati hiba esetén.
- Adatok tárolása strukturált JSON fájlban.
- Felhasználóbarát parancssori felület.

## Használt technológiák
- **Python 3**
- **Requests könyvtár** (HTTP kérésekhez)
- **JSON modul** (Adatkezeléshez)

## Futtatás
1. Győződj meg róla, hogy a Python telepítve van.
2. Telepítsd a szükséges könyvtárat:
   ```bash
   pip install requests
