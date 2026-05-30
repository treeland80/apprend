def search_answer(question, files):
    best_score = 0
    best_answer = "Je ne sais pas encore."

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        score = sum(1 for word in question.lower().split() if word in content)

        if score > best_score:
            best_score = score
            best_answer = content[:300]

    return best_answer