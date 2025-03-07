# PDF QA Bot

## Overview
The **PDF QA Bot** is a Python-based interactive question-answering system that allows users to ask questions about the contents of a PDF document. It utilizes **FAISS** for efficient vector search, **Sentence Transformers** for embeddings, and **Ollama** for generating responses based on retrieved text.

## Features
- Loads and processes PDF documents.
- Splits text into manageable chunks for better search accuracy.
- Uses **FAISS** to perform fast similarity searches on text embeddings.
- Employs **Ollama** (with LLaMA 3.2) for generating natural language responses.
- Interactive command-line interface for user queries.

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed.

### Step 1: Clone the repository
```sh
git clone https://github.com/shenoy-dsouza/pdf-qa-bot.git
cd pdf-qa-bot
```

### Step 2: Create a virtual environment (optional but recommended)
```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```sh
pip install -r requirements.txt
```

## Usage
### Running the application
```sh
python app.py
```
The script will load a predefined PDF (`pdfs/budget_speech.pdf`) and prompt you to ask questions interactively.

### Example Interaction
```
Ask a question (or type 'exit' to quit):
> What are the  major reform areas outlined in the budget?

Answer: The major reform areas outlined in the budget include:...
```

## How It Works
1. **Load PDF**: Extracts text using `PyPDFLoader`.
2. **Text Splitting**: Uses `RecursiveCharacterTextSplitter` to create manageable text chunks.
3. **Embedding Generation**: Converts text chunks into numerical vectors using `Sentence Transformers`.
4. **Indexing with FAISS**: Stores embeddings for fast similarity searches.
5. **Query Processing**:
   - Embeds user questions and searches for the most relevant text.
   - Generates a response using **Ollama**'s language model.

## Dependencies
The required libraries are specified in `requirements.txt`:
```
faiss-cpu==1.10.0
langchain==0.3.20
langchain-community==0.3.19
langchain-core==0.3.41
langchain-text-splitters==0.3.6
ollama==0.4.7
pypdf==5.3.1
sentence-transformers==3.4.1
```



