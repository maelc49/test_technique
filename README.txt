Repo Git contenant les 2 exercices du Test Technique MeilleureCopro

Exercice 1 - Dev

L'API est réalisée à l'aide de Django : le projet s'appelle exercice_dev, et l'app qui contient les codes s'appelle app_data.

Les données contenues dans le fichier csv ont été importés dans une base de données, avec les colonnes qui nous intéressent pour l'exercice.
Pour créer la base de données, il faut se rendre dans le dossier de l'application, et éxécuter la commande : 

python manage.py importation

Pour accéder à l'API, il faut éxécuter la commande :

python manage.py runserver

Il suffit d'accéder au serveur, qui se trouve à l'adresse : 127.0.0.1:8000/app_data

On peut alors connaitre le prix moyen ainsi que les quartiles à 10% et 90% de toutes les offres situées dans un département ou dans une ville spécifiques.
On peut également, à l'aide d'une annonce bienici, rajouter un bien dans la base de données.


Exercice 2 - Review

Cet exercice consiste en une refonte de code, sur une classe Tank. Le script Python contenu dans le repo est ma proposition de refonte de code, pour qu'il soit plus lisible et fonctionnel que celui proposé de base.
Le fichier Tank_reference.py est le fichier tel quel, le fichier Tank.py est le fichier qui comprend mes modifications.
