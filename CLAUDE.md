# Manuale Coppie Officina — istruzioni per Claude

App web installabile (PWA) per un manuale d'officina interattivo: marca → modello → sistema → disegno SVG cliccabile con coppie di serraggio. Utente: meccanico, scrive in italiano, lavora spesso da telefono. Rispondere in italiano semplice.

## Struttura
- `src/app.html` — tutta l'app (HTML+CSS+JS in un file). Disegni in `SYS` (viewBox, `base`, `parts` con `id`, `nome`, `shape`, `anchor`, `label`). Ordine sistemi in `ORDER`. Marche in `BRANDS`.
- `src/seed.json` — veicoli e valori distribuiti a tutti. **Aumentare `versione` di 1** a ogni modifica, altrimenti i dispositivi già installati non ricevono i nuovi veicoli. Il merge aggiunge solo id nuovi, non sovrascrive i dati dell'utente.
- `tools/build.py` — genera `docs/` (index.html, seed.js, sw.js con versione hash, manifest, icone). Mai modificare `docs/` a mano.
- `docs/` — versione pubblicata (Netlify o GitHub Pages servono questa cartella).

## Flusso di aggiornamento
1. Modifica `src/app.html` e/o `src/seed.json`.
2. `python3 tools/build.py`
3. Test rapido: `python3 -m http.server -d docs 8765` + Playwright (desktop e 390px, nessun errore console, nessuno scroll orizzontale).
4. Commit e push su `main`.

## Regole sui dati
- Mai inventare coppie di serraggio per veicoli reali. Valori veri solo se forniti dall'utente con la fonte.
- Il veicolo "Esempio / Veicolo di prova" ha valori inventati marcati `esempio: true`.
- Dati utente: localStorage chiave `manuale-coppie-v1` (modalità app) oppure archivio `db` dell'artifact Claude (modalità artifact, stesso codice: rileva `window.claude`).
