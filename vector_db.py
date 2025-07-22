import faiss
import numpy as np

class VectorDB:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
    def add_vectors(self, vectors):
        self.index.add(np.array(vectors).astype('float32'))
    def search(self, vector, k=5):
        return self.index.search(np.array([vector]).astype('float32'), k)