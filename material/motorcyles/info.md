# Valori possibili del dataset moto

Il dataset contiene 10.000 esempi generati a partire da 209 modelli reali di 19 marche, tutti sopra i 125 cc. I testi vanno da 525 a 2000 caratteri, con una media di 1270. Ogni campo ha al massimo 100 valori distinti; le tabelle riportano tutti i valori effettivamente presenti, con il numero di esempi in cui compaiono.

## File

| File | Contenuto |
|---|---|
| `train.jsonl` | 8.000 esempi in formato chat per `mlx_lm.lora` |
| `valid.jsonl` | 1.000 esempi per la validazione |
| `test.jsonl` | 1.000 esempi per il test finale |
| `dataset_completo.jsonl` | i 10.000 esempi con `id`, `modello`, `testo` e `dati`, comodi per analisi e controlli |

## marca (19 valori)

| Valore | Occorrenze |
|---|---|
| Aprilia | 545 |
| BMW | 822 |
| Benelli | 254 |
| CFMoto | 179 |
| Ducati | 902 |
| Fantic | 49 |
| Harley-Davidson | 500 |
| Honda | 975 |
| Husqvarna | 251 |
| Indian | 250 |
| KTM | 542 |
| Kawasaki | 892 |
| MV Agusta | 382 |
| Moto Guzzi | 368 |
| Moto Morini | 78 |
| Royal Enfield | 397 |
| Suzuki | 837 |
| Triumph | 895 |
| Yamaha | 882 |

## potenza_cv (100 valori)

Numero float. Nel testo compare in forme diverse: `73,4 CV`, `73.4 CV`, `settantatré virgola quattro cavalli`, `140,00 CV`, `125 CV (91,9 kW)`, `centoventicinque cavalli`.

| Valore | Occorrenze |
|---|---|
| 20.2 | 96 |
| 21.0 | 56 |
| 24.3 | 42 |
| 27.2 | 43 |
| 34.0 | 98 |
| 40.0 | 248 |
| 42.0 | 98 |
| 44.0 | 170 |
| 45.0 | 158 |
| 45.6 | 34 |
| 47.0 | 161 |
| 47.6 | 348 |
| 48.0 | 53 |
| 50.0 | 92 |
| 52.0 | 52 |
| 54.0 | 33 |
| 58.0 | 37 |
| 60.0 | 78 |
| 61.0 | 38 |
| 65.0 | 183 |
| 67.0 | 87 |
| 68.0 | 99 |
| 70.0 | 96 |
| 71.0 | 54 |
| 72.0 | 103 |
| 73.0 | 48 |
| 73.4 | 230 |
| 74.0 | 257 |
| 76.0 | 134 |
| 77.0 | 54 |
| 77.5 | 48 |
| 80.0 | 141 |
| 81.0 | 62 |
| 83.0 | 50 |
| 84.0 | 46 |
| 86.0 | 47 |
| 87.0 | 61 |
| 90.0 | 143 |
| 91.0 | 51 |
| 92.0 | 98 |
| 94.0 | 233 |
| 95.0 | 442 |
| 96.0 | 45 |
| 98.0 | 37 |
| 100.0 | 292 |
| 102.0 | 102 |
| 105.0 | 410 |
| 106.0 | 94 |
| 107.0 | 52 |
| 108.0 | 47 |
| 109.0 | 48 |
| 110.0 | 376 |
| 111.0 | 101 |
| 112.0 | 44 |
| 113.0 | 93 |
| 114.0 | 100 |
| 115.0 | 143 |
| 118.4 | 58 |
| 119.0 | 153 |
| 120.0 | 88 |
| 121.0 | 76 |
| 123.0 | 142 |
| 124.0 | 35 |
| 125.0 | 229 |
| 126.0 | 48 |
| 128.0 | 39 |
| 130.0 | 88 |
| 136.0 | 140 |
| 140.0 | 43 |
| 142.0 | 95 |
| 145.0 | 77 |
| 146.0 | 49 |
| 147.0 | 93 |
| 148.0 | 36 |
| 150.0 | 218 |
| 152.0 | 187 |
| 155.0 | 59 |
| 158.0 | 64 |
| 159.0 | 41 |
| 160.0 | 80 |
| 165.0 | 37 |
| 166.0 | 37 |
| 167.0 | 51 |
| 170.0 | 37 |
| 175.0 | 51 |
| 180.0 | 82 |
| 186.0 | 56 |
| 189.0 | 50 |
| 190.0 | 39 |
| 195.0 | 38 |
| 197.0 | 50 |
| 200.0 | 157 |
| 201.0 | 51 |
| 202.0 | 48 |
| 203.0 | 58 |
| 208.0 | 92 |
| 210.0 | 46 |
| 212.0 | 50 |
| 214.0 | 43 |
| 217.0 | 103 |

## cilindrata_cc (100 valori)

Numero float. Nel testo compare come `1254 cc`, `1.254 cc`, `1254 cm³`, `1254 centimetri cubi` oppure `milleduecentocinquantaquattro centimetri cubi`.

| Valore | Occorrenze |
|---|---|
| 313.0 | 98 |
| 321.0 | 98 |
| 349.0 | 96 |
| 373.0 | 170 |
| 374.0 | 56 |
| 398.0 | 144 |
| 399.0 | 91 |
| 451.0 | 200 |
| 452.0 | 55 |
| 457.0 | 48 |
| 471.0 | 229 |
| 500.0 | 148 |
| 599.0 | 202 |
| 600.0 | 48 |
| 636.0 | 41 |
| 645.0 | 153 |
| 648.0 | 161 |
| 649.0 | 395 |
| 659.0 | 169 |
| 660.0 | 62 |
| 675.0 | 94 |
| 689.0 | 230 |
| 693.0 | 300 |
| 696.0 | 45 |
| 698.0 | 53 |
| 744.0 | 52 |
| 745.0 | 37 |
| 749.0 | 60 |
| 750.0 | 89 |
| 754.0 | 40 |
| 755.0 | 98 |
| 765.0 | 94 |
| 773.0 | 53 |
| 776.0 | 96 |
| 779.0 | 39 |
| 782.0 | 44 |
| 798.0 | 246 |
| 799.0 | 141 |
| 800.0 | 46 |
| 803.0 | 48 |
| 821.0 | 48 |
| 847.0 | 46 |
| 853.0 | 219 |
| 883.0 | 50 |
| 888.0 | 47 |
| 889.0 | 138 |
| 890.0 | 153 |
| 895.0 | 88 |
| 896.0 | 88 |
| 900.0 | 105 |
| 931.0 | 35 |
| 937.0 | 230 |
| 942.0 | 33 |
| 947.0 | 50 |
| 948.0 | 104 |
| 955.0 | 102 |
| 975.0 | 45 |
| 998.0 | 435 |
| 999.0 | 393 |
| 1000.0 | 50 |
| 1037.0 | 52 |
| 1042.0 | 97 |
| 1043.0 | 138 |
| 1050.0 | 42 |
| 1077.0 | 51 |
| 1078.0 | 36 |
| 1079.0 | 47 |
| 1084.0 | 113 |
| 1099.0 | 53 |
| 1103.0 | 90 |
| 1133.0 | 109 |
| 1151.0 | 53 |
| 1158.0 | 37 |
| 1160.0 | 86 |
| 1170.0 | 151 |
| 1195.0 | 42 |
| 1197.0 | 40 |
| 1198.0 | 83 |
| 1199.0 | 44 |
| 1200.0 | 171 |
| 1202.0 | 94 |
| 1252.0 | 87 |
| 1254.0 | 140 |
| 1255.0 | 37 |
| 1262.0 | 136 |
| 1284.0 | 42 |
| 1298.0 | 49 |
| 1300.0 | 29 |
| 1301.0 | 89 |
| 1340.0 | 89 |
| 1380.0 | 45 |
| 1649.0 | 34 |
| 1746.0 | 50 |
| 1783.0 | 51 |
| 1802.0 | 51 |
| 1833.0 | 48 |
| 1868.0 | 137 |
| 1890.0 | 96 |
| 1923.0 | 82 |
| 2458.0 | 51 |

## fascia_prezzo (8 valori)

Gli intervalli sono chiusi a sinistra e aperti a destra: 10.000 € cade in `10.000 - 15.000 €`. Nel testo il prezzo è esatto in cifre (circa 35% degli esempi, per esempio `12.490 €`), esatto in lettere (circa 15%, per esempio `ventiduemila e settecento euro`), espresso come fascia (circa 25%, per esempio `tra i quindicimila e i ventimila euro`) oppure assente, e in quel caso il valore è `N/D`.

| Valore | Occorrenze |
|---|---|
| < 5.000 € | 243 |
| 5.000 - 7.500 € | 1616 |
| 7.500 - 10.000 € | 1190 |
| 10.000 - 15.000 € | 2370 |
| 15.000 - 20.000 € | 1277 |
| 20.000 - 30.000 € | 807 |
| > 30.000 € | 60 |
| N/D | 2437 |

## tipologia (14 valori)

Lista di stringhe: una moto può avere più tipologie, per esempio `["Sportbike", "Carenata"]` o `["Adventure", "Touring"]`. Le occorrenze contano ogni tag separatamente. Il testo contiene sempre il termine della tipologia (naked, supersportiva, carenata, tourer, adventure, cafe racer, eccetera) e non contiene mai quello di una tipologia non assegnata: lo script lo verifica su ogni esempio.

| Valore | Occorrenze |
|---|---|
| Adventure | 1995 |
| Bagger | 146 |
| Bobber | 407 |
| Cafe Racer | 198 |
| Carenata | 2001 |
| Classic | 1157 |
| Cruiser | 1190 |
| Enduro | 665 |
| Motard | 232 |
| Naked | 3277 |
| Scrambler | 432 |
| Sport-Touring | 586 |
| Sportbike | 1570 |
| Touring | 1245 |

## anno (21 valori)

Intero. Ogni anno rientra nel periodo di produzione reale del modello; nel testo compare in cifre (`2019`) o in lettere (`duemiladiciannove`).

| Valore | Occorrenze |
|---|---|
| 2005 | 7 |
| 2006 | 20 |
| 2007 | 34 |
| 2008 | 61 |
| 2009 | 74 |
| 2010 | 109 |
| 2011 | 154 |
| 2012 | 162 |
| 2013 | 246 |
| 2014 | 259 |
| 2015 | 286 |
| 2016 | 376 |
| 2017 | 453 |
| 2018 | 636 |
| 2019 | 690 |
| 2020 | 789 |
| 2021 | 931 |
| 2022 | 999 |
| 2023 | 1153 |
| 2024 | 1299 |
| 2025 | 1262 |

## Approssimazioni rispetto ai dati reali

Per restare entro i 100 valori distinti, pochi modelli hanno un valore portato al più vicino già presente. Potenza: 75 CV → 74 CV, 99 CV → 100 CV. Cilindrata: 411 cc → 399 cc, 499 cc → 500 cc, 1203 cc → 1202 cc, 450 cc → 451 cc, 449 cc → 451 cc. Potenze e cilindrate sono i valori dichiarati più comuni per il mercato europeo, e i prezzi sono stime di listino scalate per anno: vanno bene per l'addestramento, non come riferimento commerciale.
