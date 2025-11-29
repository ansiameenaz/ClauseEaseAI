# ⚖️ ClauseEase AI: Local Contract Language Simplifier

ClauseEase AI is a privacy-first web application designed to instantly simplify complex legal documents (contracts, NDAs, Terms of Service) into plain, easily understandable English. It leverages a local Large Language Model (LLM) powered by Ollama to ensure zero data transmission to the cloud, protecting sensitive information.

# ✨ Features

Privacy-First Architecture: All document analysis runs locally on your machine via Ollama.

Multilingual Support: Accepts documents in multiple languages and translates/summarizes the key legal findings into English.

Long Document Processing (Chunking): Employs a recursive chunking algorithm and Map-Reduce strategy to handle large contracts (50+ pages) without exceeding hardware memory limits.

Universal File Handling: Extracts raw text from PDF (.pdf), Word (.docx), and .txt files.

Dynamic UX: Features a clean, custom "Notepad" UI and real-time progress timers to monitor AI analysis time.

Contextual Q&A: Maintains conversation history and answers follow-up questions specifically based on the content of the uploaded document.

# 🛠️ Technology Stack

The ClauseEase AI system is built upon a specialized, privacy-focused technology stack:

Core Language: The entire application logic is written in Python (v3.10+), utilizing its extensive library ecosystem.

Frontend/UI: We use Streamlit to serve the interactive web application, allowing us to build the complex chat interface and file handling entirely in Python.

AI Backend: The inference engine is Ollama (v0.12+), which acts as a lightweight local server for running LLMs via the standard REST API (localhost:11434).

AI Model: The project relies on the Llama 3.2 (3B) model, chosen specifically for its resource optimization. This model balances high translation and summarization quality with the ability to execute efficiently on consumer-grade hardware.

Data Pipeline: Data ingestion involves specialized libraries: pypdf and python-docx for text extraction, and json and tempfile for temporary JSON storage to manage the chunking workflow.

Methodology: The system employs a core Chunking & Map-Reduce strategy to break large documents into manageable segments, ensuring both memory efficiency and comprehensive processing.
# ⚙️ Project Structure

The project maintains a clean, separation-of-concerns architecture:

ClauseEase_Demo/

 ├── .streamlit/
    
    
   └── config.toml # Streamlit global theme configuration (colors, font)
 
 |

 ├── venv/   # Virtual Environment (IGNORED by Git)

 ├── app2.py  # Core Streamlit application, UI layout, LLM logic, and data pipeline

 ├── style.css  # Custom CSS for the "Notepad" minimalist aesthetic

 ├── .gitignore # Ensures venv/ and temporary files are not committed

 └── README.md


#  Setup and Installation

This application requires Python 3.10+ and the Ollama application to be running locally.

Step 1: Install Ollama

Download and Install Ollama: Download the application installer from the official website.

Download the Required Model: Open your terminal (PowerShell or Command Prompt) and pull the optimized Llama 3.2 model:

**ollama pull llama3.2:3b**


Ensure the Ollama service is running in the background.

Step 2: Set up the Python Environment

Clone the Repository:

**git clone [YOUR_GITHUB_REPOSITORY_URL]
cd ClauseEase_Demo**

Create and Activate Virtual Environment:

**python -m venv venv
.\venv\Scripts\activate  # For Windows PowerShell**

Install Python Dependencies:

**pip install streamlit ollama pypdf python-docx**

Step 3: Run the Application

With the virtual environment active and the Ollama model running, launch the app:

**streamlit run app2.py**

The application will automatically open in your web browser, ready to analyze documents.

# 📝 Document Processing Pipeline

The system is engineered to manage memory and ensure all of the document is processed:

Extraction: User uploads file $\rightarrow$ **app2.py**uses pypdf/python-docx to extract text.

Temporary JSON Storage: Raw text is stored momentarily in a JSON file to ensure the data is clean and isolated.

Chunking: The text is passed to the custom chunk_text() function, splitting it into overlapping segments (4,000 characters).

Map-Reduce Summarization: Each segment is summarized by Llama 3.2 individually (the Map step). These summaries are then combined and fed back into the LLM for a final, cohesive Executive Summary (the Reduce step).

(Replace [YOUR_GITHUB_REPOSITORY_URL] and ensure paths match your local setup.)
