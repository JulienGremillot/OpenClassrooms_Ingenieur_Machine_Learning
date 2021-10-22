import os
import pickle

# Je me positionne dans mon répertoire de travail personnel
os.chdir("C:\\Users\\Julien Gremillot\\OneDrive\\Documents\\" +
         "OpenClassrooms\\github\\" +
         "OpenClassrooms_Ingenieur_Machine_Learning\\" +
         "Catégorisez automatiquement des questions")

# Je charge le classifier entrainé via le notebook
classifier = pickle.load(open("classifier.pkl", 'rb'))

# et le multilabelbinazer
mlb = pickle.load(open("mlb.pkl", 'rb'))

# question de test - déjà nettoyée : TODO implémenter le nettoyage
question = "best file format configuration files creating framework php need " +\
    "configuration files files unavoidably large number entries format would " +\
    "best config files quantification best easily parsed php would nice write " +\
    "parsing code deal breaker remains easily read humans even large amount " +\
    "entries widely used standard custom formats succinctness appreciated " +\
    "started using xml quickly gave obvious reasons thought json yaml wanted "

# pas besoin si pipeline ? vq = vectorizer.transform([question])
res = classifier.predict([question])
first_tag = mlb.inverse_transform(res)[0][0]

print(first_tag)
