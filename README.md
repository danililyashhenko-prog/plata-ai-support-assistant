# Plata Bank AI Support Assistant 

A high-performance, production-ready AI-driven customer support assistant microservice specifically simulated for the **Plata Bank** ecosystem. Built using **Python**, **FastAPI**, and **OpenAI API**, this project is designed to handle, analyze, and automatically respond to user inquiries with low latency.

---

##  Features

* **FastAPI Framework:** High-performance asynchronous REST API architecture with auto-generated interactive documentation (Swagger UI).
* **Production-Grade AI Integration:** Native integration with OpenAI's cutting-edge models (`gpt-4o-mini`).
* **Fintech Domain Prompting:** Tailored system prompt architecture ensuring polite, brand-safe, and context-aware responses.
* **Trilingual Ready:** Automatically adapts to the user's language (English, Czech, Russian, or Spanish).
* **Dual Mode Ingestion:** Hybrid architecture that automatically falls back to a smart mock environment if no API keys are provided (perfect for safe local testing).

---

## Tech Stack

* **Backend & Framework:** Python 3.10+, FastAPI
* **AI Integration:** OpenAI SDK v1+
* **Data Validation:** Pydantic v2 (Strict Request/Response schemas)
* **Server Gateway:** Uvicorn

---

##  Setup and Installation

### 1. Clone the repository
```bash
git clone [https://github.com/danililyashenko-prog/plata-ai-support-assistant.git](https://github.com/danililyashenko-prog/plata-ai-support-assistant.git)
cd plata-ai-support-assistant
