
import os
import json


DOSSIER = "data"
HISTORY_FILE = "memory/historique.json"


# ======================
# CHARGER DOCUMENTS
# ======================
def charger_documents():
    documents = []

    for fichier in os.listdir(DOSSIER):
        if fichier.endswith(".txt"):
            chemin = os.path.join(DOSSIER, fichier)

            with open(chemin, "r", encoding="utf-8") as f:
                texte = f.read().lower()
                documents.append((fichier, texte))

    return documents


# ======================
# RECHERCHE SIMPLE IA
# ======================
def chercher(question, documents):
    mots = question.lower().split()
    resultats = []

    for nom, texte in documents:
        score = 0

        for mot in mots:
            if mot in texte:
                score += 1

        if score > 0:
            resultats.append((score, nom, texte))

    resultats.sort(reverse=True)
    return resultats


# ======================
# REPONSE
# ======================
def repondre(resultats):
    if not resultats:
        return "Je n'ai pas trouvé d'information."

    score, nom, texte = resultats[0]

    return f"Selon {nom} :\n\n{texte[:300]}..."


# ======================
# MEMOIRE
# ======================
def save_history(user_input, response):
    data = {
        "input": user_input,
        "response": response
    }

    os.makedirs("memory", exist_ok=True)

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")


# ======================
# IA PRINCIPALE
# ======================
def chat():
    documents = charger_documents()

    while True:
        question = input("\nToi : ")

        if question.lower() in ["quit", "exit"]:
            break

        resultats = chercher(question, documents)
        reponse = repondre(resultats)

        print("\nIA :", reponse)

        save_history(question, reponse)


# LANCEMENT
chat()