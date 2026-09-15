Eine Seite, die je Jahr die zehn verbrauchsärmsten Werktage (Montag bis Freitag) im Stromnetz von Basel-Stadt als Balken zeigt; das Datum erscheint erst per Klick. Live: https://derbilla.github.io/hackamrhein-warmup/

Befund: Über alle Tage gerechnet sind die stillsten Tage keine Feiertage, sondern Sonntage, 133 der 150 Ranglistenplätze 2012–2026, der stillste Tag ist meist der Ostersonntag. Nimmt man die Wochenenden heraus, zeigt das Netz den Feiertagskalender fast lückenlos: Von 150 Werktagsplätzen sind 115 gesetzliche Feiertage, 23 Tage zwischen Weihnachten und Neujahr, 8 Brückentage und nur 4 andere Werktage; ein Feiertag liegt im Median bei 79 % des Werktagsmedians, ein Sonntag bei 79 %, ein normaler Werktag bei 100 %.

Quelle: Kantonaler Stromverbrauch, Industrielle Werke Basel über Open Data Basel-Stadt (Datensatz 100233), CC BY 4.0, Stand 11. September 2026.

Ablauf: `analysis.ipynb` liest `data/verbrauch.csv`, schreibt `data/stillste-tage.json` und `data/feiertage.json` und bettet den Inhalt in `index.html` ein, weil Browser `fetch()` aus dem Dateisystem blockieren. Nur Standardbibliothek. `fetch.py` holt die CSV neu.

Einschränkungen:
- Lokal direkt verbrauchter Solarstrom fehlt in den Daten; der Netzbezug ist deshalb untererfasst, über die Jahre zunehmend, was den Langzeitvergleich verzerrt. Die Prozentwerte je Jahr sind davon weniger betroffen.
- Die Zeitstempel 01.01.2014 00:00, 01.11.2015 00:00 und 01.10.2019 00:00 sind laut Herausgeber interpoliert; der 1. Januar 2014 steht in der Liste und ist auf der Seite entsprechend markiert.
- Die Einheit steht nicht in der Datei, vermutlich kWh je Viertelstunde; laut Portal prüfen.
- Die Feiertagsnamen stammen nicht aus den Daten: `data/feiertage.json` ist von Hand im Notebook ergänzt (gesetzliche Feiertage Basel-Stadt, Ostern per Gauss-Formel, dazu Heiligabend und Silvester), greift nicht in die Auswahl ein und liefert nur die Namen beim Aufdecken; Tage ohne Eintrag zeigen nur Datum und Wochentag.
- `fetch.py` ist ungetestet.
Offene Punkte: Feiertage an Wochenenden fallen mit den Wochenenden weg; sie hinterlassen in den Daten keine eigene Spur. Kein Tag der Datei hat 100 Intervalle; am Tag der Umstellung auf Winterzeit fehlt die doppelte Stunde. Die Teilspalten sind ab Juli 2020 teilweise gefüllt, werden aber wie zugesichert erst ab 1. September 2020 verwendet. 2026 ist bis 10. September unvollständig. GitHub Pages muss im Repository noch aktiviert werden. Das Notebook liest die CSV notfalls auch unter dem Portalnamen `data/100233.csv`.
