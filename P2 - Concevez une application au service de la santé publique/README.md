# Concevez une application au service de la santé publique

## Projet 2 OpenClassrooms - Julien Gremillot


# Présentation de l’idée d’application

À la suite d’une exploration des données présentes sur le site « Santé publique France », j'ai pu remarquer que les produits listés détaillaient leurs valeurs nutritionnelles (plus ou moins précisément) mais que __seule une fraction d'entre eux disposaient d'un nutriscore calculé__ .

Le but de l’application serait de permettre l'affichage d'un nutriscore pour les produits qui n'en disposeraient pas encore. À l’aide d’un téléphone portable, l'utilisateur pourrait ainsi soit prendre en photo les ingrédients d'un produit, soit rentrer le code du produit dans l'application, et obtiendrait un nutriscore estimé correspondant.

L’intérêt de l’application résiderait également dans le fait que les produits pour lesquels les valeurs nutritionnelles ne sont pas complètement renseignées pourraient également obtenir une estimation du nutriscore.

Dans un second temps, l'application pourrait éventuellement lui conseiller des produits de la même catégorie qui auraient un meilleur nutriscore que celui demandé.

# Opérations de nettoyage effectuées

![](img/PSant%C3%A9_03_presentation0.png)

1 – Valeurs manquantes

La première constatation réalisée sur le jeu de données s’est faite en sortant le pourcentage de valeurs manquantes pour chaque type de données.

Ainsi, sur 186 colonnes proposées dans le tableau de données, il en existe 119 dont les données sont manquantes à plus de90%.

J’ai donc commencé par supprimer ces colonnes.

# 2 - Données propres à la base OpenFoodFacts

Certaines colonnes faisaient références à des données propres à la gestion de la base en elle-même, comme l’auteur de la saisie, les dates de création/modification des données, l’état de complétion pour chaque produit, etc.

D’autres n’avaient également pas d’intérêt d’analyse, comme les URLs des fiches produits, des images associées, etc.

Ces colonnes ont été également supprimées.

# 3 – Valeurs nutritionnelles incorrectes

Plusieurs colonnes suffixées par « _100g » correspondent à des valeurs nutritionnelles pour 100g de produit. Il devrait être impossible que ces valeurs soient négatives ou supérieures à 100.

Les lignes comportant des valeurs incorrectes ont été supprimées.

# 4 - Valeurs nutritionnelles absentes

Puisque notre application vise à estimer un nutriscore en se basant sur un minimum de valeurs nutritionnelles, j’ai également supprimé les lignes pour lesquelles aucune des colonnes conservées de valeurs nutritionnelles n’était renseignée.

# 5 - Valeurs nutritionnelles aberrantes (outliers)

![](img/PSant%C3%A9_03_presentation1.png)

J’ai utilisé des boites à moustaches (boxplots) sur les valeurs nutritionnelles afin de vérifier la présence de valeurs aberrantes

En me basant sur la méthode de l'intervalle interquartile (IQR) de suppression des outliers, j’ai donc procédé à l’élimination des lignes comportant des valeurs inférieures ou supérieures selon un ratio de 1,5 fois les bornes des premier et troisième quartiles.

Ce traitement a entrainé la plus grosse suppression de lignes, avec 510.433 lignes supprimées.

# 6 – Doublons dans les données

J’ai ensuite cherché d’éventuels doublons dans les données, en commençant par les codes :

103 lignes ont pu être supprimées car ces codes produits étaient mentionnés en double dans la base.

Des recherches de doublons par nom de produit, puis par couple nom/marque, puis par ensemble nom/marque/quantité renvoyaient toujours trop de lignes.

Je n’ai donc pas poursuivi sur cette piste avec laquelle je ne me suis pas senti en confiance pour supprimer des lignes.

# 7 – Remplacement des valeurs manquantes

### Intuition

Avant de procéder à la recherche d’une méthode pour remplacer les valeurs
manquantes dans notre jeu de données, j’ai voulu vérifier une intuition qui me
laisser penser qu’il ne serait pas correct de fixer une même valeur nutritionnelle
à des produits très différents, par exemple le taux de graisse devrait être
quasi inexistant pour des fruits alors qu’il serait élevé pour des sauces.

J’ai donc fait une première corrélation entre les catégories issues de la colonne
« pnns_groups_1 » et le nutriscore.

Cette première analyse m’a conforté dans mon intuition et j’ai donc continué
mes traitements en réalisant à chaque fois une boucle sur ces catégories.

# Pourcentages de valeurs manquantes et sélection des méthodes

J’ai commencé par vérifier le pourcentage de valeurs manquantes pour les colonnes des valeurs nutritionnelles :

Ainsi, j’ai pu distinguer 2 groupes très différents de valeurs : celles qui étaient manquantes à moins de 10%, et celles à plus de 70%.

J’ai donc choisi de procéder de 2 manières différentes pour le remplissage des valeurs manquantes :

La médiane de la catégorie pour les colonnes dont le pourcentage manquant est > 70%

La valeur estimée par un modèle KNN pour les données les mieux renseignées

Le calcul de la médiane pour chaque catégorie a été relativement simple.

![](img/PSant%C3%A9_03_presentation2.png)

# Estimation des valeurs manquantes par un modèle KNN

Pour cette partie, j’ai utilisé le module KNNImputer de Scikit-Learn.

J’ai commencé par un traitement utilisant un nombre de voisins fixé arbitrairement (3) et j’ai pu constater que malgré
le nettoyage des données, le volume provoquait un temps de traitement allant jusqu’à 3h30 sur ma machine.

Ensuite, j’ai cherché à déterminer la valeur de K (nombre de voisins) optimum pour le traitement, en testant une plage
de nombres impairs entre 1 et 19. Après le traitement d’imputation sur les valeurs manquantes, j’ai procédé à un
découpage train/test et vérifié le taux d’erreur obtenu, pour chacune des colonnes de mon jeu de données.

Cette série de traitement m’a permis de déterminer que la valeur K=17 constituait le meilleur choix pour le
remplacement définitif des valeurs manquantes sur ces données.

J’ai donc pu sauvegarder mon jeu de données nettoyé et complété avant de passer à l’étape suivante.

# Conclusion du nettoyage

Je suis parti d’une base de 1 888 730 lignes et 186 colonnes, pour arriver après nettoyage à une base de 967 012
lignes et 52 colonnes.

En taille de fichiers, je suis passé de 4Go à 500Mo.

Sur les lignes restantes, seules 425672 (44%) disposent d’un nutriscore renseigné, ce qui valide le besoin de
l’application.

Sur les colonnes restantes, nous avons identifié pour notre application :

* 1 colonne de catégorie
* 2 colonnes de nutriscore
* 11 colonnes de valeurs nutritionnelles

![](img/PSant%C3%A9_03_presentation3.png)

# Description et analyse univariée des différentes variables importantes

1 – Catégories

La catégorie étant l’une des variables importantes de ces données, j’ai commencé par vérifier le nombre de produits dans
chacune d’entre elles.

![](img/PSant%C3%A9_03_presentation4.png)

# 2 – Le nutriscore

J’ai également recherché la répartition des différentes valeurs de nutriscore présentes globalement dans le jeu de
données

![](img/PSant%C3%A9_03_presentation5.png)

![](img/PSant%C3%A9_03_presentation6.png)

# Lien entre« nutrition-score-fr_100g » et « nutriscore_grade »

J’ai cherché à mieux comprendre le lien entre la valeur de la colonne « nutrition-score-fr_100g » et le nutriscore
lui-même (colonne « nutriscore_grade »).

Les courbes obtenues présentent des zones de recoupement semblant étranges, mais vérifient globalement les valeurs que
j’ai pu trouver sur internet.

![](img/PSant%C3%A9_03_presentation7.png)

# Matrice de corrélation

Pour confirmer la relation entre les deux colonnes, j’ai calculé la matrice de corrélation entre les colonnes
nutrition-score-fr_100g  et nutriscore_grade.

# Distribution du nutriscore

![](img/PSant%C3%A9_03_presentation8.png)

En examinant la distribution du nutriscore (colonne numérique « nutrition-score-fr_100g) on remarque que celle-ci
correspond à une distribution bimodale.

# 3 – Distributions des valeurs nutritionnelles

J’ai examiné la distribution des valeurs nutritionnelles restantes dans notre jeu de données, dont voici deux exemples :

![](img/PSant%C3%A9_03_presentation9.png)

![](img/PSant%C3%A9_03_presentation10.png)

Aucune des distributions visualisées ne semble particulière, elles sont globalement unimodales.


# Analyse multivariée et résultats statistiques

![](img/PSant%C3%A9_03_presentation11.png)

![](img/PSant%C3%A9_03_presentation12.png)

1 – Nutriscore par catégorie

L’analyse des nutriscores par catégorie donne des résultats qui semblent très cohérents :

Les catégories « alcool » et « snacks sucrés » présentent une majorité de mauvais nutriscores, tandis que les catégories
« fruits & légumes » et « céréales » présentent une majorité de bons nutriscores.

![](img/PSant%C3%A9_03_presentation13.png)

![](img/PSant%C3%A9_03_presentation14.png)

On constate des distributions très différentes en fonction de chaque catégorie, par exemple si on reprend deux
catégories très différentes : les « fruits et légumes » et les « snacks sucrés »

# 2 - Valeurs nutritionnelles par catégorie

J’ai ensuite visualisé les distributions de nos différentes valeurs nutritionnelles par catégorie.
Pour faciliter la lecture des visualisations, pour chaque catégorie j’ai divisé les valeurs nutritionnelles en 2
sous-ensembles pour obtenir 2 graphiques différents, en raison des différences d’échelle entre les valeurs.

![](img/PSant%C3%A9_03_presentation15.png)

![](img/PSant%C3%A9_03_presentation16.png)

J’ai également réalisé une analyse sous la forme de boxplots entre les catégories et les valeurs nutritionnelles dont voici deux exemples

![](img/PSant%C3%A9_03_presentation17.png)

Enfin, j’ai réalisé un test chi-2 entre les catégories et le nutriscore.
On vérifie que certaines catégories sont fortement corrélées avec le nutriscore :
* bon nutriscore pour les fruits
* * mauvais pour les snacks sucrés

![](img/PSant%C3%A9_03_presentation18.png)

![](img/PSant%C3%A9_03_presentation19.png)

# 3 - Valeurs nutritionnelles et nutriscore

J’ai également réalisé le même type d'analyse bivariée à l’aide de _boxplots_ entre le nutriscore et les valeurs
nutritionnelles.

Sur ces deux exemples, on constate que les produits de nutriscore « E » sont ceux présentant une distribution
élevée de « gras », tandis que les produits de nutriscore « A » présentent une plus grande quantité de
« fibres ».

![](img/PSant%C3%A9_03_presentation20.png)

![](img/PSant%C3%A9_03_presentation21.png)

# Matrice de corrélation valeurs nutritionnelles et nutriscore

Pour cette analyse, j’ai calculé la matrice de corrélation entre les valeurs nutritionnelles et le nutriscore (en
prenant en compte la valeur numérique de la colonne « nutrition-score-fr_100g »)

On a donc une corrélation forte avec certaines valeurs nutritionnelles, et moins importantes avec d'autres.

On remarque également une forte corrélation de certaines valeurs nutritionnelles entre elles (ex: fat &saturated_fat,
salt& sodium,sugar& carbohydrates)

# 4 – Réalisation d’une ACP (Analyse en Composantes Principales)

En examinant les colonnes des valeurs nutritionnelles, nous commençons par afficher l’éboulis des valeurs propres:

Ici nous n’avons pas précisé le nombre de composants, mais paramétré scikit-learn pour conserver 80% de la variance.

![](img/PSant%C3%A9_03_presentation22.png)

# Cercle des corrélations

Si on regarde les deux premiers plans, on vérifie les corrélations déjà observées et on peut en déduire les
interprétations suivantes :

* F1 : le gras (fat + saturated_fat) et le sel
* F2 : le sucre (sugars + carbohydrates)
* F3 : gras + sucre
* F4 : vitamines + sel

![](img/PSant%C3%A9_03_presentation23.png)

# Projection des individus

J’ai projetté séparément les différents nutriscores pour une meilleure visualisation.

On constate sur le premier plan qu’en descendant de nutriscore, les individus sont décalés vers la droite et le haut
(gras & sucre).

Sur le second plan, la population se décale également vers la droite (gras et sucre).

![](img/PSant%C3%A9_03_presentation24.png)

![](img/PSant%C3%A9_03_presentation25.png)

# Conclusions

Notre analyse a bien montré le lien entre les valeurs nutritionnelles et le nutriscore, en fonction de la catégorie du
produit.

On sait que le nutriscore n’est pas disponible pour un grand nombre de produits.

L’application semble réalisable et pertinente : elle ne permettra pas un simple calcul du nutriscore, mais sera capable
d’estimer les valeurs nutritionnelles manquantes en fonction de la catégorie du produit, afin de fournir une estimation
du nutriscore même lorsque le calcul est impossible.

