from src.app.rag.retriever import Retriever
from src.app.rag.generator import Generator


class RAGPipeline:

    def __init__(self, collection):

        self.retriever = Retriever(collection)

        self.generator = Generator()

    def ask(
        self,
        query,
        top_k=10,
        category=None
    ):

        # Retrieve relevant chunks
        results = self.retriever.retrieve(
            query=query,
            top_k=top_k,
            category=category
        )

        # Extract retrieved documents
        retrieved_chunks = results["documents"][0]

        # Build context
        context = "\n\n".join(retrieved_chunks)

        # Generate grounded response
        answer = self.generator.generate(
            query=query,
            context=context
        )

        return {
            "query": query,
            "answer": answer,
            "retrieved_chunks": retrieved_chunks
        }