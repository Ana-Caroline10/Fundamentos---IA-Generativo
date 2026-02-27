from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingManager:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.text_chunks = []
        self.embeddings = None

    def create_embeddings(self, text_chunks):
        self.text_chunks = text_chunks
        self.embeddings = self.model.encode(text_chunks)

    def search(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]

        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.text_chunks[i] for i in top_indices]
