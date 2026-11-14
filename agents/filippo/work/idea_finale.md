# Idea scelta — Cervello allergeni (nome provvisorio, decide Sian)

Dettagli, mercato e fonti: `piano_progetto.md`. Video: `video/idea.mp4`. Abstract: `abstract.txt`.

**In una frase:** un cervello AI che ricorda e collega tutto quello che succede in uno stabilimento alimentare e avvisa il responsabile qualità prima che un allergene finisca dove l'etichetta non lo dichiara.

**Problema:** gli allergeni non dichiarati sono la prima causa di richiami alimentari negli USA (38,8% nel 2025, Statista FDA/USDA). Le informazioni c'erano già ma erano sparse: mail del fornitore, registro di pulizia con una procedura superata, report di turno. Le approvazioni salgono la gerarchia a mano.

**Per chi:** responsabile qualità di stabilimenti con più allergeni sulle stesse linee (dolciario, forno, co-packer). Paga l'azienda; usa il responsabile qualità.

**Cosa fa (5 passi):**
1. Legge ogni documento appena arriva.
2. Lo collega in una mappa: fornitore → ingrediente → macchina → lotto → etichetta. Ogni fatto ha fonte, autore e data; le versioni superate restano marcate.
3. Incrocia i fatti e trova il rischio.
4. Avvisa il manager con le prove e propone un blocco mirato dei lotti.
5. Dopo la firma manda le istruzioni ai lavoratori. Tutto resta tracciato per l'ispettore.

**Regola:** l'AI propone, una persona decide (blocco/rilascio lotti, etichette).

**Ipotesi più rischiosa (test di oggi):** l'AI trova il rischio giusto incrociando 3 documenti sparsi, senza falsi allarmi.
**Criterio di stop:** su 10 casi di prova, se trova meno di 8 rischi giusti o dà più di 2 falsi allarmi, restringiamo a un solo tipo di documento.

**Demo:** stabilimento dolciario, linea a 4 stazioni, dati sintetici dichiarati.
