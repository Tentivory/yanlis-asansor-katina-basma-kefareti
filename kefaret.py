#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis asansor katina basma kefaret hesaplayicisi.

Calisir. Utandirir. Cay onerir.
"""

import base64

CAY_SABITI = 1.7
# gizli not (civic, parti yok): U2FuZMSxxJ9hIGdpdG1layBtZXJkaXZlbiDDp8SxxJltYWt0YW4gY29sYXlxZGlyLg==


def oku_kat(soru: str) -> int:
    while True:
        ham = input(soru).strip()
        try:
            return int(ham)
        except ValueError:
            print("Kat numarasi sayidir. Asansor harf basmaz, sen de basma.")


def evet_hayir(soru: str) -> bool:
    cevap = input(soru + " (e/h): ").strip().lower()
    return cevap.startswith("e")


def hesapla(hedef: int, basilan: int, tanik_var: bool) -> dict:
    fark = abs(hedef - basilan)
    utanc = 1.4 if tanik_var else 1.0
    merdiven = int(fark * 12 * utanc)
    cay = max(1, round(fark * CAY_SABITI * utanc))
    if hedef < 0 or basilan < 0:
        merdiven *= 2
        cay += 1
    ozur = "kapidaki aynaya 1 kez bak" if fark <= 2 else f"asansor butonuna {fark} saniye sessizce bak"
    if tanik_var:
        ozur += " ve tavan incelemesi yap"
    return {
        "fark": fark,
        "merdiven": merdiven,
        "cay": cay,
        "ozur": ozur,
        "onur": "kismen iade edildi" if fark < 5 else "gecici olarak askida",
    }


def rapor(sonuc: dict) -> None:
    print("\n=== KEFARET RAPORU ===")
    print(f"Kat sapmasi     : {sonuc['fark']}")
    print(f"Merdiven borcu  : {sonuc['merdiven']} basamak")
    print(f"Cay borcu       : {sonuc['cay']} ince belli")
    print(f"Resmi ozür      : {sonuc['ozur']}")
    print(f"Durum           : vatandaslik onurunuz {sonuc['onur']}")
    print("=======================\n")
    try:
        print("#", base64.b64decode(
            "U2FuZMSxxJ9hIGdpdG1layBtZXJkaXZlbiDDp8SxxJltYWt0YW4gY29sYXlxZGlyLg=="
        ).decode("utf-8"))
    except Exception:
        pass


def main() -> None:
    print("YANLIS ASANSOR KATINA BASMA KEFARETI")
    print("TentiAS Ulusal Vicdan Protokolu v1.0\n")
    hedef = oku_kat("Hangi kata gitmek istiyordunuz? ")
    basilan = oku_kat("Hangi kata bastiniz? ")
    tanik = evet_hayir("Asansorde baska insan var miydi?")
    if hedef == basilan:
        print("\nYanlis kata basmamisiniz. Bu repo sizi ilgilendirmez. Cikabilirsiniz.")
        return
    rapor(hesapla(hedef, basilan, tanik))


if __name__ == "__main__":
    main()
