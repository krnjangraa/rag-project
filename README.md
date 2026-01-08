# rag-project

**Study smarter: convert video lectures into searchable, interactive Q&A using RAG** 🎓

**rag-project** is an end-to-end toolkit that turns video lectures into a searchable, conversational study assistant. The pipeline extracts audio from videos, transcribes speech, segments and embeds the content, builds a vector store, and lets you ask natural-language questions about the lecture. Answers are concise, context-grounded, and cite the relevant lecture segments—ideal for studying, review, and quick revision.

## Features ✅
- End-to-end pipeline: video → transcript → chunks → embeddings → vector DB
- Conversational Q&A over lecture content with source citations
- Simple scripts: `process_video.py`, `stt.py`, `format.py`, `read_chunks.py`, `ask.py`
- Designed to exclude large media from the repo; supports Git LFS if you want to track audio/video
- Extensible to different transcription, embedding, and LLM backends

## How it works (high level) ⚙️
1. **Ingest** — extract audio and transcribe video lectures.
2. **Process** — split transcripts into chunks and generate embeddings.
3. **Query** — run the conversational interface to ask questions and get context-aware answers.

## Quick start 💡
1. Clone the repo and create a venv:
   - git clone https://github.com/krnjangraa/rag-project
   - python -m venv venv && source venv/bin/activate
2. Install dependencies (add `requirements.txt` if not present):
   - pip install -r requirements.txt
3. Process a video:
   - python process_video.py path/to/lecture.mp4
4. Ask a question:
   - python ask.py --question "What are the main takeaways from the lecture on X?"

## Notes & next steps 🔧
- Add a `requirements.txt` and usage examples for each script for smoother onboarding.
- Optionally set up GitHub Actions CI, branch protection, and Dependabot for maintenance.

---

If you'd like, I can add example usage snippets, a `requirements.txt`, and a CI workflow next—tell me which you prefer and I'll commit them.  
