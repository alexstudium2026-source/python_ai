from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from rag.ingestion.repository import get_similar_chunks


def get(request):
    vector = get_vector(request)
    chunks = get_similar_chunks(vector)

    return chunks