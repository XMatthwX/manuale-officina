# Manuale Coppie Officina

Manuale d'officina interattivo: scegli **marca → modello → sistema**, tocca il pezzo sul disegno e leggi **coppia di serraggio, sequenza, note e fonte**.

- Funziona su **telefono, tablet e PC**, si installa come un'app con la sua icona.
- Funziona **anche senza internet** dopo la prima apertura.
- Si **aggiorna da sola**: quando pubblichiamo una nuova versione, alla successiva apertura con rete arriva in automatico. I valori che hai inserito restano.
- I dati restano **sul dispositivo**. Per spostarli su un altro dispositivo: *Esporta backup* → *Importa backup*.

> I valori di coppia si inseriscono a mano dalla documentazione ufficiale del costruttore. Il "Veicolo di prova" contiene valori inventati, solo per mostrare l'app.

---

## 1. Metterla online (una volta sola)

**Con GitHub Pages (consigliato, gratis):**
1. Carica questa cartella nel repository `manuale-coppie` (oppure falla caricare a Claude).
2. Su GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
3. Branch: **main**, cartella: **/docs** → **Save**.
4. Dopo 1-2 minuti l'app è su: `https://TUO-UTENTE.github.io/manuale-coppie/`

**In alternativa, senza account (Netlify Drop):** vai su `app.netlify.com/drop` e trascina la cartella **docs**. Ti dà subito un indirizzo https.

## 2. Installarla

- **Android (Chrome):** apri l'indirizzo → menu ⋮ → **Installa app** (o "Aggiungi a schermata Home").
- **iPhone / iPad (Safari):** apri l'indirizzo → tasto **Condividi** → **Aggiungi alla schermata Home**.
- **PC (Chrome o Edge):** apri l'indirizzo → icona **Installa** nella barra degli indirizzi.

**Vuoi un file .apk per Android?** Vai su `pwabuilder.com`, incolla l'indirizzo dell'app, scegli **Android** e scarica il pacchetto. Gratis.

## 3. Aggiornarla (nuove macchine, nuove funzioni)

Struttura:
```
src/app.html      ← l'app (grafica, disegni, logica)
src/seed.json     ← veicoli e valori di partenza che arrivano a tutti con l'aggiornamento
tools/build.py    ← costruisce la versione pubblicata
docs/             ← la versione pubblicata (non modificare a mano)
```

Per aggiungere veicoli per tutti: aggiungili in `src/seed.json` e **aumenta di 1 il numero `versione`**. Poi:
```
python3 tools/build.py
git add -A && git commit -m "Nuovi veicoli" && git push
```
Ogni dispositivo, alla prossima apertura con rete, riceve la nuova versione e i nuovi veicoli, senza perdere i valori già inseriti.

Il modo più semplice: apri Claude, chiedi "aggiungi la Mazda CX-60 al manuale coppie" e fagli fare il push sul repository.
