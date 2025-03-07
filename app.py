import ollama
import faiss
import numpy as np
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_and_embed_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    chunks = text_splitter.split_documents(documents)
   
    # Convert chunks into text
    texts = [chunk.page_content for chunk in chunks]
    
    # Generate embeddings
    embeddings = embedding_model.encode(texts).astype(np.float32)
    
    # Store embeddings in FAISS
    index = faiss.IndexFlatL2(embeddings.shape[1])
    
    index.add(embeddings)
    
    return index, texts

# Search FAISS for relevant text
def search_text(index, texts, query, top_k=2):
    query_embedding = embedding_model.encode([query]).astype(np.float32)
    _, indices = index.search(query_embedding, top_k)
    retrieved_text = " ".join([texts[i] for i in indices[0]])
    return retrieved_text

# Use Ollama to generate an answer
def ask_question(pdf_path):
    """Interactive Q&A from the PDF."""
    index, texts = load_and_embed_pdf(pdf_path)

    while True:
        query = input("\n Ask a question (or type 'exit' to quit): \n").strip()
        if query.lower() == "exit":
            print("👋 Exiting...")
            break
        
        context = search_text(index, texts, query)
        prompt = f"Answer the question using the context below:\n\nContext: {context}\n\nQuestion: {query}\nAnswer:"
        
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        print("\n\n\n\n Answer:", response["message"]["content"])

# Run the interactive Q&A
pdf_file = "pdfs/budget_speech.pdf" 
ask_question(pdf_file)