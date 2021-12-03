# Catégorisation de questions

![](img/Cat%C3%A9gorisation%20de%20questions2.png)

## Julien Gremillot - Parcours OpenClassrooms - Ingénieur Machine Learning – PROJET 5

# Le Projet

![](img/Cat%C3%A9gorisation%20de%20questions4.png)

En utilisant les questions du site Stack Overflow et les tags qui leurs sont associées, le but final de ce projet est de suggérer des tags appropriésàde nouvelles questions.

![](img/Cat%C3%A9gorisation%20de%20questions5.png)

# Exploration des données

__Récupération des questions :__

  * __Avec tags__
  * __Avec réponses__
  * __1 réponse acceptée__
  * __Mise en favoris__
  * __Vues > 1000__
  * __Score > 10__

__188.065 questions (2008-2014)__

![](img/Cat%C3%A9gorisation%20de%20questions6.png)

![](img/Cat%C3%A9gorisation%20de%20questions7.png)

Exploration des données

__Nettoyage des données__

![](img/Cat%C3%A9gorisation%20de%20questions8.png)

'Title', 'Body' et 'Tags’

4.297 tags

Nettoyage préfixes (-6%)

![](img/Cat%C3%A9gorisation%20de%20questions9.png)

__41 tags présents plus de 100 fois__

![](img/Cat%C3%A9gorisation%20de%20questions10.png)

![](img/Cat%C3%A9gorisation%20de%20questions11.png)

Exploration des données

__Suppression du HTML__

__Concaténation « Title » & « Body »__

![](img/Cat%C3%A9gorisation%20de%20questions12.png)

![](img/Cat%C3%A9gorisation%20de%20questions13.png)

![](img/Cat%C3%A9gorisation%20de%20questions14.png)

Exploration des données

__Suppression des « stop__  __words__  __»__

![](img/Cat%C3%A9gorisation%20de%20questions15.png)

![](img/Cat%C3%A9gorisation%20de%20questions16.png)

![](img/Cat%C3%A9gorisation%20de%20questions17.png)

![](img/Cat%C3%A9gorisation%20de%20questions18.png)

![](img/Cat%C3%A9gorisation%20de%20questions19.png)

![](img/Cat%C3%A9gorisation%20de%20questions20.png)

![](img/Cat%C3%A9gorisation%20de%20questions21.png)

# ModélisationApproche non-supervisée

![](img/Cat%C3%A9gorisation%20de%20questions22.png)

![](img/Cat%C3%A9gorisation%20de%20questions23.png)

![](img/Cat%C3%A9gorisation%20de%20questions24.png)

![](img/Cat%C3%A9gorisation%20de%20questions25.png)

![](img/Cat%C3%A9gorisation%20de%20questions26.png)

Transformation de la liste de tags en matrice binaire à l’aide d’un __MultiLabelBinazer__ de la librairie scikit-learn

Découpage train / test

Vectorisation avec le __TfIdfVectorizer__

__Tests de__  __différents__  __modèles__

Optimisation avec __GridSearchCV__

![](img/Cat%C3%A9gorisation%20de%20questions27.png)

# Modélisation – approche semi-supervisée

CountVectorizer

LatentDirichletAllocation (13 « topics »)

OneVsRestClassifier(SVC(kernel='linear'))

![](img/Cat%C3%A9gorisation%20de%20questions28.png)

* Accuracy :  0.042
* Precision :  0.115
* Recall :  0.049
* F1 Score :  0.065
* Jaccard : 0.055

# Déploiement d’une API

Développement avec l'IDE « [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) »

Architecture issue du cours 
« [Concevez un site avec Flask](https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask) »

![](img/Cat%C3%A9gorisation%20de%20questions29.png)

[https://categorize-questions.herokuapp.com/](https://categorize-questions.herokuapp.com/)

![](img/Cat%C3%A9gorisation%20de%20questions30.png)

Traitement des questions :
* Suppression du HTML (BeautifulSoup)
* Passage en minuscules
* Tokenisation
* Suppression des « stop-words »
* Utilisation du modèle exporté.
* Récupération tags avec MultiLabelBinazer.

# Gestion des versions

![](img/Cat%C3%A9gorisation%20de%20questions31.png)

![](img/Cat%C3%A9gorisation%20de%20questions32.png)

Pour déploiement via Heroku:

[https://github.com/JulienGremillot/categorize-questions](https://github.com/JulienGremillot/categorize-questions)

![](img/Cat%C3%A9gorisation%20de%20questions33.png)

