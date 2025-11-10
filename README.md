# MoodBox
Interaktiv nettbutikk med personlige bokser

## 🎯 Om prosjektet
**MoodBox** er en nettbutikk hvor brukeren kan handle produkter og få personlige anbefalinger.  
Butikken tilbyr både vanlige varer og spesielle “bokser” – ferdigpakkede sett med produkter innenfor et tema, som for eksempel *self-care*, *snacks*, *kos* eller *trening*.  

I tillegg finnes det en liten interaktiv funksjon der brukeren kan svare på noen enkle spørsmål for å få forslag til hvilken boks som passer best.  
En **chatbot** fungerer som butikkens assistent og hjelper brukeren underveis – den kan forklare hvordan butikken fungerer, vise produkter eller komme med anbefalinger.  

Prosjektet er laget med **Flask, MariaDB, HTML/CSS og JavaScript**.  
Alt kjører på en **Raspberry Pi**, og hele løsningen er dokumentert og tilgjengelig på GitHub.

---

## 🧩 Konsept
MoodBox er ment som en moderne nettbutikk med et personlig preg.  
Målet er å skape en opplevelse som føles litt mer levende enn en vanlig nettbutikk – en side hvor du både kan handle og ha det litt gøy.

### Eksempler på produktbokser:
| Boksnavn | Tema | Eksempler på produkter |
|-----------|------|------------------------|
| 💆‍♀️ **Self-care Box** | Avslapning og egenpleie | Duftlys, te, håndkrem, ansiktsmaske |
| 🍫 **Snack Box** | Søte og salte fristelser | Sjokolade, chips, energibar, nøtter |
| 🏋️‍♀️ **Active Box** | Trening og energi | Drikkeflaske, proteinbar, treningshåndkle |
| 🏡 **Cozy Box** | Hjemmekos | Kopp, sokker, kakao, liten bok |
| 🎉 **Surprise Box** | Overraskelse | Random miks av produkter |

Brukeren kan også chatte med butikkens assistent:
> “Jeg vil ha noe koselig til helgen.”  
→ Chatboten foreslår *Cozy Box* ☕🧦  

---

## ⚙️ Teknologi
Prosjektet er bygget med:
- **Flask** som backend (Python)
- **MariaDB** som database for brukere, produkter og bokser
- **HTML/CSS/JavaScript** for frontend
- **Chatbot** integrert via Flask API

### Databasen inneholder blant annet:
- `users` – registrerte brukere  
- `products` – varer i nettbutikken  
- `boxes` – ferdige produktbokser  
- `chat_logs` – samtaler med chatboten  

---

## 💬 Funksjoner
- Handle vanlige produkter eller ferdige bokser  
- Interaktiv quiz for å finne anbefalinger  
- Chatbot som gir veiledning og tips  
- Handlekurv og bestillingssystem  
- Brukervennlig og enkel design  

---

## 🧠 Læringsmål
Dette prosjektet viser:
- hvordan man bygger en nettbutikk med Flask og MariaDB  
- bruk av datastrukturer i Python  
- oppsett av webserver (Raspberry Pi)  
- frontend-design og interaktivitet med JavaScript  
- dokumentasjon og brukerveiledning  

---

## 🚀 Videre utvikling
I fremtiden kan MoodBox utvides med:
- innlogging og brukerprofiler  
- flere bokstyper og produktkategorier  
- AI-basert anbefalingssystem  
- integrasjon med ekte betalingsløsning  
