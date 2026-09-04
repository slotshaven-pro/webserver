# Eksempel 3: Websted med database

Dette projekt introducerer brugen af SQLite3-databaser i et Flask-baseret
websted. Eleven kan se, hvordan Flask henter data fra databasefiler og viser
resultaterne i HTML-templates.

Projektet bruger to databaser:

- `db/users.db` vises på forsiden `/`.
- `db/beatles.db` vises på siden `/beatles`.

Databaseforespørgslerne ligger i `app.py`, hvor funktionen `get_db()` åbner en
SQLite-database, kører en SQL-forespørgsel og returnerer rækkerne til en
template.

## Anvendte teknologier

Dette projekt anvender følgende teknologier:

- **Python 3** – Programmeringssprog til backend-udvikling.
- **Flask** – Webframework til at oprette og håndtere webapplikationen.
- **SQLite3** – Letvægtsdatabase til lagring af data.
- **Jinja2** – Skabelonmotor til rendering af HTML-sider.
- **HTML/CSS** – Til frontend og brugergrænseflade.

Disse teknologier gør det muligt at udvikle en simpel, men funktionel webapplikation med databaseunderstøttelse.
