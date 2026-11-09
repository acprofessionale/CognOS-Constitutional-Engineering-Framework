# COGNOS

**La persona al centro. L’intelligenza artificiale al servizio della sua autonomia.**

COGNOS significa *Cognitive Operating System for Human–AI Orchestration*. È un progetto di ecosistema per coordinare persone, agenti, strumenti e conoscenza attraverso obiettivi espliciti, responsabilità definite e risultati verificabili.

Il centro di COGNOS è la persona: chi usa il sistema, chi contribuisce e chi subisce gli effetti delle sue azioni. La visione va oltre il suo ideatore. La tecnologia deve rendere le persone più capaci di capire, scegliere e agire, preservandone dignità, autonomia e diritto di interrompere un processo.

## Perché esiste

La crescita delle capacità dell’AI aumenta anche il numero di azioni che possono essere delegate. COGNOS vuole creare le condizioni perché questa evoluzione avvenga con controllo, continuità e responsabilità.

Il valore di un sistema cognitivo si misura nell’utilità dei risultati, nella qualità delle evidenze e nella capacità di riconoscere i propri limiti. Una dimostrazione convincente è un punto di partenza; l’affidabilità richiede verifiche ripetibili.

## I principi

- **Centralità della persona.** Le decisioni che incidono sulle persone richiedono responsabilità identificabili e possibilità di intervento umano proporzionate al loro impatto.
- **Evidenza prima dell’affermazione.** Fatti verificati, interpretazioni e ipotesi devono restare distinguibili.
- **Autonomia entro un mandato.** Ogni agente riceve obiettivo, perimetro, strumenti, permessi e condizioni di arresto espliciti.
- **Prevenzione prima del recupero.** I rischi si considerano durante la progettazione. Un errore non deve ampliare automaticamente i privilegi.
- **Responsabilità e tracciabilità.** Le azioni rilevanti devono poter essere ricostruite, con attenzione alla riservatezza e alla minimizzazione dei dati.
- **Evoluzione verificabile.** Nuove capacità entrano nel sistema attraverso valutazioni, test e criteri di accettazione dichiarati.

## Come si prepara al futuro

La direzione architetturale è una struttura a strati, con un nucleo fidato ridotto e interfacce controllate. Gli agenti operano attraverso servizi autorizzati; la gestione delle politiche e delle identità resta separata dall’esecuzione dei compiti.

La resilienza comprende rilevamento delle anomalie, contenimento proporzionato, conservazione delle evidenze e recupero da uno stato verificato. Il sistema deve poter limitare o sospendere le operazioni senza trasformare l’emergenza in una scorciatoia per ottenere nuovi accessi.

COGNOS valuta le protezioni offerte da hardware, sistemi operativi e piattaforme: isolamento, attestazione, protezione delle chiavi e aggiornamenti verificabili. Le capacità disponibili devono essere accertate sulla configurazione reale. La sicurezza dell’hardware non sostituisce il controllo sulle azioni degli agenti.

La memoria durevole è un ulteriore ambito di ricerca: preservare conoscenza, provenienza e versioni approvate significa conservarne anche formati e possibilità di recupero. La durata del supporto, da sola, non garantisce la verità del contenuto.

## Per chi usa l’AI e per chi gestisce CED e server farm

Quando un sistema AI può usare strumenti, un errore può diventare un’azione: modificare un file, divulgare informazioni, eseguire codice o consumare risorse. Il problema cresce con i permessi concessi, le connessioni tra servizi e la velocità delle operazioni.

OWASP identifica rischi quali manipolazione degli obiettivi, abuso di strumenti e identità, compromissione della filiera agentica ed effetti a cascata. NIST documenta anche il rischio di risultati errati presentati con sicurezza. Questi riferimenti descrivono categorie di rischio: non dimostrano che ogni agente o piattaforma sia compromesso.

| Rischio | Effetto possibile | Requisito progettuale di COGNOS |
|---|---|---|
| Istruzioni malevole dentro documenti, pagine o risposte di strumenti | Un contenuto esterno devia il compito e induce azioni non previste | Separare dati e istruzioni; applicare autorizzazioni nei servizi, indipendentemente dal modello |
| Strumenti o identità con permessi eccessivi | Un errore locale coinvolge altri utenti, clienti o sistemi | Minimo privilegio, identità distinte, isolamento dei tenant e revoca verificata |
| Componenti, dipendenze o definizioni di strumenti alterate | Il sistema esegue operazioni tramite una componente non affidabile | Verificare provenienza, versioni e aggiornamenti; limitare i componenti ammessi |
| Cicli di chiamate e deleghe senza limiti | Saturazione di code e infrastruttura, interruzioni e costi incontrollati | Budget, scadenze, quote, limiti di concorrenza e arresto controllato |
| Errori che si propagano tra agenti | Una falsa premessa diventa una catena di decisioni o modifiche | Verifiche ai confini, provenienza delle evidenze e contenimento per dominio |
| Allarmi e richieste di approvazione eccessivi | Il responsabile umano perde la capacità di valutare con attenzione | Richieste proporzionate, priorità chiare e sospensione delle azioni quando manca una decisione valida |
| Recupero mal progettato o log indisponibili | L’emergenza apre nuovi privilegi oppure impedisce di ricostruire l’incidente | Recupero separato, evidenze protette, nessun aumento automatico dei privilegi e prove di ripristino |

Per un responsabile ICT, il requisito non è soltanto far funzionare l’agente: è conoscere quali sistemi può raggiungere, quali effetti può produrre, come fermarlo e come ripristinare il servizio. Fermare un processo non annulla una comunicazione già inviata o una modifica già effettuata. Servono verifiche delle operazioni pendenti e procedure di riconciliazione.

### Prepararsi prima di estendere l’autonomia

Prima di introdurre un nuovo agente o ampliarne i poteri, il percorso proposto richiede:

1. Inventario di identità, strumenti, dati, connessioni e responsabili.
2. Mandato e limiti misurabili, con accessi strettamente necessari.
3. Valutazioni su errori, input malevoli e guasti delle dipendenze.
4. Verifica di revoca, isolamento, gestione delle code e recupero.
5. Introduzione graduale, con evidenze e criteri espliciti per proseguire o fermarsi.

La risposta di COGNOS alla rapida evoluzione dell’AI è creare queste condizioni in anticipo, così che persone e organizzazioni possano adottare nuove capacità senza affidarsi alla sola fiducia nel comportamento del modello.

La metafora dell’ondata esprime l’urgenza; il metodo resta operativo: anticipare, limitare l’esposizione, contenere il danno e preservare le funzioni essenziali. Nessuna previsione catastrofica è necessaria per progettare responsabilmente.

## Il metodo di lavoro

**Obiettivo → mandato → esecuzione autorizzata → evidenze → verifica → miglioramento.**

Prima di delegare, si chiariscono risultato atteso, vincoli e responsabilità. Durante il lavoro, si raccolgono evidenze pertinenti. Prima di estendere le capacità, si verifica che il risultato e i controlli soddisfino criteri espliciti.

Le autorizzazioni persistono solo entro il perimetro concordato. Le azioni che richiedono un’approvazione devono attendere una decisione valida; l’assenza di risposta non costituisce consenso.

## Stato e impegni

Questo documento descrive la visione e i requisiti progettuali. Non certifica che tutte le protezioni siano già implementate, operative o validate.

Gli incrementi di sviluppo dovranno indicare cosa è disponibile, cosa è stato testato, quali limiti rimangono e quali evidenze sostengono ogni risultato. Il progresso sarà reso valutabile attraverso documentazione, verifiche e cambiamenti tracciabili.

## Collaborare

COGNOS invita contributi capaci di trasformare questa visione in risultati utili: progettazione, sviluppo, sicurezza, ricerca, accessibilità, documentazione e valutazione.

Una buona proposta chiarisce il problema, il beneficio per le persone, i rischi, il perimetro e il modo di verificarne l’esito. Prima di integrare contributi, si concordano provenienza, licenze, diritti e responsabilità. Questa pagina non concede una licenza sui materiali del progetto.

## Riferimenti pubblici

- [OWASP: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) — strumenti, permessi e autonomia eccessivi; controlli nei sistemi di destinazione.
- [OWASP: Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) — rischi specifici delle applicazioni agentiche.
- [NIST: Generative AI Profile, AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — rischi e gestione dei sistemi generativi.
- [NIST: Developing Cyber-Resilient Systems](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) — anticipare, resistere, recuperare e adattarsi.

Fonti consultate il 12 ottobre 2026. I controlli descritti sono requisiti e proposte di COGNOS, non attestazioni di conformità o certificazioni.

**La verità sta al centro.**

---

Promotore: Ennio Princi · AC Professionale Lab  
Versione pubblica proposta: 0.2 · 12 ottobre 2026  
Stato: pronta per revisione; pubblicazione non effettuata.
