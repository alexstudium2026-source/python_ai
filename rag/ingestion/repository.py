from pathlib import Path
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def save(vectors):
    current_dir = Path(__file__).resolve().parent
    database_path = current_dir.parent.parent / "database" / "database.txt"
    with open(database_path, "w", encoding="utf-8") as database:
        for vector, text in vectors:
            vector_str = " ".join(map(str, vector))
            database.write(f"{vector_str};{text}\n")

#
# def get_similar_chunks(vector, top_k=2):
#     current_dir = Path(__file__).resolve().parent
#     database_path = current_dir.parent.parent / "database" / "database.txt"
#     with open(database_path, "r", encoding="utf-8") as database:
#         chunks = []
#         for line in database:
#             parts = line.split(";", 1)
#             chunk_vector = np.fromstring(parts[0], sep=" ")
#             cos_sim = cosine_similarity([vector], [chunk_vector])[0][0]
#             chunks.append((parts[1].strip(), cos_sim))
#         chunks.sort(key=lambda x: x[1], reverse=True)
#         return chunks[0:4]
def get_similar_chunks(vector, top_k=2):

    if top_k < 1:
        raise ValueError("top_k должен быть больше 0")

    current_dir = Path(__file__).resolve().parent
    database_path = current_dir.parent.parent / "database" / "database.txt"

    with open(database_path, "r", encoding="utf-8") as database:
        chunks = []

        for line in database:
            parts = line.split(";", 1)

            chunk_vector = np.fromstring(parts[0], sep=" ")

            cos_sim = cosine_similarity(
                [vector],
                [chunk_vector]
            )[0][0]

            chunks.append((parts[1].strip(), cos_sim))

        chunks.sort(key=lambda x: x[1], reverse=True)

        return chunks[:top_k]