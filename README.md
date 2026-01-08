# 📚 Enterprise Knowledge Assistant (End-to-End RAG System)

An **enterprise-grade Retrieval-Augmented Generation (RAG)** system that enables users to query large internal knowledge bases (PDFs, Word, Excel, HTML, APIs) with **high accuracy, citations, guardrails, and a real user interface**.

This project demonstrates **production-level AI engineering practices**, including advanced retrieval, re-ranking, LLM orchestration, safety controls, evaluation hooks, and a full frontend + backend stack.

---

## 🚀 Key Features

### ✅ Enterprise RAG Capabilities
- Semantic + Hybrid Retrieval (BM25 + Vector)
- Advanced **Semantic Chunking**
- Cross-Encoder Re-Ranking
- Context Compression & De-duplication
- Query Rewriting for better recall


### 🧱 Infrastructure & UI
- **Weaviate** vector database
- **LangChain** orchestration
- **FastAPI** backend
- **Streamlit** frontend
- Modular, testable architecture
- Environment-based configuration


---

## 🧩 System Breakdown

### 1️⃣ Data Ingestion
- Supports **PDF, Word, Excel, HTML, APIs**
- Metadata extraction
- Structured parsing
- Extensible loader system

### 2️⃣ Semantic Chunking & Embeddings
- Meaning-aware chunking (not naive fixed size)
- Overlap + structure-preserving chunks
- OpenAI embeddings
- Stored in Weaviate vector DB

### 3️⃣ Advanced Retrieval & Re-ranking
- **Hybrid search** (BM25 + Vector)
- **Query rewriting** using LLM
- **Cross-encoder re-ranking** for precision
- Context compression & redundancy filtering

### 4️⃣ API & Frontend
- FastAPI backend for clean separation
- Streamlit UI for live demos
- Confidence score + sources shown to user


---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
LLM | OpenAI (GPT-4o mini) |
Orchestration | LangChain |
Vector DB | Weaviate |
Backend | FastAPI |
Frontend | Streamlit |
Re-ranking | Sentence Transformers |
Config | dotenv |
Evaluation | Custom evaluators |



