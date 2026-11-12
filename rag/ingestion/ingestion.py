from rag.ingestion.loader import get_content
from rag.ingestion.cleaner import clean_content
from rag.ingestion.chunker import get_chunks
from rag.ingestion.embedder import get_vectors
from rag.ingestion.repository import save

content = get_content()
cleaned_content = clean_content(content)
chunks = get_chunks(cleaned_content)
vectors = get_vectors(chunks)
save(vectors)