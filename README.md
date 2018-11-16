# BigData
Die Big Data Install Textdatei enthält alle zur Erstellung einer lauffähigen Systemumgebung benötigten Befehle für ein Ubuntu Version 18.04 System.
Vor der Ausführung des Main Jobs muss die kettle.properties Datei auf dem System durch die kettle.properties Datei aus diesem Projekt ausgetauscht werden.

# main.kjb
Die main erstellt Jahresauswertungen auf Basis der Rohdaten von www.nyc.gov
Zum aufruf muss der Parameter load_year übergeben werden, z.B. "-param:load_year=2018"
Der Main Job (main.kjb) stößt die folgenden Jobs in entsprechender Reihenfolge an:
- download.kjb
- import.kjb
- Create Partition and Calculate.kjb
- export_all.kjb
- Cleanup (Delete Import Directory)

Das Ergebnis des Jobs sind die zwei Dateien:
- export_yellow.xls
- export_green.xls

Diese enthalten die berechneten KPIs.

# download.kjb:
Erstell Import Verzeichnisse für den Crawler.
Prüft, ob Verzeichnisse leer sind und leert diese gegebenenfalls.
Startet Crawler zum Download der CSV Dateien #An dieser Stelle muss der vollständige oder der demo Crawler eingefügt werden

# import.kjb:
Prüft, ob alle Dateien heruntergeladen wurden.
Erstellt HDFS Directories für Yellow und Green.
Verschiebt CSVs in entsprechende HDFS Directories.
Erstellt Tabellen und importiert Rohdaten.

# Create Partition and Calculate
Erstellt dynamisch Partitionierte Tabellen
Berechnet KPIs und fügt diese in Tabellen ein.

# export_all.kjb
Startet Transformation to_excel.ktr

# to_excel.ktr
Führt SQL Abfrage durch und speichert KPIs in Excel

# Crawler_demo.py
Python Crawler zur Demonstration. Funktioniert wie Crawler.py, aber läd nur die ersten zwei Monate des Jahres herunter.

# Crawler.py
Python Crawler der mit den Parametern Datenbasis (Bsp. "yellow") und Jahres Anzahl (Bsp. 2016) alle CSV Dateien des entsprechenden Jahres von www.nyc.gov herunterläd.


