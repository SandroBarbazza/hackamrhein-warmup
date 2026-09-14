Eine Seite, die je Jahr die zehn verbrauchsärmsten Tage im Stromnetz von Basel-Stadt als Balken zeigt; das Datum erscheint erst per Klick. Live: https://derbilla.github.io/hackamrhein-warmup/

Befund: Es sind nicht die Feiertage und Betriebsferien, sondern die Sonntage. 133 der 150 Ranglistenplätze 2012–2026 sind Sonntage, der stillste Tag des Jahres ist in 10 von 15 Jahren der Ostersonntag, sonst Pfingst- oder ein gewöhnlicher Sonntag; Feiertage an Werktagen liegen im Median bei 80 % des Jahresmedians, ein gewöhnlicher Sonntag bei 81 %, Werktage zwischen Weihnachten und Neujahr nur bei 92 %, und kein einziger anderer Werktag erreicht die Liste.

Quelle: Kantonaler Stromverbrauch, Industrielle Werke Basel über Open Data Basel-Stadt (Datensatz 100233), CC BY 4.0, Stand 11. September 2026.

Ablauf: `analysis.ipynb` liest `data/verbrauch.csv`, schreibt `data/stillste-tage.json` und bettet den Inhalt in `index.html` ein, weil Browser `fetch()` aus dem Dateisystem blockieren. Nur Standardbibliothek. `fetch.py` holt die CSV neu.

Einschränkungen:
- Lokal direkt verbrauchter Solarstrom fehlt in den Daten; der Netzbezug ist deshalb untererfasst, über die Jahre zunehmend, was den Langzeitvergleich verzerrt. Die Prozentwerte je Jahr sind davon weniger betroffen.
- Die Zeitstempel 01.01.2014 00:00, 01.11.2015 00:00 und 01.10.2019 00:00 sind laut Herausgeber interpoliert; sie würden im Ergebnis markiert, treffen aber keinen der gelisteten Tage.
- Die Einheit steht nicht in der Datei, vermutlich kWh je Viertelstunde; laut Portal prüfen.
- Die Feiertagsliste für den Befund (Basel-Stadt, inkl. Ostern per Gauss-Formel) ist von Hand im Notebook ergänzt; die Seite zeigt keine Feiertagsnamen, nur Datum und Wochentag.
- `fetch.py` ist ungetestet.
Offene Punkte: Kein Tag der Datei hat 100 Intervalle; am Tag der Umstellung auf Winterzeit fehlt die doppelte Stunde (96 statt 100). Die Teilspalten sind ab Juli 2020 teilweise gefüllt, werden aber wie zugesichert erst ab 1. September 2020 verwendet. 2026 ist bis 10. September unvollständig. GitHub Pages muss im Repository noch aktiviert werden (Branch main, Wurzelverzeichnis).
