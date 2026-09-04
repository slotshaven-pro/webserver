# Eksempel 6: Website med JavaScript og cookies

Dette projekt introducerer brugen af JavaScript i et Flask-baseret website.
Eleven kan se, hvordan HTML, CSS, Python/Flask og JavaScript arbejder sammen i
en simpel webapplikation.

## Hvad viser projektet?

- Flask leverer siderne fra `app.py` og `templates/`.
- CSS ligger i `static/main.css` og styrer sidernes udseende.
- JavaScript ligger i `static/js/main.js` og bliver indlæst i
  `templates/base.html`.
- JavaScript-koden kører i browseren, når siden er indlæst.
- Projektet bruger en cookie til at gemme, hvor mange gange siden er blevet
  vist i den aktuelle browser.

## JavaScript

Filen `static/js/main.js` bruger `DOMContentLoaded` til at vente, indtil HTML'en
er klar. Derefter kaldes en funktion, som opdaterer en sidevisningstæller.

JavaScript bruges her til at:

- reagere på at siden er færdigindlæst
- læse en eksisterende cookie
- øge tælleren med 1
- gemme den nye værdi i en cookie
- vise tælleren på siden i elementet med id'et `page_count`

## Cookies

En cookie er en lille tekstværdi, som browseren kan gemme for et website. I
dette projekt gemmes cookien `pageCount`.

Cookien bruges til at huske tælleren mellem sideindlæsninger. Når brugeren
genindlæser siden, kan JavaScript læse den gamle værdi fra cookien og
fortsætte med at tælle derfra.

Cookien sættes til at udløbe efter 30 dage.
