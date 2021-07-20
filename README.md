# Wikipedia-CLI

Wikipedia-CLI je malá konzolová aplikace pro vyhledávání souhrnů ze článků české Wikipedie.

## Použíté knihovny a technologie
- [Python](https://www.python.org/) (>= 3.9.6 - kompatibilní s 3.7.8)
- [Wikipedia](htps://github.com/goldsmith/Wikipedia) (>= 1.4.0) - API wrapper pro získávání dat z wikipedie
- [Django ORM](https://github.com/dancaron/Django-ORM) (>= 3.2.5) - Samostatné ORM z frameworku [Django](https://www.djangoproject.com/)
- [CMD2](https://github.com/python-cmd2/cmd2) (>= 2.1.2) - Knihovna pro tvorbu konzolových aplikací
- [SQLITE3](https://docs.python.org/3/library/sqlite3.html) (>= 3.35.5) - Využitý databázový systém pro cache

## Instalace
1. Nainstalujte python v minimální verzi 3.7.8 (ideálně 3.9.6)
2. Spusťte script **install.sh** (pro Unix/Linux založené distribuce - předpokládá existenci /bin/bash) nebo **install.bat** (pro Windows)

## Spuštění
Zavoláním scriptu **main.py**  
**př.** D:\Apps\WikipediaApp\> **python main.py**  
**př.** user@localhost:/opt/WikipediaApp# /usr/bin/python3 main.py   

## Seznam příkazů
- **search <text>** - vyhledá článek s názvem <text> nebo vypíše seznam vhodných článků  
- **exit** (alias: stop, quit) - Ukončí aplikaci  
- **clear** - Vymaže výstup v konzoli
- **clear cache** - Vymaže všechna data v mezipaměti
- **clear history** - Vymaže všechny záznamy v historii příkazů
- **clear history <n>** - Vymaže <n> záznamů v historii příkazů