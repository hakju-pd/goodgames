# GoodGames Projektanforderungen

Implementiere eine Spielebibliothek in der getrackt wird, welche Spiele von dir 
dieses Jahr gespielt wurden. 
Das Frontend ist bereits im FIle "goodgames.py" implementiert.

Um das Projekt zu starten, installiere zuerst die notwendigen Bibliotheken:
```bash
pip install tk
```
Danach kannst du das Projekt starten indem du goodgames.py ausführst:

Im Projekt müssen alle Pflichtaufgaben (50 Punkte) implentiert werden um das Projekt positiv abzuschließen.

Um dann eine bessere Note zu erhalten, kannst du zusätzlich noch optionale Aufgaben implementieren.

Die Bewertung sieht dabei folgendermaßen aus: 

 > 0 - 40 Punkte: 5 <br>
 > 41 - 50 Punkte: 4 <br>
 > 51 - 60 Punkte: 3 <br>
 > 61 - 70 Punkte: 2 <br>
 > mehr als 71 Punkte: 1 <br>

Die Punkte können sich beim Abgeben des Projekts noch ändern, wenn die Aufgaben nicht korrekt implementiert sind.

Für das Projekt können alle Hilfsmittel verwendet werden, jedoch wird bei der Abgabe überprüft, ob die Aufgaben selbstständig gelöst wurden.


## Pflichtaufgaben (insgesamt 40 Punkte)

Die Pflichtaufgaben sind im Code mit TODO: markiert. Füge dort den benötigten Code ein.

1. Spiele in CSV-Datei speichern** (10 Punkte)
   - Implementiere die Funktion "save_to_csv" in backend.py.
   - Diese Funktion wird jedes mal aufgerufen, wenn ein Spiel hinzugefügt wird.
   - Die Funktion soll die Spieleliste mit einer CSV-Datei synchronisieren.

2. Spiele aus CSV-Datei laden** (10 Punkte)
   - Implementiere die Funktion "load_from_csv" in backend.py.
   - Diese Funktion wird jedes mal aufgerufen, wenn das Programm gestartet wird.
   - Die Funktion soll die Spieleliste mit einer CSV-Datei synchronisieren.

3. **Duplikaterkennung** (5 Punkte)
   - Überprüfung, ob ein Spiel bereits in der Liste existiert
   - Verhindern von Mehrfacheinträgen des gleichen Spiels

4. **Fehlerbehandlung im Backend** (10 Punkte)
   - Implementierung von try/catch-Blöcken für robuste Fehlerbehandlung
   - Es sollen bei den CSV Zugriffen FileNoteFound Errors und bei den anderen Funktionen ValueError abgefangen werden

5. **Backend Tests** (5 Punkte)
   - Erstelle mindestens 3 weitere sinnvolle Testfälle für den Backend-Code
   - Tests müssen verschiedene Szenarien und Randfälle abdecken

## Optionale Aufgaben (insgesamt 70 Punkte)

1. **Suchfunktion nach Namen** (10 Punkte)
   - Implementierung einer Spielesuche nach Titel
   - Erstelle eine zweite Suchleiste, wie die des Filters, die nach dem Namen des Spiels sucht

3. **Trophäen-System** (5 Punkte)
   - Tracking von Spielefortschritt durch Trophäen
   - Für jedes Spiel sollte ein Trophäenfortschritt von 0-100% gespeichert werden
   - In den Spieldetails sollen die Prozente angezeigt werden

4. **Logo Integration** (5 Punkte)
   - Erstelle ein eigenes Logo für die Anwendung
   - Platziere es auf der Hauptseite

5. **KI-gestützte Reviews** (20 Punkte)
   - Automatische Generierung von Reviews
   - Wenn ein Button gedrückt wird soll mittels KI ein neues Review generiert werden
   - Dafür soll Googles Gemini API verwendet werden
   - https://ai.google.dev/gemini-api/docs/get-started/tutorial?hl=de&lang=python

6. **Statistiken** (10 Punkte)
   - Implementiere einen neuen Tab, der Statistiken über die gespielten Spiele anzeigt
   - Dabei soll folgendes angezeigt werden:
     - Anzahl der gespielten Spiele
     - Durchschnittliche Bewertung
     - Anzahl der Spiele pro Platform

7. **Genres** (5 Punkte)
   - Implementiere eine Genre-Kategorie für die Spiele
   - Jedes Spiel soll ein Genre haben
   - Wenn ein neues Spiel hinzugefügt wird, soll auch das Genre mit Dropdown ausgewählt werden 
   - Folgende Genres sollen zur Auswahl stehen: Action, Adventure, RPG, Simulation, Strategy, Sports, Puzzle

## Gesamtpunktzahl
- Pflichtaufgaben: 50 Punkte
- Optionale Aufgaben: 70 Punkte
- Maximal erreichbare Punktzahl: 120 Punkte