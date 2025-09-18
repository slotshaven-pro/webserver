# Programmering B for 3g
Materiale til undervisningen i programmering B på Slotshaven Gymnasium HTX i Holbæk.

Bemærk at dette workspace ikke er et websted i _sig selv_ - men indeholder en række underprojekter med websteder.
Hvert underprojekt indeholder et workspace hvorfra webstedet startes. Man skal altså køre projekter fra deres eget workspace.
Læs sektion **Sådan gør du** grundigt før du begynder.

## Progression
Forløbet følger en simpel progression.

### Simpelt websted med flask
Simpelt websted med frameworket flask.

Begreber:
- routes
- templates
- static files (css, images)

### Websted med GET og POST
Websted med eksempler på brug af HTTP GET og POST.

Begreber:
- GET (url-parametre)
- POST (form-data)
- routes med HTTP-metoder
- styling med CSS-selectors

### Websted med database
Websted med data fra database.

Begreber:
- sqlite3
- database-filer
- database: felter
- sql-forespørgsler
- installation af biblioteker med requirements.txt

### Websted med søgning
Websted med søgning i data fra database.

Begreber:
- sql med LIKE

## Sådan gør du
tldr;

Vigtigt: Projekt skal eksekveres ("køre i") i sin egen mappe.

Det er den mappe som man "står i" i konsollen der er bestemmer i hvilken mappe projektet kører i. Så man skal "skifte" (`cd [mappe]`) til den mappe som projektet ligger i.

**Metode 1 - anbefalet**
Brug workspace.
Åben det workspace som ligger i det projekt som du vil arbejde med.

- dobbeltklik på det, eller
- åben en ny udgave af VS Code og åben workspace

**Metode 2**
Brug konsol.
Skift til den rigtige mappe først i konsolen med ``cd [mappe]``.
Start webserver med ``python app.py`` eller klik på pilen i højre hjørne.


