# MoodBox
Interaktiv nettbutikk med personlige bokser

## Kort beskrivelse
**MoodBox** er en nettbutikk hvor brukeren kan handle vanlige produkter og ferdigpakkede produktbokser innenfor ulike temaer som *self-care*, *snacks*, *trening* og *kos*.  
Målet er å lage en moderne, brukervennlig nettbutikk med et personlig preg, der en enkel **chatbot** fungerer som en assistent som hjelper brukeren med å finne produkter og bokser.  


## Idé og mål
Prosjektet skal vise hvordan jeg kan utvikle et fungerende IT-system som består av:
- egenutviklet backend med Python (Flask)
- database (MariaDB)
- frontend med HTML, CSS og JavaScript
- chatbot-integrasjon
- dokumentasjon og brukerveiledning

---

## Teknologier
- **Python 3**
- **Flask**
- **MariaDB**
- **HTML / CSS**
- **Git & GitHub**
- **Linux (Raspberry Pi)**

---

## Funksjonalitet
- Dynamisk innhold hentet fra database
- Flask-backend med templates og static-filer
- Databasekobling til MariaDB
- Strukturert prosjektoppsett
- Grunnleggende backend-logikk i Python

---

## Database
Prosjektet bruker **MariaDB** til lagring av data.

Databasen kjører lokalt på Raspberry Pi.
---

## Installasjon 

Klon prosjektet:
git clone https://github.com/maartuhaa/MoodBox.git

cd MoodBox

Installer nødvendige pakker:
pip install flask mariadb

Start applikasjonen:
python3 app.py

Applikasjonen blir tilgjengelig i nettleser på:
http://SERVER_IP:5000

Slik bruker du MoodBox:
1. Åpne en nettleser
2. Gå til adressen til serveren (for eksempel Raspberry Pi sin IP-adresse)
3. Naviger på nettsiden
4. Innhold lastes automatisk fra databasen

## Sikkerhet
- Databasen kjører lokalt på serveren
- Sensitive filer som .env er ikke lastet opp til GitHub
- GitHub brukes kun til kode og dokumentasjon








