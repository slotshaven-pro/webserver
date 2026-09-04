# Eksempel 1: Simpelt websted med Flask

Dette projekt introducerer et helt simpelt websted bygget med Flask.
Eleven kan se, hvordan en Flask-applikation oprettes, hvordan en route
forbinder en URL med en Python-funktion, og hvordan en HTML-template vises i
browseren.

Projektet viser også et enkelt eksempel på en URL-parameter med `?name=...`,
som læses med `request.args.get()` og sendes videre til templaten.

## Hvad viser projektet?

- Flask-applikationen oprettes i `app.py`.
- Forsiden ligger på routen `/`.
- HTML'en ligger i `templates/index.html`.
- CSS og billede ligger i `static/`.
- En værdi fra URL'en kan læses i Flask og bruges i en template.

## Anvendte teknologier

- **Flask:** Webframework til at håndtere HTTP-forespørgsler og routing.
- **Jinja templates:** Bruges til at indsætte Python-værdier i HTML.
- **HTML/CSS:** Bruges til struktur og styling i browseren.
