import json


mat_list = []

with open(file="censor/mat.txt", mode="r", encoding="utf-8") as file:
    for row in file:
        word = row.lower().split("\n")[0]
        if word:
            mat_list.append(word)

with open(file="censor/cenz.json", mode="w", encoding="utf-8") as file:
    json.dump(obj=mat_list, fp=file, ensure_ascii=False)
