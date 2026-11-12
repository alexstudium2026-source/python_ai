from sentence_transformers import SentenceTransformer


def get_vectors(chunks):
    result = []
    for chunk in chunks:
        vector = get_vector(chunk)
        result.append([vector, chunk])
    return result


def get_vector(content):
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return model.encode(content)