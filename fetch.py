"""Holt den Datensatz «Kantonaler Stromverbrauch» (100233) von Open Data
Basel-Stadt neu und schreibt ihn als data/verbrauch.csv.

UNGETESTET: Dieses Skript wurde im Rahmen der Auswertung nie ausgeführt.
Die Analyse (analysis.ipynb) liest immer die lokale CSV und hängt an keiner
Stelle von einem Netzwerkaufruf ab. Wer die Daten aktualisieren will, ruft
dieses Skript bewusst selbst auf und prüft danach Kopfzeile und Zeilenzahl.

Nur Standardbibliothek. Es wird der Export-Endpunkt verwendet, nicht der
paginierte Record-Endpunkt (der bei über 500 000 Zeilen ins Leere führt).
"""
import sys
import urllib.request

URL = ("https://data.bs.ch/api/explore/v2.1/catalog/datasets/100233/exports/csv"
       "?lang=de&timezone=Europe%2FZurich&delimiter=%3B")
ZIEL = "data/verbrauch.csv"


def main():
    print("lade", URL)
    with urllib.request.urlopen(URL, timeout=600) as antwort, open(ZIEL, "wb") as ziel:
        gesamt = 0
        while True:
            block = antwort.read(1 << 20)
            if not block:
                break
            ziel.write(block)
            gesamt += len(block)
    print(f"geschrieben: {ZIEL} ({gesamt / 1e6:.1f} MB)")
    print("Nächster Schritt: analysis.ipynb von oben nach unten ausführen.")


if __name__ == "__main__":
    try:
        main()
    except Exception as fehler:  # noqa: BLE001
        print("Download fehlgeschlagen:", fehler, file=sys.stderr)
        sys.exit(1)
