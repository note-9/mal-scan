# M-Scan 🕵️‍♂️

An async FastAPI backend that lets you upload files and automatically scans them for simple malicious patterns in the background.

### Features
- Async file upload
- Background scan (FastAPI BackgroundTasks)
- SQLite + SQLModel to track scan results
- SHA256 hashing and bad pattern detection
- Simple `/upload`, `/status/{id}`, `/report/{id}` endpoints

### How to Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
