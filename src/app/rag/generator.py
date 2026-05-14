import ollama

from src.app.config import LLM_MODEL, OLLAMA_HOST


class Generator:

    def __init__(self):

        self.model_name = LLM_MODEL
        self.client = ollama.Client(
            host = OLLAMA_HOST
        )

    def generate(self, query, context):

        prompt = f"""
Eres un asistente bancario especializado en productos y servicios del BCP.

INSTRUCCIONES:
- Responde únicamente usando la información del contexto.
- Prioriza la información más relevante para la pregunta.
- No mezcles información de temas distintos.
- Si el contexto contiene varias respuestas, usa la más relacionada con la pregunta del usuario.
- No inventes información.

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.client.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]   