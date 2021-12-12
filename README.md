# OC_P9 Application Web Django

Neuvième projet de la formation "Développeur d'application - Python" d'OpenClassrooms dont le but est de créer une application Django permettant à des utilisateurs de demander ou donner des avis sur des livres.

## Pour commencer

Ces instructions vous permettent de récupérer une copie du projet pour le tester sur votre machine.

### Prerequis

Ce programme étant basé sur Python, il est nécessaire que celui-ci soit installé sur votre machine.
Vous pouvez télécharger Python [ici](https://www.python.org/downloads/)

### Installation

Pour ne pas entrer en conflit avec d'autres projets déjà existants, il est préférable d'exécuter le programme sous un environnement virtuel.

Voici les principales commandes pour:

1. créer l'environnement virtuel

```
python3 -m venv tutorial-env
```
2. activer l'environnement virtuel

```
tutorial-env\Scripts\activate.bat
```

Pour plus de détails sur l'installation d'un environnement virtuel, se reporter à [la documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html)

Il est également nécessaire d'installer les bibliothèques indispensables au bon fonctionnement du programme. 
Celles-ci sont listées dans le document `requirement.txt` et leur installation se fait via la commande suivante exécutée dans l'environnement virtuel que vous venez de créer:
```
pip install -r requirements.txt
```

## Exécution du programme

Une fois la console placée dans le dossier du programme, il suffit d'exécuter la commande suivante dans l'environnement virtuel:
```
python3 manage.py runserver
```

## Auteur

**Léo CAPOU** 

## Remerciements

* Tim
