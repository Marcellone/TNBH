<div align="center">
<!-- Titolo: -->
  <a href="https://github.com/Marcellone/TNBH/">
    <img src="https://drive.google.com/file/d/1CDtkVSs2YUhmvWThTg83t5mWdAxHZxFd/view?usp=drive_link" height="100">
  </a>
  <h1><a href="https://github.com/Marcellone/TNBH/">TNBH - TIM Numeri Brevi Helper</a></h1>
<!-- Etichette: -->
  <!-- Prima riga: -->
  </a>
  <a href="https://github.com/Marcellone/TNBH/blob/master/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square" height="20" alt="Contributions Welcome">
  </a>
  <img src="https://img.shields.io/github/repo-size/Marcellone/TNBH.svg?label=Repo%20size&style=flat-square" height="20">
   </a>
   </a>
  <!-- Seconda riga: -->
  <br>
  <a href="https://github.com/Marcellone/TNBH/actions">
  </a>
<!-- Breve descrizione: -->
  <h3>Script Python per inserire numeri brevi TIM da CSV</h3>
</div>

## Informazioni

Questo script Python ti consente di inserire numeri brevi nel sito web di TIM utilizzando i dati di un file CSV. Automatizza il processo, semplificando e velocizzando la gestione dei numeri brevi.

## Requisiti

- Python 3.x
- Browser Google Chrome (per interagire automaticamente con il web)

## Come Usare

1. Clona o scarica questa repository.
2. Installa le librerie Python necessarie eseguendo `pip install -r requirements.txt`.
3. Assicurati di avere un file CSV contenente i dati dei numeri brevi nel seguente formato: `ID;Descrizione;NumeroTelefono;Nome`. (il programma prenderà NumeroTelefono e Nome, nota che i primi due sono stati mantenuti perchè in fase di copiatura da altri centralini venivano inseriti e son comodi per inserire in maniera coordinata i valori. Se per esempio necessito alla shortcut 1 un numero, il 2 vuoto e il 3 con un numero, porremo il numero 2 con ntelefono e nome a 0)
4. Esegui lo script con `python3 main.py`.
5. Segui le istruzioni e fornisci il tuo nome utente, password e l'ID del telefono che desideri modificare e il nome del file CSV.
6. Lo script si connetterà automaticamente al sito web di TIM, si sposterà alla sezione appropriata e inserirà i numeri brevi dal file CSV.

## Nota Importante

Questo script è destinato solo a scopo educativo e non è ufficialmente supportato da TIM. Usalo a tuo rischio.
Inoltre, lo script non gestisce errori eventuali, quindi potrebbe capitare l'interruzione randomica del programma.

## Licenza

Questo progetto è concesso in licenza ai sensi della Licenza Pubblica Generale GNU v3.0. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli.

## Contributi

Accogliamo con favore i contributi a questo progetto! Leggi le nostre [Linee Guida per i Contributi](CONTRIBUTING.md) prima di inviare una pull request.

## Problemi

Se incontri problemi nell'utilizzo dello script o hai suggerimenti per miglioramenti, apri una issue nella sezione [Problemi](https://github.com/Marcellone/TNBH/issues).

## Contatti

Per qualsiasi domanda o ulteriori informazioni, non esitare a contattare il proprietario del progetto via email o tramite [LinkedIn](https://www.linkedin.com/in/your-username/).
