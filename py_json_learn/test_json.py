#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================

import json


fichier="test.json"

with open(fichier) as f:
    data = json.load(f)


#print(json.dumps(data, indent=2))

for item in data["lists"]["ressources"]:
    auteur = item["core"]["author"]
    titre = item["core"]["titre"]

    print(f"{auteur} a écrit \"{titre}\".")
