# Smart Summary API (Backend)

Backend of the **Smart Summary App** a simple application that uses AI to summarize texts.

Built with **FastAPI** + **uv** (package manager) + **Ruff** (lint), this service receives a text
and returns its summary using **LangChain + OpenAI**, with **streaming via Server-Sent Events (SSE)**.

---

## 🚀 Stack

- **FastAPI** — Python web framework.
- **uv** — modern package manager.
- **Ruff** — linting and formatting.
- **LangChain + OpenAI** — integration with LLM.
- **pytest + httpx** — asynchronous testing.
- **Docker** — containerization.

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.13+
- uv installed
- Valid OpenAI API Key

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/smart-summary-backend.git
cd smart-summary-backend

# Install dependencies
uv sync

# Run server in dev mode
uv run uvicorn app.main:app --reload --port 8000

# Tests
uv run pytest -q

# Linter
uv run ruff check --fix .
```

---

## 🔌 Endpoints

### Healthcheck

`GET /healthz` → `{"ok": true}`

### Summarization (SSE streaming)

`POST /v1/summarize`

```json
{
  "text": "Long text here...",
  "style": "bullets"
}
```

- `style`: `"bullets"` or `"paragraph"`

Response: real-time stream (`text/event-stream`) with summary chunks.

---

## 📦 Docker

```bash
docker build -t smart-summary-api .
docker run --rm -p 8000:8000 --env-file .env.example smart-summary-api
```

---

## 🏗️ Architecture

- **UI (Next.js)** → sends text → **Backend (FastAPI)**
- Backend calls **LangChain + OpenAI** and returns summary in **stream**
- **Observability** (coming soon): OpenTelemetry for metrics, tracing, and cost/token tracking.

```
[User] → Next.js → FastAPI (SSE) → LangChain → OpenAI API
                         ↓
                    Observability
```

---

## 🔐 Security

- The UI never directly calls the LLM.
- Support for JWT authentication.
- Secrets via `.env` or AWS Secrets Manager.

---

## 📈 Scalability

- Containerized backend.
- Auto-scaling based on CPU/mem/requests.
- Streaming SSE → lightweight connections, low latency.
- Cost/token monitoring per request.

---

## 💡 Future Improvements

- Real authentication via JWT (Auth0/Cognito).
- Complete observability (OTel, Grafana, LangSmith).
- Summary caching (Redis).
- File uploads (PDF/Doc → text).
- Usage dashboard (tokens, costs, p95 latency).
- Multi-cloud deployment (AWS CloudFront, Vercel, etc.).
