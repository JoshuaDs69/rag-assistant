import ollama

from src.app.config import EMBEDDING_MODEL, OLLAMA_HOST


class Embedder:

    def __init__(self):

        self.model_name = EMBEDDING_MODEL
        self.client = ollama.Client(
            host = OLLAMA_HOST
        )

    def encode(self, texts):

        embeddings = []

        for text in texts:

            response = self.client.embed(
                model=self.model_name,
                input=text
            )

            embeddings.append(
                response["embeddings"][0]
            )

        return embeddings

    def encode_query(self, query):

        response = self.client.embed(
            model=self.model_name,
            input=query
        )

        return response["embeddings"][0]