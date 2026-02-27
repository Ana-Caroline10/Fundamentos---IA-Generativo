import os
from pypdf import PdfReader
from docx import Document

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text


def load_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])