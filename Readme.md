# Pràctica MapReduce

> ## Primera part:  Carregar les dades al hdfs (15%)

Agafam 5 llibres de www.gutemberg.org 

- https://www.gutenberg.org/files/57654/57654-0.txt
- https://www.gutenberg.org/cache/epub/22045/pg22045.txt
- https://www.gutenberg.org/files/61339/61339-0.txt
- https://www.gutenberg.org/cache/epub/29640/pg29640.txt
- https://www.gutenberg.org/cache/epub/54430/pg54430.txt

Creem i obrim un [**script.sh**](script.sh)

```
touch script.sh
nano script.sh
```

Canviam els permisos de l'script

```
sudo chmod 777 script.sh
```

Executem l'script

```
./script.sh
```

> ## Segona part: Programa map reduce (75%)

*Crearem el programa amb Python*

*Per realitzar aquesta pràctica m'he basat en els següents enllaços:*

### 1. Cream [**mapper.py**](mapper.py)

*Llegirà les dades de STDIN i dividirà les línies en paraules, generarà una sortida de cada paraula amb el seu conteig individual*

Ens situem dedins la carpeta on es troben els nostres llibres

```
cd books
```

Creem i obrim l'script

```
touch mapper.py
nano mapper.py
```

L'intèrpret de Python 3 utilitza UTF-8 per la codificació per defecte, mentres que Python 2 utilitza ASCII por defecte, per aquest motiu ens dóna un error:

```diff
- SyntaxError: Non-ASCII character '\xc3'
```

Per solucionar-ho, escrivim la següent línia al començament de l'script
```
# -*- coding: utf-8 -*-
```

Executem l'script amb:

```
cat file.txt | python mapper.py
```


### 2. Cream [**reducer.py**](reducer.py)

*Implementa la lògica de reducció. Llegirà la sortida de mapper.py des de STDIN i afegirà l'aparició de cada lletra i escriurà la sortida final a STDOUT*

Executem 

```
cat 57654-0.txt | python mapper.py | sort -k1,1 | python reducer.py
```

NECESSITEM INSTAL·LAR PIP I LES LLIBRERIES DE PYTHON