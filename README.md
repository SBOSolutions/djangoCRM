# djangoCRM

suivi du tuto disponible à cette adresse, tuto de JustDjango https://youtu.be/fOukA4Qh9QA
volontairement les notes du README sont en français (voir pardon Franglais). 
Mais le code respecte les bonnes pratiques et les commentaires sont en anglais.

Lien vers le tuto [YouTubeJustDjangoCRMTuto](https://youtu.be/fOukA4Qh9QA) from JustDjango

## Version des outils
Python 3.9
Django Version 3.1.  (end of support end 2021!)

## Step by step
### Preparation de l'environnement 
Rq: j'utilise $> pour signifier le début d'une instruction bash

-> on suppose que python3 est installé, venv également, pip3 également et git + vscode

creation d'un reépertoire : git init, ajout d'un fichier .gitignore avec env à l'interieur
via vscode sync avec github et création d'un repository

ajout d'un environnement virtuel(venv ou virtualenv): $> python3 -m venv env
activation de l'environnement virtuel: $> source env/bin/activate

### Mes extentions VSCODE Django
Django from Roberth Solis
Django template from bibhasdn

### Django ?
Django est un framework Python
il est gratuit et OpenSource
encourage les developpements rapides (rapid dev approach)
Depuis 2005 (il y a une équipe derière Django même si c'est OpenSource)
focus sur la sécurité
Scalable (Sentry https://sentry.io/welcome/, Udemy, Instagram, OPENedX,...)

### Demmarage du project
installation de Django $> pip install django==3.1.5
creation du fichier de requirements :$> pip freeze > requirements.txt

ajout d'un projet django: $> django-admin startproject djcrm .
le  . permet de garder le projet à la racine de notre repertoire master

lancement du serveur: $> python manage.py runserver
lancement de la migration (database): $> python manage.py migrate   
TODO: en prod nous nous bancherons sur postgresql en dev pour le moment on reste du sqlite3

### Creation de l'application LEADS
une application est un module de notre projet (leads, sales, ...)
$> python manage.py startapp leads


#### ajout models
models => "tables de la base de données"

ajout d'une class pour définir la table des leads
```python
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
```

prise en compte dans la base de données: 
$> python manage.py makemigrations
$> python manage.py migrate
(si erreurs ou trop de modification dans la database dans ce cas on efface la base de données.)

### ajout de la gestion des utilisateurs
on ajoute une classe en héritage du model abstrait de données utilisateur 
pour faire des potentielles modification dans le futur sans alterer le moteur django.
```python
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

ne pas oublier de modifier le fichier settings du projet: 
AUTH_USER_MODEL = 'leads.User'

Rq: il est possible de lancer un shell dans notre terminal pour django avec la commande:
$> python manage.py shell

#### creation du superuser
$> python manage.py createsuperuser

### views
 
 pour la gestion des vues dans Django la gestion est la suivante:  
 on commence par ajouter une fonction dans le fichier views.py :  
 exemple:  
 ```python
from django.shortcuts import render

def home_page(request):
    return render(request, "second_page.html")
 ```

pour le fonctionnement du render: si on ne précise rien alors on recupere la page dans le dossier templates
à la racine de notre repertoire, sinon on utilise le templates de l'application

cette fonction nous permet l'affichage d'une page html (css, JS...) sur notre application

il faut déclarer l'appel à la vue dans le fichier url.py de notre projet
exemple:  
```python
from django.contrib import admin
from django.urls import path
from leads.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page)
]
```

#### ...
