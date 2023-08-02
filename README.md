# Programma per l'inserimento di numeri brevi TIM da CSV

Questo programma consente di inserire numeri brevi TIM (Short Codes) da un file CSV nel sito [https://timcomunica.timbusiness.it](https://timcomunica.timbusiness.it). Il sito non offre la funzionalità di caricare i numeri brevi da un file CSV, ma questo programma utilizza Selenium per automatizzare il processo di inserimento.

## Istruzioni per l'uso

1. Assicurati di avere installato Python sul tuo sistema.
2. Clona questo repository o scarica il file principale del programma.
3. Assicurati di avere installato il ChromeDriver corrispondente alla tua versione di Google Chrome.
4. Assicurati di avere installato tutte le dipendenze necessarie elencate nel file `requirements.txt`. Puoi installarle eseguendo il comando:

```
pip install -r requirements.txt
```

5. Inserisci i numeri brevi nel file CSV seguendo il formato corretto: ogni riga del file deve contenere due campi separati da punto e virgola (;). Il primo campo deve essere il numero di telefono breve (es. 12345) e il secondo campo deve essere il nome associato a quel numero breve (es. Dipartimento Marketing). Un esempio del formato del file CSV:

```
12345;Dipartimento Marketing
67890;Assistenza Clienti
54321;Ufficio Acquisti
```

6. Avvia il programma eseguendo il seguente comando:

```
python main.py
```

7. Segui le istruzioni del programma e inserisci il tuo username, password e l'ID della sede desiderata.
8. Il programma aprirà una finestra del browser Chrome e inizierà ad inserire i numeri brevi nel sito web automaticamente.
9. Alla fine del processo, il programma terminerà e i numeri brevi saranno stati inseriti con successo nel sito web.

## Licenza

Questo programma è distribuito con licenza GPL (GNU General Public License) versione 3 o versioni successive. Consulta il file `LICENSE` per i dettagli completi della licenza. Il copyright è di [tuo nome] (aggiorna con il tuo nome).

## Avvertenza

Questo programma utilizza Selenium per automatizzare le azioni sul sito web. L'uso di questo programma potrebbe violare i termini di servizio del sito web. Utilizzalo a tuo rischio e pericolo. L'autore non è responsabile per eventuali conseguenze derivanti dall'uso di questo programma.

**Nota:** Questo software è stato creato a scopo didattico e potrebbe non essere conforme ai termini di servizio del sito web target. L'utilizzo di questo software è a tua discrezione e responsabilità.
