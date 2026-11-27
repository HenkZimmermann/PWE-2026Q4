# KI Engineering Journal

Hier werden Beiträge und Einsätze von künstlicher Intelligenz in diesem Projekt dokumentiert. Das Projekt hat das Ziel,
weitestgehend von *Menschen* entwickelt zu werden und **KI** nur in unterstützender Rolle zu verwenden, beispielsweise
zur schnellen Recherche und Analyse von Fehlern. 

## KI Einsätze

#### Modelle / Dienste
- [ChatGPT](https://chatgpt.com/)
- [Grok](https://grok.com/)

### Design und Styling

- "Gib mir ein Farbschema für ein moderne Website für CSS"
- "Wie kann ich diesen CSS Code besser gestalten [...]"
- "Wie kriege ich eine feste breite zwischen diesen beiden Elementen: [...]"
- "Wie mache ich eine Tabelle in Markdown"
- "Wieso ist der Text im Button nicht richtig zentriert [...]"
- "Wie kann ich den angehängten css code verbessern und einfacher machen"
- "Mach Vorschläge wie die Styles bis jetzt einheitlicher und generell besser für UX werden"
- "Designe für das Projekt ein Logo/Icon"
- "Erstelle mir basieren auf dem Dashboard Design, ein Login Design mit CSS"
- "Ich habe in der Sidebar diese Elemente [...] zum Anzeigen der Userinfos hinzugefügt. Kannst du mir die CSS dafür erweitern?"
- "Erstelle mir für meine User Statistiken noch ein passendes CSS zum designen."
- "Anbei ist meine .JSX Datei für das bearbeiten zum Anzeigen des Userprofils inkl. Bearbeitungs Dialog. Scheribe dafür eine CSS Datei."
- "Wie bekomme ich Benutzername, E-Mail, Rolle und User-ID gleichmäßig nebeneinander in eine Card, sodass unter jeder Beschriftung der jeweilige Wert steht? Die Überschrift ‚Mein Profil‘ soll mittig über der Card stehen."

### Debugging von schweren Fehlern

- "Ich versuche [...] zu installieren und kriege diesen Fehler: [...]"
- "React wirft diesen Fehler [...]"
- "Meine React App findet die neu hinzugefügten JS packages nicht"
### Entwicklung (Dashboard)

- "Wie kann ich das aktuelle Datum in jsx verarbeiten"
- "JSX formular bauen, mach mir dazu eine Übersicht"
- "Wieso klappt diese SQL Abfrage nicht? [...] Kriege Fehler [...]"
- "Guck mal hier über die async logik, wie mache ich das hier mit den Signals? [...]"
- "Wie kann ich Elemente aus dem Backend live nachladen? Ohne die Seite vollständig neu aufzubauen"
- "Hat React einen Standard um Client sided Health checks durchzuführen?"
- "Gib mir eine grobe SQL Abfrage um Thread Titel via String zu durchsuchen"
- "Wie kann ich mit react markdown render ohne viel Aufwand"
- "Schreib dieses seed script neu mit mehr daten und markdown Inhalten [...]"

### Entwicklung (Suche)

- "Gib mir eine grobe SQL Abfrage um Thread Titel via String zu durchsuchen"
- "Wie könnte ich so simpel wie möglich Suchergebnisse in Text finden und markieren"
- "Skizzier mir den besten und schnellsten Weg, um in React Markdown Formatierung aus Text zu entfernen"

### Entwicklung (Login / Registrierung)

- "Ich klicke auf Login, doch die onSubmit Methode wird nicht ausgeführt. Die API bekommt wohl auch keine Anfrage. Woran kann das liegen?"
- "Die App bleibt nach dem Login bei "Anmeldung wird geprüft" hängen. Warum wird das Backend nicht angefragt?"
- "Wie kann ich mir den JWT Token am besten lokal zwischenspeichern?"
- "Das Login liefert Status 200 Ok, im Localstorage wird das Token mit dem Wert undefined angelegt. Users/me antwortet danach mit unauthorized, weil das Token weg ist. Wo geht das Token verloren?"
- "Die SQL Abfrage findet den Benutzer, aber bei user["password_hash"] meldet Python TypeError: tuple indices must be integers or slices, not str. Wie lese ich die Spalte richtig aus?"
- "Was bedeutet Context in React, und wie kann ich Benutzername, Rolle und ID in mehreren Komponenten verwenden"
- "Wie lege ich Testbenutzer mit gehashten Passwörtern direkt in meiner SQL-Seed-Datei an?"
- "Wie ergänze ich auf der Login Sectione einen Link zur Registrierung"
- "Kannst du mir basierend auf dem login.css und dem register.jsx ein register.css erstellen?"

### Entwicklung (User Profil)

- "Beim Löschen kommt im Backend DELETE /users/%5Bobject%20Object%5D statt /users/1 an. An welcher Stelle übergebe ich ein Objekt statt der ID?"
- "Beim Bearbeiten erreicht PUT /users/1 das Backend, aber FastAPI antwortet mit 422. Der Dialog übergibt onSave({ username, email }), während meine Funktion handleSave(username, email) erwartet. Warum kommt username als Objekt an und email fehlt im JSON?" 
- "Mein Dialog ruft onDelete() auf, und in der Profilseite steht handleDelete({id}). Warum bekomme ich TypeError: (destructured parameter) is undefined, obwohl die User-ID im Profil angezeigt wird?"


### Entwicklung (User Statistiken)

- "Ich möchte verschiedene Statistiken der Benutzer des Forums auswerten und anzeigen lassen, wie das Beitrittsdatum, die Anzahl an Threads oder Kommentaren. Was für interessante Statistiken kann man aus meinem Datenbankschema noch hervorheben?"
- "Kannst du mir eine SQL Abfrage erstellen die mir die interessanten Statistiken der Benutzer anhand der user_id zurückliefert?"
- "Mein Backend stellt die Daten per API bereit. Das Frontend kann die Route schon korrekt abfragen. Kannst du mir eine JSX Komponente bauen, die die Statistiken übersichtlich anzeigt, sodass ich sie in meiner Profile Page integrieren kann?"
- "Kannst du die Anzahl an Threads und Kommentaren pro woche noch als Balkendiagramm darstellen?"
- "Füg mir unter den Statistiken noch ein Link zu dem letzen Thread des Users ein."





## Details

Hier werden ein paar Beispiele vom KI-Einsatz näher erklärt.

#### 1. Design und Styling

> Um schneller bessere ```.css``` Styles zu schreiben und komplexere Styles anzupassen wurde im beschränkten Rahmen **KI**
> eingesetzt. Beispiele für verwendete Prompts stehen im Abschnitt [Design und Styling](#design-und-styling). Fokus lag hierbei auf
> der Entwicklung einheitlicher und aufeinander abgestimmter Designs, ohne, dass lange Recherchen und langes
> *"rumprobieren"* nötig war, besonders bei größeren und voneinander anbhängigen Styles. **KI** wurde hier primär als
> Analyse- und Recherche-Tool benutzt.

#### 2. Debugging von schweren Fehlern / Inkompatibilitäten

> Das Projekt hat viele verschiedene Abhängigkeiten und eine Vielzahl and Dateien und Modulen. Zusätzlich besteht der
> Anspruch, dass die Entwicklung und Ausführung auf ```Linux``` sowie ```Windows``` funktioniert. Hierbei gibt es ein
> hohes Potential für Fehler, besonders durch verschiedene Konfigurationen, Versionen von Abhängigkeiten aber auch
> anderen komplexeren Zusammenhängen. Damit die Zeit effizient für die Entwicklung aufgebracht werden kann, wurde **KI**
> zur schnellen Untersuchung und, wenn möglich, zum Beheben dieser Fehler eingesetzt. Beispiele für verwendete Prompts stehen im Abschnitt
> [Debugging von schweren Fehlern](#debugging-von-schweren-fehlern).

## Reflektion

> TODO