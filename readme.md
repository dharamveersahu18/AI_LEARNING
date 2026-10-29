// Run these commands in order for a new project.


uv init
uv venv
uv add groq pydantic pypdf python-docx
uv lock
uv sync
uv run python main.py
  