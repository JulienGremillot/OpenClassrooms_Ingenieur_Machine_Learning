# Anticipez les besoins en consommation électrique de bâtiments

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents0.jpg)

## Julien Gremillot - Parcours OpenClassrooms - Ingénieur Machine Learning – PROJET 3

# 1 – L’analyse exploratoire

## Source des données

J’ai téléchargé les 2 fichiers de données de consommation énergétique de la ville de Seattle disponibles sur le site Kaggle.

Les données concernent 2 années successives, mais leur format diffère légèrement : l’un fait 47 colonnes et l’autre 46.

En réalité, 9 colonnes manquent au premier par rapport à l’autre, et 10 colonnes dans l’autre sens.

Ma première tâche consiste donc à uniformiser.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents1.png)

# Uniformisation des données

L’une des colonnes du fichier 2015 (« Location »), comporte des informations supplémentaires sérialisées en JSON.

On peut facilement désérialiser ces données et créer des colonnes au format du fichier 2016.

D’autres colonnes portent des noms différents mais contiennent le même type d’information (vérification faite sur la description des fichiers disponible sur le [site de la ville de Seattle](https://data.seattle.gov/dataset/)) : on les renomme

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents2.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents3.png)

# Suppression des colonnes inutiles

Après la suppression des colonnes de commentaires (presque entièrement vides), je supprime également les 6 colonnes présentes uniquement dans le fichier 2015 :

Les 2 jeux de données ont maintenant le même format, avec 45 colonnes restantes.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents4.png)

# Fusion des jeux de données

Après avoir vérifié l’unicité du OSEBuildingID pour chaque fichier, je vérifie la correspondance des bâtiments entre les 2 fichiers.

On va concaténer les deux fichiers et dédoublonner via l’OSEBuildingID (en conservant les lignes les plus récentes – 2016 – pour les doublons).

On obtient un jeu de données final de 3 432 individus.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents5.png)

# Taux de remplissage des colonnes

Je regarde ensuite quelles sont les colonnes les moins renseignées.
Finalement, assez peu de données manquantes.

Pour commencer, je complète les colonnes de surfaces «GFA» avec des 0.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents6.png)

# Suppression de colonnes

* Les 2 colonnes les moins renseignées ("YearsENERGYSTARCertified" et "Outlier") ne semblent pas présenter d’intérêt et je décide de les supprimer.
* J'étudie ensuite certaines colonnes de notre jeu de données :
  * Les colonnes "City" et "State" comportent toujours les mêmes valeurs (Seattle, WA).
  * La colonne "DataYear" ne comporte que 2 valeurs en fonction du fichier d'origine (2015 ou 2016).
  * La colonne "DefaultData" donne des informations sur l'ajout de valeurs par défaut, mais sans préciser laquelle.
  * La colonne "ZipCode" est numérique mais correspond en réalité à une catégorie de localisation. On en a déjà pas mal d'autres (District,Neighborhood, Latitude/Longitude...).
* Je supprime donc ces colonnes.

# Suppression des bâtiments d’habitation (1)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents7.png)

La colonne «BuildingType» nous permet d’identifier et de supprimer des lignes d’individus correspondant à des bâtiments d’habitation.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents8.png)

La colonne «PrimaryPropertyType» nous permet également d’identifier et de supprimer des lignes d’individus correspondant à des bâtiments d’habitation.

Suite à ces suppressions, notre jeu de données comporte 1 695 individus.

# Uniformisation des données

En examinant la distribution des données de la colonne «Neighborhood», je m’aperçois que des valeurs ont des casses différentes. Je mutualise donc ces valeurs.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents9.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents10.png)

# Distribution du nombre de bâtiments

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents11.png)

Pour la colonne «NumberofBuildings», je remplace les valeurs « nan » et « 0 » par « 1 », considérant que l’individu correspond au moins à 1 bâtiment.

Ci-contre sa distribution, en log sur l’ordonnée.

# Distribution du nombre d’étages

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents12.png)

Je remplace également ici les valeurs à « 0 » par « 1 », ainsi que la valeur max « 99 », qui est incorrecte d'après [la liste des plus hauts bâtiments de Seattle](https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_Seattle) trouvée sur Wikipedia.

# Distribution du score EnergyStar

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents13.png)

Après avoir observé la distribution du scoreEnergyStar, je complète les valeurs manquantes en utilisant la médiane du score (73).

# Distribution des consommations d’énergie

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents14.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents15.png)

On observe les distributions de la consommation du total et des différents types d’énergie référencés dans nos données.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents16.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents17.png)

# Distribution des quartiers et districts sur une carte

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents18.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents19.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents20.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents21.png)

Les bâtiments se concentrent en centre-ville, et c’est là qu’on retrouve les plus âgés, et ceux qui ont le plus d’étages.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents22.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents23.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents24.png)

# Remplacement de l’année de construction par l’âge

# Distribution de la surface des bâtiments

La plupart des bâtiments ayant des surfaces réduites, nous passons l’abscisse au log.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents25.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents26.png)

# Répartition des types d’énergie consommée

J’ai ajouté une colonne donnant le type d’énergie majoritairement consommée par chaque bâtiment.

On en déduit la répartition ci-contre.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents27.png)

# Répartition géographique des consommations et émissions

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents28.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents29.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents30.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents31.png)

# Matrice de corrélation et suppression de colonnes

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents32.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents33.png)

# Distribution de la consommation et des émissions

# Nettoyage et utilisation du OneHotEncoder

Pour finir cette exploration de données, j’ai :

- supprimé les colonnes que j’estimais inutiles pour le modèle (identifiants, nom,status, adresse…)

- encodé les colonnes catégorielles restantes (*PropertyUseType,BuildingType,PrimaryPropertyType,Neighborhood,energie) via un «OneHotEncoder»

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents34.png)

# 2 – Les tests de modèles

# 

# Séparation des features et targets

Mon but étant de prédire les émissions de CO2 et la consommation totale d’énergie de bâtiments, j’ai donc défini 2 cibles («target») différentes, correspondant à mes colonnes « consommation » et «emissions».

J’ai donc 118featureset 2targets, pour lesquelles je vais devoir entrainer 2 modèles distincts.

# 2a – Consommation

# 

# Séparation des données train/test et standardisation

- Je décide de conserver 20% de mes données pour le jeu de test.

- J’utilise unStandardScaler, uniquement sur mes colonnes non-binaires.

Le but de la standardisation est de « centrer/réduire » pour obtenir des valeurs en unités compatibles avec distribution de moyenne 0 et d'écart-type 1.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents35.png)

# Modèle « Dummy » et modèles linéaires

# Modèles non-linéaires

# Optimisation des modèles via GridSearchCV

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents36.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents37.png)

C’est finalement leXGBRegressoroptimisé qui obtient le meilleur score R2 : 81%

# Importance des features

On constate que le nombre d'étage et les surfaces des bâtiments sont très importantes pour prédire leur consommation d'énergie, mais également l'âge du bâtiment et sa position géographique.

Certains types de bâtiments semblent également déterminer la consommation.

# Comparaison des scores des modèles

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents38.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents39.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents40.png)

# Comparaison des temps d’exécution des modèles

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents41.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents42.png)

# 2b – Emissions

# 

# Modèle « Dummy » et modèles linéaires

# Modèles non-linéaires

# Optimisation des modèles via GridSearchCV

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents43.png)

Après optimisation des paramètres, c’est encore leXGBRegressoroptimisé qui obtient le meilleur score R2 : 71%

# Importance des features

Comme pour la consommation, le nombre d'étage et les surfaces des bâtiments sont très importantes pour prédire leur émissions de gaz à effet de serre, et également l'âge du bâtiment et sa position géographique.

Certains types de bâtiments semblent également déterminer la consommation.

On voit apparaître le type d’énergie consommée par les bâtiments : l’électricité est la 2e feature.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents44.png)

# Comparaison des scores des modèles

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents45.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents46.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents47.png)

# Comparaison des temps d’exécution des modèles

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents48.png)

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents49.png)

# 3 – Intérêt de l’EnergyStarScore	& conclusions

# 

# Intérêt de l’"ENERGY STAR Score" pour la prédiction d’émissions

J’ai supprimé la colonne «EnergyStarScore» des données et relancé le notebook.

![](img/Anticipez%20les%20besoins%20en%20consommation%20%C3%A9lectrique%20de%20b%C3%A2timents50.png)

# Meilleurs modèles

Pour les 2 cibles (consommation et émissions), le meilleur modèle - à la fois en terme de score et de temps d’exécution - est le __XGBRegressor__.

Dans les paramètres optimisés, on peut retenir le __n_estimators__ qui doit généralement être relevé.

La prise en compte du __EnergyStarScore__ semble avoir un effet important sur les performances obtenues par notre modèle sur la __consommation__.

Mais comme la mission le suggérait, l’EnergyStarScore n’a aucune influence sur les performance du modèle concernant les __émissions__.

