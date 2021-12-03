# Segmentez des clients d'un site de e-commerce

![](img/Segmentez%20des%20clients%20d%27un%20site0.jpg)

## Julien Gremillot - Parcours OpenClassrooms - Ingénieur Machine Learning – PROJET 4

# Analyse exploratoire

## Compréhension des données

Les données sont disponibles sous la forme de 9 fichiers CSV distincts

![](img/Segmentez%20des%20clients%20d%27un%20site1.png)

L’un des fichiers ne contient qu’une traduction des catégories de produits : c’est donc ce fichier que j’ai choisi de
traiter en premier


## Traduction des catégories

* 74 catégories dans le fichier «products»
* 71 catégories dans le fichier «category_name_translation»
  * > 2 catégories non-traduites + les valeurs « nan »
* J'ajoute les traductions manquantes dans le tableau de traduction.
* J’ajoute une catégorie «misc» pour les valeurs non renseignées.


## Merge « orders » & « customers »

On vérifie que le __customer_id__ est une jointure entre les tables orders & customers: on va donc commencer par faire 
un merge de ces 2 tables.

  * Nombre de lignes dans orders: 99441
  * Nombre de lignes dans customers: 99441
  * Nombre decustomer_iduniques dansorders: 99441
  * Nombre decustomer_iduniques danscustomers: 99441
  * Shape deorders: (99441, 8)
  * Shape decustomers: (99441, 5)
  * Shape de la table mergée: (99441, 12)
  * Shape de la table sans la colonne de jointure: ( __99441__ , __11__ )


## Merge avec « order_reviews »

On voit qu'il y a une colonne order_id commune à notre nouvelle table et à la table order_reviews, on regarde comment
merger :

  * Nombre de lignes dansorder_reviews: 100000
  * Nombre de lignes dans data: 99441
  * Nombre deorder_iduniques dansorder_reviews: 99441
  * Nombre deorder_iduniques dans data: 99441

Ces chiffres nous indiquent qu'il y a parfois plusieurs reviews pour une même commande.
On considère que pour une même commande, la __review__  __la plus récente__ est celle qui doit être conservée.
On trie donc par date de review avant de dédoublonner la table order_reviews.

  * Shape de order_reviews: (99441, 7)
  * Shape de data: (99441, 11)
  * Shape de la table mergée: ( __99441, 16__ )


# Merge avec « order_payments »

La table «order_payments» contient 103 886 lignes : on a donc des doublons, soit plusieurs paiements pour une même
commande. Il s’agit en fait de paiements avec __différents moyens de paiement__.

On pourrait dédoublonner en faisant simplement la somme des paiements, mais on perdrait l'information concernant le
__moyen de paiement__. On va donc ajouter l'information sur la commande avant de faire le total des paiements.

  * Shape de data: (99441, 16)
  * Shape de vouchers: (3866, 2)
  * Shape decredit_card: (76505, 2)
  * Shape deboleto: (19784, 2)
  * Shape dedebit_card: (1528, 2)
  * Shape de la table mergée: (99441, 20)

On ajoute la __somme des paiements__ pour chaque commande

  * Shape de data: (99441, 20)
  * Shape desum_payments: (99440, 2)
  * Shape de la table mergée: (99441, 21)

Il y a quelques 0 dans cette colonne, mais il semble que le montant soit correct :
le paiement est égal à la somme des prix des produits achetés plus les frais de transport. 
On considère qu'il s'agit de valeur erronées, on les supprime (4 lignes).
  

## Merge avec « order_items » (1/2)

On peut trouver une autre information dans la table "order_items" : le __nombre de produits achetés__. 
On ajoute une nouvelle colonne à nos données.
  * Shape de data: (99437, 23)
  * Shape denb_items: (98666, 2)
  * Shape de la table mergée: ( __99437, 24__ )
Si à l'inverse on regarde le nombre de commandes pour chaque produit, on peut en déduire une " __popularité__ " de
chaque produit (plus un produit est vendu, plus il est "populaire"). Or certains clients sont plus rassurés en achetant
les produits qui se classent dans les "meilleures ventes".

![](img/Segmentez%20des%20clients%20d%27un%20site19.png)

* Shape de order_items: (112650, 7)
* Shape de nb_orders_by_product: (32951, 2)
* Shape de order_itemsmergée: (112650, 8)
* Shape de data: (99437, 24)
* Shape de avg_popularite: (98666, 2)
* Shape de la table mergée: ( __99437, 25__ )

## Merge « order_items » & « products »

On merge les informations produits dans «order_items» :

  * Shape deorder_items: (112650, 8)
  * Shape deproducts: (32951, 9)
  * Shape de la tableorder_itemsmergée: (112650, 16)

On examine la distribution des catégories produits, on simplifie et on utilise OneHotEncoder:

![](img/Segmentez%20des%20clients%20d%27un%20site20.png)

![](img/Segmentez%20des%20clients%20d%27un%20site21.png)

![](img/Segmentez%20des%20clients%20d%27un%20site22.png)

## Merge avec « order_items » (2/2)

On choisit de conserver les valeurs de longueur de textes et du nombre de photos :

![](img/Segmentez%20des%20clients%20d%27un%20site23.png)

Puis on merge dans la table finale :

  * Shape de data: (99437, 25)
  * Shape desum_categs: (98666, 13)
  * Shape de la table mergée: ( __99437, 37__ )
  

## Examen des localisations

* Dans le fichier «customers» :
  * Nombre d'états différents : 27
  * Nombre de villes différentes : 4119
  * Nombre dezip_code_prefixdifférents : 14994

* Dans le fichier «geolocation» :
  * Nombre d'états différents : 27
  * Nombre de villes différentes : 8011
  * Nombre dezip_code_prefixdifférents : 19015

![](img/Segmentez%20des%20clients%20d%27un%20site32.png)

![](img/Segmentez%20des%20clients%20d%27un%20site33.png)

Distribution des états dans le fichier «customers»

## Regroupements par client

__Nombre de commandes__ par client

__Taille du commentaire__ laissé par le client

Colonnes précisant si la commande a été passée en __semaine ou le week-end__ , en renseignant 1 si c'est le cas et 0
si ce n'est pas le cas. Ainsi, les sommes par client me donneront le nombre de commandes passées la semaine ou le 
week-end.

Colonne du jour de la semaine de la commande, et je fais un groupby suivi d'un value_counts afin d'obtenir le 
__jour d'achat le plus fréquent__ du client.

De même, j’identifie __l'heure la plus fréquente__ pour la commande, par client.

Je transforme la date de la dernière commande en __temps écoulé depuis la dernière commande__ (en jours) et la première
en __temps écoulé depuis la première commande__.

Je calcule également le __temps de livraison__ pour la commande.

## Suppression des variables corrélées

![](img/Segmentez%20des%20clients%20d%27un%20site34.png)


# Approches de modélisation

## Segmentation RFM

La segmentation RFM est une méthode de segmentation principalement développée à l'origine pour les actions de marketing
direct des véadistes et qui s'applique désormais également aux acteurs du e-commerce et du commerce traditionnel.

La segmentation RFM prend en compte la Récence (date de la dernière commande), la Fréquence des commandes et le Montant
(de la dernière commande ou sur une période donnée) pour établir des segments de clients homogènes.

La segmentation RFM permet de cibler les offres, d'établir des segments basés sur la valeur des clients et de prévenir
l'attrition en identifiant des segments à risque.

Dans nos données ces variables correspondent à :
  * Récence = time_since_last_order (nombre de jours depuis la dernière commande)
  * Fréquence = nb_orders (nombre de commandes sur la période étudiée)
  * Montant = sum_payments (total des paiements)

## Distribution de la Récence

La Récence correspond à notre colonne «time_since_last_order»

![](img/Segmentez%20des%20clients%20d%27un%20site35.png)

## Distribution de la Fréquence

La Fréquence correspond à nb_orders (nombre de commandes sur la période étudiée)

![](img/Segmentez%20des%20clients%20d%27un%20site36.png)

## Distribution du Montant

Le Montant correspond à notre colonne «sum_payments»

On a beaucoup de petits paiements, on effectue donc un passage au log :

![](img/Segmentez%20des%20clients%20d%27un%20site37.png)

![](img/Segmentez%20des%20clients%20d%27un%20site38.png)

## Test 1 avec toutes les colonnes

![](img/Segmentez%20des%20clients%20d%27un%20site39.png)

![](img/Segmentez%20des%20clients%20d%27un%20site40.png)

![](img/Segmentez%20des%20clients%20d%27un%20site41.png)

![](img/Segmentez%20des%20clients%20d%27un%20site42.png)

![](img/Segmentez%20des%20clients%20d%27un%20site43.png)

Silhouette Coefficient: 0.162

## Test 2 avec les 3 colonnes "RFM"

![](img/Segmentez%20des%20clients%20d%27un%20site44.png)

![](img/Segmentez%20des%20clients%20d%27un%20site45.png)

![](img/Segmentez%20des%20clients%20d%27un%20site46.png)

![](img/Segmentez%20des%20clients%20d%27un%20site47.png)

![](img/Segmentez%20des%20clients%20d%27un%20site48.png)

![](img/Segmentez%20des%20clients%20d%27un%20site49.png)

Silhouette Coefficient: 0,367

### Moyennes des RFM par cluster

![](img/Segmentez%20des%20clients%20d%27un%20site50.png)

On interprète les caractéristiques des clusters :
  * 0 : ancien client
  * 1 : client récent, gros montant
  * 2 : client récent, petit montant
  * 3 : client qui commande souvent

## Test 3 : RFM + nombres + catégories

![](img/Segmentez%20des%20clients%20d%27un%20site51.png)

J’ai à nouveau fait un test avec les colonnes suivantes :

![](img/Segmentez%20des%20clients%20d%27un%20site52.png)

![](img/Segmentez%20des%20clients%20d%27un%20site53.png)

![](img/Segmentez%20des%20clients%20d%27un%20site54.png)

![](img/Segmentez%20des%20clients%20d%27un%20site55.png)

Silhouette Coefficient: 0,209

## Test 4 : RFM + note

J’ai ajouté aux colonnes « RFM » la note de satisfaction du client

![](img/Segmentez%20des%20clients%20d%27un%20site56.png)

![](img/Segmentez%20des%20clients%20d%27un%20site57.png)

![](img/Segmentez%20des%20clients%20d%27un%20site58.png)

![](img/Segmentez%20des%20clients%20d%27un%20site59.png)

![](img/Segmentez%20des%20clients%20d%27un%20site60.png)

Silhouette Coefficient: 0,318

![](img/Segmentez%20des%20clients%20d%27un%20site61.png)

![](img/Segmentez%20des%20clients%20d%27un%20site62.png)

## Conclusion segmentation

La meilleure segmentation obtenue en terme de coefficient de silhouette reste la « simple » segmentation RFM : Récence / Fréquence / Montant

On obtient donc les populations suivantes :

  * nouveau client
  * client qui commande souvent
  * client qui ne commande pas souvent, mais pour un gros montant
  * client qui commande de temps en temps, pour un petit montant

# Stabilité du modèle

## Stabilité 1 : augmentation Récence

J’ai fait une première simulation consistant à augmenter la récence progressivement et recalculer avec le modèle obtenu
précédemment les nouvelles répartitions dans les clusters.

![](img/Segmentez%20des%20clients%20d%27un%20site63.png)

![](img/Segmentez%20des%20clients%20d%27un%20site64.png)

On constate une rapide dégradation des résultats : quasiment tous les clients se retrouvent dans le même cluster après
4 mois.

Le modèle semble très instable, avec un effondrement dès le 2emois.

### ARI avec cette méthode

![](img/Segmentez%20des%20clients%20d%27un%20site65.png)

  * ARI 1 mois : -79.14971315150562
  * ARI 2 mois : -18.307005358270324
  * ARI 3 mois : 1.378514642705499
  * ARI 4 mois : -1.42240473963668
  * ARI 5 mois : 7.646988851102375
  * ARI 6 mois : 3.939774705703473
  * ARI 7 mois : 3.824441674281984
  * ARI 8 mois : 3.228914002622343
  * ARI 9 mois : 1.3271415232916262
  * ARI 10 mois : 0.17309312419603912
  * ARI 11 mois : 0.1012532747884434
  * ARI 12 mois : 0.1012532747884434

Le « Adjusted rand index » a des valeurs très étranges puisqu’il est censé produire un chiffre entre -1 et 1, où 1
signifie une correspondance parfaite et 0 un score proche de l’aléatoire.

C’est le signe d’une mauvaise piste dans cette première méthode.

## Stabilité 2 : retour dans le temps

Pour une meilleure vérification de la stabilité d'un modèle, je suis reparti des données fournies au modèle RFM et 
supprimé les clients des __6 derniers mois__ . Je manipule la récence pour « reculer » de 6 mois et entrainer 
mon modèle, puis procède à des prédictions par « pas » de 1 mois successifs.

![](img/Segmentez%20des%20clients%20d%27un%20site66.png)

![](img/Segmentez%20des%20clients%20d%27un%20site67.png)

![](img/Segmentez%20des%20clients%20d%27un%20site68.png)

![](img/Segmentez%20des%20clients%20d%27un%20site69.png)

![](img/Segmentez%20des%20clients%20d%27un%20site70.png)

![](img/Segmentez%20des%20clients%20d%27un%20site71.png)

![](img/Segmentez%20des%20clients%20d%27un%20site72.png)

![](img/Segmentez%20des%20clients%20d%27un%20site73.png)

Ici, le « Cluster 3 » qui concerne les clients les plus anciens, devient vite __majoritaire__ au fur et à mesure
que l’on avance dans le temps.

Le score ARI chute quasiment en ligne droite sur les 5 périodes comparées, et est divisé par 2 au bout de __3 mois__ .

Mon conseil aux équipes d’Olist serait donc de renouveler le modèle __tous les trimestres__ .

![](img/Segmentez%20des%20clients%20d%27un%20site74.png)

![](img/Segmentez%20des%20clients%20d%27un%20site75.png)


# Respect de la PEP 8

J’ai pris soin comme demandé dans le sujet du projet de respecter la norme PEP 8.

Pour cela, j’ai installé le module «pycodestyle» sur mon instanceJupyter, et utilisé les commandes

```
%load_ext
pycodestyle_magic
```

et

```
%pycodestyle_on
```

J’ai également suivi le cours OpenClassRooms
«[Écrivez du code Python maintenable](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable)»

![](img/Segmentez%20des%20clients%20d%27un%20site76.png)

