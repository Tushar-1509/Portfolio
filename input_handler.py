
import json
from PyPDF2 import PdfReader

def handle_input(file_or_text):
    if file_or_text.endswith(".pdf"):
        reader = PdfReader(file_or_text)
        return {"type": "pdf", "content": "\n".join(p.extract_text() for p in reader.pages)}
    try:
        data = json.loads(file_or_text)
        return {"type": "json", "content": data}
    except:
        if "From:" in file_or_text or "Subject:" in file_or_text:
            return {"type": "email", "content": file_or_text}
    raise ValueError("Unsupported input format")
