# Eksempel 4: Website med søgning

Dette projekt introducerer søgning i en database fra et Flask-websted.
Søgningen udføres mod en SQLite3-database ved hjælp af en HTML-formular,
en Flask-route med `GET` og `POST`, og en SQL-forespørgsel med `LIKE`.

## Hvad viser projektet?

- Brugeren indtaster et søgeord i `templates/search.html`.
- Formularen sendes med `POST` til Flask-routen `/`.
- Flask læser søgeordet med `request.form.get()`.
- SQL bruger `LIKE` til at finde albums, hvor titlen matcher søgeordet.
- Resultaterne sendes tilbage til templaten og vises i browseren.

**Anvendte teknologier:**
- **Python:** Backend-programmeringssprog.
- **Flask:** Webframework til at håndtere HTTP-forespørgsler og routing.
- **SQLite3:** Letvægtsdatabase til lagring og forespørgsel af data.
- **SQL LIKE:** Bruges til søgning i tekstfelter.
