import random

from .models import Content, Gender

def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    if len(contents) == 0:
        return Content("Erreur : pas de contenu en base", Gender['male'])
    else:
        return random.choice(contents)
