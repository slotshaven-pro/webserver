# Database scripts

Projektet indeholder Python-scripts, der opretter SQLite3-databaser. Det er et
hjælpeprojekt til webserver-eksemplerne, hvor databaserne senere kan bruges fra
Flask.

Før de kan bruges til egne formål, skal de modificeres. Læs kommentarerne i koden.

## IDE udvidelser

Anbefalet udvidelse: Sqlite Explorer. Kan bruges til at inspicere sqlite3-databaser.

## Scripts

**db-init.py** Opretter en database med Beatles-albums. Data er defineret i scriptet.

**db-from-csv.py** Opretter en database med kunstværker. Data ligger i en csv-fil i folderen `csv`.
