# In dem Modul csv werden Funktionen zum Lesen und Schreiben von CSV-Dateien bereitgestellt. Module werden über das
# Schlüsselwort "import" eingebunden und stehen typischerweise am Anfang der Datei.
import csv

# Die Funktion "open" öffnet die Datei im Textmodus. Auf die Datei können wir über die Variable "csv_file" (Typ: reader object)
# zugreifen. Da die Funktion nur den Dateinamen als Parameter angibt, wird sie im Lesemodus geöffnet, d.h. wir können
# nicht in die Datei schreiben innerhalb des Blocks. Der Funktion "open" können mehrere optionale Parameter mitgegeben
# werden. Damit die die Funktion weiß, welche gemeint sind, müssen diese angegeben werden, indem wir schreiben
# "Parametername=Wert". Hier geben wir an, dass die Datei-Kodierung UTF-8 ist (z.B. für Umlaute wichtig)
with open('produkte.csv', encoding='utf-8') as csv_file:
    # Das Modul "csv" stellt eine Funktion "reader" bereit, die uns beim Einlesen von CSV-Dateien hilft. Als Parameter
    # finden wir in diesem Beispiel die geöffnete Datei csv_file (siehe oben, Typ: reader object) und das Trennzeichen
    # (engl. delimiter). Der erste Paramter muss immer angegeben werden, daher tragen wir ihn direkt ein. Der Funktion
    # "reader" können aber noch mehrere optionale Parameter mitgegeben werden. Damit die die Funktion weiß, welche
    # gemeint sind, müssen diese angegeben werden, indem wir schreiben "Parametername=Wert". Für eine Übersicht der
    # Formatierungsparameter siehe https://docs.python.org/3/library/csv.html#csv-fmt-params
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Wir wollen die einzelnen Zeilen der Datei mitzählen, daher legen wir uns eine Variable an, die wir mit dem Wert
    # 0 initialisieren.
    line_count = 0
    # Die Header-Einträge wollen wir in einer Liste speichern.
    header = []
    # Wir können jetzt in einer Schleife durch die einzelnen Einträge (Zeilen) der CSV-Datei iterieren. Diese stehen
    # dann jeweils als Liste in der Variable "row".
    for row in csv_reader:
        # In der ersten Zeile stehen die Header-Einträge. Diese müssen anders behandelt werden als die einzelnen
        # Datensätze
        if line_count == 0:
            header = row.copy()
            # Die Funktion join fügt alle Elemente der Liste "row" zu einem String zusammen. Der String ", ", für den
            # diese Funktion aufgerufen wird, dient als Trennzeichen.
            print("Die Spaltennamen sind {}".format(", ".join(row)))
            line_count += 1
        else:
            # Hier geben wir ein paar Informationen zum Produkt aus
            print("Das Produkt mit der {0} {1} hat den Preis {2}.". format(header[1], row[1], row[2]))
            line_count += 1
    print("Es wurden {} Zeilen verarbeitet.".format(line_count))