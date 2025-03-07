# PDF QA Bot

## PDF QA Bot - AI-Powered Question Answering

PDF QA Bot is an interactive AI-based application that allows users to ask questions from a PDF document. It leverages **FAISS** for efficient embedding storage and **Ollama's Llama 3.2 model** for generating responses, enabling quick and accurate information retrieval from PDFs.

---

## How It Works

1. **Upload a PDF**: The application loads and processes the PDF document.
2. **Text Embedding**: The content is split into chunks and converted into vector embeddings using `sentence-transformers`.
3. **Search & Retrieve**: FAISS is used to efficiently search and retrieve relevant text based on user queries.
4. **Generate Response**: Ollama’s Llama 3.2 model generates answers based on the retrieved context.
5. **Interactive Q&A**: Users can ask multiple questions interactively.

---

## Technologies Used

- **Python**: Core programming language for the application.
- **FAISS**: For efficient similarity search and indexing.
- **LangChain**: For document processing and text splitting.
- **Sentence Transformers**: For generating embeddings from text.
- **Ollama**: For generating AI-powered responses.
- **PyPDFLoader**: For extracting text from PDFs.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shenoy-dsouza/pdf-qa-bot.git
   cd pdf-qa-bot
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the chatbot with a PDF file:
   ```bash
   python app.py
   ```

2. Once started, enter your questions based on the PDF content. Type `exit` to quit.

---

## Potential Impact

This application can significantly improve information retrieval and document analysis by:
- Enabling quick Q&A from lengthy documents.
- Reducing manual effort in searching for specific information.
- Enhancing productivity for professionals working with research papers, legal documents, and reports.

---

## Example Interaction

1. Run the chatbot with a PDF file:
   ```bash
   python app.py
   ```

2. Ask a question (or type `exit` to quit):
   ```
    What are the key highlights of the budget?
   ```

3. Example response:
   ```
   1. Initiating transformative reforms across six domains to augment growth potential and global competitiveness.
   2. Emphasis on Agriculture as the '1st Engine' for growth and development.
   3. Goals to accelerate growth, secure inclusive development, invigorate private sector investments, uplift household sentiments, and enhance spending power of India's rising middle class.
   These points suggest a comprehensive approach with multiple focus areas, aiming to drive transformation and growth in various sectors over the next five years.


---
