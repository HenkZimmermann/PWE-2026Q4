INSERT INTO Roles (role_id, name, permissions) VALUES
(1, 'Admin', ARRAY[
    'users.manage',
    'roles.manage',
    'groups.manage',
    'threads.delete',
    'comments.delete'
]),
(2, 'Moderator', ARRAY[
    'threads.delete',
    'comments.delete',
    'groups.manage'
]),
(3, 'User', ARRAY[
    'threads.create',
    'comments.create',
    'threads.vote',
    'comments.vote'
])
ON CONFLICT DO NOTHING;

INSERT INTO Users (
    user_id, username, email, password_hash, role_id
) VALUES
(1, 'admin', 'admin@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 1),
(2, 'max_mustermann', 'max@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3),
(3, 'lisa_dev', 'lisa@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3),
(4, 'tom_gaming', 'tom@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3),
(5, 'anna_mod', 'anna@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 2),
(6, 'sarah_design', 'sarah@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3),
(7, 'ben_python', 'ben@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3),
(8, 'mia_student', 'mia@example.com', '$2b$12$gz9dyVPiDxaJ9d6ap1rYyuCWucIj3Wllk7y5YsBo1lIkoRR9aiIpO', 3)
ON CONFLICT DO NOTHING;


INSERT INTO Groups (
    group_id, group_name, category, members,
    system_created, description
) VALUES
(1, 'Python Community', 'Programmierung', 120, TRUE,
 'Fragen, Tipps und Projekte rund um Python.'),

(2, 'Web Development', 'Technologie', 85, TRUE,
 'Frontend, Backend, APIs und moderne Webtechnologien.'),

(3, 'Gaming Lounge', 'Gaming', 210, FALSE,
 'Spieleempfehlungen, Gaming-News und Diskussionen.'),

(4, 'University Life', 'Studium', 64, FALSE,
 'Lerntipps, Prüfungen und Erfahrungen aus dem Studium.'),

(5, 'Design & UX', 'Kreativität', 47, FALSE,
 'UI-Design, Prototypen und User Experience.'),

(6, 'Hardware & Homelab', 'Technologie', 93, FALSE,
 'Server, Netzwerke, Container und Hardware.')
ON CONFLICT DO NOTHING;

INSERT INTO Threads (
    thread_id, created_at, message,
    user_id, votes, group_id, title
) VALUES
(1, '2026-10-20 09:30:00',
 $md$Ich lerne gerade Python und möchte nach den ersten Übungen ein kleines Projekt bauen, das ich im Alltag tatsächlich benutze. Eine To-do-Liste wäre naheliegend, aber ein Programm für meine Ausgaben fände ich auch spannend.

**Mein Ziel:** In einer Woche etwas haben, das ich im Terminal starten und am nächsten Tag weiterbenutzen kann. Gibt es ein Projekt, bei dem man gut mit einer kleinen Version anfangen kann?$md$,
 2, 15, 1, 'Gute Python-Projekte für Anfänger'),

(2, '2026-10-21 14:15:00',
 'Ich suche ein Framework für meine erste REST-API. Was würdet ihr empfehlen?',
 3, 8, 2, 'Welches Webframework ist empfehlenswert?'),

(3, '2026-10-22 18:45:00',
 'Was spielt ihr aktuell am liebsten? Ich suche etwas Neues für den Feierabend.',
 4, 22, 3, 'Spieleempfehlungen für den Herbst'),

(4, '2026-10-23 11:00:00',
 'Wie organisiert ihr euch während der Prüfungsphase?',
 8, 12, 4, 'Tipps für eine stressfreie Prüfungsphase'),

(5, '2026-10-24 16:20:00',
 $md$Ich möchte für unsere Lerngruppe eine kleine REST-API entwickeln. Man soll Aufgaben anlegen, abhaken und nach Kurs filtern können. Den ersten Entwurf habe ich schon lokal, aber bei den Schnittstellen bin ich mir noch unsicher.

- Welche Fehler sollte ich von Anfang an abfangen?
- Wie würdet ihr die Rückgabe für eine Aufgabe gestalten, die es nicht gibt?
- Ab wann lohnt es sich, Tests für die API zu schreiben?

Das Projekt soll überschaubar bleiben. Mich interessiert vor allem, welche Entscheidungen euch am Anfang später Arbeit erspart haben.$md$,
 2, 19, 2, 'Die erste REST-API entwickeln'),

(6, '2026-10-25 13:10:00',
 'Welche kostenlosen Tools verwendet ihr für UI-Prototypen?',
 6, 7, 5, 'Kostenlose Tools für UI-Design'),

(7, '2026-10-26 20:00:00',
 'Welche Vorteile haben Docker-Container gegenüber virtuellen Maschinen?',
 7, 11, 6, 'Docker oder virtuelle Maschinen?'),

(8, '2026-10-27 08:50:00',
 'Habt ihr Empfehlungen für gute Lernressourcen zu Datenbanken?',
 4, 5, 4, 'Datenbanken verständlich lernen'),

(9, '2026-10-27 15:40:00',
 'Ich habe Probleme mit verschachtelten Kommentaren in meiner Datenbank.',
 3, 6, 2, 'Wie speichert man Kommentar-Antworten?'),

(10, '2026-10-28 10:15:00',
 'Was sollte ein gutes Community-Forum unbedingt bieten?',
 5, 9, 5, 'Features für eine moderne Community'),

(11, '2026-10-29 17:45:00',
 $md$Ich exportiere meine Ausgaben als CSV und möchte pro Monat sehen, wie viel für Lebensmittel, Mobilität und Freizeit zusammenkommt. Die Datei kann ich schon einlesen. Schwieriger wird es, wenn eine Kategorie fehlt oder ein Betrag leer ist.

Am Ende hätte ich gern eine kurze Zusammenfassung im Terminal und eine Liste der Zeilen, die ich nachsehen muss. Würdet ihr ungültige Werte beim Einlesen abfangen oder erst anschließend prüfen?$md$,
 7, 0, 1, 'Ausgaben aus einer CSV zusammenfassen'),

(12, '2026-10-30 19:10:00',
 $md$In meinem React-Projekt haben wir bisher fast alles mit `useState` gelöst. Beim Filtern von Beiträgen speichern wir jetzt aber sowohl die ursprüngliche Liste als auch das gefilterte Ergebnis. Nach einem Update bleiben manchmal alte Treffer stehen.

**Mein Verdacht:** Wir halten denselben Inhalt an zwei Stellen vor. Würdet ihr die sichtbare Liste direkt beim Rendern berechnen? Mich interessiert auch, ab wann ihr euch über die Kosten der Berechnung Gedanken macht.$md$,
 3, 0, 2, 'Gefilterte Listen in React verwalten'),

(13, '2026-11-01 18:20:00',
 'Wir suchen zu dritt ein Koop-Spiel für einen festen Abend pro Woche. Zwei von uns spielen regelmäßig, die dritte Person hat wenig Erfahrung mit Controller-Steuerung. Rätsel oder gemeinsames Bauen wären ideal. Wichtig wäre uns auch, dass man nach einer Woche Pause wieder schnell reinkommt. Was hat bei euch als gemischte Gruppe gut funktioniert?',
 4, 0, 3, 'Koop-Spiele für drei Personen'),

(14, '2026-11-03 12:30:00',
 $md$In unserem Gruppenprojekt stehen Aufgaben in zwei Chats und einem geteilten Dokument. Wenn jemand nicht im Meeting war, dauert es ewig, bis klar ist, was als Nächstes ansteht.

Für die nächsten zwei Wochen wollen wir ein kleines Board testen:

1. Jede Aufgabe bekommt eine zuständige Person.
2. Blockaden werden direkt an der Aufgabe festgehalten.
3. Entscheidungen landen mit Datum im gemeinsamen Dokument.

Wie haltet ihr so ein Board aktuell, ohne im Treffen jede Karte einzeln durchzugehen?$md$,
 8, 0, 4, 'Aufgaben im Gruppenprojekt besser verteilen'),

(15, '2026-11-05 15:30:00',
 $md$Ich überarbeite ein Formular für eine Veranstaltungsanmeldung. Manche Fehlermeldungen passen direkt unter das Feld, andere betreffen zwei Felder gleichzeitig, etwa ein Enddatum vor dem Startdatum.

Mir wäre wichtig, dass man nach dem Absenden **schnell zur richtigen Stelle zurückfindet**. Wo platziert ihr solche Fehlermeldungen, wenn mehrere Felder zusammenhängen?$md$,
 6, 0, 5, 'Fehlermeldungen in längeren Formularen'),

(16, '2026-11-06 20:15:00',
 $md$Mein kleiner Heimserver läuft seit einem halben Jahr. Ein paar Dienste haben mittlerweile Daten, deren Verlust ich wirklich merken würde: Fotos, Notizen und die Konfigurationsdateien meiner Container.

Ich würde zuerst einen Ordner auf eine externe Platte sichern und danach testweise in ein leeres Verzeichnis zurückspielen. Wie habt ihr geprüft, dass eure Sicherung auch auf einem frisch eingerichteten Rechner funktioniert?$md$,
 7, 0, 6, 'Erster Wiederherstellungstest fürs Homelab'),

(17, '2026-11-08 10:40:00',
 $md$Ich lade Einstellungen für ein kleines Python-Programm aus einer Datei. Wenn die Datei fehlt, funktioniert der Standardwert. Wenn die Datei da ist, aber einen Tippfehler enthält, läuft das Programm gerade ebenfalls mit dem Standardwert weiter. Das habe ich erst gemerkt, als es in den falschen Ordner geschrieben hat.

Würdet ihr bei einer ungültigen Konfiguration mit einer verständlichen Meldung abbrechen oder trotzdem versuchen, etwas Sinnvolles zu machen?$md$,
 7, 0, 1, 'Umgang mit fehlerhaften Einstellungen'),

(18, '2026-11-10 16:50:00',
 $md$Wir haben eine Suche mit einer gruppenübergreifenden Ergebnisliste. Beim Klick auf einen Treffer und anschließendem Zurückgehen fehlen mir manchmal Suchbegriff und ausgewählte Gruppe.

Ich würde beide Werte als URL-Parameter speichern, etwa `?q=python&group=1`. Damit könnte man die Suche auch weitergeben. Legt ihr die Seite der Trefferliste ebenfalls in die URL oder speichert ihr die Position auf andere Weise?$md$,
 2, 0, 2, 'Suchfilter beim Zurückgehen behalten'),

(19, '2026-11-12 21:05:00',
 'Ich habe am Wochenende zum ersten Mal einen eigenen kleinen Level gebaut. Meine Testspieler haben an einer Abzweigung alle denselben Gang übersehen. Der Eingang lag im Schatten, während der falsche Weg gut ausgeleuchtet war. Ich probiere jetzt, die beiden Wege anders auszuleuchten. Woran merkt ihr beim Testen, ob ein optionaler Weg zu schwer zu entdecken ist?',
 4, 0, 3, 'Wie führt ihr Spieler durch eigene Levels?'),

(20, '2026-11-15 14:00:00',
 $md$In zwei Wochen habe ich meine erste mündliche Prüfung in Datenbanken. SQL-Aufgaben kann ich am Rechner lösen, aber wenn ich erklären soll, warum ich einen Join verwende, springe ich gedanklich gleich zum Ergebnis.

Ich will die nächsten Tage jeden Abend ein Beispiel laut erklären, etwa **wann ein LEFT JOIN zusätzliche Zeilen sichtbar macht**. Habt ihr Aufgaben, die sich zum Üben mit einer zweiten Person eignen?$md$,
 8, 0, 4, 'Mündliche Prüfung in Datenbanken vorbereiten'),

(21, '2026-11-18 17:25:00',
 $md$Für unseren Prototyp gibt es bisher nur eine Desktop-Ansicht. Beim ersten Test am Handy ist mir aufgefallen, dass die Karten kaum Platz für längere Titel lassen und die Filter zu viel Höhe einnehmen.

Ich skizziere gerade eine Ansicht mit einer Spalte und teste sie mit echten Beispieltexten. Welche Stellen schaut ihr euch bei so einem ersten mobilen Durchgang zuerst an?$md$,
 6, 0, 5, 'Desktop-Prototyp auf dem Handy testen'),

(22, '2026-11-22 19:35:00',
 $md$Mein Heimserver steht im Arbeitszimmer und die Lüfter drehen nachts merklich hoch. Ich habe Temperatur und Auslastung mitgeschrieben. Die Ausschläge fallen ziemlich genau mit dem täglichen Fotoimport zusammen.

Als Erstes möchte ich **den Import zeitlich verschieben** und die Werte noch ein paar Tage beobachten. Welche Messwerte habt ihr bei ähnlichen Problemen hilfreich gefunden?$md$,
 7, 0, 6, 'Nächtliche Last auf dem Heimserver eingrenzen')
ON CONFLICT DO NOTHING;

INSERT INTO Comments (
    comment_id, thread_id, parent_comment_id,
    message, votes, user_id, created_at
) VALUES

(1, 1, NULL,
 'Ein To-do-Programm ist ein guter Einstieg. Danach kannst du eine kleine API bauen.',
 6, 3, '2026-10-20 10:00:00'),

(2, 1, 1,
 'Danke! Ich werde zuerst das To-do-Programm ausprobieren.',
 2, 2, '2026-10-20 10:15:00'),

(3, 1, NULL,
 'Ich würde zusätzlich ein kleines Web-Scraping-Projekt empfehlen.',
 4, 7, '2026-10-20 11:30:00'),

(4, 2, NULL,
 $md$Für Python würde ich **FastAPI** ausprobieren. Bei meinem ersten Projekt hat mir vor allem die automatisch erzeugte Dokumentation geholfen. Unter `/docs` konnte ich direkt sehen, welche Felder erwartet werden, und einen Beispielaufruf testen.$md$,
 9, 2, '2026-10-21 15:00:00'),

(5, 2, 4,
 'Sehe ich auch so. Gerade für REST-APIs ist FastAPI sehr angenehm.',
 3, 3, '2026-10-21 15:30:00'),

(6, 2, 4,
 'Django ist auch eine gute Wahl, wenn man viele Funktionen direkt mitbringen möchte.',
 5, 7, '2026-10-21 16:00:00'),

(7, 3, NULL,
 'Ich spiele aktuell Baldur’s Gate 3 und kann es sehr empfehlen.',
 7, 6, '2026-10-22 19:00:00'),

(8, 3, NULL,
 'Wenn du etwas mit Freunden suchst, probiere ein Koop-Spiel aus.',
 4, 4, '2026-10-22 19:20:00'),

(9, 4, NULL,
 'Ich plane jeden Tag drei Lernblöcke und mache dazwischen Pausen.',
 8, 2, '2026-10-23 12:00:00'),

(10, 4, 9,
 'Die Pomodoro-Technik hilft mir auch, konzentriert zu bleiben.',
 3, 8, '2026-10-23 12:20:00'),

(11, 4, 10,
 'Ich nutze zusätzlich Karteikarten für Definitionen und Fachbegriffe.',
 2, 5, '2026-10-23 12:45:00'),

(12, 5, NULL,
 'Achte auf passende HTTP-Statuscodes, Validierung und eine klare Struktur.',
 10, 5, '2026-10-24 17:00:00'),

(13, 5, 12,
 'Und vergiss nicht, Fehlerfälle und Berechtigungen zu testen.',
 5, 3, '2026-10-24 17:15:00'),

(14, 6, NULL,
 'Figma ist für Prototypen und erste UI-Entwürfe sehr praktisch.',
 6, 2, '2026-10-25 14:00:00'),

(15, 6, 14,
 'Für einfache Wireframes kann man auch Penpot ausprobieren.',
 3, 6, '2026-10-25 14:30:00'),

(16, 7, NULL,
 'Container sind ressourcenschonend, weil sie den Kernel des Hosts teilen.',
 8, 3, '2026-10-26 20:30:00'),

(17, 7, 16,
 'VMs sind dafür praktisch, wenn man unterschiedliche Betriebssysteme benötigt.',
 4, 7, '2026-10-26 20:45:00'),

(18, 8, NULL,
 'Die PostgreSQL-Dokumentation ist ein guter Startpunkt.',
 5, 5, '2026-10-27 09:00:00'),

(19, 9, NULL,
 'Du kannst parent_comment_id als Fremdschlüssel auf comment_id verwenden.',
 7, 7, '2026-10-27 16:00:00'),

(20, 9, 19,
 'Genau so ist es bei mir umgesetzt. NULL bedeutet, dass es ein Hauptkommentar ist.',
 3, 3, '2026-10-27 16:20:00'),

(21, 9, 20,
 'Für die Anzeige musst du die Antworten dann rekursiv oder über mehrere Abfragen laden.',
 4, 2, '2026-10-27 16:45:00'),

(22, 10, NULL,
 'Eine gute Suche und sinnvolle Kategorien sind meiner Meinung nach besonders wichtig.',
 6, 6, '2026-10-28 11:00:00'),

(23, 10, 22,
 'Ich würde außerdem Benachrichtigungen für Antworten einbauen.',
 4, 5, '2026-10-28 11:20:00'),

(24, 11, NULL,
 $md$Ich würde beim Einlesen festhalten, welche **Zeilennummer** zu einem fehlerhaften Wert gehört. Dann kannst du die gültigen Zeilen zusammenfassen und am Ende anzeigen, was fehlt. Bei einer unbekannten Kategorie würde ich den Betrag unter „Sonstiges“ zählen, sofern der Betrag selbst gültig ist.$md$,
 4, 3, '2026-10-29 18:10:00'),

(25, 11, 24,
 'Die Zeilennummer ist eine gute Idee. Bisher habe ich nur den Betrag ausgegeben und musste in der Datei danach suchen.',
 1, 7, '2026-10-29 18:40:00'),

(26, 11, NULL,
 $md$Bei Geldbeträgen lohnt sich ein Blick auf `Decimal`. Ich würde auch gleich einen Testfall mit Komma als Dezimaltrennzeichen anlegen, wenn dein Export deutsche Zahlenformate verwendet.$md$,
 3, 2, '2026-10-30 09:20:00'),

(27, 12, NULL,
 $md$Für eine kleine Liste würde ich die sichtbaren Einträge direkt aus der Liste und dem Suchbegriff ableiten:

```jsx
const visibleThreads = threads.filter((thread) =>
    thread.title.toLowerCase().includes(query.toLowerCase())
);
```

Dann hängt das Ergebnis bei jedem Rendern von den aktuellen Werten ab. Ob die Berechnung zu teuer wird, würde ich erst mit realistischen Daten messen.$md$,
 5, 2, '2026-10-30 19:45:00'),

(28, 12, 27,
 'Das war es! Nach dem Anlegen eines Beitrags habe ich nur die ursprüngliche Liste aktualisiert.',
 2, 3, '2026-10-30 20:15:00'),

(29, 13, NULL,
 'Bei uns hat Unrailed! zu dritt gut funktioniert. Die Aufgaben lassen sich spontan aufteilen. Eine Person baut Gleise, die anderen sammeln Material oder halten den Weg frei.',
 4, 6, '2026-11-01 19:00:00'),

(30, 13, NULL,
 'Trine 4 hat bei uns gut gepasst. Man kann bei vielen Rätseln gemeinsam überlegen und ausprobieren, bevor jemand springen oder kämpfen muss.',
 3, 3, '2026-11-02 10:40:00'),

(31, 14, NULL,
 $md$Wir fragen im Meeting nur: **Was ist blockiert und wer kann helfen?** Alles andere aktualisieren wir vorab. Bei Aufgaben, die länger als ein paar Tage offen sind, schauen wir gemeinsam, ob man sie kleiner schneiden kann.$md$,
 6, 5, '2026-11-03 13:15:00'),

(32, 14, 31,
 'Wie erinnert ihr euch ans Aktualisieren vor dem Treffen? Bei uns fällt das oft erst auf, wenn wir schon im Termin sind.',
 2, 8, '2026-11-03 13:45:00'),

(33, 14, 32,
 'Der Link steht im Kalendereintrag. Wir nehmen uns vor dem Termin zwei Minuten für das Board. Wenn eine Karte aktuell ist, gibt es auch nichts zu ergänzen.',
 1, 5, '2026-11-03 14:05:00'),

(34, 15, NULL,
 $md$Bei eurem Beispiel würde ich die Meldung am Enddatum anzeigen, weil sich der Fehler dort meistens beheben lässt. Eine mögliche Formulierung:

> Das Enddatum muss am oder nach dem Startdatum liegen.

Nach dem Absenden kann oben eine kurze Zusammenfassung auf das Feld verlinken. Bei längeren Formularen spart das viel Scrollen.$md$,
 5, 3, '2026-11-05 16:10:00'),

(35, 15, 34,
 'Ich teste den Sprung zum Feld auch einmal nur mit der Tastatur. Bei unserem alten Formular ist man beim Scrollen zwar am richtigen Feld gelandet, aber der Fokus war noch auf dem Absende-Button.',
 3, 6, '2026-11-05 17:00:00'),

(36, 16, NULL,
 $md$Ich habe für meinen Test einen alten Laptop genommen und nur die Sicherung und meine Notizen verwendet. Erst dabei ist mir aufgefallen, dass ich die Konfiguration gesichert hatte, aber die Daten eines Dienstes in einem anderen Verzeichnis lagen.

Prüf beim Wiederherstellen ruhig eine konkrete Sache, etwa ob sich eine ältere Notiz öffnen lässt. Dass ein Dienst startet, sagt noch wenig darüber aus, ob seine Daten vollständig da sind.$md$,
 6, 4, '2026-11-06 21:10:00'),

(37, 16, 36,
 'Ich fange mit den Notizen an. Da kann ich schnell sehen, ob Anhänge und ältere Einträge wirklich dabei sind.',
 2, 7, '2026-11-07 09:30:00'),

(38, 17, NULL,
 $md$In deinem Fall würde ich **mit einer konkreten Fehlermeldung abbrechen**. Gib den Dateipfad und den Namen der ungültigen Einstellung aus. Bei einer fehlenden Datei ist ein bewusst gewählter Standardwert okay, aber wenn ich einen Ausgabeordner angegeben habe, möchte ich erfahren, dass er nicht übernommen wurde.$md$,
 4, 3, '2026-11-08 11:15:00'),

(39, 17, NULL,
 'Ich würde die Einstellungen komplett prüfen, bevor das Skript die erste Datei schreibt. Dann lässt sich der Fehler korrigieren, ohne vorher halbfertige Ausgaben einsammeln zu müssen.',
 2, 2, '2026-11-08 12:00:00'),

(40, 18, NULL,
 $md$Ich lege bei klassischer Seitennavigation auch `page` in die URL. Ändert sich der Suchbegriff, setze ich die Seite auf 1 zurück. Die Scrollposition ist für mich etwas anderes: Die brauche ich beim Zurückgehen, aber selten in einem geteilten Link.$md$,
 5, 3, '2026-11-10 17:30:00'),

(41, 18, 40,
 'Das Zurücksetzen beim Filterwechsel hatte ich nicht bedacht. Sonst kann man leicht auf einer leeren Seite landen, obwohl es Treffer gibt.',
 2, 2, '2026-11-10 18:00:00'),

(42, 19, NULL,
 'Ich würde erst mal beobachten, wohin die Kamera zeigt, wenn die Person an der Kreuzung ankommt. Vielleicht ist der Eingang bei geradem Blick sichtbar, aber alle kommen leicht nach rechts gedreht aus der vorherigen Passage.',
 4, 6, '2026-11-13 08:45:00'),

(43, 19, 42,
 'Hab mir die Aufnahme nochmal angesehen. Der Eingang liegt tatsächlich direkt hinter der linken Schulter, wenn man aus der Passage kommt.',
 2, 4, '2026-11-13 18:20:00'),

(44, 20, NULL,
 $md$Nimm zwei kleine Tabellen und sag zuerst laut, welche Zeilen du im Ergebnis erwartest. Eine Person ohne passende Buchung ist dafür ein gutes Beispiel: Beim `LEFT JOIN` bleibt die Person enthalten und die Spalten der Buchung sind leer.

Danach kann die zweite Person eine Zeile in der Beispieltabelle ändern und dich fragen, wie sich die Ausgabe verändert.$md$,
 5, 5, '2026-11-15 15:00:00'),

(45, 20, NULL,
 'Was mir geholfen hat: dieselbe Abfrage einmal einem Kommilitonen erklären und einmal jemandem ohne SQL-Kenntnisse. Bei der zweiten Runde merkt man schnell, welche Begriffe man nur auswendig gelernt hat.',
 4, 2, '2026-11-15 17:40:00'),

(46, 21, NULL,
 $md$Ich teste zuerst mit **langen Titeln und großen Systemschriften**, dann mit dem längsten Filterwert. Im Prototyp hat bei uns alles gepasst, bis aus „Design“ plötzlich „Softwarearchitektur und Datenbanken“ wurde.$md$,
 3, 3, '2026-11-18 18:05:00'),

(47, 21, 46,
 'Mit größerer Schrift sind die beiden Filter bei mir direkt umgebrochen. Ich lasse die Filter jetzt untereinander stehen, sobald die Beschriftung nicht mehr reinpasst.',
 2, 6, '2026-11-18 19:20:00'),

(48, 22, NULL,
 $md$Miss zusätzlich zur CPU-Temperatur nach Möglichkeit die **Lüfterdrehzahl** und notier die Dauer der Ausschläge. Bei mir war ein kurzer Anstieg beim Start eines Imports gut hörbar, auch wenn die Durchschnittstemperatur über die ganze Nacht fast gleich blieb.$md$,
 4, 4, '2026-11-22 20:10:00'),

(49, 22, 48,
 'Die Drehzahl kann ich auslesen. Ich nehme sie in die Messung auf und vergleiche danach zwei Nächte mit und zwei ohne Import.',
 1, 7, '2026-11-22 20:45:00'),

(50, 1, NULL,
 $md$Für eine erste Version reicht eine Liste mit drei Befehlen: hinzufügen, anzeigen und abhaken. Speicher die Einträge in einer Datei und starte das Programm danach neu. Wenn alles noch da ist, hast du schon etwas Fertiges, auf dem du aufbauen kannst.$md$,
 3, 8, '2026-10-21 09:00:00')

ON CONFLICT DO NOTHING;


SELECT setval(
    pg_get_serial_sequence('roles', 'role_id'),
    (SELECT MAX(role_id) FROM Roles)
);

SELECT setval(
    pg_get_serial_sequence('users', 'user_id'),
    (SELECT MAX(user_id) FROM Users)
);

SELECT setval(
    pg_get_serial_sequence('groups', 'group_id'),
    (SELECT MAX(group_id) FROM Groups)
);

SELECT setval(
    pg_get_serial_sequence('threads', 'thread_id'),
    (SELECT MAX(thread_id) FROM Threads)
);

SELECT setval(
    pg_get_serial_sequence('comments', 'comment_id'),
    (SELECT MAX(comment_id) FROM Comments)
);

INSERT INTO votes (user_id, thread_id) VALUES
(2, 1),
(3, 1),
(7, 1),
(2, 2),
(5, 2),
(6, 3),
(2, 3),
(3, 3),
(8, 4),
(2, 4),
(5, 5),
(7, 5),
(3, 5),
(2, 6),
(6, 6),
(3, 7),
(7, 7),
(2, 7),
(5, 8),
(8, 8),
(7, 9),
(2, 9),
(6, 10),
(5, 10),
(3, 11),
(2, 11),
(2, 12),
(7, 12),
(6, 13),
(3, 13),
(5, 14),
(2, 14),
(3, 15),
(5, 15),
(4, 16),
(2, 16),
(3, 17),
(2, 17),
(3, 18),
(7, 18),
(6, 19),
(3, 19),
(5, 20),
(2, 20),
(3, 21),
(5, 21),
(4, 22),
(3, 22)
ON CONFLICT DO NOTHING;


INSERT INTO member_of (user_id, group_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 4),
(3, 1),
(3, 2),
(3, 5),
(4, 3),
(4, 6),
(5, 1),
(5, 2),
(5, 4),
(5, 5),
(6, 4),
(6, 5),
(6, 2),
(7, 1),
(7, 2),
(7, 6),
(8, 4),
(8, 1)
ON CONFLICT DO NOTHING;


INSERT INTO follows (user_id, followed_user_id) VALUES
(2, 3),
(2, 5),
(2, 7),
(3, 2),
(3, 7),
(3, 6),
(4, 6),
(4, 7),
(5, 2),
(5, 3),
(5, 6),
(6, 3),
(6, 5),
(7, 2),
(7, 3),
(7, 5),
(8, 2),
(8, 5)
ON CONFLICT DO NOTHING;
