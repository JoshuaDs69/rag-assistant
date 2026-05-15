# Banking RAG Assistant with FastAPI and Ollama 🤖

A production-style Retrieval-Augmented Generation (RAG) assistant built with FastAPI, ChromaDB, Ollama, Docker and Streamlit, using a banking-focused corpus based on BCP public information.

<img width="1024" height="1024" alt="BCP RAG Assistant" src="https://github.com/user-attachments/assets/8a97142b-4021-4073-9068-a33df3320379" />

---

## Features

- Retrieval-Augmented Generation (RAG) pipeline
- Banking-focused question answering system
- FastAPI backend API
- Streamlit conversational frontend
- ChromaDB vector database integration
- Local LLM inference with Ollama
- Dockerized multi-service architecture
- Automated CI pipeline with GitHub Actions
- API testing with Pytest
- Modular backend architecture
- Retrieved chunks visualization

---

## Architecture

```text
User
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
RAG Pipeline
   ↓
ChromaDB Retrieval
   ↓
Ollama (LLM)
   ↓
Generated Response
```

---

## Application Preview

### Streamlit Frontend

<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/37a8c7d5-081f-46f2-a72f-f01241b97524" />

---

## API Documentation

The backend exposes a FastAPI REST API with automatic Swagger/OpenAPI documentation.

### Swagger UI

<img width="1871" height="784" alt="image" src="https://github.com/user-attachments/assets/4e6dc8ad-7f85-4260-8a47-e8e1d9363d9b" />

---


## Tech Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI, Python |
| Frontend | Streamlit |
| Vector Database | ChromaDB |
| LLM Runtime | Ollama |
| Containerization | Docker, Docker Compose |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Version Control | Git, GitHub |

---



## Running the Project

### Clone repository

```bash
git clone https://github.com/JoshuaDs69/rag-assistant.git
cd rag-assistant
```

### Run with Docker Compose

```bash
docker compose up --build
```

### Access application

- Frontend: http://localhost:8501
- Backend API Docs: http://localhost:8000/docs

---

## CI/CD Pipeline

The project includes a GitHub Actions CI pipeline that automatically:

- Installs dependencies
- Validates Python syntax
- Runs automated tests with Pytest
- Validates Docker image builds

##CI/CD Bagde

![CI](https://github.com/JoshuaDs69/rag-assistant/actions/workflows/ci.yml/badge.svg)

---

## Project Structure

```text
rag-assistant/
│
├── src/
│   ├── app/
│   │   ├── api/            # FastAPI routes
│   │   ├── db/             # ChromaDB client
│   │   ├── embeddings/     # Embedding generation
│   │   ├── rag/            # RAG pipeline logic
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── config.py
│   │   └── main.py
│
├── frontend/
│   ├── app.py              # Streamlit frontend
│   └── Dockerfile
│
├── tests/
│   ├── test_api.py
│   ├── test_ask.py
│   └── test_basic.py
│
├── data/
│   ├── raw/                # Source banking documents
│   ├── processed/          # Chunked and embedded data
│   └── vector_db/          # ChromaDB persistence
│
├── notebooks/              # RAG experimentation notebooks
├── scripts/                # Ingestion scripts
├── .github/workflows/      # GitHub Actions CI pipeline
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---


## RAG Pipeline

The system follows a Retrieval-Augmented Generation workflow:

1. User submits a banking-related query through the Streamlit frontend
2. FastAPI backend receives the request
3. Query embeddings are generated
4. Relevant chunks are retrieved from ChromaDB
5. Retrieved context is sent to Ollama
6. The LLM generates a context-aware response
7. Retrieved chunks are displayed alongside the final answer


---

## Testing

The backend includes automated API and integration tests using Pytest.

Tests validate:

- FastAPI endpoints
- API responses
- Request handling
- Mocked RAG pipeline behavior

---


## Future Improvements

- Cloud deployment
- Kubernetes orchestration
- Authentication and user management
- Conversation memory
- GPU acceleration
- Advanced observability and logging
