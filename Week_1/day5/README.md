# 🚀 AI Learning Journey — Day 5

A hands-on learning repository documenting my progress through the **Pratyush AI learning series**. This folder contains the code, experiments, and practice exercises completed during Day 5.

The goal is to learn AI concepts by writing code, understanding how each component works, and experimenting with practical examples.

## 📌 Overview

- **Learning Series:** Pratyush AI
- **Week:** 1
- **Day:** 5
- **Language:** Python
- **Package Manager:** [uv](https://docs.astral.sh/uv/), if configured for this project

## 🛠️ Prerequisites

Install the following before running the project:

- Python version specified in `.python-version`, if present
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Git
- API key for the relevant AI provider, if required by the code

Verify your installations:

```bash
python --version
uv --version
git --version
```

## 📂 Project Structure

```text
day5/
├── src/                # Source code, if present
├── .gitignore
├── .python-version     # Python version, if present
├── pyproject.toml      # Project configuration, if present
├── uv.lock             # Locked dependencies, if present
└── README.md
```

*Update this tree to match the actual files in the repository.*

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/dharamveersahu18/AI_LEARNING.git
cd AI_LEARNING/Week_1/day5
```

### 2. Install dependencies

If `pyproject.toml` and `uv.lock` are present:

```bash
uv sync
```

This installs the project's dependencies and creates a virtual environment when needed.

### 3. Configure environment variables

If the project requires an API key, create a `.env` file in the directory expected by the code.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Replace the placeholder with your own key. Never commit your actual `.env` file or expose API credentials publicly.

### 4. Run the code

Run the relevant Python script using:

```bash
uv run python filename.py
```

Replace `filename.py` with the actual script name.

If the code is inside `src/`, use the appropriate path or the project's configured entry point.

## ▶️ Running Individual Lessons

Run each script separately according to its purpose and dependencies.

```bash
uv run python example1.py
uv run python example2.py
```

*Replace these example filenames with the actual Day 5 filenames. Not every script should necessarily be executed in sequence.*

## 📚 Learning Notes

Use this section to document:

- Concepts explored
- Important code snippets
- Errors encountered and how they were fixed
- Practical applications of the concepts
- Key takeaways from the lesson

## 🐛 Troubleshooting

**`uv` is not recognized**

Install `uv`, reopen the terminal, and verify with `uv --version`.

**Missing dependency**

Run:

```bash
uv sync
```

**API key not found**

Check that your `.env` file exists in the expected location and that the variable name matches the one used in your code.

**Python file not found**

Confirm that your terminal is in the correct directory and use the actual script path.

## 🔗 Repository

[View the complete AI Learning repository](https://github.com/dharamveersahu18/AI_LEARNING)

## 📈 Learning Philosophy

> Learn by building, understand by debugging, and improve through consistent practice.

This repository is part of my ongoing journey to understand Python, AI, and LLM-based application development one step at a time.

⭐ If you find the learning notes useful, feel free to explore the repository.

