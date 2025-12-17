# SmartQ - Multiplayer Quiz and Game Platform

SmartQ is a modern, multiplayer web platform for hosting quizzes and browser-based games, built with FastAPI and powered by OpenAI.

## ✨ Features

- **Dynamic Quiz Generation**: Uses OpenAI's `gpt-4o` to create unique quizzes on the fly.
- **Real-time API**: Built with FastAPI for high performance.
- **Modern Frontend**: A clean, responsive lobby page built with HTML, CSS, and vanilla JavaScript.
- **Easy Dependency Management**: Uses `uv` for fast and efficient package management.
- **Secure API Key Handling**: Manages secrets using environment variables and `.env` files.

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

- Python 3.12 or higher
- `uv` installed (`pip install uv`)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd SmartQ
    ```

2.  **Create a virtual environment:**
    ```sh
    uv venv
    ```

3.  **Activate the virtual environment:**
    - On Windows (PowerShell):
      ```sh
      .\.venv\Scripts\Activate.ps1
      ```
    - On macOS/Linux:
      ```sh
      source .venv/bin/activate
      ```

4.  **Install dependencies:**
    ```sh
    uv pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt`, you can install from `pyproject.toml` with `uv pip install .`)*

5.  **Set up your environment variables:**
    - Create a file named `.env` in the project root.
    - Add your OpenAI API key to it:
      ```
      OPENAI_API_KEY="sk-your-secret-key-here"
      ```

## 🖥️ Usage

To run the web server, execute the following command from the project root:

```sh
uvicorn server:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

- **Lobby**: [http://127.0.0.1:8000/top.html](http://127.0.0.1:8000/top.html)
- **API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

- `GET /`: Serves the main lobby page (`top.html`).
- `GET /health`: Checks the connection status with the OpenAI API.
- `GET /quiz`: Fetches a new, dynamically generated quiz question.
- `POST /answer`: Submits an answer and checks if it is correct.

## 📂 Project Structure

```
.
├── .env          # Stores environment variables (e.g., API keys)
├── .gitignore    # Specifies files to be ignored by Git
├── pyproject.toml # Project metadata and dependencies
├── README.md     # This file
├── server.py     # The main FastAPI application logic
├── static/
│   └── index.html  # The old static index file (can be removed)
├── top.css       # Styles for the lobby page
└── top.html      # The main lobby page HTML
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License.
