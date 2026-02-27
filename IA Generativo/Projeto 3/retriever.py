import os
from embeddings import EmbeddingManager
from file_loader import load_txt, load_pdf, load_docx

embedding_manager = EmbeddingManager()


def load_conhecimento(folder_path="."):
    """
    Lê todos os arquivos .txt, .pdf e .docx da pasta
    e gera embeddings.
    """

    full_text = ""

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            full_text += load_txt(path) + "\n"

        elif file.endswith(".pdf"):
            full_text += load_pdf(path) + "\n"

        elif file.endswith(".docx"):
            full_text += load_docx(path) + "\n"

    # 🔹 Criar chunks simples
    chunks = [chunk.strip() for chunk in full_text.split("\n\n") if chunk.strip()]

    # 🔹 Gerar embeddings
    embedding_manager.create_embeddings(chunks)

    print(f"{len(chunks)} chunks carregados e vetorizados.")

    return chunks


def semantic_retriever(query, top_k=1):
    results = embedding_manager.search(query, top_k=top_k)
    return "\n".join(results)
