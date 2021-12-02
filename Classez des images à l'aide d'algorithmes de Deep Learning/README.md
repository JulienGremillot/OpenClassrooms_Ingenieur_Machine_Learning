![](img/P6_05_presentation0.jpg)

# Classification d’images à l'aide d'algorithmes de Deep Learning

## Parcours OpenClassrooms Ingénieur Machine Learning
Projet 6 – novembre 2021
Julien Gremillot

# Le projet

* Le but de ce projet est d’obtenir un algorithme capable de classer des images en fonction de la race du chien présent sur l'image\.
* Les données à disposition sont le «[Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)»
  * 120 races dechiens
  * Environ ~150 images par race
  * Nombretotald’images: 20 580

![](img/P6_05_presentation1.png)

# Les données

* Récupération des données
  * 741 Mo d’images
* Division en jeux train / valid :
  * 80% \(16 464 images\) pour entrainement
  * 20% \(4 116 images\) pour la validation
* Uniformisation des tailles au format 224 x 224 pixels

# Mon réseau CNN

![](img/P6_05_presentation2.png)

* En m’inspirant du réseau VGG étudié en cours\, j’ai assemblé un CNN composé des couches suivantes :
  * Rescaling
  * Convolution \+ MaxPooling \(x2\)
  * Flatten
  * Dense \(x2\)
  * Dense avec 120 sorties

![](img/P6_05_presentation3.png)

# Premiers résultats

* Entrainement du CNN sur 10 epochs
* Premiers résultats très mauvais :
  * L’accuracy est très faible – quasiment 1/120
  * Les valeurs de loss sont hautes et ne varient pas – le modèle n’apprend rien

# Réduction de la complexité

![](img/P6_05_presentation4.png)

12 races \(10%\)

L’accuracy est meilleure\, mais entre 1/10 et 1/12…

La valeur de loss est réduite

![](img/P6_05_presentation5.png)

# Augmentation de données

![](img/P6_05_presentation6.png)

symétrie

rotation aléatoire

zoom aléatoire

![](img/P6_05_presentation7.png)

![](img/P6_05_presentation8.png)

* Ajout :
  * Translation aléatoire
  * Contraste aléatoire

![](img/P6_05_presentation9.png)

# Passage des images en noir et blanc

![](img/P6_05_presentation10.png)

# Optimisation des hyper-paramètres

Utilisation de Keras Tuner

![](img/P6_05_presentation11.png)

![](img/P6_05_presentation12.png)

# Entrainement avec les hyper-paramètres

![](img/P6_05_presentation13.png)

# Entrainement sur les 120 races

![](img/P6_05_presentation14.png)

Avec les mêmes hyper\-paramètres sur le jeu de données initial

11% d’accuracy sur le jeu de validation avec 120 races

![](img/P6_05_presentation15.png)

# Comparaison avec modèle VGG-16

![](img/P6_05_presentation16.png)

# Transfer Learning – ajout classifiers

![](img/P6_05_presentation17.png)

* Je charge le modèle VGG16 sans la dernière couche
* Je lui ajoute mes propres couches de classifiers
  * 1 x 1024
  * 1 x 12

# Transfer Learning – entrainement total

<span style="color:#000000">optimizer=</span>  <span style="color:#A31515">'adam'</span>

![](img/P6_05_presentation18.png)

# Transfer Learning – poids fixes

![](img/P6_05_presentation19.png)

![](img/P6_05_presentation20.png)

Je fixe les poids des premières couches

# Transfer Learning avec ResNet50

![](img/P6_05_presentation21.png)

![](img/P6_05_presentation22.png)

# Transfer Learning avec InceptionV3

![](img/P6_05_presentation23.png)

« Factorisation »

![](img/P6_05_presentation24.png)

«Depthwise Separable Convolutions »

![](img/P6_05_presentation25.jpg)

![](img/P6_05_presentation26.png)

# Transfer Learning avec EfficientNet

![](img/P6_05_presentation27.png)

![](img/P6_05_presentation28.png)

# Optimisation des hyper-paramètres

![](img/P6_05_presentation29.png)

![](img/P6_05_presentation30.png)

![](img/P6_05_presentation31.png)

# Augmentation des données

![](img/P6_05_presentation32.png)

![](img/P6_05_presentation33.png)

> 93% d’accuracy

# Passage en noir & blanc

![](img/P6_05_presentation34.png)

![](img/P6_05_presentation35.png)

# Equalization

![](img/P6_05_presentation36.png)

![](img/P6_05_presentation37.png)

![](img/P6_05_presentation38.png)

# Passage sur 120 classes

Au final, j’obtiens 81% d’accuracy sur le jeu de données complet, en utilisant les optimisations issues de mes tests sur 10% des classes.

Je sauvegarde les classes au format Pickle, et les poids du modèle au format h5.

# Utilisation du modèle

* J’ai réalisé un script qui :
  * Charge le modèle à partir de l’export
  * Charge les classes de prédictions
  * Traite l’image reçue en entrée
  * Réalise la prédiction
  * Sort les 3 premières races avec leurs taux de probabilité associés
  * 
* Utilisation en ligne de commande :

![](img/P6_05_presentation39.png)

![](img/P6_05_presentation40.png)

![](img/P6_05_presentation41.png)

![](img/CP6_05_presentation42.png)

![](img/P6_05_presentation43.png)

![](img/P6_05_presentation44.png)

![](img/P6_05_presentation45.png)

# Utilisation avec interface Gradio

J’ai utilisé la librairie de [Gradio](https://gradio.app/) permettant l’utilisation de mon modèle via une interface graphique dans le navigateur.

![](img/P6_05_presentation46.png)

# Pistes d’amélioration

* Augmenter le nombre de photos, notamment pour les races qui se ressemblent (ex:English foxhound\, Walker hound & Beagle)

![](img/P6_05_presentation47.jpg)

![](img/P6_05_presentation48.jpg)

![](img/P6_05_presentation49.jpg)

* Tester EfficientNetV2

[https://paperswithcode\.com/paper/efficientnetv2\-smaller\-models\-and\-faster](https://paperswithcode.com/paper/efficientnetv2-smaller-models-and-faster)

* Utiliser les Transformers à la place d’un CNN

[https://towardsdatascience\.com/are\-transformers\-better\-than\-cnns\-at\-image\-recognition\-ced60ccc7c8](https://towardsdatascience.com/are-transformers-better-than-cnns-at-image-recognition-ced60ccc7c8)


