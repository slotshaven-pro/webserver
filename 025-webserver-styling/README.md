# Eksempel 4: Website med base templates

Dette projekt introducerer brugen af base templates i Flask. Pointen er, at fælles HTML-struktur kun skrives ét sted i `templates/base.html`, mens de enkelte sider genbruger layoutet og kun definerer deres eget indhold.

`base.html` indeholder den fælles sideopbygning:

- HTML-dokumentets grundstruktur
- link til CSS-filen `static/main.css`
- logo fra `static/slotshaven-logo.png`
- navigationsmenu
- template blocks til sidetitel og sideindhold

De andre templates arver fra `base.html` med:

```html
{% extends "base.html" %}
```

Derefter udfylder de de dele af siden, som er forskellige fra side til side:

```html
{% block title %}Frontpage{% endblock %}

{% block content %}
<h1>{{ title }}</h1>
{% endblock %}
```

På den måde kan layout, styling og menu ændres ét sted, uden at den samme HTML skal gentages i alle templates.

**Templates i projektet:**

- `templates/base.html`: Fælles grundlayout med logo, menu, stylesheet og blocks.
- `templates/frontpage.html`: Forsiden, som arver fra base templaten.
- `templates/search.html`: Søgesiden, som arver fra base templaten og viser en formular samt søgeresultater.
- `templates/default.html`: Genbrugelig standardside til simple undersider som About og Tech Stack.

Projektet indeholder også en søgefunktion mod en SQLite-database med Beatles-albums. Når en bruger søger på `/search`, sender Flask søgeordet videre til en SQL-forespørgsel, og resultaterne vises i `search.html`.

**Anvendte teknologier:**
- **Python:** Backend-programmeringssprog.
- **Flask:** Webframework til at håndtere HTTP-forespørgsler og routing.
- **Jinja templates:** Flask templates med inheritance, `extends` og `block`.
- **SQLite3:** Letvægtsdatabase til lagring og forespørgsel af data.
