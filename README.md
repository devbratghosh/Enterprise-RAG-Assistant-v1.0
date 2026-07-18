# Enterprise-RAG-Assistant

> Production-ready Retrieval-Augmented Generation (RAG) application built with Python, ChromaDB, Sentence Transformers, Streamlit, Docker, Oracle Cloud Infrastructure, and Cloudflare Tunnel.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-success)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Enterprise-RAG-Assistant is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to query enterprise documents using natural language.

The project demonstrates the complete lifecycle of an enterprise AI application—from document ingestion and semantic search to Docker containerization, cloud deployment, production operations, and release management.

Unlike a typical tutorial project, this repository emphasizes production engineering practices including deployment automation, operational documentation, troubleshooting, and release governance.

---

## Key Features

- Recursive document-aware chunking
- Semantic search using Sentence Transformers
- ChromaDB persistent vector database
- OpenRouter LLM integration
- Streamlit web interface
- Dockerized deployment
- Oracle Cloud Infrastructure deployment
- Cloudflare Tunnel integration
- Production deployment handbook
- Operations & troubleshooting documentation

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| UI | Streamlit |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| LLM | OpenRouter |
| PDF Processing | PyPDF2 |
| Containerization | Docker |
| Cloud | Oracle Cloud Infrastructure |
| Networking | Cloudflare Tunnel |
| Version Control | Git & GitHub |

---

## Architecture

```
                 PDF Documents
                       │
                       ▼
               Recursive Chunking
                       │
                       ▼
              Sentence Embeddings
                       │
                       ▼
                 ChromaDB Vector DB
                       │
                       ▼
                 Semantic Retrieval
                       │
                       ▼
                  OpenRouter LLM
                       │
                       ▼
                Streamlit Web UI
```

---

## Project Structure

```
Enterprise-RAG-Assistant
│
├── app.py
├── requirements.txt
├── src/
├── deployment/
├── docs/
├── data/
├── evaluation/
└── screenshots/
```

---

## Local Development

Clone the repository

```bash
git clone <repository-url>
cd Enterprise-RAG-Assistant
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```powershell
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app.py
```

---

## Docker

Build

```bash
docker build \
-f deployment/docker/Dockerfile \
-t enterprise-rag-assistant:v1.0.0 \
.
```

Run

```bash
docker run \
-p 8601:8601 \
--env-file .env \
enterprise-rag-assistant:v1.0.0
```

---

## Deployment

The application has been validated on

- Oracle Cloud Infrastructure
- Docker
- Cloudflare Tunnel

Production URL

```
https://rag.devbratghosh.com
```

---

## Documentation

Detailed documentation is available in the `docs/` directory.

Included documents:

- Deployment Handbook
- Operations Handbook
- Troubleshooting Guide
- Release Management
- Deployment Optimization
- Architecture Notes

---

## Current Version

**v1.0.0**

### Included

- End-to-end RAG pipeline
- Recursive chunking
- ChromaDB integration
- Semantic retrieval
- Docker deployment
- Oracle Cloud deployment
- Cloudflare integration
- Production documentation

---

## Known Limitation

Version 1.0 has a known retrieval limitation for certain high-level conceptual sections (for example, *Corporate Vision*). This will be addressed in Version 1.1 through retrieval quality improvements.

---

## Roadmap

### Version 1.1

- Improved retrieval accuracy
- Better chunk ranking
- Metadata-aware retrieval
- Enhanced evaluation framework

### Version 1.2

- Conversation history
- Source highlighting
- Confidence scores
- Improved user experience

### Version 2.0

- Multi-document support
- Authentication
- REST API
- Enterprise dashboard

---

## Screenshots

Example screenshots are available under

```
screenshots/
```

including

- Docker
- Oracle Cloud
- Cloudflare
- Deployment
- Application

---

## Author

**Devbrat Ghosh**

Technical Program Manager | AI Solutions | Enterprise Architecture | GenAI | RAG | Cloud

GitHub

```
https://github.com/<your-github>
```

Portfolio

```
https://devbratghosh.com
```

LinkedIn

```
https://linkedin.com/in/<your-profile>
```

---

## License

MIT License

---

⭐ If you find this project useful, consider giving it a Star.
