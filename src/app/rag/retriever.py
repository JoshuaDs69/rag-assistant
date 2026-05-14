from src.app.embeddings.embedder import Embedder


class Retriever:

    def __init__(self, collection):

        self.collection = collection

        self.embedder = Embedder()

    def retrieve(
        self,
        query,
        top_k=5,
        category=None
    ):

        # Generate query embedding
        query_embedding = self.embedder.encode_query(query)

        # Optional metadata filtering
        where_filter = None

        if category:

            where_filter = {
                "category": category
            }

        # Query ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_filter
        )

        return results